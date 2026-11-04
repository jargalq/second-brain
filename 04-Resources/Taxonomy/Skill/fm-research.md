---
type: taxonomy
axis: skill
value: fm-research
label: "Судалгааны урсгал"
icon: "🔬"
invoke: "fm:research"
agent: research
tools:
  - "drive"
inputs:
  - "асуулт"
  - "spec"
outputs:
  - "тайлан"
  - "эх сурвалжийн жагсаалт"
aliases:
  - "fm:research"
date: 2026-10-25
tags: [taxonomy, skill]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 🔬 Судалгааны урсгал

**Тэнхлэг:** `skill:` — нэг agent, нэг сешнд эхнээс нь дуустал хийх нэг чадвар. @mention: `@fm-research`.

## Юу вэ
Асуултыг товч, сэдэв, мөчлөг гэж ангилж, судалгааны skill-үүдийг дараалуулж, шинэ subagent-аар fact-check хийж тайлан гаргана.

## Хэзээ хэрэглэх
Судалгаа, мөчлөгийн тайлан хийх үед. Task-д `skill: fm-research` гэж бичнэ, эсвэл чатад `@fm-research` гэж дуудна.

## Дуудлага
- Skill: `fm:research`
- Ажиллуулах дүр: `research`
- Хэрэгсэл: `drive`
