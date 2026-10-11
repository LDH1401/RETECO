# Dữ liệu thí điểm tuyển chọn của RETECO

Thư mục này là một tập con bằng chứng nhỏ gọn, đã được con người kiểm tra, sao chép từ
các bản phát hành chính thức của **TEMPO** và **RECOR**. Nó minh chứng rằng cả hai hạng mục
được đề xuất đều có định dạng dữ liệu vận hành được, truy vấn/hội thoại, tập bằng chứng
dương đầy đủ và qrels máy đọc được.

## Phạm vi quan trọng

- Đây là **tài liệu thí điểm/dùng thử**, không phải một phần chia mới của bộ đánh giá chuẩn và
  không phải tập kiểm tra ẩn của SemEval-2027.
- Việc lựa chọn được cố ý làm đa dạng và dễ xem xét; không tuyên bố là mang tính
  đại diện thống kê hay cân bằng giữa các lĩnh vực.
- Mọi tài liệu dương được tham chiếu đều có trong gói. Không bổ sung mẫu âm tổng hợp,
  nhãn liên quan, truy vấn, câu trả lời hay lượt hội thoại nào.
- Tập tài liệu đi kèm chỉ là một tập con bằng chứng. Các hệ thống cơ sở truy xuất
  và việc chấm điểm chính thức phải dùng toàn bộ kho ngữ liệu của hạng mục, chứ không chỉ xếp hạng
  các tài liệu dương này.
- Tất cả bản ghi đều bằng tiếng Anh.

## Nội dung

### `track1_tempo/`

- `examples.jsonl`: 5 ví dụ truy xuất theo thời gian hoàn chỉnh.
- `steps.jsonl`: các bản ghi bước chính thức tương ứng của TEMPO.
- `documents.jsonl`: toàn bộ 26 đoạn văn chuẩn khác nhau được các ví dụ tham chiếu.
- `qrels.txt`: 26 nhãn đánh giá dương theo cặp truy vấn–tài liệu ở định dạng TREC.

### `track2_recor/`

- `benchmark.jsonl`: 4 bản ghi hội thoại hoàn chỉnh gồm 13 lượt.
- `documents.jsonl`: toàn bộ 15 đoạn văn khác nhau được các lượt đó tham chiếu.
- `qrels.txt`: 32 nhãn đánh giá dương theo cặp lượt–tài liệu ở định dạng TREC. ID truy vấn có dạng
  `<conversation_id>#turn<turn_id>`.

### Các tệp ở thư mục gốc

- `manifest.json`: số lượng, các ID được chọn, URL nguồn và các phiên bản được cố định.


