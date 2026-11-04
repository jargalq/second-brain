---
type: taxonomy
axis: tool
value: github
label: "GitHub"
icon: "🐙"
aliases:
  - "GitHub"
bridge: "gh CLI"
command: "gh <команд>"
path_or_file: "github.com дээрх repo"
workflow:
  - "Branch үүсгэ"
  - "Commit хий"
  - "gh pr create-ээр PR нээ"
  - "Review-ийн дараа merge хий"
date: 2026-10-25
tags: [taxonomy, tool]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🐙 GitHub

**Тэнхлэг:** `tool:` — ажил хаана хийгддэг вэ, ямар гүүрээр холбогддог вэ.

## Юу вэ
GitHub — гүүр: gh CLI. Команд: `gh <команд>`. Байршил: `github.com дээрх repo`.

## Хэзээ хэрэглэх
Task эсвэл төслийн ажил GitHub-д хийгдэх бол `tool: github` гэж бичнэ.

## Урсгал
1. Branch үүсгэ
2. Commit хий
3. gh pr create-ээр PR нээ
4. Review-ийн дараа merge хий

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
