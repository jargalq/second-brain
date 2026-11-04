---
type: taxonomy
axis: skill
value: sheet-xlsx
label: "Excel хүснэгт"
icon: "📈"
invoke: "anthropic-skills:xlsx"
agent: project
tools:
  - "drive"
  - "codebase"
inputs:
  - "өгөгдөл (csv, хүснэгт)"
  - "тооцооны дүрэм"
outputs:
  - "Output/*.xlsx"
aliases:
  - "anthropic-skills:xlsx"
date: 2026-10-26
tags: [taxonomy, skill]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 📈 Excel хүснэгт

**Тэнхлэг:** `skill:` — нэг agent, нэг сешнд эхнээс нь дуустал хийх нэг чадвар. @mention: `@sheet-xlsx`.

## Юу вэ
Excel (.xlsx) хүснэгт үүсгэх, засах: томьёо, тооцоо, форматлалт, график, өгөгдөл цэвэрлэх.

## Хэзээ хэрэглэх
Тооцоо, төсөв, жагсаалт, хүснэгтэн тайлан хэрэгтэй үед. Task-д `skill: sheet-xlsx` гэж бичнэ, эсвэл чатад `@sheet-xlsx` гэж дуудна.

## Дуудлага
- Skill: `anthropic-skills:xlsx`
- Ажиллуулах дүр: `project`
- Хэрэгсэл: `drive`, `codebase`
