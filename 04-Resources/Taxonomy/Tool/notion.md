---
type: taxonomy
axis: tool
value: notion
label: "Notion"
icon: "🗒️"
aliases:
  - "Notion"
bridge: "Notion API (fm:notion)"
command: "fm:notion skill"
path_or_file: "Notion workspace-ийн database"
workflow:
  - "Vault-аас эх өгөгдлөө ав"
  - "Notion API-аар бичлэг үүсгэ, шинэчил"
  - "Холбоосыг vault-ийн note-д буцааж бич"
date: 2026-10-25
tags: [taxonomy, tool]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🗒️ Notion

**Тэнхлэг:** `tool:` — ажил хаана хийгддэг вэ, ямар гүүрээр холбогддог вэ.

## Юу вэ
Notion — гүүр: Notion API (fm:notion). Команд: `fm:notion skill`. Байршил: `Notion workspace-ийн database`.

## Хэзээ хэрэглэх
Task эсвэл төслийн ажил Notion-д хийгдэх бол `tool: notion` гэж бичнэ.

## Урсгал
1. Vault-аас эх өгөгдлөө ав
2. Notion API-аар бичлэг үүсгэ, шинэчил
3. Холбоосыг vault-ийн note-д буцааж бич

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
