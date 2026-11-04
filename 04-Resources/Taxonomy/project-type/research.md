---
type: taxonomy
axis: project-type
value: research
label: "Судалгаа"
icon: "🔍"
date: 2026-10-26
tags: [taxonomy, project-type]
ai-first: true
key-activity: []
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Taxonomy/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 🔍 Судалгаа

**Тэнхлэг:** `project-type:` — төсөл ямар төрлийн ажил вэ.

## Юу вэ
Хууль, татвар, зах зээл, бизнес моделийн судалгаа; гаралт нь тайлан, атом.

## Key Activity
Канвасын activity: өөрийн Key Activity. Дүгнэлт: таарна — судалгаа (Revenue: Consulting).

## Анхдагч самбар
Preset нь `04-Resources/Taxonomy/project-type/research.json` файлд байна. Төсөл үүсэхэд `_dashboard.json` руу хуулагдана (лавлагаа биш, хуулбар).

## Стандарт (stub)
> Суурь: .

| Хэсэг | Одоогийн нотолгоо |
|---|---|
| Гаралт ба загвар | Хавтас: эх `Inbox/`, гаралт `Output/`; лавлагаа бүр «## Дүгнэлт» + `atoms:` (); дата CSV |
| Хэрэгсэл | `fm:research`, `fm:save`, `fm:watch`, deep-research, last30days |
| Шат | vault → вэб → тайлан (Research) → атом, glossary (Wiki); мөчлөг дүгнэлтээр хаагдана |
| «Дууссан» шалгуур | эх сурвалж бүр огноо + confidence, зөрчил тэмдэглэгдсэн; ❓ itge.e шийднэ — нэмэлт шалгуур |
| Хориг | байгааг дахин татахгүй; хэмжилтээр дүгнэлт зарлахгүй, асуулт тавина |
| Эх сурвалж |  |

## Хэзээ хэрэглэх
Frontmatter-т `project-type: research` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

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
