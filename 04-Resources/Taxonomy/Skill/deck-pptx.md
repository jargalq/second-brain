---
type: taxonomy
axis: skill
value: deck-pptx
label: "PowerPoint слайд"
icon: "📊"
invoke: "anthropic-skills:pptx"
agent: creative
tools:
  - "drive"
  - "codebase"
inputs:
  - "brief, агуулга"
  - "загвар (заавал биш)"
outputs:
  - "Output/*.pptx"
aliases:
  - "anthropic-skills:pptx"
date: 2026-10-26
tags: [taxonomy, skill]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 📊 PowerPoint слайд

**Тэнхлэг:** `skill:` — нэг agent, нэг сешнд эхнээс нь дуустал хийх нэг чадвар. @mention: `@deck-pptx`.

## Юу вэ
PowerPoint (.pptx) слайд үүсгэх, засах: бүтэц, загвар, зураг, тэмдэглэл.

## Хэзээ хэрэглэх
Танилцуулга, pitch deck, хичээлийн слайд хэрэгтэй үед. Task-д `skill: deck-pptx` гэж бичнэ, эсвэл чатад `@deck-pptx` гэж дуудна.

## Дуудлага
- Skill: `anthropic-skills:pptx`
- Ажиллуулах дүр: `creative`
- Хэрэгсэл: `drive`, `codebase`
