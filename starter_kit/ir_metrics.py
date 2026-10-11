"""Các metric đánh giá chính thức của RETECO (thuần Python, không có dependency).

Cài đặt các metric được dùng cho cả hai track của RETECO:

  * nDCG@k          -- metric chính thức của leaderboard (cả hai track)
  * Temporal Precision@k (TP)   -- precision có trọng số theo vị trí của các tài liệu liên quan về thời gian
  * Temporal Relevance@k (TR)   -- tỷ lệ trong top-k được đánh giá là liên quan về thời gian
  * Temporal Coverage@k  (TC)   -- tỷ lệ các giai đoạn thời gian cần thiết của truy vấn (query) được bao phủ
  * NDCG|FC@k       -- nDCG@k trên các truy vấn đạt độ bao phủ thời gian đầy đủ (TC==1)

Trên tập test ẨN, mức độ liên quan (relevance) về thời gian và độ bao phủ giai đoạn được gán bởi
LLM-as-judge (prompt được ghi lại + calibration bằng các golden case + con người spot-check).
Với scorer pilot NGOẠI TUYẾN (offline) ở đây, các gold relevance label trong `qrels` được dùng
làm oracle cho mức độ liên quan về thời gian, và các tệp bước của từng truy vấn cung cấp
tập các giai đoạn thời gian cần thiết (một bước == một giai đoạn cần thiết). Cách này mô phỏng
việc scorer trên tập test ẩn sẽ sử dụng label của judge, nên cùng một luồng mã được dùng lại.
"""
from math import log2


# ------------------------------------------------------------- DCG cốt lõi ----
def _dcg(rels):
    """Discounted cumulative gain của một danh sách có thứ tự các mức liên quan (relevance grade)."""
    return sum(r / log2(i + 2) for i, r in enumerate(rels))  # i=0 -> 1/log2(2)=1


def ndcg_at_k(ranked_docids, gold, k=10):
    """nDCG@k nhị phân (binary). `gold` là set/dict các doc id liên quan (mức 1)."""
    grades = [1.0 if d in gold else 0.0 for d in ranked_docids[:k]]
    ideal = sorted([1.0] * min(len(gold), k), reverse=True)
    idcg = _dcg(ideal)
    return (_dcg(grades) / idcg) if idcg > 0 else 0.0


# ------------------------------------------------------ các metric thời gian -------
def temporal_relevance_at_k(ranked_docids, temporally_relevant, k=10):
    """TR@k: tỷ lệ trong top-k liên quan về thời gian."""
    top = ranked_docids[:k]
    if not top:
        return 0.0
    return sum(1 for d in top if d in temporally_relevant) / len(top)


def temporal_precision_at_k(ranked_docids, temporally_relevant, k=10):
    """TP@k: precision có trọng số theo vị trí (thưởng cho việc xếp tài liệu liên quan lên sớm hơn).

    TP@k = sum_i w_i * rel_i / sum_i w_i ,  w_i = 1/log2(i+1), i=1..k
    """
    top = ranked_docids[:k]
    num = den = 0.0
    for i, d in enumerate(top):
        w = 1.0 / log2(i + 2)
        den += w
        if d in temporally_relevant:
            num += w
    return (num / den) if den > 0 else 0.0


def temporal_coverage_at_k(ranked_docids, period_gold, k=10):
    """TC@k: tỷ lệ các giai đoạn thời gian cần thiết được bao phủ bởi >=1 tài liệu trong top-k.

    `period_gold` là danh sách các tập gold-id, mỗi tập ứng với một giai đoạn cần thiết (bước).
    """
    if not period_gold:
        return None  # truy vấn không có giai đoạn xác định -> loại khỏi TC
    top = set(ranked_docids[:k])
    covered = sum(1 for gs in period_gold if top & set(gs))
    return covered / len(period_gold)


# --------------------------------------------------------------- tổng hợp -----
def mean(xs):
    xs = [x for x in xs if x is not None]
    return (sum(xs) / len(xs)) if xs else 0.0
