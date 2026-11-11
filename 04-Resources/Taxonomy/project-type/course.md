---
type: taxonomy
axis: project-type
value: course
label: "Сургалт"
icon: "🎓"
date: 2026-10-26
tags: [taxonomy, project-type]
ai-first: true
key-activity: []

up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 🎓 Сургалт

**Тэнхлэг:** `project-type:` — төсөл ямар төрлийн ажил вэ.

## Юу вэ
Хөтөлбөр, хичээл бэлтгэх, заах, даалгавар хянах төсөл.

## Key Activity
Канвасын activity: канваст тохирох activity алга. Дүгнэлт: шинэ — «Сургалт бэлтгэх, заах» (Revenue: Course).

## Анхдагч самбар
Preset нь `04-Resources/Taxonomy/project-type/course.json` файлд байна. Төсөл үүсэхэд `_dashboard.json` руу хуулагдана (лавлагаа биш, хуулбар).

## Стандарт (stub)
> Суурь: . Гаралтын загвар нь [[04-Resources/Taxonomy/project-type/content|content]]-ийн «Уншвар / хичээл» мөрийг дагана.

| Хэсэг | Одоогийн нотолгоо |
|---|---|
| Гаралт ба загвар | Хичээл = `_lesson-template` (68ch, HTML диаграм); хөтөлбөр PDF (Figma v11 export); нийтлэл `itge-intro.vercel.app/lessons/NN/` |
| Хэрэгсэл | `build_lesson.py`, `export_html.py`, Figma (Spectral + IBM Plex DS), Vercel |
| Шат | ❓ itge.e шийднэ — curriculum Architect-ийн шинэ атомыг хүлээж түр зогссон |
| «Дууссан» шалгуур | ❓ itge.e шийднэ (заагдсан + материал нийтлэгдсэн + даалгавар хянагдсан?) |
| Хориг | самбарын screenshot хичээлд оруулахгүй; artifact болгохгүй |

## Хэзээ хэрэглэх
Frontmatter-т `project-type: course` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

Шийдвэр: 

## 🔗 Хэрэглэсэн газар

```base
filters:
  and:
    - '!file.inFolder("_trash")'
    - or:
        - list(tool).contains(this)
        - list(task-type).contains(this)
        - list(project-type).contains(this)
views:
  - type: table
    name: Хэрэглэсэн газар
    groupBy:
      property: type
      direction: ASC
    order: [file.name, type, status, project]
```
