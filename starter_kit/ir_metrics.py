"""Các chỉ số đánh giá chính thức của RETECO (thuần Python, không có phụ thuộc).

Cài đặt các chỉ số được dùng cho cả hai hạng mục của RETECO:

  * nDCG@k          -- chỉ số chính thức của bảng xếp hạng (cả hai hạng mục)
  * Temporal Precision@k (TP)   -- độ chính xác có trọng số theo vị trí của các tài liệu liên quan về thời gian
  * Temporal Relevance@k (TR)   -- tỷ lệ trong top-k được đánh giá là liên quan về thời gian
  * Temporal Coverage@k  (TC)   -- tỷ lệ các giai đoạn thời gian cần thiết của truy vấn được bao phủ
  * NDCG|FC@k       -- nDCG@k trên các truy vấn đạt độ bao phủ thời gian đầy đủ (TC==1)

Trên tập kiểm tra ẨN, mức độ liên quan về thời gian và độ bao phủ giai đoạn được gán bởi
LLM làm giám khảo (prompt được ghi lại + hiệu chỉnh bằng các trường hợp chuẩn + con người kiểm tra xác suất).
Với trình chấm điểm thí điểm NGOẠI TUYẾN ở đây, nhãn liên quan chuẩn trong `qrels` được dùng
làm nguồn đối chiếu (oracle) cho mức độ liên quan về thời gian, và các tệp bước của từng truy vấn
cung cấp tập các giai đoạn thời gian cần thiết (một bước == một giai đoạn cần thiết). Cách này mô phỏng
việc trình chấm điểm trên tập kiểm tra ẩn sẽ sử dụng nhãn của giám khảo, nên cùng một luồng mã được dùng lại.
"""
from math import log2


# ------------------------------------------------------------- DCG cốt lõi ----
def _dcg(rels):
    """Độ lợi tích lũy có chiết khấu (DCG) của một danh sách có thứ tự các mức liên quan."""
    return sum(r / log2(i + 2) for i, r in enumerate(rels))  # i=0 -> 1/log2(2)=1


def ndcg_at_k(ranked_docids, gold, k=10):
    """nDCG@k nhị phân. `gold` là set/dict các id tài liệu liên quan (mức 1)."""
    grades = [1.0 if d in gold else 0.0 for d in ranked_docids[:k]]
    ideal = sorted([1.0] * min(len(gold), k), reverse=True)
    idcg = _dcg(ideal)
    return (_dcg(grades) / idcg) if idcg > 0 else 0.0


# ------------------------------------------------ các chỉ số thời gian -------
def temporal_relevance_at_k(ranked_docids, temporally_relevant, k=10):
    """TR@k: tỷ lệ trong top-k liên quan về thời gian."""
    top = ranked_docids[:k]
    if not top:
        return 0.0
    return sum(1 for d in top if d in temporally_relevant) / len(top)


def temporal_precision_at_k(ranked_docids, temporally_relevant, k=10):
    """TP@k: độ chính xác có trọng số theo vị trí (thưởng cho việc xếp tài liệu liên quan lên sớm hơn).

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
