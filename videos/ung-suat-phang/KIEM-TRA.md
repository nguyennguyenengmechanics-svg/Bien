# Kiểm tra video ứng suất phẳng

- MP4 H.264, 1080 × 1920, 30 fps, 7.455 khung hình; thời lượng 248,500 giây. Âm thanh AAC.
- FFmpeg giải mã toàn bộ hình và tiếng với `-xerror`: đạt.
- HyperFrames: lint, runtime, layout, craft và audio không có lỗi/cảnh báo. Bố cục lấy mẫu 15 thời điểm; tương phản 97/97 đạt. Kiểm tra lấy mẫu không chứng nhận mọi khung hình.
- Đã xem ảnh trước xuất của 11 cảnh và ảnh tổng hợp từ MP4. Đã sửa nhãn sát mép, tách ký hiệu bề rộng bánh răng khỏi tiêu đề và tăng thời gian đọc hai đoạn mở đầu.
- Timeline có 11 cảnh, 35 đoạn phụ đề, chuyển trang hữu hạn và lệnh đặt opacity về 0 sau mỗi đoạn. Không có lặp vô hạn. Motion audit tự động không bật; chuyển động rà qua mã timeline và ảnh lấy mẫu.
- Âm lượng đo trên MP4: -13,22 LUFS tích hợp, true peak -1,68 dBTP, LRA 3,20 LU. Không có đỉnh đo vượt 0 dBTP. Đây là đo kỹ thuật, không phải tuyên bố đã nghe duyệt thủ công.
- Đối chiếu ví dụ: εz=−0,3×100/200.000=−0,00015=−150 µε; nếu εz=0 và cùng σx=100 MPa, σy=0 thì σz=30 MPa. Bình trụ kín thành mỏng: Pr/t=50 MPa, Pr/(2t)=25 MPa, t/r=0,02; σr từ−1 đến0 MPa.
- Không thực hiện FEA hoặc thí nghiệm. Hình co dày/uốn phóng đại để minh họa. Phạm vi giả thiết và các hiệu chỉnh so với PDF xem GHI-CHU.txt.
- ZIP mã nguồn đã kiểm tra CRC. Các tệp đưa vào kho được đối chiếu SHA-256 với bản đã kiểm tra.
