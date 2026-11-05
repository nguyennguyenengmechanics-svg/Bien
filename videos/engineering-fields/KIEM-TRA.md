# Kiểm tra — 22 lĩnh vực kỹ thuật: hiểu đúng để chọn ngành

- MP4 h264/aac, 1080 × 1920, 30/1 fps, 9342 khung hình, 311.400 giây.
- FFmpeg đã giải mã toàn bộ hình và âm thanh, không lỗi. WAV lời đọc có thật; timing đo theo từng đoạn WAV, không ước lượng theo độ dài chữ.
- Lint/runtime cuối: không lỗi, không cảnh báo. Bố cục cuối không lỗi ở 12 mốc kiểm tra. Tương phản: 111/111 mẫu đạt ở lượt kiểm tra màu. Các nhãn sát nhau đã được giãn và mũi tên làm rõ sau đó.
- Đã xem ảnh hero của từng cảnh và ảnh trích từ MP4 cuối (bìa, cảnh nội dung/đồ thị/công thức và khung kết). Đây là xem mẫu, không phải xem thủ công mọi khung hình.
- Đo âm thanh từ MP4: -13.35 LUFS; true peak -1.67 dBTP; LRA 2.80 LU. Không khẳng định đã nghe duyệt thủ công toàn bộ âm thanh.
- Lượt craft ban đầu có 42 cảnh báo. Đã rà: chủ yếu là ngưỡng thời gian đọc dùng chuỗi tách bằng khoảng trắng. Trong tiếng Việt, chuỗi này thường đếm tiếng thay vì từ ghép. Giữ phụ đề theo nhịp giọng thực và khu vực chữ 34px; cảnh báo tốc độ đọc là giới hạn còn ghi nhận, không báo thành “0 cảnh báo”. Motion audit tự động không bật; timeline hữu hạn, seekable và có chuyển cảnh. Nhãn được kiểm tra bằng ảnh và bộ đo bố cục.
- Nội dung, số giả định và giới hạn mô hình được ghi trong GHI-CHU.txt; không coi sơ đồ là dữ liệu đo hoặc kết quả FEA/CFD thực. Các nguồn lương, tuyển dụng, số thương mại chưa được xác minh hiện hành đã được bỏ hoặc diễn đạt theo phạm vi.
- Gói ZIP kèm HTML/SVG, font/giấy phép, WAV cuối và mã dựng; không kèm mô hình TTS nặng, cache hoặc tệp đính kèm gốc.

Cảnh báo cỡ chữ ở ba dòng ghi chú sơ đồ trong phần vào cảnh: khoảng27,3–28px do hiệu ứng scale nhẹ. Các nhãn nội dung chính lớn hơn; đã xem ảnh và giữ hiệu ứng. Không dùng data-layout-ignore để che cảnh báo này.
