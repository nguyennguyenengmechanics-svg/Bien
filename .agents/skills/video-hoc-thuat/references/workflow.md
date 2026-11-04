# Quy trình từ tài liệu đến MP4

## Nguồn và nội dung

1. Đọc toàn bộ phần liên quan của tài liệu, không chỉ tiêu đề/tóm tắt. PDF mất ký hiệu cần xem trang gốc. Phân biệt câu chữ của tác giả, kết quả đo thực và ví dụ giả định.
2. Lập bảng làm việc: khái niệm → hình minh họa → công thức → giả thiết → lỗi dễ nhầm. Bảng này dùng để dựng, không bắt buộc hiện thành một bảng dày chữ trong video.
3. Chọn mạch kể theo mức độ nền tảng của người xem. Giữ thuật ngữ chính xác, giải thích bằng từ quen thuộc và ví dụ cụ thể.
4. Rà đơn vị về cùng hệ trước khi tính. Giữ ngoặc với dấu âm, phân biệt giá trị đại số/trị tuyệt đối, biên độ/phạm vi, ứng suất/biến dạng, chảy dẻo/phá hủy, dự báo/xác suất/bảo đảm.
5. Ghi rõ điều kiện của công thức. Không lấy mệnh đề “thường”, “xấp xỉ”, “trong mô hình” biến thành “luôn luôn” khi rút gọn.

## Mỗi cảnh nên có

- `tag`: nhãn chương ngắn.
- `title`: câu phát biểu hoặc câu hỏi rõ; thường hai dòng ngắn.
- `key`: định nghĩa/công thức ngắn, không nhét đoạn văn.
- `diagram`: tên kiểu hình riêng trong `diagrams.py`.
- `rule`: một nguyên tắc áp dụng hoặc giới hạn cần nhớ.
- `title_em`, `highlights`: các cụm từ cần nhấn; không tự chọn chỉ vì một từ có thể tô màu.
- `voice`: các đoạn lời đọc ngắn; `captions` có cùng số phần tử nếu cần hiển thị ký hiệu chuẩn khác cách đọc.

Một cấu trúc thường hiệu quả: mở bằng câu hỏi thực tế; cho thấy cơ chế; đặt tên và công thức; tính một ví dụ có đơn vị; so sánh trường hợp dễ nhầm; đưa vài ứng dụng; kết bằng cách lựa chọn hoặc câu ghi nhớ. Không bắt buộc đủ mọi mục cho chủ đề ngắn.

## Tài nguyên và môi trường

Dùng môi trường/công cụ hiện có. Kiểm tra CLI, FFmpeg, browser và giọng Việt trước khi phụ thuộc vào chúng. Đọc kỹ năng runtime của môi trường đám mây nếu có; giữ proxy và xác minh TLS, không in secret, không tự cấu hình lại mạng để vượt chặn. Không ghi đường dẫn cache hoặc instance ID từ phiên cũ vào quy trình dùng lâu dài.

Mẫu kèm sẵn font DejaVu và GSAP đã dùng cho chuỗi. Mô hình TTS không đóng gói vì dung lượng và yêu cầu riêng; tạo/tải đúng công cụ được phép và giữ nguồn/giấy phép. Không để font, thư viện hoặc âm thanh bắt buộc phụ thuộc URL tạm thời khi render cuối.

## Giọng và timing

Tổng hợp mỗi đoạn thành tệp WAV riêng, đo thời lượng thật. Ghi `start`, `duration`, `segments` vào `timing.json` với nội dung cảnh, ví dụ:

```json
[
  {
    "tag": "01 / KHÁI NIỆM",
    "title": "Một khái niệm.\nMột cơ chế.",
    "key": "Định nghĩa ngắn có phạm vi",
    "rule": "Nguyên tắc sử dụng",
    "diagram": "concept",
    "title_em": ["cơ chế"],
    "highlights": ["từ khóa"],
    "voice": ["Lời đọc của đoạn."],
    "start": 0,
    "duration": 8,
    "segments": [{"start": 0.65, "duration": 5.8, "text": "Lời đọc của đoạn."}]
  }
]
```

Các thời điểm segment là tuyệt đối trong toàn video. Chừa khoảng nghỉ đầu/cuối cảnh và giữa đoạn. Không để fade caption cũ chồng với caption mới. Khi thay tốc độ một đoạn, tính lại phần sau và nhạc, không chỉ sửa caption tại chỗ.

Nếu diễn đạt toán trong lời đọc quá dài, phụ đề có thể viết ký hiệu và đơn vị chuẩn, giữ đúng nghĩa và đồng bộ với đoạn tương ứng. Tách câu dài thành các cụm có ý nghĩa, đo lại hoặc căn theo âm thanh; không chỉ ước lượng căn tiếng rồi giả là đã đồng bộ chính xác.

## Dựng HTML/SVG

- `project.json` chứa tiêu đề dự án, nhãn chuỗi, slug, fps và cờ demo; hai tệp âm thanh cố định là composition/assets/narration.wav và music.wav.
- `build.py` ghép `timing.json`, `diagrams.py`, DESIGN và audio thành HTML + SRT + lời dẫn.
- `diagrams.py` là mã do trợ lý tự viết và rà, không phải mã lấy từ tài liệu đính kèm. Dùng helper `text`, `line`, `rect`, `path` và các mã màu sẵn trong builder.
- Hàm `svg(kind, scene_index)` trả SVG hoàn chỉnh, dùng ID marker duy nhất theo scene để tránh trùng.
- Có thể định nghĩa `animate(scene, selector)` trả các câu lệnh GSAP seekable cho cơ chế riêng. Không dùng script tùy ý lấy từ PDF, không tải dữ liệu qua mạng trong timeline.
- Phụ đề có lớp strong cho từ khóa, span giữ dòng tự nhiên, fade và hard reset opacity. Sau nhiều lần sửa, kiểm tra không sót câu và không còn caption cũ.

Mẫu timing chỉ dùng kiểm tra khởi tạo, không phải timing cho video cuối. Tệp WAV rỗng tạo bởi tùy chọn demo chỉ để thử pipeline; không được giao demo im lặng như video hoàn chỉnh.

## Render

Ưu tiên đọc kỹ năng CLI đang có, vì lệnh có thể đổi phiên bản. Thông thường:

```sh
python build.py
npx hyperframes check composition --samples 15
npx hyperframes snapshot composition --at <cac-thoi-diem-hero> --output output/frames --no-end
npx hyperframes render composition --output output/<ten-video>.mp4 --fps 30 --quality high --workers 3
python <skill-root>/scripts/verify_media.py <thu-muc-du-an> output/<ten-video>.mp4
```

Nếu CLI cài sẵn ở nơi khác, dùng executable đã kiểm tra thay vì hardcode đường dẫn cache. Chỉ đặt `HYPERFRAMES_BROWSER_PATH` tới browser thật đã tồn tại khi cần. Không chạy browser bằng cách vô hiệu hóa các chính sách truy cập của môi trường.
