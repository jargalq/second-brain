---
төрөл: шийдвэр
type: session-decision
ai-first: true
төлөв: идэвхтэй
огноо: 2026-11-06
date: 2026-11-06
хэн: Mugi
буцааж-болох: тийм (_trash-аас буцааж зөөнө)
areas: ["[[03-Areas/AI Team/ai-workers/GTD]]"]
tags: [шийдвэр, vault, base, fm]
aliases: [Duplicate bases moved to trash]
---
# Дэд хавтсан дахь давхар base-ийг trash руу зөөв

## For future agent

fm 0.10.9-ийн upgrade шалгалтаар (`/fm:setup` upgrade) олдсон бүтцийн 4 зөрүүг зассан шийдвэр. Base-ууд PARA-ийн дээд хавтсанд шууд байх дүрмийн дагуу.

- **Хэн:** Mugi ("Тийм, зас"), Claude шалгаж гүйцэтгэв.
- **Шийдвэр:**
  - `03-Areas/Docs/Docs.base`, `03-Areas/Products/Products.base`, `04-Resources/Taxonomy/Ангилал.base` нь дээд хавтсан дахь хуулбартайгаа hash-аар яг ижил байсан тул `_trash/bases-2026-11-06-dup/` руу зөөв.
  - `04-Resources/library/repos/Багаж ба skill.base`-ийг `04-Resources/` руу `fm_migrate --apply`-аар зөөж, 2 холбоосыг засав.
- **Яагаад:** Base байршлын дүрэм (2026-10-09): бүх `.base` PARA-ийн дээд хавтсанд, дэд хавтсанд хэзээ ч биш. Давхар хуулбар зөрөх эрсдэлтэй.
- **Хөндөөгүй:** `_system/skills/Skills.base` (байршил тодорхойгүй), `00-Soul/SOUL - ноорог (D-PROJECT).md` (SOUL-ийг Mugi өөрөө удирдана).
- **Үлдсэн:** 48 base аль нэг дүрд оноогдоогүй, 77 шийдвэрийн атом төсөлгүй — мэдээллийн чанартай.
- **Буцааж болох эсэх:** Болно, `_trash/bases-2026-11-06-dup/`-аас буцааж зөөнө.

Холбоос: [[2026-11-04 - Way Academy fm plugin суулгах]] — өмнөх migrate-ийн үргэлжлэл · [[01-GTD/Daily/2026-11-06]]
