---
date: 2026-11-05
type: task
tags:
  - task
ai-first: true
# status: inbox | next-action | in-progress | waiting | someday | completed | cancelled
status: inbox
context: work
owner: "💼 Project"
project: "[[02-Projects/Цэгц/Сур - арьс ширний бүртгэлийн програм]]"
step:          # төслийн step (_BRAIN.md «Step ба milestone»), жишээ "S2 · Дизайн ба прототип"
projects: []      # олон төсөл: бүх холбогдох төсөл (project: = гол нь)
# RACI (2026-10-14): responsible = хийх дүр (анхдагч owner) · accountable = ганц эцсийн хариуцагч (анхдагч owner)
# consulted = дуусгахаас өмнө асуух дүр/төсөл · informed = мэдээлэх дүр/төсөл (projects-ийн бусад төсөл автоматаар)
responsible: architect
accountable: project
consulted: []
informed: ["me"]
device:           # PC | Mac — зөвхөн тэр машин claim хийнэ (хоосон = аль нь ч)
activity:   # Key Activity (шат): [[03-Areas/Business/activities/<Activity>]]
task-type:  # хийц: build | research | design | lesson | content | decision | document | meeting — [[04-Resources/Taxonomy/Ангилал]]
job:
requested_by:
resources:
up: "[[01-GTD/Tasks/Tasks]]"
next_action:   # дараагийн ганц алхам (Next action хэсгийн товч)
outputs: []    # гаралтын эх сурвалж: [[Output/...]] эсвэл код зам
due: 
# started / completed: YYYY-MM-DD HH:MM (эхлэх / дуусах үед) · claimed: PC | Mac (auto-claim бичнэ)
started:
completed:
claimed:
priority: medium
aliases:
  - "Сур: GitHub-д private репо үүсгэж push хийх"
delegated_from: architect
delegated: 2026-11-06
---

# Сур: GitHub-д private репо үүсгэж push хийх

## For future agent

Нэг ажлын урсгал = энэ task. Эх сурвалж хоёр давхарга: (1) энэ md — яагаад, юу (шаардлага эх үгээр, шийдвэр, RACI, next action, түүх, дүгнэлт); (2) «Гаралт»-д заасан бүтээл — хэрхэн (прототип, код, баримт). Figma, апп зэрэг нь гаралтаас үүсмэл. Ажил эхлэхээсээ өмнө энэ md-г бүтэн унш; хэрэглэгчийн шинэ үгийг «Шаардлага»-д эх үгээр нэм, хасахгүй.

## Шаардлага (эх үгээр)

<!-- Mugi / хүсэгчийн үг товчлолгүй, огноотой: - YYYY-MM-DD «...» -->


## Шийдэх асуудал / яагаад

<!-- нэг догол: энэ ажил ямар асуудлыг шийдэх вэ, хэнд, яагаад одоо — маягт биш -->

## Амжилтын шалгуур

<!-- «сайн үр дүн» гэж юу вэ — шалгаж болохуйц 2–4 мөр -->

## Буруу чиглэл

<!-- юу хийвэл зорилгоос зөрөх вэ (жишээ: хэлбэрийг дагаад утгыг алдах) -->

## Next action

<!-- дараагийн ганц алхам · хэн (RACI) — мэдэгдэл ирэхэд шинэчил -->

## Гаралт

<!-- эх сурвалж бүтээл: [[Output/...]] эсвэл код зам · үүсмэл: Figma section, апп хуудас -->

## Үр дүн

<!-- хүргэсэн зүйл + нотолгоо (commit, файл, шийдвэр) — fm:task done энд бичнэ -->

## Дүгнэлт

<!-- milestone / дуусахад: юу сурсан, дараагийн загварт юу оруулах (Дүгнэх ↺) · шийдвэр/атом: [[04-Resources/Atomic/decisions/...]] -->

## Өөрчлөлтийн түүх

| Цаг | Юу | Хаана |
|---|---|---|


## Шаардлага

Код D:\PARA\1-Projects\Цэгц\sur-д commit хийгдсэн (сүүлийнх 428e3ed), remote алга, энэ PC-д gh нэвтрээгүй. Хүлээж буй зүйл: Mugi өөрөө терминалд gh auth login хийнэ. Дараа нь agent private репо үүсгэж push хийнэ; Vercel тэр репогоос байршуулна. Mugi 2026-11-05: «repo odoo update hiichih uu».

## Өмнөх

Энэ task юуны үргэлжлэл вэ (автоматаар санал болгов: хамаарахгүйг хас, дутууг нэм):
- [[01-GTD/Tasks/Сур- Цэгц Facebook page нээх]] · next-action · 2026-11-05

## Шилжүүлэлт
- 2026-11-06 🏛️ Architect → 💼 Project: «Сур» төслийн байршуулалтын алхам тул төслийн сешн хийнэ; хүлээж буй зүйл: Mugi `gh auth login` хийсний дараа private репо үүсгэж `D:\PARA\1-Projects\Цэгц\sur`-ийг push хийх (Vercel үүнээс хамаарна).

## Явц
- 2026-11-05 23:59 📌 үүсгэв
