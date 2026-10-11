---
license: cc-by-sa-4.0
language:
  - en
task_categories:
  - text-retrieval
  - question-answering
tags:
  - semeval-2027
  - reasoning-retrieval
  - temporal-reasoning
  - conversational-retrieval
  - rag
pretty_name: RETECO SemEval-2027 Training and Development Data
size_categories:
  - 1M<n<10M
---

<div align="center">

<img src="https://raw.githubusercontent.com/DataScienceUIBK/RETECO/main/docs/assets/brand/reteco-mark.svg" alt="RETECO" width="88">

# RETECO

## Dữ liệu huấn luyện &amp; phát triển · Nhiệm vụ 1 của SemEval-2027

Truy xuất cần suy luận về **thời điểm** bằng chứng còn áp dụng<br>
và **những gì cuộc hội thoại đã xác lập**.

[![Trang web nhiệm vụ](https://img.shields.io/badge/Trang%20web%20nhi%E1%BB%87m%20v%E1%BB%A5-%C4%90ang%20ho%E1%BA%A1t%20%C4%91%E1%BB%99ng-1f6feb?style=for-the-badge)](https://datascienceuibk.github.io/RETECO/)
[![Bộ công cụ khởi đầu](https://img.shields.io/badge/B%E1%BB%99%20c%C3%B4ng%20c%E1%BB%A5%20kh%E1%BB%9Fi%20%C4%91%E1%BA%A7u-GitHub-07101d?style=for-the-badge&logo=github)](https://github.com/DataScienceUIBK/RETECO/tree/main/starter_kit)
[![SemEval-2027](https://img.shields.io/badge/SemEval--2027-Nhi%E1%BB%87m%20v%E1%BB%A5%201-5dd9ff?style=for-the-badge)](https://semeval.github.io/SemEval2027/)

![Lĩnh vực](https://img.shields.io/badge/l%C4%A9nh%20v%E1%BB%B1c-24-informational?style=flat-square)
![Tài liệu](https://img.shields.io/badge/t%C3%A0i%20li%E1%BB%87u-1.67M-informational?style=flat-square)
![Cách chia](https://img.shields.io/badge/train%2Fdev-70%2F30-informational?style=flat-square)
![Dung lượng](https://img.shields.io/badge/dung%20l%C6%B0%E1%BB%A3ng-3.2%20GB-informational?style=flat-square)
![Ngôn ngữ](https://img.shields.io/badge/ng%C3%B4n%20ng%E1%BB%AF-ti%E1%BA%BFng%20Anh-informational?style=flat-square)

**[📋 Nhiệm vụ](https://datascienceuibk.github.io/RETECO/task.html)** ·
**[📊 Dữ liệu](https://datascienceuibk.github.io/RETECO/data.html)** ·
**[📐 Đánh giá](https://datascienceuibk.github.io/RETECO/evaluation.html)** ·
**[🚀 Tham gia](https://datascienceuibk.github.io/RETECO/participate.html)** ·
**[🧰 Bộ công cụ khởi đầu](https://github.com/DataScienceUIBK/RETECO/tree/main/starter_kit)**

</div>

---

## 🎯 Tổng quan nhanh

| | |
| :--- | :--- |
| **Là gì** | Dữ liệu huấn luyện và phát triển chính thức của RETECO, nhiệm vụ chung SemEval-2027 về truy xuất định hướng suy luận |
| **Phạm vi** | 2 hạng mục · 5 hạng mục con · 24 lĩnh vực độc lập, tự chứa đầy đủ |
| **Quy mô** | 1,674,300 tài liệu · 1,730 truy vấn thời gian · 3,976 bước · 707 hội thoại · 2,971 lượt |
| **Cách chia** | 70 / 30 train / dev cho mỗi lĩnh vực · seed cố định · nhãn đánh giá chuẩn cho cả hai tập |
| **Chỉ số** | nDCG@10 qua `pytrec_eval` |
| **Giấy phép** | Văn bản: CC BY-SA 4.0 · Chú thích của RETECO: CC BY 4.0 |
| **Liên hệ** | [abdelrahman.abdallah@uibk.ac.at](mailto:abdelrahman.abdallah@uibk.ac.at) |

> ⚠️ **Đây không phải tập kiểm tra SemEval.** Chỉ gồm train và dev. Việc chấm điểm cuối cùng dùng một
> tập kiểm tra riêng, chưa từng được công bố công khai, với nhãn đánh giá chuẩn được giữ kín.

---

## 🆕 v1.1 · Loại bỏ trùng lặp trong kho ngữ liệu Hạng mục 1

Kho ngữ liệu Hạng mục 1 kế thừa nhiều bản trùng lặp chính xác từ TEMPO gốc: cùng một
văn bản web được lưu dưới nhiều ID (phần đầu ghi giấy phép, tuyên bố miễn trừ trách nhiệm, và cùng một phần
của trang được lưu một lần cho mỗi truy vấn đã truy xuất nó). v1.1 giữ một bản cho mỗi văn bản.

- **Hạng mục 1: 1,654,055 → 1,167,159 tài liệu** (đã loại bỏ 486,896 bản trùng lặp, 29.4%).
  Mức giảm lớn nhất: bitcoin 50%, cardano 46%, history 44%, monero 37%.
- **Không mất văn bản chuẩn nào.** Khi một nhóm bản sao có chứa tài liệu chuẩn, ID chuẩn
  là ID được giữ lại. Ở những chỗ hai ID chuẩn chứa cùng một văn bản, 92 ID được gộp
  thành một; 57 dòng qrels liệt kê cùng một văn bản hai lần cho một truy vấn hoặc một bước cũng được gộp.
  Mọi chú thích hướng dẫn (guidance) đều được giữ lại, nên 36 bản ghi guidance hiện có nhiều hơn một
  chú thích cho cùng một `doc_id` (tổng cộng 53 chú thích dư ra).
- **Chỉ gộp các văn bản giống hệt nhau.** Khác biệt về khoảng trắng (dấu cách, ngắt
  dòng, dòng trống) được bỏ qua; mọi khác biệt khác, kể cả chỉ ở dấu câu
  hay định dạng, đều khiến các tài liệu được giữ riêng, nên không có ngày tháng, con số hay phiên bản nào
  bị gộp mất.
- **Mọi ID bị loại bỏ đều được ánh xạ sang ID được giữ lại** trong `track1_tempo/<domain>/duplicate_map.json`.
  Để chấm điểm một kết quả chạy tạo trên v1.0, hãy thay từng ID tài liệu theo bảng ánh xạ và bỏ
  các ID lặp lại trong cùng một danh sách xếp hạng.
- **Không thay đổi:** truy vấn, các bước, cách chia tập, ID chủ đề và toàn bộ Hạng mục 2.
- v1.0 vẫn có sẵn: `hf download DataScience-UIBK/RETECO-SemEval2027 --repo-type dataset --revision v1.0`.

---

## 📦 Nội dung bộ dữ liệu

Hai hạng mục, 24 lĩnh vực độc lập, mỗi lĩnh vực tự chứa đầy đủ với kho ngữ liệu
truy xuất của riêng nó. Không cần lấy thêm gì từ nơi khác.

| | Lĩnh vực | Tài liệu kho ngữ liệu | Mục nhiệm vụ |
| --- | ---: | ---: | --- |
| **Hạng mục 1 · Truy xuất có căn cứ thời gian** | 13 | 1,167,159 | 1,730 truy vấn · 3,976 bước |
| **Hạng mục 2 · Truy xuất hội thoại** | 11 | 507,141 | 707 hội thoại · 2,971 lượt |

Năm hạng mục con của RETECO sử dụng dữ liệu này như sau:

| Hạng mục con | Bạn truy xuất cho | Tệp bạn cần |
| --- | --- | --- |
| **1a** Truy xuất theo thời gian | toàn bộ một truy vấn thời gian | `examples_*.jsonl` + `qrels_*.txt` |
| **1b** Truy xuất từng bước | từng bước phân rã của một truy vấn | `steps_*.jsonl` + `qrels_steps_*.txt` |
| **2a** Truy xuất hội thoại | từng lượt mục tiêu của một hội thoại | `benchmark_*.json` + `qrels_*.txt` |
| **2b** Sinh câu trả lời từ đoạn văn chuẩn | câu trả lời từ các đoạn văn chuẩn được cung cấp | `benchmark_*.json` |
| **2c** RAG hội thoại đầy đủ | truy xuất **và** trả lời cho mỗi lượt | `benchmark_*.json` + `qrels_*.txt` |

---

## ✂️ Cách chia tập: train / dev

Mỗi lĩnh vực được chia theo tỷ lệ **70 / 30** với seed cố định (`20270101`). Danh sách ID
chính xác theo từng lĩnh vực có trong [`split_manifest.json`](split_manifest.json), nên
cách chia hoàn toàn có thể tái lập và kiểm tra.

| | Huấn luyện | Phát triển |
| --- | ---: | ---: |
| Truy vấn Hạng mục 1 | 1,211 | 519 |
| Bước Hạng mục 1 | 2,762 | 1,214 |
| Hội thoại Hạng mục 2 | 496 | 211 |
| Lượt Hạng mục 2 | 2,113 | 858 |

Ba quy tắc xác định cách chia:

1. **Kho ngữ liệu không bao giờ bị chia.** `documents.jsonl` là toàn bộ kho ngữ liệu của lĩnh vực và
   được dùng chung cho train và dev — việc truy xuất luôn chạy trên mọi tài liệu của
   lĩnh vực, ở cả hai tập.
2. **Hạng mục 1 chia theo truy vấn.** Các bước phân rã của một truy vấn nằm lồng *bên trong*
   chính bản ghi của nó, nên một bước không bao giờ bị tách khỏi truy vấn của nó.
3. **Hạng mục 2 chia theo toàn bộ cuộc hội thoại.** Mọi lượt của một hội thoại nằm
   trong cùng một tập, nên không có lịch sử hội thoại nào bị rò rỉ qua ranh giới.

Nhãn đánh giá chuẩn được phát hành cho **cả hai** tập. Dùng `train` để phát triển và
tinh chỉnh; dùng `dev` làm phép kiểm tra trên dữ liệu giữ lại. Tập kiểm tra ẩn của SemEval là riêng biệt.

---

## 🗂️ Cấu trúc thư mục

```text
track1_tempo/<domain>/
  documents.jsonl              # toàn bộ kho ngữ liệu, dùng chung cho cả hai tập: {id, content}
  duplicate_map.json           # v1.1: ID trùng lặp bị loại bỏ -> ID được giữ lại
  examples_train.jsonl         # 1a: {id, query, gold_ids, gold_answers}
  examples_dev.jsonl
  steps_train.jsonl            # 1b: một bản ghi cho mỗi truy vấn, các bước lồng bên trong
  steps_dev.jsonl
  guidance_train.jsonl         # siêu dữ liệu thời gian + chú thích đoạn văn chuẩn
  guidance_dev.jsonl
  qrels_train.txt              # nhãn đánh giá 1a — TREC: qid 0 docid 1
  qrels_dev.txt
  qrels_steps_train.txt        # nhãn đánh giá 1b — ID chủ đề = step_id
  qrels_steps_dev.txt

track2_recor/<domain>/
  documents.jsonl              # toàn bộ kho ngữ liệu: {doc_id, content}
  benchmark_train.json         # hội thoại: các lượt, lịch sử, gold_doc_ids
  benchmark_dev.json
  qrels_train.txt              # nhãn đánh giá 2a/2c — qid = <conv_id>_turn_<turn_id>
  qrels_dev.txt

split_manifest.json            # seed, số lượng theo lĩnh vực, danh sách ID chính xác, nguồn gốc
```

**Các lĩnh vực của Hạng mục 1** — bitcoin, cardano, economics, genealogy, history, hsm, iota,
law, monero, politics, quant, travel, workplace.
**Các lĩnh vực của Hạng mục 2** — biology, drones, earth_science, economics, hardware, law,
medicalsciences, politics, psychology, robotics, sustainable_living.

### 📄 Định dạng bản ghi

```jsonc
// track1_tempo/<domain>/examples_{train,dev}.jsonl        — Hạng mục con 1a
{"id": "124973_5", "query": "How long does Bitcoin Core store forked chains? ...",
 "gold_ids": ["bitcoin/45eff6bd_1297.txt", ...], "gold_answers": ["..."]}

// track1_tempo/<domain>/steps_{train,dev}.jsonl           — Hạng mục con 1b
{"id": "124973_5", "query": "How long does Bitcoin Core store forked chains? ...",
 "steps": [
   {"step_id": "124973_5_step1", "step": 1,
    "step_instruction": "Consult Bitcoin Core official documentation ...",
    "gold_ids": ["bitcoin/45eff6bd_1297.txt"]},
   {"step_id": "124973_5_step2", "step": 2, "...": "..."}]}

// track2_recor/<domain>/benchmark_{train,dev}.json        — Hạng mục con 2a/2b/2c
{"id": "ex_3025", "task": "drones", "original_query": "...", "original_answer": "...",
 "turns": [
   {"turn_id": 1, "query": "In FPV drone motors, why is lubrication only ...",
    "answer": "...", "conversation_history": "No previous conversation.",
    "subquestion_reasoning": "...", "gold_doc_ids": ["drones_ex_3025_doc_0", ...]}],
 "metadata": {"num_turns": 4, "gold_doc_count": 11, "source": "annotated_data"}}

// qrels — TREC 4 cột, mức liên quan nhị phân, phân tách bằng tab
124973_5        0       bitcoin/45eff6bd_1297.txt       1
ex_3025_turn_1  0       drones_ex_3025_doc_0            1
```

**ID chủ đề** (dùng chính xác các dạng này trong bài nộp):
1a `id` · 1b `step_id` = `<query_id>_step<n>` · 2a/2c `<conversation_id>_turn_<turn_id>`

---

## 🚀 Cách sử dụng

### 1️⃣ Tải xuống

```bash
pip install huggingface_hub
hf download DataScience-UIBK/RETECO-SemEval2027 --repo-type dataset \
    --local-dir reteco_data
```

### 2️⃣ Lấy các hệ thống cơ sở

```bash
git clone https://github.com/DataScienceUIBK/RETECO.git
cd RETECO/starter_kit
pip install -r requirements.txt          # pytrec_eval, gensim, pyserini (cần JDK)
```

### 3️⃣ Chạy trên **train**, sau đó trên **dev**

Script chạy nhận tham số `--splits`, nên train và dev là cùng một lệnh, chỉ khác một
từ. Phát triển trên `train`; giữ `dev` làm phép kiểm tra trên dữ liệu giữ lại.

```bash
export JAVA_HOME=/path/to/jdk
export JVM_PATH=$JAVA_HOME/lib/server/libjvm.so

# tập dùng để phát triển (train) — tinh chỉnh ở đây
python official_baseline.py --data ../../reteco_data --out ../../baselines \
    --splits train

# tập giữ lại (dev) — kiểm tra ở đây
python official_baseline.py --data ../../reteco_data --out ../../baselines \
    --splits dev

# hoặc cả hai trong một lượt (kho ngữ liệu được lập chỉ mục một lần và dùng lại cho các tập)
python official_baseline.py --data ../../reteco_data --out ../../baselines \
    --splits train dev

# một lĩnh vực, để chạy thử nhanh (smoke test)
python official_baseline.py --track1 iota --track2 drones --splits train dev
```

Mỗi lần chạy ghi, cho từng lĩnh vực, một tệp kết quả chạy TREC `run_<subtrack>_<split>.trec` và một
tệp `results.json`; thư mục cấp cao nhất có tệp `summary.json` chứa các chỉ số theo từng lĩnh vực và
trung bình macro. Kết quả theo lĩnh vực được lưu đệm, nên một lần chạy bị gián đoạn sẽ
tiếp tục từ chỗ đã dừng.

### 4️⃣ Chấm điểm kết quả chạy của bạn

nDCG@10 qua `pytrec_eval` là chỉ số chính thức của RETECO.

```bash
python -c "
import pytrec_eval, json
qrels = {}
for ln in open('reteco_data/track1_tempo/iota/qrels_dev.txt'):
    q,_,d,r = ln.split(); qrels.setdefault(q,{})[d] = int(r)
run = {}
for ln in open('my_run.trec'):
    q,_,d,rank,score,_tag = ln.split(); run.setdefault(q,{})[d] = float(score)
ev = pytrec_eval.RelevanceEvaluator(qrels, {'ndcg_cut.10'})
s = ev.evaluate(run)
print('nDCG@10', sum(v['ndcg_cut_10'] for v in s.values())/len(s))
"
```

Một hệ thống cơ sở khởi đầu và trình chấm điểm không cần phụ thuộc (`bm25_baseline.py`, `scorer.py`)
cũng có trong `starter_kit/` nếu bạn muốn bắt đầu mà không cần cài JDK.

---

## 📈 Hệ thống cơ sở tham chiếu

BM25 trên bản phát hành này, lấy trung bình macro theo các lĩnh vực, nDCG@10. Truy xuất và
chấm điểm dùng cùng cách cài đặt với các bộ đánh giá chuẩn gốc: bộ phân tích Lucene
cùng `LuceneBM25Model` của gensim, k1=0.9 / b=0.4; dùng `pytrec_eval` để tính chỉ số.

| Hạng mục con | Huấn luyện | Phát triển |
| --- | ---: | ---: |
| 1a · truy xuất toàn bộ truy vấn | 0.1075 | 0.1147 |
| 1b · truy xuất từng bước | 0.1024 | 0.1177 |
| 2a · chỉ lượt hiện tại | 0.1837 | 0.1827 |
| 2a · truy vấn + lịch sử hội thoại | 0.4539 | 0.4379 |

Số liệu Hạng mục 1 được đo trên kho ngữ liệu v1.1 đã loại bỏ trùng lặp. Trên v1.0, chúng là
0.0879 / 0.0967 (1a, train / dev) và 0.0852 / 0.1063 (1b), chủ yếu vì
các bản sao lặp lại của cùng một văn bản từng chiếm chỗ trong top-10.

Có hai điều rút ra từ bảng này. Chỉ so khớp từ vựng thì yếu trên Hạng mục 1 —
căn cứ thời gian không phải là bài toán từ khóa, và còn rất nhiều dư địa cải thiện.
Còn trên Hạng mục 2, chỉ cần nối thêm lịch sử hội thoại là BM25 đã tăng từ 0.18
lên 0.44, đó chính là độ lớn của tín hiệu mà một hệ thống hội thoại cần khai thác.

Số liệu theo từng lĩnh vực cho cả hai tập: `BASELINE_RESULTS.md` trong kho mã RETECO.

---

## 🔗 Nguồn gốc

Được xây dựng một cách tất định từ các phiên bản gốc được cố định:

| Nguồn | Bộ dữ liệu | Phiên bản (revision) |
| --- | --- | --- |
| TEMPO | [`tempo26/Tempo`](https://huggingface.co/datasets/tempo26/Tempo) | `f9df06c05688225e37701974d23c8e3c5d4efaf6` |
| RECOR | [`RECOR-Benchmark/RECOR`](https://huggingface.co/datasets/RECOR-Benchmark/RECOR) | `d9faa639019dcfa1a1fea2aece55ebcba3083c00` |

Mọi số lượng truy vấn, bước, hội thoại và lượt đã công bố đều được tái lập chính xác, kho ngữ liệu
Hạng mục 2 cũng vậy. Kho ngữ liệu Hạng mục 1 là kho ngữ liệu gốc sau khi loại bỏ các bản
trùng lặp chính xác (xem phần v1.1 ở trên); `duplicate_map.json` cho phép khôi phục mọi ID
gốc. Bốn cấu hình viết lại truy vấn bằng LLM của TEMPO **không** được đưa vào: đầu vào
chính thức của hệ thống là truy vấn gốc. Ba ID tài liệu chuẩn của RECOR trỏ đến
các tài liệu không có trong bất kỳ kho ngữ liệu nào; chúng bị loại khỏi qrels để vẫn có thể đạt được
xếp hạng hoàn hảo, và được liệt kê theo từng lĩnh vực trong `split_manifest.json`.

---

## ⚖️ Giấy phép

Hai giấy phép, vì văn bản và chú thích có nguồn gốc khác nhau:

- **Kho ngữ liệu và văn bản hỏi đáp — CC BY-SA 4.0.** Toàn bộ văn bản đoạn văn có nguồn gốc từ Stack
  Exchange (trực tiếp, hoặc thông qua [BRIGHT](https://huggingface.co/datasets/xlangai/BRIGHT)
  đối với sáu lĩnh vực của Hạng mục 2). Các đóng góp trên Stack Exchange theo giấy phép CC BY-SA, tức là
  chia sẻ tương tự (share-alike): việc phân phối lại phải giữ nguyên giấy phép và phần ghi công. Vì
  lý do này, kho dữ liệu được gắn nhãn `cc-by-sa-4.0`.
- **Chú thích của RETECO — CC BY 4.0.** Việc phân chia tập, qrels TREC và
  `split_manifest.json` do ban tổ chức RETECO đóng góp.

Quyền ghi công cho nội dung gốc vẫn thuộc về các tác giả ban đầu trên Stack Exchange.
Không phân phối lại dữ liệu đánh giá ẩn hoặc các nhãn chuẩn suy luận được.

---

## 📚 Trích dẫn

```bibtex
@article{abdallah2026tempo,
  title={TEMPO: A Realistic Multi-Domain Benchmark for Temporal Reasoning-Intensive Retrieval},
  author={Abdallah, Abdelrahman and Ali, Mohammed and Abdul-Mageed, Muhammad and Jatowt, Adam},
  journal={arXiv preprint arXiv:2601.09523}, year={2026},
  url={https://arxiv.org/abs/2601.09523}
}

@inproceedings{ali2026recor,
  title={RECOR: Reasoning-focused Multi-turn Conversational Retrieval Benchmark},
  author={Ali, Mohammed and Abdallah, Abdelrahman and Agarwal, Amit and Patel, Hitesh Laxmichand and Jatowt, Adam},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  pages={2688--2723}, year={2026},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2026.findings-acl.129}
}
```

Trích dẫn bài mô tả nhiệm vụ RETECO sẽ được bổ sung khi kỷ yếu SemEval-2027
được xuất bản.
