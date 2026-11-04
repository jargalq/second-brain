---
type: taxonomy
axis: skill
value: doc-docx
label: "Word баримт"
icon: "📄"
invoke: "anthropic-skills:docx"
agent: project
tools:
  - "drive"
  - "codebase"
inputs:
  - "агуулга, бүтэц"
  - "загвар (заавал биш)"
outputs:
  - "Output/*.docx"
aliases:
  - "anthropic-skills:docx"
date: 2026-10-26
tags: [taxonomy, skill]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 📄 Word баримт

**Тэнхлэг:** `skill:` — нэг agent, нэг сешнд эхнээс нь дуустал хийх нэг чадвар. @mention: `@doc-docx`.

## Юу вэ
Word (.docx) баримтыг үүсгэх, засах, форматлах: гарчиг, хүснэгт, зураг, хуудасны загвар.

## Хэзээ хэрэглэх
Тайлан, гэрээ, санал, захидал Word форматаар хэрэгтэй үед. Task-д `skill: doc-docx` гэж бичнэ, эсвэл чатад `@doc-docx` гэж дуудна.

## Дуудлага
- Skill: `anthropic-skills:docx`
- Ажиллуулах дүр: `project`
- Хэрэгсэл: `drive`, `codebase`
