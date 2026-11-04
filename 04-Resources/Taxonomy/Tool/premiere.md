---
type: taxonomy
axis: tool
value: premiere
label: "Premiere Pro"
icon: "🎞️"
aliases:
  - "Premiere Pro"
bridge: "premiere bridge"
command: "premiere bridge-ийн команд"
path_or_file: "Төслийн .prproj файл"
workflow:
  - "Эх бичлэгийг импортло (файл бүрээр)"
  - "Sequence-ийг байранд нь шинэчил"
  - "MOGRT, Essential Sound-ээр засвар хий"
  - "Экспортыг Output/-д хадгал"
date: 2026-10-25
tags: [taxonomy, tool]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🎞️ Premiere Pro

**Тэнхлэг:** `tool:` — ажил хаана хийгддэг вэ, ямар гүүрээр холбогддог вэ.

## Юу вэ
Premiere Pro — гүүр: premiere bridge. Команд: `premiere bridge-ийн команд`. Байршил: `Төслийн .prproj файл`.

## Хэзээ хэрэглэх
Task эсвэл төслийн ажил Premiere Pro-д хийгдэх бол `tool: premiere` гэж бичнэ.

## Урсгал
1. Эх бичлэгийг импортло (файл бүрээр)
2. Sequence-ийг байранд нь шинэчил
3. MOGRT, Essential Sound-ээр засвар хий
4. Экспортыг Output/-д хадгал

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
