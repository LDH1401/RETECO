# Hệ thống cơ sở BM25 chính thức của RETECO — train và dev

Truy xuất: nguyên văn hàm `retrieval_bm25` từ các kho mã TEMPO và RECOR gốc
(bộ phân tích Lucene của pyserini + `LuceneBM25Model` của gensim, k1=0.9, b=0.4, top-1000).
Chấm điểm: hàm `calculate_retrieval_metrics` gốc — `pytrec_eval`, `ndcg_cut_10`.
Lấy trung bình macro theo các lĩnh vực, giống như cả hai bài báo.

Số liệu Hạng mục 1 được đo trên **dữ liệu v1.1** (kho ngữ liệu Hạng mục 1 đã loại bỏ trùng lặp,
25/09/2026). Trên v1.0, trung bình macro của Hạng mục 1 là 1a 0.0879 / 0.0967 và
1b 0.0852 / 0.1063 (train / dev). Dữ liệu Hạng mục 2 không thay đổi.

## nDCG@10 trung bình macro

| Hạng mục con | train | dev | đã công bố (toàn bộ tập) |
| --- | ---: | ---: | ---: |
| 1a · truy xuất toàn bộ truy vấn | 0.1075 | 0.1147 | 0.108 (bài báo TEMPO) |
| 1b · truy xuất từng bước | 0.1024 | 0.1177 | không báo cáo |
| 2a · Base (chỉ lượt hiện tại) | 0.1837 | 0.1827 | 0.185 (RECOR, Bảng 3) |
| 2a · +History (kèm lịch sử hội thoại) | 0.4539 | 0.4379 | 0.446 (RECOR, Bảng 3) |

Các tập của chúng tôi bao gồm 70% / 30% của mỗi lĩnh vực, nên không kỳ vọng kết quả bằng chính xác
các con số đã công bố trên toàn bộ tập; Hạng mục 2 tái lập được cả hai cấu hình
BM25 đã công bố với sai lệch trong phạm vi 0.003. Kho ngữ liệu Hạng mục 1 bản v1.1 cũng đã được
loại bỏ trùng lặp, nên nhỏ hơn kho ngữ liệu được dùng trong bài báo TEMPO.

## nDCG@10 theo từng lĩnh vực

### Hạng mục 1 · TEMPO (dữ liệu v1.1)

| Lĩnh vực | 1a train | 1a dev | 1b train | 1b dev |
| --- | ---: | ---: | ---: | ---: |
| bitcoin | 0.0856 | 0.0370 | 0.0888 | 0.0299 |
| cardano | 0.1848 | 0.1027 | 0.1655 | 0.0627 |
| economics | 0.0382 | 0.0467 | 0.0300 | 0.0463 |
| genealogy | 0.1242 | 0.1949 | 0.1181 | 0.2183 |
| history | 0.0654 | 0.0873 | 0.0614 | 0.1015 |
| hsm | 0.1736 | 0.2489 | 0.1729 | 0.2140 |
| iota | 0.1563 | 0.3309 | 0.1403 | 0.4195 |
| law | 0.0946 | 0.0574 | 0.0854 | 0.0549 |
| monero | 0.0382 | 0.0320 | 0.0622 | 0.0113 |
| politics | 0.2810 | 0.2625 | 0.2403 | 0.2371 |
| quant | 0.0255 | 0.0237 | 0.0085 | 0.0403 |
| travel | 0.0506 | 0.0442 | 0.0423 | 0.0645 |
| workplace | 0.0798 | 0.0230 | 0.1162 | 0.0297 |

### Hạng mục 2 · RECOR

| Lĩnh vực | 2a train | 2a dev | 2a_hist train | 2a_hist dev |
| --- | ---: | ---: | ---: | ---: |
| biology | 0.2250 | 0.2034 | 0.6369 | 0.6065 |
| drones | 0.1400 | 0.1695 | 0.3162 | 0.2954 |
| earth_science | 0.2757 | 0.2195 | 0.6324 | 0.6264 |
| economics | 0.1573 | 0.1629 | 0.4593 | 0.4739 |
| hardware | 0.1472 | 0.1605 | 0.2935 | 0.3378 |
| law | 0.1047 | 0.1147 | 0.2721 | 0.3437 |
| medicalsciences | 0.1188 | 0.1168 | 0.2267 | 0.1730 |
| politics | 0.1609 | 0.1514 | 0.4423 | 0.3219 |
| psychology | 0.2208 | 0.2596 | 0.5558 | 0.5726 |
| robotics | 0.1847 | 0.1574 | 0.5773 | 0.5123 |
| sustainable_living | 0.2851 | 0.2938 | 0.5801 | 0.5531 |
