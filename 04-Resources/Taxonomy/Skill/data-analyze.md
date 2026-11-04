---
type: taxonomy
axis: skill
value: data-analyze
label: "Өгөгдлийн шинжилгээ"
icon: "🔎"
invoke: "data:analyze"
agent: project
tools:
  - "drive"
  - "codebase"
inputs:
  - "өгөгдөл (csv, хүснэгт, асуулга)"
  - "асуулт"
outputs:
  - "дүгнэлт, тоон үр дүн"
  - "Output/*.xlsx"
aliases:
  - "data:analyze"
date: 2026-10-26
tags: [taxonomy, skill]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🔎 Өгөгдлийн шинжилгээ

**Тэнхлэг:** `skill:` — нэг agent, нэг сешнд эхнээс нь дуустал хийх нэг чадвар. @mention: `@data-analyze`.

## Юу вэ
Өгөгдлийг асуулгаас статистик, дүрслэл хүртэл шинжилж, дүгнэлт гаргана.

## Хэзээ хэрэглэх
Тоон өгөгдлөөс асуултад хариулах, хэв маяг олох үед. Task-д `skill: data-analyze` гэж бичнэ, эсвэл чатад `@data-analyze` гэж дуудна.

## Дуудлага
- Skill: `data:analyze`
- Ажиллуулах дүр: `project`
- Хэрэгсэл: `drive`, `codebase`
