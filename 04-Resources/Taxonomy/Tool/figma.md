---
type: taxonomy
axis: tool
value: figma
label: "Figma"
icon: "🎨"
aliases:
  - "Figma"
bridge: "fig.py bridge (Figma desktop dev plugin)"
command: "python fig.py <команд>"
path_or_file: "Season 2, Inai Website, Journal-ийн Figma файлууд"
workflow:
  - "Төслийн design system-ийг унш"
  - "Холбогдох section дотор, өмнөх хувилбарын баруун талд frame үүсгэ"
  - "fig.py-ээр зур, contrast шалга"
  - "Export хийж төслийн Output/-д хадгал"
date: 2026-10-25
tags: [taxonomy, tool]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🎨 Figma

**Тэнхлэг:** `tool:` — ажил хаана хийгддэг вэ, ямар гүүрээр холбогддог вэ.

## Юу вэ
Figma — гүүр: fig.py bridge (Figma desktop dev plugin). Команд: `python fig.py <команд>`. Байршил: `Season 2, Inai Website, Journal-ийн Figma файлууд`.

## Хэзээ хэрэглэх
Task эсвэл төслийн ажил Figma-д хийгдэх бол `tool: figma` гэж бичнэ.

## Урсгал
1. Төслийн design system-ийг унш
2. Холбогдох section дотор, өмнөх хувилбарын баруун талд frame үүсгэ
3. fig.py-ээр зур, contrast шалга
4. Export хийж төслийн Output/-д хадгал

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
