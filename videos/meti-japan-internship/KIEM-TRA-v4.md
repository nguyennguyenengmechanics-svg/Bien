# Kiểm tra v4 — Mở đầu nhanh, hình quay thoáng

## Thay đổi

Sáu giây đầu: bốn cảnh 1,5 giây từ part 1 đã xử lý, chữ mở đầu xuất hiện theo nhịp và đường bay SGN → NRT. Bỏ cảnh hộ chiếu cần che nhiều thông tin ở mở đầu. Sau mốc 6 giây, nguồn hình tiếp tục theo trình tự đã duyệt. Bỏ nền kín sau chữ ở cảnh quay; dùng chữ trắng, bóng và lớp tối trong suốt ở mép. Giữ đúng hai hướng Arrivals, Domestic / International Transfer; thẻ Visit Japan Web vẫn nhỏ.

## Xác minh

- Hai MP4 H.264/AAC, 1080 × 1920, 30 fps, 2744 khung hình, 91,47 giây. Cả hai giải mã toàn bộ thành công.
- Payload video SHA256 của hai bản giống nhau: c580924d7e984651f871479822d2f7beea3d2e699b54d0008d0f6c61b1b6687c. Bản chỉ lời dẫn thay track âm thanh, không đổi hình.
- Đã xem khung hình mẫu từ MP4 cuối ở đoạn mở đầu và Narita, cùng các khung xem thử ở đoạn người, máy bay, biển chỉ dẫn và cuối video. Không phải xem thủ công mọi khung hình.
- Lint/runtime không lỗi; bố cục cuối: không lỗi ở 13 mốc kiểm tra.
- Kiểm tra tương phản đầu tiên 53/53 mẫu đạt. Sau khi tăng chữ phụ lên tối thiểu 28px, kiểm tra mở đầu phát hiện dòng METI có tỷ lệ 2,97:1 ở 2,3 giây. Đã đổi dòng này sang trắng và render lại đúng 6 giây đầu; kiểm tra cuối tại 2,3 giây đạt 13/13 mẫu, không cảnh báo. File xuất cuối dùng đoạn đã sửa.
- Motion audit tự động không bật. Đã kiểm tra các mốc mở đầu .4, 1.4, 2.3, 3.8, 5.2 giây; timeline hữu hạn/paused.
- Âm thanh bản có nhạc: −16,11 LUFS; true peak −2,85 dBTP; LRA 4,70 LU. Đây là phép đo kỹ thuật, không khẳng định đã nghe thủ công toàn bộ lời đọc.
- SHA256 lời đọc, phụ đề, ảnh bạn bè đã xử lý và ảnh biển gốc không đổi so với v3. Không đưa tệp MOV/HEIC/RAR gốc vào gói mã nguồn.

## Nhạc còn chờ

Nhạc bản xem thử là bản gốc tạm 120 BPM, không phải bài đang trend được xác minh. Đã tạo bản riêng chỉ lời dẫn để ghép âm thanh TikTok. Các trang tra cứu bị proxy403; yêu cầu chọn và chèn nhạc trend vẫn chưa hoàn tất. Đã lưu bản nháp bổ sung các nguồn tra cứu vào mạng; chưa áp dụng/publish. Xem NHAC-TIKTOK-v4.md.

Bản v1/v2/v3 được giữ nguyên trên GitHub.
