# Kiểm tra video Khám phá mô đun Young

- MP4: H.264, 1080 × 1920, 30 fps, 6.633 khung hình, 221,10 giây.
- Âm thanh AAC 48 kHz; đo trên MP4: -13,30 LUFS, true peak -1,69 dBTP.
- FFmpeg giải mã toàn bộ hình và tiếng với `-xerror`: thành công.
- HyperFrames: lint, runtime, layout, contrast và audio không có lỗi; không có cảnh báo độ tương phản.
- Đã xem khung đại diện của đủ 12 cảnh trước xuất; xem lại bảng khung trích từ MP4 và khung cuối phần tính E, thấy đầy đủ dữ liệu đầu vào và kết quả.
- Tính đối chiếu: 10 kN = 10000 N; σ = 10000/100 = 100 MPa; ε = 0,05/100 = 0,0005 = 0,05%; E = 100/0,0005 = 200000 MPa = 200 GPa. Dùng nhầm ε = 0,05 cho E = 2000 MPa = 2 GPa, nhỏ hơn 100 lần.
- Các dữ liệu của ví dụ được đánh dấu giả định minh họa, không phải dữ liệu đo hay một thí nghiệm đã được thực hiện.
- Còn 3 cảnh báo craft: khung 0 đang bắt đầu hiệu ứng vào; nhãn phụ dưới ngưỡng chữ đề xuất; 1 câu phụ đề ngắn hơn ngưỡng đọc mặc định khoảng 0,08 giây. Không tắt kiểm tra để che cảnh báo; có ảnh bìa riêng.
- Mã nguồn ZIP đã kiểm tra CRC, không phát hiện lỗi.
- Chưa có đánh giá nghe độc lập hoặc thử nghiệm vật liệu. Hình nguyên tử, dầm và đồ thị là minh họa định tính có phóng đại; không phải mô phỏng thực hoặc chứng nhận thiết kế.
