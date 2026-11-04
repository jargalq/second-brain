---
type: taxonomy
axis: tool
value: codebase
label: "Codebase"
icon: "💻"
aliases:
  - "Codebase"
bridge: "локал repo + Claude Code"
command: "git, python, pnpm"
path_or_file: "D:/CodeBase/goomnet"
workflow:
  - "Task-аа vault-д claim хий"
  - "Repo-д тест бичиж кодоо өөрчил"
  - "Тест ажиллуул"
  - "Commit хийж task-д тэмдэглэ"
date: 2026-10-25
tags: [taxonomy, tool]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 💻 Codebase

**Тэнхлэг:** `tool:` — ажил хаана хийгддэг вэ, ямар гүүрээр холбогддог вэ.

## Юу вэ
Codebase — гүүр: локал repo + Claude Code. Команд: `git, python, pnpm`. Байршил: `D:/CodeBase/goomnet`.

## Хэзээ хэрэглэх
Task эсвэл төслийн ажил Codebase-д хийгдэх бол `tool: codebase` гэж бичнэ.

## Урсгал
1. Task-аа vault-д claim хий
2. Repo-д тест бичиж кодоо өөрчил
3. Тест ажиллуул
4. Commit хийж task-д тэмдэглэ

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
