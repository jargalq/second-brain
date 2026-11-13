---
төрөл: атом
type: atomic
date: 2026-11-12
ai-first: true
төлөв: идэвхтэй
confidence: observed
tags: [атом, AutoCAD, DWG, хэрэгсэл]
projects:
  - "[[Зүүн наран - ашиглалт 2027]]"
aliases: [Open AutoCAD visibly before dxf2dwg]
---
# `dxf2dwg_groups.ps1`-ийн нуугдмал AutoCAD гацаж, унадаг тул AutoCAD-ыг урьдчилан цонхтой нээнэ

- **Баримт (2026-11-12):** скрипт AutoCAD-ыг нуугдмал горимоор асаахад `Documents.Open` дээр гацах эсвэл асмагцаа унах (err 462 «remote server machine does not exist or is unavailable») болсон. 5 минутын хүлээлттэй хуулбар ч тусалсангүй.
- **Арга:** AutoCAD-ыг ердийнхөөр (цонхтой) нээгээд скриптийг ажиллуулна — скрипт нээлттэй AutoCAD-д холбогдож, зөвхөн өөрийн нээсэн баримтыг хаана. Гацсан `acad.exe`, `cscript`-ийг хүчээр хаахгүй; хэрэглэгч Task Manager-ээс хаана.
- **Эх:** Зүүн наран зургийн гаралт, subagent-ийн тайлан 2026-11-12. Шалтгааныг бүрэн тогтоогоогүй (таамаг: нуугдмал горимд эхлэх цонх/лиценз).

Холбоотой: [[zurag-uurhai]] · [[dairga]]
