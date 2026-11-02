# Kiểm tra bản bàn giao

- MP4: H.264, 1080 × 1920, 30 fps, 5.998 khung hình, khoảng 199,93 giây.
- Âm thanh: AAC, 48 kHz; đo trên MP4: -13,30 LUFS, true peak -1,73 dBTP.
- Giải mã toàn bộ hình và tiếng bằng FFmpeg với `-xerror`: thành công.
- HyperFrames: lint, runtime, layout, contrast và audio đều không có lỗi; không có cảnh báo độ tương phản.
- Đã xem khung đại diện đủ 12 cảnh trước xuất; xem lại bảng khung trích từ MP4 sau xuất, gồm cả đồ thị tháo tải và mặt cắt nghiêng.
- Tính đối chiếu: A = π × 20² / 4 = 314,159265 mm²; Fy với Sy = 250 MPa là 78,539816 kN; 1/1000 = 0,001 = 0,1%; tại θ = 45°, cos²θ = sinθ cosθ = 0,5.
- Giả thiết của ví dụ được nêu rõ bằng hình và lời đọc: kéo đúng tâm, thanh tròn đặc, 250 MPa được giả sử là giới hạn chảy. Không gọi 78,54 kN là tải cho phép hoặc tải đứt.
- Còn 24 cảnh báo craft: khung 0 đang bắt đầu hiệu ứng vào; nhãn phụ dưới ngưỡng chữ đề xuất; 22 câu phụ đề ngắn hơn ngưỡng đọc mặc định khoảng 0,06–0,60 giây. Phụ đề hiển thị theo câu với lời đọc tương ứng, không căn từng từ bằng nhận dạng. Không tắt kiểm tra để che cảnh báo; có ảnh bìa riêng.
- Chưa thực hiện đánh giá nghe độc lập hoặc thử nghiệm vật liệu. Các đồ thị là định tính, không phải số liệu đo; sơ đồ biến dạng có phóng đại, không phải mô phỏng số hay chứng nhận an toàn thiết kế.
