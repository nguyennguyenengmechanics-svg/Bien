---
name: video-du-lich
description: Dựng vlog du lịch hoặc nhật ký hành trình tiếng Việt từ cảnh quay và ảnh, theo phong cách METI–Narita v3 mà người dùng đã chọn. Dùng khi gọi $video-du-lich hoặc yêu cầu làm vlog tương tự v3; yêu cầu chỉ viết caption hoặc sửa kịch bản thì chỉ xử lý phần đó.
---

# Video du lịch — mẫu chuẩn v3

Tạo vlog hoàn chỉnh có thể tải về, giữ phong cách **METI Japan Internship v3**, không mặc định chuyển sang v4 hoặc phong cách video học thuật. Chỉ dẫn mới của người dùng được ưu tiên. Thông báo ngắn rằng đang dùng kỹ năng.

## Dấu ấn đã được chọn

- Dọc **1080 × 1920, 30 fps, MP4 H.264/AAC**; thời lượng theo câu chuyện và tư liệu, không cố kéo dài. Mẫu gốc khoảng 91 giây, không phải giới hạn cho mọi vlog.
- **Be Vietnam Pro**: tiêu đề 60px semibold, lời chú thích khoảng 35px medium, nhãn khoảng 28px; từ khóa bold, nhấn màu có chọn lọc. Không dùng serif của kỹ năng học thuật.
- Kem **#FCFAF5**, mực **#17353B**, xanh ngọc **#31746A / #245F55**, nhấn đất **#A84936**. Thẻ sáng bo góc nhẹ, viền mảnh, bóng tiết chế. Giữ hình người và cảnh dễ nhìn; không biến thành slide chữ dày.
- Thương hiệu nhỏ phía trên, tiêu đề gọn, vùng cảnh quay lớn, phụ đề ở dưới, tiến trình mảnh. Chuyển động êm và có mục đích; không tự thêm montage nhanh, tiêu đề trắng không nền hoặc nhạc 120BPM của v4.
- Cảnh thật và mục đích chuyến đi là chính. Website, mẹo thủ tục và thông tin tham khảo là **thẻ phụ nhỏ**, chỉ xuất hiện lúc lời dẫn liên quan.

Đọc [thiết kế v3](references/DESIGN.md) trước khi dựng. Mẫu CSS, font và bộ dựng không chứa tư liệu cá nhân nằm trong `assets/template/`.

## Kể đúng chuyến đi

Xác định mục đích trung tâm từ yêu cầu hiện tại: du lịch, đi học, thực tập, công tác hoặc trải nghiệm. Với video mẫu, trọng tâm là **tham gia METI Japan Internship**, không phải hướng dẫn nhập cảnh. Không áp mục đích METI hay địa điểm Nhật Bản cho chuyến khác.

Đọc và kiểm tra tư liệu thực: thứ tự phần, độ dài, hướng xoay, giờ trên bảng, lời người dùng xác nhận, âm thanh, cảnh có thể dùng và cảnh thiếu. Giữ thứ tự người dùng yêu cầu; chỉ dùng hook đảo thời gian khi phù hợp và đã được chốt. Không suy đoán ngày đến, quốc tịch người trong ảnh, loại visa hoặc sự kiện chưa được xác nhận.

Giờ khởi hành/đến phải có múi giờ địa phương nếu khác nhau. Không lấy hiệu hai giờ địa phương làm thời gian bay. Biển sân bay phải đọc **đúng nhóm chữ và hướng thực tế**, không tách từ thành những lối đi không tồn tại. Ví dụ v3 Narita có hai nhóm: **“Arrivals, Domestic”** và **“International Transfer”**; đây là ví dụ của biển ấy, không phải quy tắc cho mọi sân bay.

Cảnh không được quay: kể bằng lời và thẻ có nhãn, không dùng hình khác giả làm cảnh người dùng đã quay. Với Nhật, chỉ nhắc Visit Japan Web khi liên quan; không hứa làm thủ tục nhanh chắc chắn hay nói người dùng đã dùng nếu chưa xác nhận. Hình minh họa giao diện phải có nhãn khi không phải ảnh chụp trực tiếp đã kiểm tra. Không đưa QR nhập cảnh cá nhân vào phần minh họa.

## Kịch bản trước, dựng sau

Đối với vlog mới, mặc định trình bày **kịch bản cụ thể để người dùng duyệt trước khi dựng bản đầy đủ**, như quy trình người dùng đã yêu cầu cho vlog gốc. Đưa bảng ngắn: cảnh/đoạn tư liệu → lời dẫn → chữ nhấn → thẻ phụ hoặc cảnh không quay. Có thể kiểm tra file, chuyển HEIC/HEVC và dựng mẫu tĩnh trong lúc chờ. Nếu kịch bản đã được duyệt hoặc người dùng yêu cầu làm thẳng, tiếp tục trong phạm vi đó, không hỏi duyệt lại chỉ vì kỹ năng.

Giọng kể tiếng Việt tự nhiên, thường xưng “mình”, bám trải nghiệm thật, có mở–hành trình–kết. Dùng ảnh cuối hoặc khoảnh khắc gặp gỡ khi người dùng chọn, không tự mặc định mọi chuyến kết thúc bằng ảnh hộ chiếu. Video tham khảo dùng để hiểu nhịp và cách trình bày, không mặc định lấy hình/nhạc/giọng của người khác.

## Dựng, kiểm tra và giao

Theo [quy trình và mẫu dữ liệu](references/workflow.md):

1. Cắt và nối cảnh thật, bỏ đoạn lặp/logo kết ứng dụng khi thích hợp; cân sáng nhẹ và giữ màu tự nhiên. Che dữ liệu vé, QR/barcode, địa chỉ và nhãn cá nhân nhìn thấy trước khi đóng gói tư liệu dẫn xuất.
2. Tạo giọng Việt bằng khả năng thực sự có, đo từng đoạn WAV rồi lập `timing.json`. Phụ đề đúng nghĩa, đồng bộ, tối đa khoảng 1–2 cụm đậm/màu mỗi đoạn; không chồng caption.
3. Nhạc nhẹ hơn lời, dùng tài nguyên có quyền sử dụng. Nếu yêu cầu nhạc trend, kiểm tra nguồn và thời điểm thực tế; khi không truy cập được, báo đúng hạn chế, không gọi nhạc tự tạo là nhạc trend. Có thể giao thêm bản chỉ lời dẫn để thêm âm thanh trong TikTok.
4. Nếu dùng HyperFrames/GSAP, đọc kỹ năng đang có và giữ timeline deterministic, paused, đăng ký đúng, hiệu ứng hữu hạn. Khởi tạo mẫu bằng `scripts/scaffold.py`; điền media thật và dữ liệu đã duyệt trước khi build.
5. Kiểm tra bố cục và tương phản, xem các khung nhiều nội dung nhất và ảnh từ MP4 cuối; FFprobe/FFmpeg kiểm tra kích thước, fps, codec, số frame, giải mã toàn tệp và mức âm. Chỉ nói đã nghe/xem điều thực sự đã làm.
6. Giao MP4, SRT, lời dẫn, caption TikTok, ảnh bìa, ghi chú và ZIP mã nguồn cần thiết để render. Không đưa MOV/HEIC/RAR gốc hay video tham khảo vào gói công khai.

Trong ngữ cảnh kho Bien này, tiếp tục cách giao đã được người dùng chọn: đưa kết quả lên **nguyennguyenengmechanics-svg/Bien**, giữ phiên bản cũ, không force push và chỉ thêm tệp thuộc công việc. Kỹ năng không cấp phép truy cập hoặc đăng sang kho/tài khoản khác. Chỉ nói đã đưa lên GitHub sau push thành công.

## Cách gọi

> Dùng $video-du-lich dựng vlog từ các clip này theo mẫu v3. Trọng tâm là [mục đích chuyến đi]. Đưa kịch bản cho tôi duyệt trước.

Nếu chỉ cần caption, trả caption phù hợp, không tự render lại video.
