---
type: taxonomy
axis: task-type
value: lesson
label: "Хичээл"
icon: "🎓"
date: 2026-10-26
tags: [taxonomy, task-type]
ai-first: true
key-activity: []

up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Taxonomy/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 🎓 Хичээл

**Тэнхлэг:** `task-type:` — task ямар хийцийн ажил вэ.

## Юу вэ
Хичээл, хөтөлбөр, тайлбар материал бэлтгэх, заах.

## Key Activity
Канвасын activity: канваст тохирох activity алга. Дүгнэлт: шинэ — «Сургалт бэлтгэх, заах».

## Хэзээ хэрэглэх
Frontmatter-т `task-type: lesson` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

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
