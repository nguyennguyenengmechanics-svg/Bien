# Kiểm tra video các thuyết phá hủy

- MP4 H.264, 1080 × 1920, 30 fps, 8.117 khung hình; thời lượng 270,567 giây. Âm thanh AAC.
- FFmpeg giải mã toàn bộ hình và tiếng với `-xerror`: đạt.
- HyperFrames: lint, runtime, layout, craft và audio không có lỗi/cảnh báo. Bố cục lấy mẫu 15 thời điểm; tương phản 92/92 đạt. Đây là kiểm tra lấy mẫu, không chứng nhận mọi khung hình.
- Đã xem ảnh trước xuất của 11 cảnh, ảnh tổng hợp từ MP4, ảnh so sánh Tresca–von Mises và khung kết. Sửa nhãn sát mép trong cây lựa chọn; tăng thời gian đọc 7 đoạn dài.
- Timeline có 11 cảnh, 43 đoạn phụ đề; chuyển trang hữu hạn; từng phụ đề có lệnh đặt opacity về0 sau khi kết thúc. Không dùng lặp vô hạn. Motion audit tự động không bật; chuyển động kiểm tra qua mã timeline và ảnh lấy mẫu.
- Âm lượng MP4 đo được: -13,24 LUFS tích hợp, true peak -1,65 dBTP, LRA3,00 LU. Không có đỉnh đo vượt0dBTP. Đây là kiểm tra kỹ thuật, không phải tuyên bố đã nghe duyệt thủ công.
- Đối chiếu số học: Tresca200 MPa, von Mises√30400≈174,356 MPa; dự trữ1,25 và≈1,4338. Cắt thuần:125 và≈144,338 MPa; chênh≈15,47% so với Tresca. Coulomb–Mohr trong miền kéo–nén:0,4+0,4=0,8.
- Các ví dụ là giả định; không thực hiện FEA hoặc thử vật liệu. Phạm vi và các hiệu chỉnh so với PDF được ghi trong GHI-CHU.txt.
- Gói mã nguồn ZIP đã kiểm tra CRC. Các tệp sao chép vào kho được đối chiếu SHA-256 với bản đã kiểm tra.
