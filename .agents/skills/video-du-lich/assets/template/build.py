"""Build a v3-style vlog from measured narration timing and sanitized local media."""
from pathlib import Path, PurePosixPath
import json, html, re, math
R=Path(__file__).resolve().parent;P=R/'composition';O=R/'output';O.mkdir(exist_ok=True)
c=json.loads((R/'project.json').read_text());sc=json.loads((R/'timing.json').read_text());E=html.escape
if not sc:raise SystemExit('Điền timing.json từ lời đọc đã chốt và đo từng WAV trước khi dựng.')
def asset(src):
 p=PurePosixPath(src)
 if p.is_absolute() or '..'in p.parts or not (P/src).is_file():raise ValueError('Cần tài nguyên cục bộ trong composition: '+src)
 return E(src,quote=True)
for f in ['assets/base.mp4','assets/narration.wav','assets/music.wav']:asset(f)
T=round(sc[-1]['start']+sc[-1]['duration'],3);prev=0
for s in sc:
 if s['start']<prev-.002 or s['duration']<=0:raise ValueError('Thời gian cảnh phải tăng và không chồng lấn.')
 prev=s['start']+s['duration'];last=s['start']-.26
 for seg in s['segments']:
  if seg['duration']<=0 or seg['start']<last+.26-.002 or seg['start']+seg['duration']>prev+.002:raise ValueError('Rà thời gian và khoảng nghỉ phụ đề.')
  last=seg['start']+seg['duration']
def rich(t,keys):
 keys=[k for k in sorted(keys,key=len,reverse=True)if k.casefold()in t.casefold()][:2];v=E(t)
 return re.sub('|'.join(re.escape(E(k))for k in keys),lambda m:'<strong>'+m[0]+'</strong>',v,flags=re.I)if keys else v
def stamp(t):
 m=round(t*1000);return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'
css=(R/'theme.css').read_text()
parts=['<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><title>'+E(c['title'])+'</title><script src="assets/gsap.min.js"></script><style>'+css+'</style></head><body>',f'<div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-start="0" data-duration="{T}"><video id="footage" src="assets/base.mp4" data-start="0" data-duration="{T}" data-track-index="0" muted playsinline></video>'];an=[];srt=[];ci=0
for i,s in enumerate(sc):
 start=s['start'];ident=f's{i}';kind=s.get('kind','footage');body=''
 if kind=='photo':
  body=f'<div class="friends-photo"><img src="{asset(s["image"])}"/></div>'
  if s.get('note'):body+='<div class="friends-note">'+E(s['note'])+'</div>'
 elif kind=='procedure':
  steps=''.join('<div'+(' class="active"'if j==s.get('active_step',0)else '')+'>'+E(v)+'</div>'for j,v in enumerate(s.get('steps',[])))
  body='<div class="no-film"><div class="big">'+E(s.get('message',s['title']))+'</div>'+('<div class="small">'+E(s['note'])+'</div>'if s.get('note')else '')+('<div class="steps">'+steps+'</div>'if steps else '')+'</div>'
 elif kind=='signs':
  rows=''.join('<div class="guide-row'+(' good'if g.get('active')else '')+'">'+E(g['label'])+'<br><span>'+E(g.get('explanation',''))+'</span></div>'for g in s['groups'])
  body='<div class="guide"><div class="label">BIỂN CHỈ DẪN TRONG HÀNH TRÌNH</div><div class="sign-image"><img src="'+asset(s['image'])+'"/></div>'+rows+('<div class="route-note">'+E(s['note'])+'</div>'if s.get('note')else '')+'</div>'
 elif kind=='footage':
  if s.get('note'):body='<div class="chip">'+E(s['note'])+'</div>'
 else:raise ValueError('Loại cảnh chưa hỗ trợ: '+kind)
 aux=s.get('auxiliary')
 if aux:
  body+=f'<div class="mini-vjw" id="aux{i}"><div class="mini-site-title">THÔNG TIN PHỤ</div><div class="mini-name">{E(aux["title"])}</div>'
  if aux.get('image'):body+='<img class="mini-site-shot" src="'+asset(aux['image'])+'"/>'
  if aux.get('url'):body+='<div class="mini-url">'+E(aux['url'])+'</div>'
  if aux.get('note'):body+='<div class="mini-copy">'+E(aux['note'])+'</div>'
  body+='</div>';j=aux.get('cue_segment',1)
  if not 0<=j<len(s['segments']):raise ValueError('cue_segment nằm ngoài danh sách lời đọc.')
  an+=[f'tl.fromTo("#aux{i}",{{opacity:0,y:22}},{{opacity:1,y:0,duration:.6,ease:"power3.out",immediateRender:false}},{s["segments"][j]["start"]});']
 caps=''
 for j,seg in enumerate(s['segments']):
  cap=f'cap{i}-{j}';caps+=f'<div class="caption" id="{cap}" style="opacity:0"><span>{rich(seg["text"],s.get("highlights",[]))}</span></div>'
  an+=[f'tl.to("#{cap}",{{opacity:1,duration:.13}},{seg["start"]});',f'tl.to("#{cap}",{{opacity:0,duration:.13}},{seg["start"]+seg["duration"]+.12});',f'tl.set("#{cap}",{{opacity:0}},{seg["start"]+seg["duration"]+.25});']
  ci+=1;srt.append(f'{ci}\n{stamp(seg["start"])} --> {stamp(seg["start"]+seg["duration"])}\n{seg["text"]}\n')
 parts+=[f'<section class="scene {"procedure-with-aux" if kind=="procedure" and aux else ""}" id="{ident}" style="opacity:{1 if i==0 else 0};z-index:{i+1}"><div class="scene-content"><div class="brand"><span>{E(c["brand"])}</span><span>{E(c["route"])}</span></div><div class="head"><div class="tag">{E(s["tag"])}</div><h1 class="headline"><span>{rich(s["title"],s.get("title_em",[]))}</span></h1></div><div class="stage">{body}</div><div class="caption-zone">{caps}</div><div class="footer"><span>{E(c["footer"])}</span><span>{i+1:02} / {len(sc):02}</span></div></div></section>']
 if i:
  parts+=[f'<div class="chapter-wipe" id="wipe{i}"></div>'];an+=[f'tl.fromTo("#wipe{i}",{{x:-1080}},{{x:1080,duration:.44,ease:"power2.inOut",immediateRender:false}},{start-.22});',f'tl.set("#s{i-1}",{{opacity:0}},{start});',f'tl.set("#{ident}",{{opacity:1}},{start});']
 for cls,props,at in [('brand','y:-10,opacity:0,duration:.5,ease:"power2.out"',.15),('head','x:-30,opacity:0,duration:.7,ease:"power3.out"',.25),('stage','y:20,opacity:0,duration:.7,ease:"sine.out"',.5),('footer','opacity:0,duration:.5,ease:"sine.out"',.4)]:
  if i==0 and cls=='head':continue
  an+=[f'tl.from("#{ident} .{cls}",{{{props}}},{start+at});']
 if kind=='signs':an+=[f'tl.from("#{ident} .guide-row",{{x:25,opacity:0,stagger:.3,duration:.6,ease:"power3.out"}},{start+1.4});']
 if kind=='photo':an+=[f'tl.from("#{ident} .friends-photo img",{{scale:.96,opacity:0,duration:1.1,ease:"sine.out"}},{start+.3});']
parts+=[f'<div class="progress"><div id="progress" class="fill"></div></div><audio id="voiceover" src="assets/narration.wav" data-start="0" data-duration="{T}" data-track-index="2" data-volume="1"></audio><audio id="music" src="assets/music.wav" data-start="0" data-duration="{T}" data-track-index="3" data-volume="1"></audio></div>','<script>window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});'+'\n'.join(an)+f'\ntl.from("#progress",{{scaleX:0,duration:{T},ease:"none"}},0);window.__timelines.main=tl;</script></body></html>']
(P/'index.html').write_text(''.join(parts));(O/'phu-de.vi.srt').write_text('\n'.join(srt));(O/'loi-dan.txt').write_text('\n\n'.join(s['tag']+'\n'+' '.join(s.get('voice',[]))for s in sc));print('Built',T,'s;',math.ceil(T*30),'frames; use actual narration/media only for delivery.')
