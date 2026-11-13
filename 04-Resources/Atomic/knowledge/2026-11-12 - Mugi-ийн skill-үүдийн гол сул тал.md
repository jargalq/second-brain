---
type: atomic
төрөл: атом
төлөв: идэвхтэй
date: 2026-11-12
confidence: tested
tags: [atomic, skill, аудит, зураг, уул-уурхай]
aliases: [Main weaknesses of Mugi's skills]
ai-first: true
resources:
  - "[[04-Resources/Research/Skill-ийн аудит 2026-11-12]] — бүтэн тайлан, 10 санал"
related:
  - "[[2026-11-12 - mine-planning skill андезитийн уурхайд тохирохгүй]] — туршилтын нотолгоо"
  - "[[_system/skills/zurag-uurhai/SKILL|zurag-uurhai]] — хамгийн их засвар хэрэгтэй skill"
---
# Mugi-ийн skill-үүдийн гол сул тал: буруу зам, хоорондоо зөрсөн дүрэм, тестгүй давхардсан скрипт

## For future agent
2026-11-12-нд 9 skill-ийг шалгав. Гол олдвор:
- **Буруу зам.** `tezu`, `obsidian-tezu-vault`, `zurag-shtamp` гурав vault-ийг `D:\Seond brain` гэж заадаг. Ийм хавтас байхгүй тул `zurag-shtamp`-ийн импорт бүтэлгүйтнэ.
- **`geo-section-plan`-ийн алдаа.** Азимут хоосон байхад цооногийн координат NaN болно. Python-оор туршиж батлав.
- **`mine-planning` агуулгагүй ордод тохирохгүй.** Андезит, дайрганд хэрэглэхгүй.
- **Зөрчилтэй дүрэм.** `zurag-uurhai` §1 ба §5 (`hRock` хээ), `dairga` §4 ба `zurag-uurhai` §5 (ахилтын өнгө), `dairga` болон agent-ийн гаралтын зам хоорондоо зөрнө.
- **Давхардсан скрипт.** `zn_*`/`bn_*` скриптүүд хуулбараар олширч, тест огт алга.

Skill засахын өмнө тайланг уншина. Засварыг Mugi зөвшөөрсний дараа л хийнэ.
