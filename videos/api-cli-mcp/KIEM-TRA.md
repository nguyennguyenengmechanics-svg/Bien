# Kiểm tra video API · CLI · MCP

- Thời lượng thực: 255.733 giây, khoảng 4 phút 16 giây.
- Hình: 1080×1920, 30 fps, H.264, 7.672 khung hình; khớp timing.
- Âm thanh: AAC, có giọng Việt tổng hợp và nhạc nền tự tạo.
- Kích thước tệp: 20,526,747 byte.
- FFmpeg giải mã toàn bộ video và âm thanh với `-xerror`: đạt, không lỗi.
- HyperFrames 0.8.221: lint, runtime, layout, contrast, craft và audio đều không có lỗi/cảnh báo ở lần kiểm tra cuối. Layout lấy 15 mẫu; contrast lấy 5 mẫu, 106 phép kiểm tra đạt.
- Timeline kiểm tra 257 tween; quét caption mỗi 0,1 giây không phát hiện hai caption cùng hiện trong một cảnh.
- Đã xem ảnh bố cục HTML cho đủ 10 cảnh, khung đầu có tiêu đề, và 10 ảnh hero trích từ chính MP4; đã sửa nhãn nhỏ và đường nối vướng. Đã xem khung kết từ MP4. Đây là kiểm tra ảnh lấy mẫu, không phải xem lại toàn bộ từng khung.
- Mức âm đo trong MP4: -13.30 LUFS tích hợp, true peak -1.49 dBTP, LRA 3.10 LU. Đây là các giá trị input đo từ file, không phải thông số mục tiêu của bộ lọc. Không thực hiện nghe duyệt bằng công cụ nghe.
- 40 đoạn WAV tạo giọng được đo thời lượng thật; phụ đề rút gọn theo từng đoạn, không nhận là căn từng từ.
- Gói nguồn: 22 tệp, ZIP CRC đạt. Âm thanh FLAC trong gói đã so sánh SHA-256 PCM giải mã, trùng hai WAV đã dùng render, không mất dữ liệu. Runtime source-package với FLAC không có lỗi/cảnh báo.
- Không kèm bản ghi gốc, secret, API key, mô hình TTS hay cache trong gói.
- Hình thanh ngữ cảnh chỉ minh họa thành phần; số dòng 1000 và 10 là giả định; không thực hiện benchmark MCP/CLI/API.

SHA-256 MP4: `280bb34934a5b4a58e838d6f37f88b5c876fa6bfb48cd0a5a7096a1cfd0ccdb5`
