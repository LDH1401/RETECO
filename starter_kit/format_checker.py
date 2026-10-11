#!/usr/bin/env python3
"""Format checker cho bài nộp (submission) của RETECO.

Kiểm tra một run file ở định dạng TREC:

    qid   Q0   docid   rank   score   tag

Các quy tắc được áp dụng (giống với checker mà CodaBench sẽ dùng):
  * đúng 6 cột phân tách bằng khoảng trắng trên mỗi dòng không rỗng
  * rank là số nguyên dương, score là số thực
  * các rank trong một topic là duy nhất
  * (cảnh báo) score trong một topic không tăng khi rank tăng
  * (tùy chọn) --qrels giới hạn tập topic id hợp lệ và cảnh báo khi gặp docid không xác định

Mã thoát 0 = hợp lệ, 1 = phát hiện lỗi.

Cách dùng:
    python format_checker.py run.txt
    python format_checker.py run.txt --qrels qrels.txt --corpus documents.jsonl
"""
import argparse
import json
import sys


def load_ids(path, key):
    ids = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                ids.add(json.loads(line)[key])
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--qrels", help="tùy chọn: qrels.txt để kiểm tra topic id")
    ap.add_argument("--corpus", help="tùy chọn: documents.jsonl để kiểm tra doc id")
    ap.add_argument("--doc-key", default="id", help="trường doc id trong corpus (id|doc_id)")
    args = ap.parse_args()

    valid_topics = None
    if args.qrels:
        valid_topics = set()
        with open(args.qrels) as f:
            for ln in f:
                if ln.strip():
                    valid_topics.add(ln.split()[0])
    valid_docs = load_ids(args.corpus, args.doc_key) if args.corpus else None

    errors, warnings = [], []
    per_topic_ranks, per_topic_last_score = {}, {}
    n = 0
    with open(args.run) as f:
        for lineno, raw in enumerate(f, 1):
            line = raw.strip()
            if not line:
                continue
            n += 1
            cols = line.split()
            if len(cols) != 6:
                errors.append(f"L{lineno}: expected 6 columns, got {len(cols)}")
                continue
            qid, q0, docid, rank, score, tag = cols
            try:
                rank = int(rank)
                assert rank > 0
            except Exception:
                errors.append(f"L{lineno}: rank must be a positive integer, got '{cols[3]}'")
            try:
                score = float(score)
            except Exception:
                errors.append(f"L{lineno}: score must be a float, got '{cols[4]}'")
                continue
            if valid_topics is not None and qid not in valid_topics:
                warnings.append(f"L{lineno}: topic '{qid}' not in qrels")
            if valid_docs is not None and docid not in valid_docs:
                warnings.append(f"L{lineno}: docid '{docid}' not in corpus")
            ranks = per_topic_ranks.setdefault(qid, set())
            if isinstance(rank, int):
                if rank in ranks:
                    errors.append(f"L{lineno}: duplicate rank {rank} in topic '{qid}'")
                ranks.add(rank)
            prev = per_topic_last_score.get(qid)
            if prev is not None and score > prev + 1e-9:
                warnings.append(f"L{lineno}: score increases with rank in topic '{qid}'")
            per_topic_last_score[qid] = score

    print(f"lines: {n}  topics: {len(per_topic_ranks)}  "
          f"errors: {len(errors)}  warnings: {len(warnings)}")
    for e in errors[:50]:
        print("  ERROR  ", e)
    for w in warnings[:20]:
        print("  warn   ", w)
    if errors:
        print("RESULT: INVALID")
        sys.exit(1)
    print("RESULT: VALID")


if __name__ == "__main__":
    main()
