import json,pathlib,html,shutil,math
R=pathlib.Path(__file__).parent; P=R/'composition'
config=json.loads((R/'project.json').read_text())
scenes=json.loads((R/'timing.json').read_text())
if not scenes: raise SystemExit('Hãy điền timing.json từ lời đọc thực trước khi build.')
last_end=0
for scene in scenes:
 if scene['start'] < last_end-.002 or scene['duration'] <= 0: raise ValueError('Các cảnh phải có thời gian tăng và không chồng lấn.')
 last_end=scene['start']+scene['duration']
 prev_end=scene['start']-.25
 for seg in scene['segments']:
  if seg['start'] < prev_end+.25-.002: raise ValueError('Để ít nhất0,25giây giữa hai caption; tránh chồng fade.')
  prev_end=seg['start']+seg['duration']
  if seg['duration'] <= 0 or seg['start'] < scene['start'] or seg['start']+seg['duration'] > last_end+.002: raise ValueError('Đoạn phụ đề nằm ngoài cảnh.')
for name in ('narration.wav','music.wav'):
 if not (P/'assets'/name).is_file(): raise SystemExit(f'Thiếu composition/assets/{name}; tạo âm thanh trước khi build.')
(R/'output').mkdir(exist_ok=True)

E=html.escape
import re
def rich(value, words):
 escaped=E(value)
 chosen=[w for w in sorted(words,key=len,reverse=True) if w.casefold() in value.casefold()][:2]
 if not chosen:return escaped
 rx=re.compile('|'.join(re.escape(E(w)) for w in chosen),re.I)
 return rx.sub(lambda m:'<strong class="em">'+m.group(0)+'</strong>',escaped)

ink='#142D38';red='#B83B16';green='#2D6842';pale='#E5E7DE'
def text(x,y,s,size=30,color=ink,anchor='middle',bold=False,cls=''):
 size=max(size,28)
 return f'<text class="{cls}" x="{x}" y="{y}" fill="{color}" text-anchor="{anchor}" font-family="DejaVu Sans" font-size="{size}" font-weight="{700 if bold else 400}">{E(s)}</text>'
def line(x1,y1,x2,y2,color=ink,w=5,extra=''):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" {extra}/>'
def rect(x,y,w,h,fill=pale,stroke=ink,rx=10,extra=''):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="4" {extra}/>'
def path(d,color=ink,w=6,fill='none',extra=''):
 return f'<path d="{d}" stroke="{color}" stroke-width="{w}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def arrow(x1,y1,x2,y2,idx,color=red):
 return line(x1,y1,x2,y2,color,6,f'marker-end="url(#a{idx})" class="force"')
def support(x,y):
 return path(f'M{x-35} {y+30} L{x} {y} L{x+35} {y+30} Z',ink,4,pale)+line(x-45,y+40,x+45,y+40,ink,4)
def labelbox(x,y,w,s,color=ink):
 return rect(x,y,w,54,'#F1F0E4','none',10)+text(x+w/2,y+36,s,25,color,bold=True)
exec((R/'diagrams.py').read_text())
css='''.em{font-weight:700;color:#A82F0D;background:#FFE1BD;padding:1px 5px;border-radius:5px}.headline .em{background:none;padding:0;color:#B83B16}.growing-crack,.stage-crack,.existing-crack{stroke-dasharray:300;stroke-dashoffset:0}.caption strong{font-weight:700}@font-face{font-family:"DejaVu Serif";src:url(assets/DejaVuSerif-Bold.ttf);font-weight:700}@font-face{font-family:"DejaVu Sans";src:url(assets/DejaVuSans.ttf);font-weight:400}@font-face{font-family:"DejaVu Sans";src:url(assets/DejaVuSans-Bold.ttf);font-weight:700}*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#F1F0E4;color:#142D38;font-family:"DejaVu Sans",sans-serif}#root{width:1080px;height:1920px;position:relative}.scene{position:absolute;inset:0;width:1080px;height:1920px;background:#F1F0E4;overflow:hidden}.scene-content{width:100%;height:100%;padding:90px 80px 110px;display:flex;flex-direction:column;gap:25px}.brand{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #142D3840;padding-bottom:24px;font-size:28px;letter-spacing:3px;font-weight:700}.brand span:last-child{color:#B83B16;letter-spacing:1px}.kicker{font-size:28px;color:#B83B16;font-weight:700;letter-spacing:2px;margin-top:16px}.headline{font-family:"DejaVu Serif",serif;font-size:78px;font-weight:700;line-height:1.16;letter-spacing:-3px;white-space:pre-line;margin:0;min-height:200px;display:flex;align-items:center}.key{font-size:29px;font-weight:700;color:#0A527B;line-height:1.3;min-height:80px;display:flex;align-items:center}.figure{height:620px;flex-shrink:0;background:#FFFFFF;border:2px solid #142D3818;border-radius:22px;box-shadow:0 12px 30px #142D3809;overflow:hidden}.figure svg{width:100%;height:100%;display:block}.rule{border-left:8px solid #2D6842;background:#E5E7DE;padding:24px 27px;border-radius:0 15px 15px 0;min-height:130px;display:flex;flex-direction:column;justify-content:center;gap:12px}.rule-label{font-size:28px;letter-spacing:2px;color:#2D6842;font-weight:700}.rule-text{font-size:30px;line-height:1.4;font-weight:700}.caption-zone{height:238px;position:relative;margin-top:8px;flex-shrink:0}.caption{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.5;font-size:36px;color:#142D38;font-weight:400;padding:5px 8px}.foot{margin-top:auto;display:flex;justify-content:space-between;font-size:28px;color:#2D6842;gap:10px;line-height:1.5}.progress{position:absolute;bottom:55px;left:80px;width:920px;height:5px;background:#142D3815}.progress-fill{height:100%;background:#B83B16;transform-origin:left}.force{transform-box:fill-box;transform-origin:center}.crack{stroke-dasharray:240;stroke-dashoffset:0}.hotspot{transform-origin:center;transform-box:fill-box}'''
parts=['<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><title>VIDEO_TITLE</title><script src="assets/gsap.min.js"></script><style>'+css+'</style></head><body>']
parts[0]=parts[0].replace('VIDEO_TITLE',E(config['title']))
total=round(scenes[-1]['start']+scenes[-1]['duration'],3)
parts+=[f'<div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-start="0" data-duration="{total}">']
anims=[];srt=[];ci=0
for i,s in enumerate(scenes):
 ident=f's{i}';start=s['start'];duration=s['duration']
 caps=''
 for j,seg in enumerate(s['segments']):
  caps+=f'<div id="cap{i}-{j}" class="caption" style="opacity:0"><span>{rich(seg["text"],s.get("highlights",[]))}</span></div>'
  anims += [f'tl.to("#cap{i}-{j}",{{opacity:1,duration:.13}}, {seg["start"]});',f'tl.to("#cap{i}-{j}",{{opacity:0,duration:.13}}, {seg["start"]+seg["duration"]+.12});']
  anims += [f'tl.set("#cap{i}-{j}",{{opacity:0}}, {seg["start"]+seg["duration"]+.25});']
  ci+=1
  def stamp(t):
   ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
  srt.append(f'{ci}\n{stamp(seg["start"])} --> {stamp(seg["start"]+seg["duration"])}\n{seg["text"]}\n')
 foot=config.get('footer','Sơ đồ minh họa · Xem ghi chú nguồn')
 parts += [f'<section class="scene" data-layout-allow-overflow id="{ident}" style="opacity:{1 if i==0 else 0};z-index:{i+1}"><div class="scene-content"><div class="brand"><span>{E(config['brand'])}</span><span>{i+1:02} / {len(scenes):02}</span></div><div class="kicker">{E(s["tag"])}</div><h1 class="headline"><span>{rich(s["title"],s.get("title_em",[]))}</span></h1><div class="key">{E(s["key"])}</div><div class="figure">{svg(s["diagram"],i)}</div><div class="rule"><div class="rule-label">'+('NGUYÊN TẮC ÁP DỤNG' if 1<=i<=10 else 'GHI NHỚ')+f'</div><div class="rule-text">{E(s["rule"])}</div></div><div class="caption-zone">{caps}</div><div class="foot"><span>{foot}</span><span>{i+1:02}</span></div></div></section>']
 if i:
  anims += [f'tl.to("#s{i-1}",{{x:-1080,duration:.45,ease:"power3.inOut"}},{start});',f'tl.set("#s{i-1}",{{opacity:0}},{start+.45});']
  anims += [f'tl.fromTo("#{ident}",{{x:1080,opacity:1}},{{x:0,opacity:1,duration:.45,ease:"power3.inOut",immediateRender:false}},{start});']
 anims += [f'tl.from("#{ident} .brand",{{y:-12,opacity:0,duration:.45,ease:"power2.out"}},{start+.12});',f'tl.from("#{ident} .kicker",{{x:-25,opacity:0,duration:.45,ease:"power3.out"}},{start+.18});',f'tl.from("#{ident} .headline",{{y:35,opacity:0,duration:.65,ease:"power3.out"}},{start+.25});',f'tl.from("#{ident} .key",{{x:25,opacity:0,duration:.6,ease:"sine.out"}},{start+.4});',f'tl.from("#{ident} .figure",{{scale:.96,opacity:0,duration:.65,ease:"power2.out"}},{start+.5});',f'tl.from("#{ident} .rule",{{y:24,opacity:0,duration:.6,ease:"back.out(1.05)"}},{start+1.1});',f'tl.from("#{ident} .foot",{{opacity:0,duration:.5,ease:"sine.out"}},{start+.6});']
 anims +=[f'tl.from("#{ident} .node",{{y:18,opacity:0,stagger:.22,duration:.65,ease:"power3.out"}},{start+1.3});'] if 'class="node"' in svg(s['diagram'],i) else []
 if callable(globals().get('animate')):
  anims += animate(s,ident)
parts +=[f'<div class="progress"><div id="progress" class="progress-fill"></div></div><audio id="voiceover" src="assets/narration.wav" data-start="0" data-duration="{total}" data-track-index="2" data-volume="1"></audio><audio id="music" src="assets/music.wav" data-start="0" data-duration="{total}" data-track-index="3" data-volume="1"></audio></div>']
# progress belongs above all scenes
anims=[a for a in anims if 'tl.from("#s0 .headline"' not in a]
parts += ['<style>.progress{z-index:50}</style><script>window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});'+ '\n'.join(anims)+f'\ntl.from("#progress",{{scaleX:0,duration:{total},ease:"none"}},0);\nwindow.__timelines.main=tl;</script></body></html>']
(P/'index.html').write_text(''.join(parts));(R/'output/phu-de.vi.srt').write_text('\n'.join(srt))
(R/'output/loi-dan.txt').write_text('\n\n'.join(s['tag']+'\n'+' '.join(s['voice']) for s in scenes))
# narration is normalized separately after source generation
print('Built',total,'seconds')
