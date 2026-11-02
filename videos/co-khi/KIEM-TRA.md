# Kiểm tra bản bàn giao

- MP4: H.264, 1080 × 1920, 30 fps, 5.478 khung hình, 182,60 giây.
- Âm thanh: AAC, 48 kHz. Đo trên MP4: -13,37 LUFS, true peak -1,70 dBTP.
- Giải mã toàn bộ video và âm thanh bằng FFmpeg với `-xerror`: thành công.
- Đã xem các khung trích xuyên suốt video, khung kết và cảnh mỏi được sửa nhãn.
- Cảnh mỏi thay nhãn tuyệt đối bằng “TẢI LẶP LẠI → NGUY CƠ HƯ HẠI TÍCH LŨY”. Thay cảnh theo đúng số khung; xác minh tổng số khung không đổi và hash luồng AAC trước/sau giống nhau.
- Kiểm tra HyperFrames trước sửa nhãn: lint, runtime, layout, contrast và audio không có lỗi. Lint sau sửa nhãn: 0 lỗi, 0 cảnh báo. Nhãn mới đã được xem trên khung xuất riêng của cảnh.
- Bộ kiểm tra tự động còn 9 cảnh báo craft: khung 0 đang bắt đầu hiệu ứng vào cảnh; nhãn phụ nhỏ hơn ngưỡng đề xuất; 7 câu phụ đề ngắn hơn sàn đọc mặc định khoảng 0,05–0,35 giây. Phụ đề có lời đọc tương ứng, câu chữ được giữ nguyên; không tắt kiểm tra để che cảnh báo. Có ảnh bìa riêng cho thumbnail.
- Không thực hiện đánh giá nghe độc lập hoặc thử nghiệm thiết kế cơ khí. Các hình là sơ đồ nguyên lý, không phải FEA hay chứng nhận an toàn.
