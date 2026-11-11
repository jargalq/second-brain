---
type: atomic
төрөл: атом
төлөв: идэвхтэй
date: 2026-11-05
ai-first: true
confidence: high
tags: [atomic, видео, moviepy, auto-editor, хэрэгсэл]
aliases: [MoviePy Auto-Editor installed on PC, ComfyUI needs GPU]
areas: ["[[03-Areas/Tools/README]]"]
sources: ["https://www.threads.com/share/BAV0-VPU_E"]
---
# Энэ PC дээр MoviePy, Auto-Editor ажилласан; ComfyUI-д NVIDIA GPU хэрэгтэй

## For future agent
Багшийн хуваалцсан AI видео репогийн жагсаалтаас (Threads, 2026-11-05) энэ PC-д юу ажиллахыг Inbox сешн шалгасан.

## Баримт
- **MoviePy 2.1.2** (ffmpeg хамт) суулгаж, дуутай туршилтын видео үүсгэсэн.
- **Auto-Editor 29.3.1** суулгаж, туршилтын видеоны чимээгүй хэсгийг тайрч 12 сек-ийг 8.4 сек болгосон. Хэрэглээ: `auto-editor видео.mp4` → `видео_ALTERED.mp4`.
- Суулгаагүй: **ComfyUI** (NVIDIA GPU 8 ГБ+ хэрэгтэй, энэ PC-д алга), **WhisperX** (ажиллана ч удаан, ~3 ГБ, 8 ГБ RAM-д ачаалал), **Remotion** (Node.js хэрэгтэй).
- Пост «10 репо» гэсэн ч 5 нь л харагдсан; үлдсэн 5 TBD.
- 2026-11-06: Node.js (v26.13.0) энэ PC-д аль хэдийн суусан байсан. **Remotion**-ийн agent skill-ийг (`remotion-dev/skills`, 13 skill) Claude Code-д global суулгав. Remotion-ийн npm багцыг видео төсөл үүсгэх үед суулгана.

**Холбоос:** [[03-Areas/Tools/README]] — хэрэгслийн хүрээ · [[01-GTD/Tasks/Багшаас үлдсэн 5 видео репогийн нэрийг тодру]] — үлдсэн 5-ыг тодруулах task
