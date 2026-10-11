#!/usr/bin/env python3
"""Hệ thống cơ sở BM25 chính thức của RETECO -- mã gốc, chạy trên bản phát hành RETECO.

Phần truy xuất là *nguyên văn* hàm `retrieval_bm25` từ các kho mã benchmark chính thức
(github.com/tempo-bench/Tempo và github.com/RECOR-Benchmark/RECOR, vốn có các cài đặt
giống hệt nhau đến từng byte): bộ phân tích Lucene qua pyserini, LuceneBM25Model của gensim
với k1=0.9 / b=0.4, cắt ở top-1000. Phần chấm điểm là hàm `calculate_retrieval_metrics`
gốc, tức pytrec_eval với ndcg_cut/map_cut/recall/P và recip_rank.

Cách xây dựng truy vấn theo đúng bản gốc:
  1a  examples['query']
  1b  f"{base_query}\n\nStep: {step_instruction}"      (Tempo/run_step.py)
  2a  turn['query'], ID chủ đề "{conv_id}_turn_{turn_id}" (RECOR/run_retrieval.py)

Kho ngữ liệu được phân tích và lập chỉ mục một lần cho mỗi lĩnh vực và dùng lại cho cả hai tập;
đây là điểm khác biệt duy nhất so với luồng chạy theo từng lần gọi của bản gốc -- nó không thay đổi
gì về điểm số, chỉ thay đổi thời gian chạy thực tế.

Cách dùng:
    JAVA_HOME=... JVM_PATH=... python official_baseline.py \
        --data ../reteco_data --out ../baselines_official --splits train dev
"""
import argparse
import json
import os
from collections import defaultdict

import pytrec_eval
from tqdm import tqdm

K_VALUES = [1, 5, 10, 25, 50, 100]


# ---------------------------------------------------------------------------
# Phần chấm điểm gốc (Tempo/retrievers.py :: calculate_retrieval_metrics, và bản sao
# giống hệt đến từng byte trong RECOR/experiments/retrieval/retrievers.py), được rút gọn
# chỉ còn các chỉ số mà RETECO báo cáo -- khối oracle-reranker là đầu ra chẩn đoán của
# bản gốc và không thuộc bảng xếp hạng chính thức của RETECO.
# ---------------------------------------------------------------------------
def calculate_retrieval_metrics(results, qrels, k_values=K_VALUES):
    ndcg, _map, recall, precision = {}, {}, {}, {}
    mrr = {"MRR": 0}
    for k in k_values:
        ndcg[f"NDCG@{k}"] = 0.0
        _map[f"MAP@{k}"] = 0.0
        recall[f"Recall@{k}"] = 0.0
        precision[f"P@{k}"] = 0.0

    ks = ",".join(str(k) for k in k_values)
    evaluator = pytrec_eval.RelevanceEvaluator(
        qrels, {f"map_cut.{ks}", f"ndcg_cut.{ks}", f"recall.{ks}", f"P.{ks}",
                "recip_rank"})
    scores = evaluator.evaluate(results)
    if not scores:
        return {}

    for qid in scores:
        for k in k_values:
            ndcg[f"NDCG@{k}"] += scores[qid][f"ndcg_cut_{k}"]
            _map[f"MAP@{k}"] += scores[qid][f"map_cut_{k}"]
            recall[f"Recall@{k}"] += scores[qid][f"recall_{k}"]
            precision[f"P@{k}"] += scores[qid][f"P_{k}"]
        mrr["MRR"] += scores[qid]["recip_rank"]

    n = len(scores)
    for k in k_values:
        ndcg[f"NDCG@{k}"] = round(ndcg[f"NDCG@{k}"] / n, 5)
        _map[f"MAP@{k}"] = round(_map[f"MAP@{k}"] / n, 5)
        recall[f"Recall@{k}"] = round(recall[f"Recall@{k}"] / n, 5)
        precision[f"P@{k}"] = round(precision[f"P@{k}"] / n, 5)
    mrr["MRR"] = round(mrr["MRR"] / n, 5)
    return {**ndcg, **_map, **recall, **precision, **mrr, "num_topics": n}


# ---------------------------------------------------------------------------
# Phần truy xuất gốc (retrieval_bm25), được tách ra để chỉ mục chỉ cần xây dựng một lần.
# ---------------------------------------------------------------------------
class OfficialBM25:
    def __init__(self, documents, doc_ids):
        from pyserini import analysis
        from gensim.corpora import Dictionary
        from gensim.models import LuceneBM25Model
        from gensim.similarities import SparseMatrixSimilarity

        self.analyzer = analysis.Analyzer(analysis.get_lucene_analyzer())
        self.doc_ids = doc_ids
        corpus = [self.analyzer.analyze(x) for x in
                  tqdm(documents, desc="  analyze corpus", unit="doc", leave=False)]
        self.dictionary = Dictionary(corpus)
        self.model = LuceneBM25Model(dictionary=self.dictionary, k1=0.9, b=0.4)
        bm25_corpus = self.model[list(map(self.dictionary.doc2bow, corpus))]
        self.index = SparseMatrixSimilarity(
            bm25_corpus, num_docs=len(corpus), num_terms=len(self.dictionary),
            normalize_queries=False, normalize_documents=False)

    def search(self, queries, query_ids, desc=""):
        all_scores = {}
        for qid, query in tqdm(list(zip(query_ids, queries)), desc=desc,
                               unit="q", leave=False):
            toks = self.analyzer.analyze(query)
            sims = self.index[self.model[self.dictionary.doc2bow(toks)]].tolist()
            pairs = sorted(zip(self.doc_ids, sims), key=lambda x: x[1],
                           reverse=True)[:1000]
            all_scores[str(qid)] = {d: s for d, s in pairs}
        return all_scores


# ---------------------------------------------------------- các hàm nạp dữ liệu --
def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(ln) for ln in f if ln.strip()]


def load_corpus(path, key):
    ids, texts = [], []
    with open(path, encoding="utf-8") as f:
        for ln in f:
            if ln.strip():
                d = json.loads(ln)
                ids.append(d[key])
                texts.append(d["content"])
    return ids, texts


def topics_1a(domain_dir, split):
    recs = read_jsonl(os.path.join(domain_dir, f"examples_{split}.jsonl"))
    gt = {r["id"]: {g: 1 for g in r["gold_ids"]} for r in recs}
    return [r["query"] for r in recs], [r["id"] for r in recs], gt


def topics_1b(domain_dir, split):
    recs = read_jsonl(os.path.join(domain_dir, f"steps_{split}.jsonl"))
    queries, ids, gt = [], [], {}
    for r in recs:
        for st in r["steps"]:
            # Tempo/run_step.py: combined_query = f"{base_query}\n\nStep: {step_text}"
            queries.append(f"{r['query']}\n\nStep: {st['step_instruction']}")
            ids.append(st["step_id"])
            gt[st["step_id"]] = {g: 1 for g in st["gold_ids"]}
    return queries, ids, gt


def _recor_topics(domain_dir, split, append_history):
    """Cách xây dựng truy vấn theo RECOR/experiments/retrieval/ablation_eval.py."""
    convs = json.load(open(os.path.join(domain_dir, f"benchmark_{split}.json"),
                           encoding="utf-8"))
    queries, ids, gt = [], [], {}
    for c in convs:
        for t in c["turns"]:
            gold = t.get("gold_doc_ids") or t.get("supporting_doc_ids") or []
            if not gold:                       # bản gốc bỏ qua các lượt không có tài liệu chuẩn
                continue
            parts = [t["query"]]
            if append_history:
                hist = t.get("conversation_history", "")
                if hist and hist != "No previous conversation.":
                    parts.append(f"Conversation History:\n{hist}")
            qid = f"{c['id']}_turn_{t['turn_id']}"
            queries.append("\n\n".join(parts))
            ids.append(qid)
            gt[qid] = {g: 1 for g in gold}
    return queries, ids, gt


def topics_2a(domain_dir, split):
    """Cấu hình 'Base' ở Bảng 3/4 của bài báo: chỉ lượt hiện tại."""
    return _recor_topics(domain_dir, split, append_history=False)


def topics_2a_hist(domain_dir, split):
    """Cấu hình '+Hist' ở Bảng 3/4 của bài báo: truy vấn + lịch sử hội thoại."""
    return _recor_topics(domain_dir, split, append_history=True)


def restrict_to_corpus(gt, corpus_ids):
    """Dữ liệu chuẩn gốc đôi khi trỏ đến một tài liệu không có trong kho ngữ liệu; nhãn đánh giá
    như vậy không thể đạt được và bị loại bỏ (cũng bị loại khỏi qrels của bản phát hành)."""
    out = {}
    for qid, docs in gt.items():
        keep = {d: r for d, r in docs.items() if d in corpus_ids}
        if keep:
            out[qid] = keep
    return out


# --------------------------------------------------------------------- main --
def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--data", default=os.path.join(here, "..", "reteco_data"))
    ap.add_argument("--out", default=os.path.join(here, "..", "baselines_official"))
    ap.add_argument("--splits", nargs="+", default=["train", "dev"])
    ap.add_argument("--track1", nargs="*")
    ap.add_argument("--track2", nargs="*")
    args = ap.parse_args()

    data, out = os.path.abspath(args.data), os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    results = defaultdict(lambda: defaultdict(dict))

    jobs = []
    t1 = os.path.join(data, "track1_tempo")
    for dom in (args.track1 if args.track1 is not None else sorted(os.listdir(t1))):
        jobs.append(("track1_tempo", dom, os.path.join(t1, dom), "id",
                     {"1a": topics_1a, "1b": topics_1b}))
    t2 = os.path.join(data, "track2_recor")
    for dom in (args.track2 if args.track2 is not None else sorted(os.listdir(t2))):
        jobs.append(("track2_recor", dom, os.path.join(t2, dom), "doc_id",
                     {"2a": topics_2a, "2a_hist": topics_2a_hist}))

    for track, dom, ddir, corpus_key, subtracks in jobs:
        cache = os.path.join(out, track, dom, "results.json")
        if os.path.isfile(cache):
            results[track][dom] = json.load(open(cache))
            print(f"[cached] {track}/{dom}", flush=True)
            continue
        os.makedirs(os.path.dirname(cache), exist_ok=True)

        print(f"\n=== {track}/{dom} ===", flush=True)
        doc_ids, documents = load_corpus(os.path.join(ddir, "documents.jsonl"),
                                         corpus_key)
        corpus_ids = set(doc_ids)
        print(f"  indexing {len(documents)} documents", flush=True)
        bm25 = OfficialBM25(documents, doc_ids)

        entry = {}
        for sub, loader in subtracks.items():
            for split in args.splits:
                queries, qids, gt = loader(ddir, split)
                if not qids:
                    continue
                gt = restrict_to_corpus(gt, corpus_ids)
                scores = bm25.search(queries, qids, desc=f"  {sub}/{split}")
                scores = {q: v for q, v in scores.items() if q in gt}
                m = calculate_retrieval_metrics(scores, gt)
                entry[f"{sub}_{split}"] = m
                run_path = os.path.join(out, track, dom, f"run_{sub}_{split}.trec")
                with open(run_path, "w") as f:
                    for qid, docs in scores.items():
                        for rank, (d, s) in enumerate(
                                sorted(docs.items(), key=lambda x: -x[1])[:100], 1):
                            f.write(f"{qid}\tQ0\t{d}\t{rank}\t{s:.6f}\tbm25\n")
                print(f"  {sub}/{split:<5} nDCG@10 {m['NDCG@10']:.4f}  "
                      f"({m['num_topics']} topics)", flush=True)

        with open(cache, "w") as f:
            json.dump(entry, f, indent=2)
        results[track][dom] = entry

    # ---- tổng hợp: trung bình macro theo các lĩnh vực, giống như run.py của bản gốc ----
    summary = {"per_domain": {k: dict(v) for k, v in results.items()},
               "macro_average": {}}
    for track, doms in results.items():
        keys = sorted({k for d in doms.values() for k in d})
        summary["macro_average"][track] = {}
        for key in keys:
            vals = [d[key] for d in doms.values() if key in d]
            if not vals:
                continue
            summary["macro_average"][track][key] = {
                m: round(sum(v[m] for v in vals) / len(vals), 5)
                for m in vals[0] if m != "num_topics"}
            summary["macro_average"][track][key]["num_topics"] = sum(
                v["num_topics"] for v in vals)

    with open(os.path.join(out, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 70)
    print("MACRO-AVERAGE nDCG@10 (official BM25, pytrec_eval)")
    print("=" * 70)
    for track, subs in summary["macro_average"].items():
        for key, m in sorted(subs.items()):
            print(f"  {track:<14} {key:<10} nDCG@10 {m['NDCG@10']:.4f}   "
                  f"MAP@10 {m['MAP@10']:.4f}  Recall@10 {m['Recall@10']:.4f}  "
                  f"MRR {m['MRR']:.4f}  ({m['num_topics']} topics)")
    print(f"\nwrote {os.path.join(out, 'summary.json')}")


if __name__ == "__main__":
    main()
