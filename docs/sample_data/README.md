# Dữ liệu pilot tuyển chọn của RETECO

Thư mục này là một tập con bằng chứng (evidence) nhỏ gọn, đã được con người kiểm tra, sao chép từ
các bản phát hành chính thức của **TEMPO** và **RECOR**. Nó minh chứng rằng cả hai track
được đề xuất đều có định dạng dữ liệu vận hành được, truy vấn (query)/hội thoại, tập positive evidence
đầy đủ và qrels máy đọc được.

## Phạm vi quan trọng

- Đây là **tài liệu pilot/dùng thử (trial)**, không phải một split benchmark mới và
  không phải tập test ẩn của SemEval-2027.
- Việc lựa chọn được cố ý làm đa dạng và dễ xem xét; không tuyên bố là mang tính
  đại diện thống kê hay cân bằng giữa các lĩnh vực (domain).
- Mọi positive document được tham chiếu đều có trong gói. Không bổ sung negative tổng hợp,
  relevance label, truy vấn, câu trả lời hay lượt hội thoại (turn) nào.
- Tập tài liệu (document) đi kèm chỉ là một tập con evidence. Các baseline truy xuất (retrieval)
  và việc chấm điểm chính thức phải dùng toàn bộ corpus của track, chứ không chỉ xếp hạng
  các positive document này.
- Tất cả bản ghi đều bằng tiếng Anh.

## Nội dung

### `track1_tempo/`

- `examples.jsonl`: 5 ví dụ temporal retrieval hoàn chỉnh.
- `steps.jsonl`: các bản ghi bước chính thức tương ứng của TEMPO.
- `documents.jsonl`: toàn bộ 26 gold passage khác nhau được các ví dụ tham chiếu.
- `qrels.txt`: 26 positive judgment theo cặp truy vấn–tài liệu ở định dạng TREC.

### `track2_recor/`

- `benchmark.jsonl`: 4 bản ghi hội thoại hoàn chỉnh gồm 13 lượt.
- `documents.jsonl`: toàn bộ 15 đoạn văn (passage) khác nhau được các lượt đó tham chiếu.
- `qrels.txt`: 32 positive judgment theo cặp lượt–tài liệu ở định dạng TREC. Query ID có dạng
  `<conversation_id>#turn<turn_id>`.

### Các tệp ở thư mục gốc

- `manifest.json`: số lượng, các ID được chọn, URL nguồn và các revision được cố định (pinned).


