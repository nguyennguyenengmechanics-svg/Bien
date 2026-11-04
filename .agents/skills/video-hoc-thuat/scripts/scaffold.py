#!/usr/bin/env python3
"""Create a portable project. --demo adds SILENT test WAVs, never deliver as narration."""
import argparse,json,pathlib,shutil,wave
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('destination',type=pathlib.Path);p.add_argument('--demo',action='store_true')
a=p.parse_args();root=pathlib.Path(__file__).resolve().parents[1];dest=a.destination.resolve()
if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):p.error('Thư mục đích phải chưa tồn tại hoặc đang rỗng; không ghi đè công việc cũ.')
shutil.copytree(root/'template',dest,dirs_exist_ok=True)
(dest/'output').mkdir(exist_ok=True)
if a.demo:
 config=json.loads((dest/'project.json').read_text());config.update(demo=True,title='Mẫu kiểm tra bố cục',brand='MẪU KỸ NĂNG');(dest/'project.json').write_text(json.dumps(config,ensure_ascii=False,indent=2))
 scene=dict(tag='01 / MẪU KIỂM TRA',title='Từ khóa đậm.\nSơ đồ rõ.',key='Mẫu kiểm tra pipeline; cần thay bằng nội dung mới',rule='Không giao mẫu im lặng như video hoàn chỉnh.',diagram='concept',title_em=['Từ khóa đậm'],highlights=['nội dung mới'],voice=['Đây là mẫu để kiểm tra bố cục trước khi tạo nội dung mới.'],start=0,duration=10,segments=[dict(start=.65,duration=8,text='Đây là mẫu để kiểm tra bố cục trước khi tạo nội dung mới.')])
 for n in ['timing.json','scenes.json']:(dest/n).write_text(json.dumps([scene],ensure_ascii=False,indent=2))
 for name in ['narration.wav','music.wav']:
  with wave.open(str(dest/'composition/assets'/name),'wb')as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(22050);f.writeframes(bytes(22050*2*10))
print(f'Đã tạo {dest}')
print('DEMO IM LẶNG: chỉ kiểm tra bố cục, không phải video để giao.' if a.demo else 'Điền project/scenes/timing, dựng diagrams và tạo narration.wav + music.wav trước khi chạy build.py.')
