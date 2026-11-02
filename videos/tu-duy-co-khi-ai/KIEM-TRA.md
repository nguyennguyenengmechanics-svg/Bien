# Kiểm tra video tư duy thiết kế cơ khí và AI

- Tệp MP4: H.264, 1080 × 1920, 30 fps, 5.795 khung hình, khoảng 193,17 giây.
- Âm thanh AAC, 48 kHz. Đo trên MP4: -13,42 LUFS; true peak -1,70 dBTP.
- FFmpeg giải mã toàn bộ hình và tiếng với `-xerror`: thành công.
- HyperFrames: lint, runtime, layout, contrast và audio không có lỗi. Không có cảnh báo độ tương phản.
- Đã xem bảng khung hình của đủ 12 cảnh trước render; xem lại bảng trích từ MP4 sau render. Các tiêu đề dài đã rút gọn; không có chữ chồng hoặc tràn vùng nội dung tại những khung kiểm tra.
- Còn 10 cảnh báo craft tự động: khung 0 bắt đầu hiệu ứng vào; nhãn nguồn và nhãn phụ dưới ngưỡng chữ đề xuất; 8 câu phụ đề ngắn hơn sàn đọc mặc định khoảng 0,06–0,35 giây. Lời đọc đã giảm tốc, phụ đề giữ theo câu tương ứng; không tắt kiểm tra để che cảnh báo. Có ảnh bìa riêng.
- Chưa thực hiện đánh giá nghe độc lập. Sơ đồ là minh họa lập luận, không phải kết quả thử nghiệm hay mô phỏng kỹ thuật.
- Nội dung là bản chuyển thể từ tài liệu người dùng; không khẳng định một ngành nghề chắc chắn không thể bị AI thay thế.
