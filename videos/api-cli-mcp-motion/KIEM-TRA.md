# Kiểm tra bản motion graphic API · CLI · MCP

- Thời lượng MP4: 229.100 giây, khoảng 3 phút 49 giây.
- 1080×1920, 30 fps, H.264/AAC, 6.873 khung hình; khớp số frame từ duration nguồn làm tròn và tốc độ khung.
- Giải mã toàn bộ video và audio bằng FFmpeg với -xerror: đạt, không lỗi.
- HyperFrames 0.8.221, lần kiểm tra cuối: lint, runtime, layout, contrast, craft và audio không có lỗi/cảnh báo. Layout lấy 15 mẫu; kiểm tra này không phải xem thủ công mọi khung.
- Rà timeline: 279 tween; quét caption mỗi 0,1 giây, không có hai caption cùng hiện trong một cảnh. Bộ motion audit tự động riêng của CLI không được bật; chuyển động được dựng bằng timeline và rà qua ảnh theo thời điểm.
- Đã xem 9 ảnh hero bố cục; sửa vị trí quay bánh răng và đường đi packet để không che nhãn; xem lại các cảnh có thay đổi.
- Sau xuất: đã xem 9 ảnh hero trích từ MP4, gồm cảnh giảm giá, bếp, API, script, MCP, CLI, kết hợp, cây lựa chọn và kết. Không khẳng định đã xem toàn bộ video theo thời gian thực.
- Âm lượng đo từ MP4: -13.38 LUFS tích hợp, true peak -1.54 dBTP, LRA 2.90 LU. Có giọng Việt tổng hợp và nhạc gốc. Chỉ kiểm tra kỹ thuật âm thanh, không thực hiện nghe duyệt.
- Phụ đề có 36 đoạn, căn theo WAV thực, không căn từng từ.
- ZIP nguồn 23 tệp, CRC đạt; hai FLAC so sánh hash PCM giải mã trùng WAV dùng render. Runtime bản nguồn FLAC không có lỗi/cảnh báo.
- Không chứa tài khoản, API key, mô hình TTS, cache hay bản ghi gốc trong gói nguồn.
- Đã rà phép tính giảm 20%: 100→80; 200→160; 300→240 nghìn đồng. Không benchmark hiệu năng, không thao tác cửa hàng thật.

SHA-256 MP4: `e730140ac12129ba74cdfca064982eb50551a5ab82445c32f749970180fd644c`
