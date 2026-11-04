# Đầu ra và xuất bản

## Bộ tệp cho mỗi video

Trong `videos/<slug>/`:

- `<slug>.mp4`: H.264/AAC, dọc 1080×1920, 30 fps theo mặc định.
- `phu-de.vi.srt`: phụ đề tiếng Việt, không chứa thẻ strong/HTML.
- `loi-dan.txt`: lời dẫn cuối đã dùng để tạo giọng.
- `CAPTION-TIKTOK.txt`: caption đăng ngay được.
- `anh-bia.jpg`: ảnh bìa lấy từ video hoặc thiết kế có nội dung tương ứng.
- `GHI-CHU.txt`: nguồn, giả thiết, hiệu chỉnh, ví dụ giả định, tài nguyên và giấy phép.
- `KIEM-TRA.md`: kết quả kiểm tra thật và hạn chế.
- `ma-nguon-video.zip`: HTML, SVG/GSAP, font/audio/tài nguyên cần render, mã dựng và hướng dẫn dùng lại.

Không cần đóng gói tệp PDF gốc của người dùng hoặc mọi tệp tạm vào kho công khai. Không dùng tên video/ghi chú cũ khi tạo bộ mới.

## Caption TikTok

Mở bằng câu hỏi hoặc sự nhầm lẫn đúng với video, 1–2 câu giải thích giá trị người xem nhận được, một câu hỏi tương tác hoặc lời nhắc lưu, khoảng 4–7 hashtag liên quan. Không giật tít sai khoa học, không đưa một giả thiết thành bảo đảm an toàn. TikTok thường không hiển thị Markdown đậm: caption phải vẫn đọc tốt khi bỏ dấu `**`.

Ví dụ giọng điệu:

> Ứng suất phẳng ≠ biến dạng phẳng! ⚙️ σz = 0 nhưng chiều dày vẫn có thể co do Poisson. Khi nào dùng 2D, khi nào cần tấm/vỏ hoặc 3D? Lưu lại để ôn cách chọn mô hình nhé!

Sửa khoảng cách đơn vị, từ và số trong bản cuối; ví dụ trên chỉ là nội dung tham khảo, không tái dùng cho chủ đề khác.

## GitHub trong ngữ cảnh người dùng này

Kho đã được người dùng chọn: `nguyennguyenengmechanics-svg/Bien`, nhánh `main`. Cập nhật README với phần video mới, giữ nguyên các video trước. Dùng đường dẫn tải MP4 thật:

`https://github.com/nguyennguyenengmechanics-svg/Bien/raw/refs/heads/main/videos/<slug>/<slug>.mp4`

Trước khi ghi/push: kiểm tra worktree, nhánh và remote; đọc AGENTS hiện hành; fetch để biết có thay đổi đồng thời. Không force push, không ghi đè sửa đổi khác. Nếu nhánh remote tiến lên, tích hợp thay đổi phù hợp hoặc dùng nhánh/PR để giữ nguyên công việc. Không dùng skill để cấp quyền cho kho/tài khoản mới ngoài phạm vi người dùng yêu cầu.

Hoàn tất render, kiểm tra và đóng gói trước khi xử lý bước xuất bản cuối. Nếu môi trường thiếu quyền GitHub, báo đúng trở ngại và giao bản cục bộ/gói tải thay thế có thật; không bảo người dùng chờ một lần tiếp tục để nhận phần công việc vẫn có thể làm ngay.

## Câu trả lời cuối

Ngắn, tự chứa đủ thông tin. Ví dụ:

“Đã tạo xong và đưa lên GitHub.
🎬 Tải video … — MP4: URL thật
Video dài …, có giọng Việt, phụ đề và sơ đồ chuyển động; từ khóa đậm, nhấn màu rõ.
📝 Caption TikTok: URL thật”

Chỉ dùng câu “đưa lên GitHub” nếu đã xác nhận thành công. Không dán hash, log hoặc thống kê kiểm tra dài khi người dùng chỉ cần tải video.
