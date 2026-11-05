# Workflow and portable starter

## Inspect and script
Check the user-provided order, real shot timestamps/orientation and what each clip actually shows. Make a short edit plan and script: footage → voice → emphasized words → optional supporting card. Keep the purpose central. If script approval is still required, finish the concrete script and independent asset inspection before waiting. Approved script or “do it directly” means proceed without redundant approval.

## Starter

```sh
python <skill-directory>/scripts/scaffold.py /path/to/new-project
```

The new directory must be absent or empty. No personal footage/photos/voice are bundled. Populate project.json and scenes.json; create composition/assets/base.mp4, narration.wav and music.wav. Base is the sanitized edited footage with correct order/timing and no original audio, plus neutral backgrounds where filming is missing. Match its frame count to the final timeline. Do not render placeholder material as a completed vlog.

Build expects timing.json, an array of scenes from the approved script with actual measured audio timing:

```json
[
  {
    "kind": "footage",
    "tag": "CHẶNG KHỞI HÀNH",
    "title": "Bắt đầu hành trình.",
    "title_em": ["hành trình"],
    "highlights": ["khởi hành"],
    "voice": ["Lời dẫn tiếng Việt đã chốt."],
    "start": 0,
    "duration": 6,
    "segments": [{"start": 0.65, "duration": 4.5, "text": "Lời dẫn tiếng Việt đã chốt."}]
  }
]
```

This is schema illustration, not ready-to-deliver audio timing. Measure each generated WAV; use absolute segment times and at least0.26s between captions. Recalculate downstream timing after narration changes. Use short captions and natural wrapping; names may be written phonetically for TTS but standard spelling in captions.

Optional scene types, adapting to actual content:
- `footage`: optional `note` chip.
- `photo`: `image` path relative to composition plus optional `note`.
- `procedure`: `steps` array, zero-based `active_step`; optional `message` and `note`. Never imply all procedural scenes prohibit filming; state “không ghi hình” only when confirmed.
- `signs`: actual `image` and `groups` array `{label, explanation, active}`. Keep compounds from the real sign together. Do not copy the old fixed Arrivals highlight rectangle onto a different photo.
- `auxiliary`: optional object on any scene, with `title`, `image`, `url`, `note`, `cue_segment` (default1). It uses a small lower-right card only from that narration segment. Omit unneeded fields. Check its placement against the footage/procedure card and captions.

Font and GSAP paths are local. CSS is the v3 reference, meant to be adapted to the new scene’s text length without changing the identity. build.py escapes content instead of treating user-provided text as HTML.

## Audio, render and delivery
Prefer existing available Vietnamese TTS; no invented API keys or model paths. Keep music lower than speech. For requested trend music, verify the actual source/availability or report the blocker; a voice-only version allows later in-app audio selection. Do not promise virality.

Use the installed HyperFrames CLI’s actual supported commands. Typical:

```sh
python build.py
npx hyperframes check composition --samples 12
npx hyperframes snapshot composition --at <hero-times> --output output/frames --no-end
npx hyperframes render composition --output output/vlog.mp4 --fps 30 --quality high
```

Review overflow, contrast, grouped sign labels, privacy masks, local times and end photo. FFprobe/FFmpeg must confirm1080×1920,30fps,H.264/AAC, expected frames, full decode and audio levels. Aim roughly−16 to−13LUFS with true peak below about−1dBTP; prioritize clear speech. Never claim manual listening when only measurements were performed.

Deliver MP4, phu-de.vi.srt, loi-dan.txt, CAPTION-TIKTOK.txt, cover, source notes, honest check report and a portable source ZIP with sanitized derivatives. In Bien, preserve old versions and publish only to the user-selected repo. Check Git changes and remote state; verify copied-file hashes, ZIP CRC and push success. Installation in this environment does not imply availability in every device/account/session; the ZIP is portable to supported skill directories.
