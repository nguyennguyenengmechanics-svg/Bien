#!/usr/bin/env python3
"""Verify a rendered academic video using FFprobe/FFmpeg; produce diagnostic artifacts."""
import argparse,json,pathlib,subprocess,math
p=argparse.ArgumentParser(description=__doc__);p.add_argument('project',type=pathlib.Path);p.add_argument('video',type=pathlib.Path);a=p.parse_args()
r=a.project.resolve();video=a.video if a.video.is_absolute()else r/a.video
cfg=json.loads((r/'project.json').read_text())
if cfg.get('demo'):raise SystemExit('Từ chối nghiệm thu mẫu im lặng. Tạo nội dung/giọng thật và đặt demo=false.')
t=json.loads((r/'timing.json').read_text());duration=round(t[-1]['start']+t[-1]['duration'],3);fps=cfg.get('fps',30);frames=math.ceil(duration*fps)
out=r/'output';out.mkdir(exist_ok=True)
def run(args,**kwargs):return subprocess.run(args,check=True,**kwargs)
d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]))
v=next(s for s in d['streams']if s['codec_type']=='video');audio=next(s for s in d['streams']if s['codec_type']=='audio')
checks=[(v['width']==1080 and v['height']==1920,'Kích thước khác1080×1920'),(v['codec_name']=='h264','Video không phải H.264'),(v['r_frame_rate']==f'{fps}/1','FPS không khớp'),(int(v['nb_frames'])==frames,'Số frame không khớp timing'),(audio['codec_name']=='aac','Âm thanh không phải AAC')]
for ok,msg in checks:
 if not ok:raise SystemExit(msg)
(out/'media-info.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
run(['ffmpeg','-v','error','-xerror','-threads','2','-i',str(video),'-map','0:v','-map','0:a','-f','null','-'])
for at,name in [(min(6,duration/2),'anh-bia.jpg'),(max(0,duration-5),'khung-ket.jpg')]:run(['ffmpeg','-v','error','-y','-ss',str(at),'-i',str(video),'-frames:v','1',str(out/name)])
interval=max(duration/12,.1)
run(['ffmpeg','-v','error','-y','-i',str(video),'-vf',f'fps=1/{interval},scale=270:-1,tile=4x3','-frames:v','1',str(out/'khung-hinh-kiem-tra.jpg')])
with (out/'final-loudness.txt').open('w')as f:run(['ffmpeg','-hide_banner','-i',str(video),'-af','loudnorm=I=-16:TP=-1.5:LRA=9:print_format=json','-f','null','-'],stdout=subprocess.DEVNULL,stderr=f)
print(f'PASS kỹ thuật: {frames}frames,1080×1920,{fps}fps,H.264/AAC,giải mã toàn tệp. Cần xem ảnh, rà công thức và nghe duyệt khi có khả năng trước khi nghiệm thu nội dung.')
