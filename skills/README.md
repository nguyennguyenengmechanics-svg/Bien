# Kỹ năng video học thuật

Quy trình đã được đóng gói thành **video-hoc-thuat**, dùng lại phong cách các video trong kho này: nền kem, sơ đồ kỹ thuật chuyển động, giọng Việt, phụ đề, từ khóa đậm có màu tương phản và nhánh sơ đồ rõ.

- [Đọc SKILL.md](../.agents/skills/video-hoc-thuat/SKILL.md)
- [Tải gói kỹ năng ZIP](https://github.com/nguyennguyenengmechanics-svg/Bien/raw/refs/heads/main/skills/video-hoc-thuat.zip)
- [Thiết kế hình ảnh](../.agents/skills/video-hoc-thuat/references/DESIGN.md)
- [Quy trình dựng](../.agents/skills/video-hoc-thuat/references/workflow.md)
- [Kiểm tra và bàn giao](../.agents/skills/video-hoc-thuat/references/review.md)

## Cách gọi

> Dùng $video-hoc-thuat để tạo video học thuật từ tài liệu này.

Hoặc khi làm trong kho Bien:

> Tạo video học thuật từ PDF này, theo phong cách các video trước.

`AGENTS.md` ở gốc kho định tuyến yêu cầu đến kỹ năng. Các yêu cầu chỉ viết caption vẫn chỉ tạo caption.

## Dùng ở môi trường khác

Giải nén ZIP, chép thư mục `video-hoc-thuat` vào `.agents/skills/` của dự án hỗ trợ kiểu kỹ năng này; hoặc thư mục kỹ năng mà môi trường của bạn quy định. Nếu có AGENTS.md sẵn, chỉ thêm quy tắc định tuyến trong `AGENTS.example.md`, không ghi đè tệp cũ. Làm mới phiên nếu công cụ cần tải lại danh sách kỹ năng.

Nếu cuộc trò chuyện mới không truy cập kho hoặc không hỗ trợ cài kỹ năng, đính kèm ZIP và yêu cầu đọc SKILL.md. Việc lưu kỹ năng trong kho không tự cài nó vào toàn bộ tài khoản hay mọi cuộc trò chuyện.

## Mẫu và kiểm tra

```sh
python .agents/skills/video-hoc-thuat/scripts/scaffold.py /duong/dan/du-an-moi
```

Để chỉ thử bố cục, thêm `--demo`; mẫu thử dùng âm thanh im lặng, có đánh dấu rõ và không được giao như video thật. Điền nội dung, dựng hình mới và tạo giọng đọc trước khi sản xuất video hoàn chỉnh.

Mẫu dựng được kiểm tra bằng HyperFrames; xem [báo cáo](KIEM-TRA.md). Font và GSAP kèm thông báo giấy phép; gói không chứa mô hình TTS hay dữ liệu riêng của người dùng.
