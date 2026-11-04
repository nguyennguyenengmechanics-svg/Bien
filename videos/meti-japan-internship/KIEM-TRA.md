# Kiểm tra vlog METI — Ngày đầu tiên

- MP4 H.264, 1080 × 1920, 30 fps, 2.744 khung hình; thời lượng 91,467 giây. Âm thanh AAC. Nguồn quay 720×1280; bản xuất được phóng lên1080×1920, không phải phục hồi chi tiết quay gốc.
- FFmpeg giải mã toàn bộ hình và tiếng với `-xerror`: đạt.
- HyperFrames lint, runtime, layout, contrast, craft và audio: không có lỗi/cảnh báo. Layout lấy mẫu15thời điểm; tương phản62/62 đạt. Motion audit tự động không bật; timeline và ảnh lấy mẫu được rà riêng.
- Đã rà ảnh từng phần và ảnh từ chính MP4: sân bay ban đêm, selfie, giờ khởi hành/đến, Arrivals, phần không ghi hình, Visit Japan Web, khu vực đón xe và ảnh cuối. Thẻ Visit Japan Web đã sửa để không xuất hiện sớm rồi nháy trước lời nhắc.
- Đã kiểm tra thứ tự part1→part2 trong edit-decisions.json; không có hình/voice của video tham khảo trong bản chính. Hai phần không quay là thẻ đồ họa có nhãn, không phải cảnh mô phỏng nhập cảnh.
- Mốc00:25 theo xác nhận của người dùng;08:00 là giờ Nhật Bản theo thông tin người dùng. Không tự tính ngày đến hoặc thời gian bay thực.
- Mã trên vé và nhãn trong ảnh cuối được che trong tài nguyên dẫn xuất trước khi render. Rà khung đầu/giữa/cuối cảnh giấy tờ và ảnh kết; source ZIP không chứa MOV, HEIC, RAR hoặc ảnh chưa che mã.
- Thẻ Visit Japan Web là minh họa trình bày lại từ ảnh người dùng, chỉ thông tin phụ. Trang trực tiếp bị môi trường chặn; không coi thumbnail là bản chụp giao diện hiện hành đã kiểm chứng. QR vẽ trong hình không phải mã nhập cảnh cá nhân.
- Đo âm lượng MP4: khoảng−13,33LUFS tích hợp, true peak−0,98dBTP, LRA4,10LU; không có đỉnh đo vượt0dBTP. Đây là kiểm tra kỹ thuật, không phải tuyên bố đã nghe duyệt thủ công hay dùng giọng của người dẫn video tham khảo.
- ZIP nguồn đã kiểm tra CRC và chứa HTML cuối với timing thẻ phụ đã sửa. Tệp chép vào kho được đối chiếu SHA-256 với bản đã kiểm tra.
