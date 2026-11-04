---
type: taxonomy
axis: project-type
value: investment
label: "Хөрөнгө оруулалт, IR"
icon: "💼"
date: 2026-10-26
tags: [taxonomy, project-type]
ai-first: true
key-activity: []

up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Taxonomy/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 💼 Хөрөнгө оруулалт, IR

**Тэнхлэг:** `project-type:` — төсөл ямар төрлийн ажил вэ.

## Юу вэ
Хөрөнгө татах, оруулах: тооцоо, deck, cap table, хэлэлцээр.

## Key Activity
Канвасын activity: канваст тохирох activity алга. Дүгнэлт: шинэ — «Хөрөнгө оруулалт татах, IR бэлтгэх» (канваст алга).

## Анхдагч самбар
Preset нь `04-Resources/Taxonomy/project-type/investment.json` файлд байна. Төсөл үүсэхэд `_dashboard.json` руу хуулагдана (лавлагаа биш, хуулбар).

## Стандарт (stub)
> Суурь: .

| Хэсэг | Одоогийн нотолгоо |
|---|---|
| Гаралт ба загвар | Тооцоо = vault-ийн CSV, хүснэгт, Excel биш (); зардлын ангилал () |
| Хэрэгсэл | `Data/*.csv`, Finance дүр |
| Шат | ❓ itge.e шийднэ |
| «Дууссан» шалгуур | ❓ itge.e шийднэ |
| Хориг | `03-Areas/Business/finances/private/`-ийг иш татахгүй; хөрөнгө оруулалтын зөвлөгөө өгөхгүй |

## Хэзээ хэрэглэх
Frontmatter-т `project-type: investment` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

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
