---
type: taxonomy
axis: project-type
value: coaching
label: "Хувийн коучинг"
icon: "🤝"
date: 2026-10-26
tags: [taxonomy, project-type]
ai-first: true
key-activity: []

up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Taxonomy/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 🤝 Хувийн коучинг

**Тэнхлэг:** `project-type:` — төсөл ямар төрлийн ажил вэ.

## Юу вэ
Нэг хүнтэй тогтмол уулзалт, PR review, case study.

## Key Activity
Канвасын activity: канваст тохирох activity алга. Дүгнэлт: шинэ — «Сургалт бэлтгэх, заах»-д багтана (Customer Relationships: 1:1).

## Анхдагч самбар
Preset нь `04-Resources/Taxonomy/project-type/coaching.json` файлд байна. Төсөл үүсэхэд `_dashboard.json` руу хуулагдана (лавлагаа биш, хуулбар).

## Стандарт (stub)
> Суурь: .

| Хэсэг | Одоогийн нотолгоо |
|---|---|
| Гаралт ба загвар | Уулзалт бүр task/Event; RACI pipeline ((дотоод жишээ)); newsletter гаралт content стандартаар |
| Хэрэгсэл | Цаглабар, `waiting_on` |
| Шат | ❓ itge.e шийднэ — сессийн тэмдэглэлийн загвар алга |
| «Дууссан» шалгуур | ❓ itge.e шийднэ |
| Хориг | хувийн мэдээллийг нийтийн гаралтад оруулахгүй |

## Хэзээ хэрэглэх
Frontmatter-т `project-type: coaching` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

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
