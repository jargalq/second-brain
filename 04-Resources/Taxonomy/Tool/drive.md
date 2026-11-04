---
type: taxonomy
axis: tool
value: drive
label: "Google Drive"
icon: "🗂️"
aliases:
  - "Google Drive"
bridge: "Google Drive mirror (Drive for desktop)"
command: "файлын систем (Mirror files)"
path_or_file: "Vault-ийн хавтас (Drive-д тусгагдсан)"
workflow:
  - "Нэг удаад нэг машин дээр бич"
  - "(1) давхар файл гарвал нэгтгэ"
  - "Сэргээх бол Drive-ийн version history"
date: 2026-10-25
tags: [taxonomy, tool]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🗂️ Google Drive

**Тэнхлэг:** `tool:` — ажил хаана хийгддэг вэ, ямар гүүрээр холбогддог вэ.

## Юу вэ
Google Drive — гүүр: Google Drive mirror (Drive for desktop). Команд: `файлын систем (Mirror files)`. Байршил: `Vault-ийн хавтас (Drive-д тусгагдсан)`.

## Хэзээ хэрэглэх
Task эсвэл төслийн ажил Google Drive-д хийгдэх бол `tool: drive` гэж бичнэ.

## Урсгал
1. Нэг удаад нэг машин дээр бич
2. (1) давхар файл гарвал нэгтгэ
3. Сэргээх бол Drive-ийн version history

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
