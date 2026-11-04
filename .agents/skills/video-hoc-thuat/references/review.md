# Kiểm tra trước khi giao

## Nội dung

- Định nghĩa và ký hiệu nhất quán; đơn vị, dấu âm, ngoặc và số học đúng.
- Công thức đi cùng giả thiết. Không gọi kết quả mô hình là kết quả thử nghiệm.
- Ví dụ số giả định có nhãn; biến dạng phóng đại, đồ thị định tính và hình cắt đều được giải thích.
- Không khẳng định đã làm FEA, thí nghiệm hoặc tra nguồn khi chưa làm.

## Hình và chuyển động

- Lint/runtime/layout đạt; mọi cảnh báo phải được xem và sửa hoặc ghi nhận với lý do cụ thể.
- Xem ảnh từng cảnh ở trạng thái hoàn chỉnh; công cụ đạt không thay thế nhìn ảnh.
- Tiêu đề từ frame 0; không mất chữ ở SVG, sát mép thẻ, bị lớp khác che hoặc strong tạo các cột.
- Công thức đọc được trên điện thoại; trục/đơn vị/mũi tên đúng. Nhánh sơ đồ đậm và dễ phân biệt.
- Chuyển cảnh có chủ ý, không để cảnh trước trống trước khi chuyển. Caption hết phải biến mất; không có vòng lặp vô hạn.

## Âm thanh và phụ đề

- Có giọng Việt thật trong tệp xuất, không chỉ có thẻ audio tham chiếu tệp thiếu.
- Từ ngữ/đơn vị phát âm dễ hiểu; thời gian theo WAV đã dùng, cập nhật sau mọi thay đổi.
- Nhạc nhẹ hơn giọng. Mục tiêu tham khảo khoảng −16 đến −13 LUFS tích hợp, true peak không cao hơn khoảng −1 dBTP; ưu tiên nghe rõ, không ép xử lý thêm chỉ để đạt một con số.
- Đo mức âm trong MP4. Nếu có công cụ nghe, nghe các đoạn khó; chỉ ghi “đã nghe duyệt” khi thực sự đã nghe. Nếu chỉ đo, báo là kiểm tra kỹ thuật.
- Caption không nhanh quá hoặc cắt giữa ý; nhấn 1–2 cụm quan trọng bằng bold/màu, không làm cả câu rối.

## MP4 và gói giao

- FFprobe xác nhận kích thước, fps, codec, số frame và thời lượng.
- FFmpeg giải mã toàn tệp không lỗi. Nếu có lỗi, sửa hoặc render lại rồi kiểm tra lại.
- Xem ảnh trích từ chính MP4, gồm cảnh công thức, bìa và kết; đừng chỉ dựa vào ảnh preview HTML.
- ZIP có nguồn và mọi tài nguyên render cần thiết, CRC đạt; loại bỏ secret, credential, mô hình TTS nặng không cần thiết, cache và tệp tạm.
- `KIEM-TRA.md` ghi kết quả thật, số mẫu và giới hạn; không trình bày kiểm tra lấy mẫu như chứng nhận toàn bộ nội dung.
- Nếu sao chép MP4 đã kiểm tra vào kho, đối chiếu hash trước khi commit.
- Chỉ cập nhật README và tệp thuộc công việc; xác nhận push thành công trước khi giao link GitHub.
