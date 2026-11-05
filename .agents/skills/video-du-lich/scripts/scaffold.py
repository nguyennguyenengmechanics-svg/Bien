"""Copy the media-free v3 starter; never overwrite an existing project."""
import argparse,pathlib,shutil
p=argparse.ArgumentParser(description=__doc__);p.add_argument('destination',type=pathlib.Path);a=p.parse_args();dest=a.destination.resolve()
if dest.exists() and (not dest.is_dir()or any(dest.iterdir())):p.error('Thư mục đích phải chưa tồn tại hoặc đang rỗng.')
src=pathlib.Path(__file__).resolve().parents[1]/'assets/template';shutil.copytree(src,dest,dirs_exist_ok=True);(dest/'output').mkdir(exist_ok=True)
print('Đã tạo mẫu v3 tại',dest)
print('Chưa có video hoàn chỉnh: cần kịch bản đã duyệt, footage/ảnh đã xử lý, giọng đọc, nhạc và timing đo thực.')
