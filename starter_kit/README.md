# Bộ công cụ khởi đầu RETECO

Mã tham chiếu cho Nhiệm vụ 1 của SemEval-2027. Gồm hai cấp độ:

| | Phụ thuộc | Công dụng |
| --- | --- | --- |
| **Hệ thống cơ sở chính thức** (`official_baseline.py`) | pyserini + JDK, gensim, pytrec_eval | Tái lập các con số hệ thống cơ sở RETECO đã công bố |
| **Bản khởi đầu thuần Python** (`bm25_baseline.py` + `scorer.py`) | không có | Điểm khởi đầu không cần cài đặt; kết quả gần đúng |

## Hệ thống cơ sở chính thức

Phần truy xuất là nguyên văn hàm `retrieval_bm25` từ hai kho mã benchmark gốc,
vốn có các cài đặt giống hệt nhau đến từng byte:

- https://github.com/tempo-bench/Tempo — `retrievers.py`
- https://github.com/RECOR-Benchmark/RECOR — `experiments/retrieval/retrievers.py`

Cụ thể là: bộ phân tích Lucene qua pyserini, `LuceneBM25Model` của gensim với
`k1=0.9, b=0.4`, cắt ở top-1000. Phần chấm điểm là hàm `calculate_retrieval_metrics` gốc
— `pytrec_eval` với `ndcg_cut`, `map_cut`, `recall`, `P` và `recip_rank`.
**nDCG@10 từ `pytrec_eval` là chỉ số chính thức của RETECO.**

Cách xây dựng truy vấn theo đúng bản gốc:

| Hạng mục con | Truy vấn | ID chủ đề |
| --- | --- | --- |
| 1a | `examples['query']` | `id` |
| 1b | `f"{base_query}\n\nStep: {step_instruction}"` | `step_id` |
| 2a | `turn['query']` (chỉ lượt hiện tại) | `{conversation_id}_turn_{turn_id}` |

```bash
export JAVA_HOME=/path/to/jdk
export JVM_PATH=$JAVA_HOME/lib/server/libjvm.so
python official_baseline.py --data ../reteco_data --out ../baselines_official \
    --splits train dev
# chỉ một lĩnh vực:
python official_baseline.py --track1 iota --track2 drones --splits dev
```

Tệp `results.json` của từng lĩnh vực được lưu đệm, nên lần chạy có thể tiếp tục khi bị gián đoạn. Kho ngữ liệu được
phân tích và lập chỉ mục một lần cho mỗi lĩnh vực và được dùng lại cho các tập — đây là điểm
khác biệt duy nhất so với luồng chạy theo từng lần gọi của bản gốc, và nó chỉ thay đổi thời gian chạy thực tế,
không thay đổi điểm số.

## Bản khởi đầu thuần Python

Hoàn toàn không có phụ thuộc. Mô phỏng gần đúng thiết lập chính thức (cùng `k1`/`b`, cách
tách từ đơn giản hơn) và bổ sung các chỉ số chẩn đoán về thời gian và độ sâu lượt của RETECO, vốn
không thuộc các chỉ số truy xuất gốc.

```bash
python run_release.py --data ../reteco_data --split dev --track1 iota --track2 drones
```

## Xây dựng bản phát hành từ nguồn gốc

```bash
python download_raw.py                     # bản chụp TEMPO + RECOR với phiên bản được cố định
python build_release.py --raw ../hf_raw --out ../reteco_data_v1.0
python dedup_track1.py --src ../reteco_data_v1.0 --dst ../reteco_data       # dữ liệu v1.1
python verify_dedup_track1.py --old ../reteco_data_v1.0 --new ../reteco_data
```

`build_release.py` có tính tất định: cùng seed, cùng cách chia, và nó kiểm tra lại
mọi số lượng đã công bố ở mỗi lần chạy. Script này tạo ra dữ liệu v1.0.

`dedup_track1.py` chuyển v1.0 thành v1.1. Trong mỗi kho ngữ liệu Hạng mục 1, script giữ một
bản cho mỗi văn bản (giống hệt nhau khi bỏ qua khoảng trắng), luôn giữ lại một ID chuẩn
khi một nhóm bản sao có chứa ID đó, và đổi tên các ID bị loại bỏ thành ID được giữ lại trong
mọi tệp nhiệm vụ. Script ghi tệp `duplicate_map.json` (ID bị loại bỏ -> ID được giữ lại) cho mỗi
lĩnh vực. Hạng mục 2 được sao chép nguyên vẹn. `verify_dedup_track1.py` kiểm tra kết quả
so với v1.0: không mất văn bản chuẩn nào, qrels và các tệp nhiệm vụ bằng với v1.0 sau khi ánh xạ ID,
Hạng mục 2 giống hệt đến từng byte.

## Trình kiểm tra định dạng

`format_checker.py` kiểm tra một bài nộp trước khi bạn gửi đi. Hãy chạy nó trên mọi
tệp kết quả chạy — một bài nộp không vượt qua kiểm tra thì không bao giờ nên được đưa lên
nền tảng thi đấu.
