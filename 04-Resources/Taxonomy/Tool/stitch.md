---
type: taxonomy
axis: tool
value: stitch
label: "Stitch"
icon: "🧵"
aliases:
  - "Stitch"
bridge: "Google Stitch (вэб)"
command: "https://stitch.withgoogle.com/"
path_or_file: "Stitch төсөл"
workflow:
  - "Brief-ээ бэлд"
  - "Stitch-д UI ноорог үүсгэ"
  - "Шилдгийг Figma руу шилжүүл"
date: 2026-10-25
tags: [taxonomy, tool]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🧵 Stitch

**Тэнхлэг:** `tool:` — ажил хаана хийгддэг вэ, ямар гүүрээр холбогддог вэ.

## Юу вэ
Stitch — гүүр: Google Stitch (вэб). Команд: `https://stitch.withgoogle.com/`. Байршил: `Stitch төсөл`.

## Хэзээ хэрэглэх
Task эсвэл төслийн ажил Stitch-д хийгдэх бол `tool: stitch` гэж бичнэ.

## Урсгал
1. Brief-ээ бэлд
2. Stitch-д UI ноорог үүсгэ
3. Шилдгийг Figma руу шилжүүл

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
