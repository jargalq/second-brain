---
type: taxonomy
axis: skill
value: pdf
label: "PDF"
icon: "📕"
invoke: "anthropic-skills:pdf"
agent: project
tools:
  - "drive"
  - "codebase"
inputs:
  - "PDF файл эсвэл агуулга"
outputs:
  - "Output/*.pdf"
  - "задалсан текст, хүснэгт"
aliases:
  - "anthropic-skills:pdf"
date: 2026-10-26
tags: [taxonomy, skill]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 📕 PDF

**Тэнхлэг:** `skill:` — нэг agent, нэг сешнд эхнээс нь дуустал хийх нэг чадвар. @mention: `@pdf`.

## Юу вэ
PDF унших, текст ба хүснэгт задлах, нэгтгэх, хуваах, форм бөглөх, шинээр үүсгэх.

## Хэзээ хэрэглэх
PDF-тэй ажиллах бүрт. Task-д `skill: pdf` гэж бичнэ, эсвэл чатад `@pdf` гэж дуудна.

## Дуудлага
- Skill: `anthropic-skills:pdf`
- Ажиллуулах дүр: `project`
- Хэрэгсэл: `drive`, `codebase`
