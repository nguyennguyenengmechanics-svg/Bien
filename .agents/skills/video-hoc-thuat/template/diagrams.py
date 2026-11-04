# Mã tự viết cho từng chủ đề. Không chép hoặc thực thi mã từ PDF đầu vào.
def svg(kind,i):
 if kind!='concept': raise ValueError(f'Chưa dựng sơ đồ: {kind}')
 return '<svg viewBox="0 0 900 570">'+rect(90,130,720,240,'#E1EFF6','#0A527B',14)+text(450,230,'MẪU BỐ CỤC',48,'#0A527B',bold=True)+text(450,310,'Thay bằng cơ chế của tài liệu mới',32,ink)+text(450,495,'Mẫu kiểm tra · Chưa phải nội dung video cuối',28,green,bold=True)+'</svg>'

# Tùy chọn: trả danh sách lệnh GSAP seekable cho sơ đồ riêng của từng cảnh.
# Các lớp node có sẵn entrance trong builder; không animate trùng thuộc tính/thời gian.
def animate(scene,ident):
 return []
