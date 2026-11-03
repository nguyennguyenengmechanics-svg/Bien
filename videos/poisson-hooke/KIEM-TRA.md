# Kiểm tra video hệ số Poisson và Hooke tổng quát

- MP4: H.264, 1080 × 1920, 30 fps, 6.956 khung hình, khoảng 231,87 giây.
- Âm thanh AAC 48 kHz; đo trên MP4: -13,43 LUFS, true peak -1,63 dBTP.
- FFmpeg giải mã toàn bộ hình và tiếng với `-xerror`: thành công.
- HyperFrames: lint, runtime, layout, contrast và audio không có lỗi; không có cảnh báo độ tương phản.
- Đã xem khung đại diện của đủ 12 cảnh trước xuất. Đã xem lại bảng khung trích từ MP4 và khung cuối ví dụ hai trục, có đủ dữ liệu, công thức và kết quả.
- Các phương trình Hooke phần ứng suất pháp đã rà đúng ngoặc: toàn bộ [σi - ν(σj + σk)] chia E, sửa sự thiếu nhất quán trong phương trình cuối tài liệu nguồn.
- Đối chiếu số học: ε dọc = 0,1/100 = 0,001; ε bên = -0,006/20 = -0,0003; ν = 0,3.
- Ví dụ đa trục E = 200000 MPa, ν = 0,3, σ = (100,50,0) MPa: ε = (0,000425; 0,000100; -0,000225). Tổng = 0,0003 = 0,03%, khớp công thức biến dạng thể tích bậc nhất.
- Các ví dụ số được ghi là giả định minh họa; hình co–nở có phóng đại, không dùng để suy ra giá trị ν từ kích thước trên hình.
- Còn 5 cảnh báo craft: khung 0 bắt đầu hiệu ứng vào; nhãn phụ dưới ngưỡng chữ đề xuất; 3 câu phụ đề ngắn hơn ngưỡng đọc tự động khoảng 0,05–0,17 giây. Không tắt kiểm tra để che cảnh báo; có ảnh bìa riêng.
- Mã nguồn ZIP đã kiểm tra CRC, không phát hiện lỗi đóng gói.
- Chưa có đánh giá nghe độc lập hay thử nghiệm vật liệu. Sơ đồ và khối lập phương là minh họa nguyên lý, không phải mô phỏng vật liệu, dữ liệu đo hoặc chứng nhận thiết kế. Xem GHI-CHU.txt về giả thiết và giới hạn kỹ thuật.
