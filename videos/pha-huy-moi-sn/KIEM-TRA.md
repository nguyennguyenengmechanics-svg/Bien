# Kiểm tra video phá hủy mỏi và đường cong S–N

- MP4 H.264, 1080 × 1920, 30 fps, 6.931 khung hình; thời lượng 231,033 giây; âm thanh AAC.
- FFmpeg giải mã toàn bộ hình và âm thanh với `-xerror`: đạt.
- HyperFrames lint, runtime, layout và audio: không có lỗi/cảnh báo; bố cục lấy mẫu 12 thời điểm. Kiểm tra tương phản: 101/101 đạt.
- Xem ảnh bản xuất ở 12 cảnh, ảnh đọc đồ thị, bìa và kết thúc. Đã sửa lỗi ngắt dòng do strong trong flex; từ khóa cam đậm và nhánh xanh–cam hiện đúng.
- Khung đầu có tiêu đề. Cỡ nhãn/footer tăng lên 28 px.
- Còn 4 cảnh báo đọc phụ đề theo ngưỡng heuristic: 4 câu thiếu khoảng 0,05–0,23 giây so với ngưỡng công cụ. Phụ đề đi theo lời đọc tổng hợp; không coi đây là kiểm chứng khả năng đọc của mọi người xem.
- Âm lượng đo trên MP4: -13,40 LUFS tích hợp, true peak -1,69 dBTP, LRA 3,70 LU; không phát hiện đỉnh vượt 0 dBTP. Đây là đo kỹ thuật, không phải tuyên bố đã nghe duyệt thủ công.
- Các công thức/ví dụ đã đối chiếu: Δσ=100 MPa → σa=50 MPa; 500.000 phút ≈347 ngày; Miner 0,2+0,2=0,4. Đồ thị và nhóm tải minh họa, không phải dữ liệu thử.
- Gói ZIP đã kiểm tra CRC. Giả thiết, hạn chế, nguồn và giấy phép xem GHI-CHU.txt.
