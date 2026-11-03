# Kiểm tra video mô đun Young

- MP4: H.264, 1080 × 1920, 30 fps, 6.562 khung hình, khoảng 218,73 giây.
- Âm thanh AAC 48 kHz; đo trên MP4: -13,30 LUFS, true peak -1,63 dBTP.
- FFmpeg giải mã toàn bộ hình và tiếng với `-xerror`: thành công.
- HyperFrames bản bàn giao: lint, runtime, layout, contrast và audio không có lỗi. Không có cảnh báo độ tương phản.
- Đã xem khung đại diện đủ 12 cảnh; kiểm tra thêm các thời điểm liên kết giãn–hồi, mạng trượt và tiết diện xoay. Nhãn “16I” chỉ vào khi tiết diện gần xoay xong để tránh che hình.
- Đã xem lại bảng khung trích từ MP4 sau xuất, gồm đồ thị thế năng, biểu đồ vật liệu, so sánh thép và các công thức dầm.
- Đối chiếu số học: A nằm = A đứng = 400 mm²; I nằm = 3333,333 mm⁴; I đứng = 53333,333 mm⁴; tỉ số = 16. Trong mô hình đã nêu, E × 2 → δ/2 và L × 2 → δ × 8.
- Còn 8 cảnh báo craft: khung 0 bắt đầu hiệu ứng vào; nhãn phụ dưới ngưỡng chữ đề xuất; 6 câu phụ đề ngắn hơn sàn đọc tự động, chênh tối đa 0,25 giây. Lời đọc đã giảm tốc; có ảnh bìa riêng. Không tắt kiểm tra để che cảnh báo.
- Mã nguồn ZIP đã kiểm tra CRC, không phát hiện lỗi đóng gói.
- Phụ đề theo mốc câu, không căn từng từ bằng nhận dạng. Một số câu được trình bày bằng số và ký hiệu tương đương để dễ đọc.
- Chưa có đánh giá nghe độc lập hoặc thử nghiệm vật liệu. Chuyển động nguyên tử, đồ thị và độ võng là minh họa có phóng đại, không phải dữ liệu đo hoặc mô phỏng nguyên tử thực. Xem GHI-CHU.txt về giả thiết và giới hạn kỹ thuật.
