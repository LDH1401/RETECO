<div align="center">

<img src="docs/assets/brand/reteco-mark.svg" alt="RETECO" width="88">

# RETECO

### Shared task SemEval-2027 về reasoning-oriented retrieval

Truy xuất (retrieval) cần suy luận (reasoning) về **thời điểm** bằng chứng còn áp dụng<br>
và **những gì cuộc hội thoại đã xác lập**.

[![SemEval-2027 Task 1](https://img.shields.io/badge/SemEval--2027-Task%201-07101d?style=for-the-badge)](https://semeval.github.io/SemEval2027/)
[![Bộ dữ liệu trên Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20B%E1%BB%99%20d%E1%BB%AF%20li%E1%BB%87u-%C4%90%C3%A3%20ph%C3%A1t%20h%C3%A0nh-5dd9ff?style=for-the-badge)](https://huggingface.co/datasets/DataScience-UIBK/RETECO-SemEval2027)
[![Trang web](https://img.shields.io/badge/Trang%20web-%C4%90ang%20ho%E1%BA%A1t%20%C4%91%E1%BB%99ng-1f6feb?style=for-the-badge)](https://datascienceuibk.github.io/RETECO/)

![Lĩnh vực](https://img.shields.io/badge/l%C4%A9nh%20v%E1%BB%B1c-24-informational?style=flat-square)
![Tài liệu](https://img.shields.io/badge/t%C3%A0i%20li%E1%BB%87u-1.67M-informational?style=flat-square)
![Split](https://img.shields.io/badge/train%2Fdev-70%2F30-informational?style=flat-square)
![Ngôn ngữ](https://img.shields.io/badge/ng%C3%B4n%20ng%E1%BB%AF-ti%E1%BA%BFng%20Anh-informational?style=flat-square)
![Giấy phép văn bản](https://img.shields.io/badge/v%C4%83n%20b%E1%BA%A3n-CC%20BY--SA%204.0-brightgreen?style=flat-square)
![Giấy phép chú thích](https://img.shields.io/badge/ch%C3%BA%20th%C3%ADch-CC%20BY%204.0-brightgreen?style=flat-square)

**[🌐 Trang web](https://datascienceuibk.github.io/RETECO/)** ·
**[📋 Task](https://datascienceuibk.github.io/RETECO/task.html)** ·
**[📊 Dữ liệu](https://datascienceuibk.github.io/RETECO/data.html)** ·
**[🔍 Dữ liệu mẫu](https://datascienceuibk.github.io/RETECO/samples.html)** ·
**[📐 Đánh giá](https://datascienceuibk.github.io/RETECO/evaluation.html)** ·
**[📄 Bài báo](https://datascienceuibk.github.io/RETECO/papers.html)** ·
**[🚀 Tham gia](https://datascienceuibk.github.io/RETECO/participate.html)**

[📕 Đọc đề xuất task (PDF)](docs/assets/papers/RETECO_SemEval_2027_Proposal.pdf)

</div>

---

## 📰 Tin tức

| Ngày | | Cập nhật |
| :--- | :---: | :--- |
| **25/09/2026** | 🧹 | **Dữ liệu v1.1: đã loại bỏ tài liệu trùng lặp khỏi Track 1.** Các văn bản được lưu nhiều lần dưới các ID khác nhau giờ chỉ được giữ lại một lần (1,654,055 → 1,167,159 tài liệu (document) của Track 1). Gold label được giữ nguyên; truy vấn (query), các split và Track 2 không thay đổi. Vui lòng tải lại dữ liệu và xây dựng lại chỉ mục (index) — [những gì đã thay đổi](https://datascienceuibk.github.io/RETECO/data.html#versions). |
| **30/08/2026** | 🚀 | **Đã phát hành dữ liệu huấn luyện và phát triển (train/dev).** Cả 24 lĩnh vực (domain), 2.16M tài liệu, các split train/dev theo tỷ lệ 70/30 kèm gold judgment cho cả hai — [tải về từ Hugging Face](https://huggingface.co/datasets/DataScience-UIBK/RETECO-SemEval2027). |
| **30/08/2026** | 🧰 | **Đã công bố starter kit.** Các baseline BM25, scorer chính thức dùng `pytrec_eval`, format checker cho bài nộp và script build tất định (deterministic) — [`starter_kit/`](starter_kit/). |
| **30/08/2026** | 🧪 | **Các baseline tham chiếu** cho mọi sub-track truy xuất trên cả hai split — [`BASELINE_RESULTS.md`](starter_kit/BASELINE_RESULTS.md). |
| **11/08/2026** | ✅ | **RETECO được chấp nhận là SemEval-2027 Task 1** — [xem danh sách task](https://semeval.github.io/SemEval2027/). |
| **08/08/2026** | 📦 | **Đã công bố dữ liệu mẫu** — một gói nhỏ gọn, đã được con người kiểm tra, thể hiện chính xác định dạng bản ghi và bài nộp. [Xem các mẫu](https://datascienceuibk.github.io/RETECO/samples.html). |

> [!NOTE]
> **Sắp tới:** đăng ký, mailing list cho người tham gia và nền tảng thi đấu.
> Các thông tin này sẽ được thông báo tại đây và trên
> [hướng dẫn tham gia](https://datascienceuibk.github.io/RETECO/participate.html).

---

## ⚡ Bắt đầu nhanh

```bash
# 1 — lấy dữ liệu (v1.1, ~3.2 GB; mọi thứ bạn cần, trong một lần tải)
pip install huggingface_hub
hf download DataScience-UIBK/RETECO-SemEval2027 --repo-type dataset --local-dir reteco_data

# 2 — lấy các baseline
git clone https://github.com/DataScienceUIBK/RETECO.git
cd RETECO/starter_kit && pip install -r requirements.txt

# 3 — phát triển trên train, sau đó tự kiểm tra trên dev
python official_baseline.py --data ../../reteco_data --splits train
python official_baseline.py --data ../../reteco_data --splits dev
```

Mới làm quen với task? [Hướng dẫn tham gia](https://datascienceuibk.github.io/RETECO/participate.html)
sẽ dẫn bạn qua các bước chọn sub-track, xây dựng hệ thống và chấm điểm cục bộ
bằng đúng metric mà leaderboard sử dụng.

## 🎯 Các track

| Track | Sub-track | Đầu ra yêu cầu | Điểm truy xuất chính thức |
| --- | --- | --- | --- |
| 1 · Temporal Grounded Retrieval | 1a Temporal Retrieval | Tài liệu được xếp hạng cho mỗi truy vấn | nDCG@10 |
| 1 · Temporal Grounded Retrieval | 1b Step-wise Retrieval | Tài liệu được xếp hạng cho mỗi bước được cung cấp | nDCG@10 cấp bước |
| 2 · Conversational Retrieval | 2a Conversational Retrieval | Đoạn văn (passage) được xếp hạng cho mỗi lượt mục tiêu (target turn) | nDCG@10 |
| 2 · Conversational Retrieval | 2b Gold-Passage Generation | Câu trả lời có căn cứ (grounded answer) | Năm tiêu chí đánh giá sinh văn bản (generation) |
| 2 · Conversational Retrieval | 2c Full Conversational RAG | Đoạn văn được xếp hạng + câu trả lời có căn cứ | nDCG@10; phần sinh văn bản được báo cáo song song |

Xem [định nghĩa task đầy đủ](https://datascienceuibk.github.io/RETECO/task.html)
và [kế hoạch đánh giá](https://datascienceuibk.github.io/RETECO/evaluation.html).

## 📊 Dữ liệu huấn luyện và phát triển

Bản phát hành train/dev chính thức có trên Hugging Face:
**[DataScience-UIBK/RETECO-SemEval2027](https://huggingface.co/datasets/DataScience-UIBK/RETECO-SemEval2027)**

```bash
hf download DataScience-UIBK/RETECO-SemEval2027 --repo-type dataset --local-dir reteco_data
```

Một lần tải chứa mọi thứ cần thiết cho bất kỳ sub-track nào: toàn bộ corpus truy xuất
của cả 24 lĩnh vực, các tệp task và qrels TREC cho cả hai split.

| | train | dev |
| --- | ---: | ---: |
| Truy vấn của Track 1 | 1,211 | 519 |
| Bước của Track 1 | 2,762 | 1,214 |
| Hội thoại của Track 2 | 496 | 211 |
| Lượt của Track 2 | 2,113 | 858 |

Tỷ lệ chia là 70/30 cho mỗi lĩnh vực với seed cố định. Corpus không bao giờ bị chia;
Track 1 chia theo truy vấn (các bước nằm lồng trong bản ghi truy vấn của chúng) và
Track 2 chia theo toàn bộ cuộc hội thoại. Gold judgment được cung cấp cho cả hai split —
tập test SemEval là riêng biệt và không bao giờ được phát hành.

### 🧰 Starter kit

[`starter_kit/`](starter_kit/) chứa các baseline, scorer, format checker và
script build tạo ra bản phát hành từ các revision upstream được cố định (pinned), cùng với
script loại bỏ trùng lặp (deduplication) tạo ra dữ liệu v1.1 và script kiểm chứng của nó.

```bash
cd starter_kit && pip install -r requirements.txt
python official_baseline.py --data ../../reteco_data --splits train dev
```

BM25 tham chiếu, nDCG@10, lấy trung bình macro (macro-average) theo các lĩnh vực:

| Sub-track | Truy vấn đưa vào retriever | train | dev |
| --- | --- | ---: | ---: |
| 1a Temporal retrieval | Toàn bộ truy vấn | 0.1075 | 0.1147 |
| 1b Step-wise retrieval | Truy vấn + chỉ dẫn của bước (step instruction) | 0.1024 | 0.1177 |
| 2a Conversational retrieval | Chỉ lượt hiện tại | 0.1837 | 0.1827 |
| 2a Conversational retrieval | Lượt + lịch sử hội thoại | 0.4539 | 0.4379 |

Số liệu Track 1 được đo trên dữ liệu v1.1. Số liệu theo từng lĩnh vực: [`starter_kit/BASELINE_RESULTS.md`](starter_kit/BASELINE_RESULTS.md).

## 🔍 Dữ liệu mẫu

Repository chứa một gói nhỏ gọn, đã được con người kiểm tra, sao chép từ các
bản phát hành chính thức của TEMPO và RECOR:

- Track 1: 5 ví dụ TEMPO, 26 đoạn văn hỗ trợ (supporting passage) và 26 positive qrels.
- Track 2: 4 hội thoại RECOR gồm 13 lượt, 15 đoạn văn hỗ trợ
  và 32 positive qrels.
- Một manifest cố định (pin) revision của các bộ dữ liệu nguồn và ID của các bản ghi được chọn.

[Xem mẫu trực tuyến](https://datascienceuibk.github.io/RETECO/samples.html) ·
[Tải tệp ZIP](https://datascienceuibk.github.io/RETECO/assets/downloads/RETECO_curated_sample_data.zip) ·
[Duyệt các tệp nguồn](docs/sample_data/)

Dữ liệu mẫu là bản minh họa về định dạng và tính khả thi—không phải một split benchmark mới
và không phải tập test ẩn của SemEval. Nó chỉ chứa positive evidence được tham chiếu,
nên không được đánh giá các hệ thống truy xuất chỉ trên corpus mẫu.

## 🗂️ Dữ liệu và corpus

### Track 1: TEMPO

[TEMPO](https://github.com/tempo-bench/Tempo) gồm 1,730 truy vấn thời gian phức tạp,
3,976 bước truy xuất phân rã (decomposed retrieval step) và 1,654,055 tài liệu thuộc 13 corpus
lĩnh vực độc lập. RETECO v1.1 giữ một bản cho mỗi văn bản bị trùng lặp,
còn lại 1,167,159 tài liệu.

| Nhóm | Lĩnh vực | Truy vấn | Tài liệu trong corpus (TEMPO) | RETECO v1.1 |
| --- | --- | ---: | ---: | ---: |
| Blockchain | Bitcoin | 100 | 153,291 | 76,706 |
| Blockchain | Cardano | 51 | 87,201 | 47,509 |
| Blockchain | IOTA | 10 | 10,372 | 9,680 |
| Blockchain | Monero | 65 | 85,093 | 53,955 |
| Khoa học xã hội | Kinh tế học | 83 | 93,756 | 74,692 |
| Khoa học xã hội | Luật | 35 | 43,288 | 36,110 |
| Khoa học xã hội | Chính trị | 150 | 183,394 | 135,207 |
| Khoa học xã hội | Lịch sử | 801 | 356,493 | 200,252 |
| Ứng dụng | Tài chính định lượng | 34 | 28,785 | 25,040 |
| Ứng dụng | Du lịch | 100 | 177,677 | 158,771 |
| Ứng dụng | Nơi làm việc | 36 | 64,659 | 43,584 |
| Ứng dụng | Phả hệ học | 115 | 156,228 | 136,101 |
| STEM | Lịch sử khoa học và toán học | 150 | 213,818 | 169,552 |
| **Tổng** | **13 lĩnh vực** | **1,730** | **1,654,055** | **1,167,159** |

- Bộ dữ liệu: [tempo26/Tempo trên Hugging Face](https://huggingface.co/datasets/tempo26/Tempo)
- Mã nguồn và baseline: [tempo-bench/Tempo](https://github.com/tempo-bench/Tempo)
- Bài báo: [arXiv:2601.09523](https://arxiv.org/abs/2601.09523)

### Track 2: RECOR

[RECOR](https://github.com/RECOR-Benchmark/RECOR) gồm 707 hội thoại,
2,971 lượt mục tiêu và 507,141 tài liệu thuộc 11 corpus lĩnh vực. Sáu lĩnh vực
đến từ BRIGHT và năm lĩnh vực từ StackExchange.

| Nguồn | Lĩnh vực | Hội thoại | Lượt | Tài liệu trong corpus |
| --- | --- | ---: | ---: | ---: |
| BRIGHT | Sinh học | 85 | 362 | 57,359 |
| BRIGHT | Khoa học Trái Đất | 98 | 454 | 121,249 |
| BRIGHT | Kinh tế học | 74 | 288 | 50,220 |
| BRIGHT | Tâm lý học | 84 | 333 | 52,835 |
| BRIGHT | Robot học | 68 | 259 | 61,961 |
| BRIGHT | Lối sống bền vững | 78 | 319 | 60,792 |
| StackExchange | Máy bay không người lái | 37 | 142 | 16,381 |
| StackExchange | Phần cứng | 46 | 188 | 26,308 |
| StackExchange | Luật | 50 | 230 | 20,027 |
| StackExchange | Khoa học y khoa | 44 | 183 | 23,297 |
| StackExchange | Chính trị | 43 | 213 | 16,712 |
| **Tổng** | **11 lĩnh vực** | **707** | **2,971** | **507,141** |

- Bộ dữ liệu: [RECOR-Benchmark/RECOR trên Hugging Face](https://huggingface.co/datasets/RECOR-Benchmark/RECOR)
- Mã nguồn và baseline: [RECOR-Benchmark/RECOR](https://github.com/RECOR-Benchmark/RECOR)
- Bài báo đã công bố: [ACL Anthology 2026.findings-acl.129](https://aclanthology.org/2026.findings-acl.129/)

Đây là các nguồn upstream. Bản phát hành RETECO ở trên đóng gói chúng thành
các split train/dev kèm qrels. Việc chấm điểm SemEval cuối cùng dùng một tập test riêng,
chưa từng được công bố công khai, với gold judgment được giữ kín.

## 📄 Bài báo

### TEMPO

**TEMPO: A Realistic Multi-Domain Benchmark for Temporal Reasoning-Intensive
Retrieval**  
Abdelrahman Abdallah, Mohammed Ali, Muhammad Abdul-Mageed và Adam Jatowt.  
arXiv:2601.09523, 2026. [Bài báo](https://arxiv.org/abs/2601.09523)

```bibtex
@article{abdallah2026tempo,
  title={TEMPO: A Realistic Multi-Domain Benchmark for Temporal Reasoning-Intensive Retrieval},
  author={Abdallah, Abdelrahman and Ali, Mohammed and Abdul-Mageed, Muhammad and Jatowt, Adam},
  journal={arXiv preprint arXiv:2601.09523},
  year={2026},
  url={https://arxiv.org/abs/2601.09523}
}
```

### RECOR

**RECOR: Reasoning-focused Multi-turn Conversational Retrieval Benchmark**  
Mohammed Ali, Abdelrahman Abdallah, Amit Agarwal, Hitesh Laxmichand Patel và
Adam Jatowt.  
Findings of ACL 2026, trang 2688–2723.
[Bài báo](https://aclanthology.org/2026.findings-acl.129/) ·
[DOI](https://doi.org/10.18653/v1/2026.findings-acl.129)

```bibtex
@inproceedings{ali2026recor,
  title={RECOR: Reasoning-focused Multi-turn Conversational Retrieval Benchmark},
  author={Ali, Mohammed and Abdallah, Abdelrahman and Agarwal, Amit and Patel, Hitesh Laxmichand and Jatowt, Adam},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  pages={2688--2723},
  year={2026},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2026.findings-acl.129},
  url={https://aclanthology.org/2026.findings-acl.129/}
}
```

Cả hai bản ghi đều có trong [CITATIONS.bib](CITATIONS.bib). Trích dẫn bài báo task
chính thức của RETECO sẽ được bổ sung sau khi bài mô tả task (task description) SemEval-2027
được công bố.

## 🗺️ Sơ đồ repository

```text
RETECO/
├── docs/                         # Trang web GitHub Pages
│   ├── index.html
│   ├── task.html
│   ├── data.html                 # Chi tiết corpus theo từng lĩnh vực
│   ├── samples.html              # Ví dụ dễ đọc cho con người
│   ├── evaluation.html
│   ├── papers.html               # Đề xuất, bài báo, trích dẫn
│   ├── participate.html
│   ├── timeline.html
│   ├── sample_data/              # Dữ liệu mẫu tuyển chọn, máy đọc được
│   └── assets/
│       ├── downloads/
│       └── papers/
├── starter_kit/                  # Baseline, scorer, format checker, script build
├── .github/workflows/            # Triển khai Pages
├── CITATIONS.bib
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── README.md
```

Format checker, scorer cục bộ và các baseline khởi đầu nằm trong
[`starter_kit/`](starter_kit/). Các bài nộp mẫu sẽ được bổ sung khi giao diện của
nền tảng thi đấu được chốt.

## 💻 Xem trước trang web trên máy

Trang web không có phụ thuộc (dependency) nào:

```bash
python -m http.server 8000 --directory docs
```

Sau đó mở `http://localhost:8000/`.

## 🌐 Triển khai GitHub Pages

Workflow đi kèm sẽ xuất bản thư mục `docs/`. Trong phần cài đặt của repository, hãy chọn
**GitHub Actions** làm nguồn cho Pages. URL của trang là:

```text
https://datascienceuibk.github.io/RETECO/
```

## 📅 Các mốc thời gian quan trọng

- Dữ liệu mẫu: 08/08/2026
- Dữ liệu huấn luyện: **đã phát hành ngày 30/08/2026**
- Đánh giá: 10–31/01/2027
- Mốc bài báo và workshop: dự kiến; xem
  [lịch chính thức của SemEval-2027](https://semeval.github.io/SemEval2027/)

## 👥 Ban tổ chức

Abdelrahman Abdallah, Mohammed Ali, Muhammad Abdul-Mageed, Kevin Duh và
Adam Jatowt.

Nếu có câu hỏi về task, hãy liên hệ
[Abdelrahman Abdallah](mailto:abdelrahman.abdallah@uibk.ac.at).

## ⚖️ Giấy phép

Bản phát hành dữ liệu áp dụng hai giấy phép. **Corpus và văn bản câu hỏi/câu trả lời
theo giấy phép CC BY-SA 4.0** — toàn bộ văn bản đoạn văn có nguồn gốc từ Stack Exchange, nơi các
đóng góp của người dùng được cấp phép CC BY-SA, vốn là giấy phép share-alike (chia sẻ tương tự) và không thể
cấp phép lại theo điều khoản khác. **Annotation của RETECO (phân chia split, qrels TREC,
`split_manifest.json`) theo giấy phép CC BY 4.0.** Quyền ghi công (attribution) cho nội dung gốc
vẫn thuộc về các tác giả ban đầu trên Stack Exchange.

Dữ liệu và mã nguồn của các benchmark hiện có có thể dùng giấy phép khác; hãy tham khảo giấy phép
đi kèm với từng tài nguyên. Một giấy phép phần mềm cho toàn bộ repository sẽ được bổ sung
trước bản phát hành mã nguồn RETECO đầu tiên có gắn tag.
