---
date: 2026-11-13
updated: 2026-11-13
type: atomic
kind: fact
tags: [atomic, fm, obsidian, хэрэгсэл]
confidence: high
sources: ["[[_system/logs/2026-11-13]]"]
role: project
projects: ["[[02-Projects/AI дата төв/AI дата төв]]"]
up: "[[04-Resources/Atomic/knowledge/Atoms]]"
areas: ["[[03-Areas/AI Team/ai-workers/Architect]]"]
supersededby: []
aliases: [fm_project new writes obsidian snippet]
ai-first: true
---

# fm_project.py new нь .obsidian-д CSS snippet бичдэг

## For future agent

`fm_project.py new` төсөл үүсгэхдээ `.obsidian/snippets/fm-project-status.css`-ийг асуулгүй үүсгэдэг. Энэ нь vault-ийн 7-р дүрэмтэй («`.obsidian/` тохиргоог зөвшөөрөлгүй өөрчлөхгүй») зөрчилддөг. 2026-11-12-нд «AI дата төв» төслийг үүсгэхэд илэрсэн.

## Баримт

- Скриптийн тусламжид: «After new/move the Obsidian snippet `<vault>/.obsidian/snippets/fm-project-status.css` is regenerated».
- Өмнө нь энэ vault-д тэр файл байгаагүй. Төсөл үүсгэсний дараа Project agent файлыг устгасан.
- Mugi энэ snippet хэрэгтэй гэвэл дахин үүсгэнэ: `fm_project.py status-css <vault>`.

## Санал

`fm_project.py new`, `move`-д `--no-css` сонголт нэмэх, эсвэл snippet бичихээс өмнө асуух. Энэ нь Architect дүрийн ажил.

**Холбоос:** [[02-Projects/AI дата төв/AI дата төв]] · [[03-Areas/AI Team/ai-workers/Architect]]
