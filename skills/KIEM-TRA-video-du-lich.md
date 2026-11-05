# Kiểm tra kỹ năng video-du-lich

- Skill Creator quick_validate: đạt cho bản trong kho và bản cài cá nhân.
- Đã cài vào $CODEX_HOME/skills/video-du-lich trong môi trường hiện tại; đối chiếu SHA256 từng tệp với nguồn trong kho. Không suy ra đã cài toàn tài khoản hoặc trên thiết bị khác; có thể cần làm mới danh sách kỹ năng khi giao diện chưa cập nhật.
- Mẫu chuẩn được ghim vào video METI–Narita v3, không chuyển mặc định sang v4. Thông tin METI, giờ bay và hai nhóm biển được giữ dưới dạng ví dụ tham chiếu, không thành mặc định của mọi hành trình.
- Đã chạy scaffold với thư mục mới; từ chối ghi đè thư mục có tệp; builder từ chối timeline rỗng.
- Đã build mẫu 16 giây / 480 khung hình có bốn loại cảnh: footage, signs, procedure cùng thẻ phụ và photo. Bố cục không lỗi ở bốn mốc 2/6/10/14 giây; đã xem ảnh chụp cả bốn cảnh.
- Mẫu kiểm tra dùng nền đơn sắc, ảnh màu và âm thanh im lặng, có nhãn kiểm tra rõ. Mẫu này ở ngoài gói kỹ năng, không giao như video thật. Không render lại video du lịch hoặc xác nhận chất lượng âm thanh trong tác vụ tạo kỹ năng.
- ZIP CRC đạt; chỉ có chỉ dẫn, mẫu mã/CSS, metadata gọi kỹ năng, font Be Vietnam Pro/OFL và GSAP cùng đầu giấy phép. Không có cảnh quay/ảnh cá nhân, MOV/HEIC/RAR, WAV hay video tham khảo.
- Kiểm tra này xác minh cấu trúc và mẫu dựng, không bảo đảm mọi kịch bản/footage tương lai đều phù hợp. Cần kiểm tra tài nguyên, lời dẫn, dữ liệu thời gian và bản render thực theo kỹ năng.
