# Kiểm tra gói video-hoc-thuat

- SKILL.md có metadata name/description và tên khớp thư mục kỹ năng.
- Đã kiểm tra các liên kết tệp nội bộ, cú pháp Python và JSON.
- Đã chạy scaffold và build mẫu thành HTML, SRT và lời dẫn; scaffold không ghi đè thư mục đang có nội dung.
- HyperFrames kiểm tra mẫu: lint, runtime, layout, contrast và craft không có lỗi/cảnh báo. Hai cảnh báo âm thanh im lặng đúng với lựa chọn `--demo` có chủ ý.
- Đã xem ảnh mẫu ở giây6: tiêu đề hiện, từ khóa đậm cam và phụ đề nằm trong bố cục. Đây là kiểm tra mẫu bố cục, không phải nghiệm thu một video học thuật mới.
- verify_media.py từ chối nghiệm thu dự án còn đánh dấu demo trước cả khi mở MP4.
- Không render MP4 mới trong công việc đóng gói kỹ năng này; các video mẫu hoàn chỉnh đã có trong thư mục videos của kho. Script kiểm tra media là bản tổng quát hóa quy trình FFprobe/FFmpeg đã dùng cho các video đó.
- Gói ZIP đã kiểm tra CRC và đối chiếu từng tệp đóng gói với bản nguồn. Không có WAV demo, PDF người dùng, secret, credential, cache hoặc mô hình TTS trong gói kỹ năng.
- Việc lưu kỹ năng có phạm vi theo kho; không tự cài toàn tài khoản. Hướng dẫn chuyển sang môi trường khác có trong README.
