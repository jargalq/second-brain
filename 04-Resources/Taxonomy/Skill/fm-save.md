---
type: taxonomy
axis: skill
value: fm-save
label: "Vault руу хадгалах"
icon: "💾"
invoke: "fm:save"
agent: wiki
tools:
  - "drive"
inputs:
  - "яриа эсвэл URL"
outputs:
  - "атом"
  - "лавлагаа"
  - "task, лог"
aliases:
  - "fm:save"
date: 2026-10-25
tags: [taxonomy, skill]
ai-first: true
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Юу болохыг тодорхойлсон note; `Ангилал.base` дээр бүгд хүснэгт болно. Өөрт тохирохгүйг нь устгаад, дутууг ижил хэлбэрээр нэм.

# 💾 Vault руу хадгалах

**Тэнхлэг:** `skill:` — нэг agent, нэг сешнд эхнээс нь дуустал хийх нэг чадвар. @mention: `@fm-save`.

## Юу вэ
Яриаг vault руу хадгална: атом, PARA холбоос, task, хүн, лог. Горим: энгийн, checkpoint, URL (лавлагаа болгож, атом гаргаад fact-check хийнэ).

## Хэзээ хэрэглэх
Сэдэв дуусах, ярианы дунд барьж авах, линк хадгалах үед. Task-д `skill: fm-save` гэж бичнэ, эсвэл чатад `@fm-save` гэж дуудна.

## Дуудлага
- Skill: `fm:save`
- Ажиллуулах дүр: `wiki`
- Хэрэгсэл: `drive`
