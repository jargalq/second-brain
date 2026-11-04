---
төрөл: шийдвэр
type: session-decision
date: 2026-11-04
ai-first: true
төлөв: идэвхтэй
tags: [шийдвэр, second-brain, way-academy, plugin]
topics: ["[[Second Brain Season 2 - Way Academy]]"]
aliases: [Install Way Academy fm plugin]
---
# Way Academy-ийн fm plugin, template-ийг vault-д суулгах

- **Хэн:** Mugi (2026-11-04) «Бүгдийг» сонгосон. Claude репог хянаж, суулгав.
- **Шийдвэр:**
  - `rollingbd/way-academy-season-2` репог marketplace (`second-brain-season-2`) болгон нэмж, `fm` plugin (v0.10.3) суулгав (user scope). `/fm:*` командууд, SessionStart (BOOT.md), PostToolUse (lint, changelog) hook, app-ийн task band.
  - Vault-ийг `~/.fmos/config.json`-д бүртгэв (vault `D:\Seond brain`, эзэн Mugi, PC).
  - `template/vault`-аас vault-д **байхгүй** 110 файлыг нэмэв: 2 skill (`odroo-haah`, `link-hadgalah`), `04-Resources/Taxonomy/` ангиллууд, base-ууд, `Жишээ ...` note-ууд, `_system/fm/registry.json`. Байгаа файл, `CLAUDE.md`, `00-Soul/`, `.obsidian/`-д хүрээгүй.
  - Hook `python3`-ыг дууддаг тул `Python313\python3.exe` хуулбар үүсгэж, User PATH-д Python313-ийг WindowsApps-ын өмнө шилжүүлэв.
- **Яагаад:** курсын W1–W3 «хэрэглэх» шат fm plugin-гүйгээр ажиллахгүй (`/fm:*`, BOOT.md inject). Vault аль хэдийн template-ийн өмнөх хувилбараас үүссэн тул бүтнээр нь хуулахгүй, зөвхөн дутууг нэмэв.
- **Хяналт:** hook скриптүүд, UI модульд сүлжээ рүү автоматаар илгээх, систем өөрчлөх код олдсонгүй. Discord watcher зөвхөн гараар (📡) асна, token тохируулаагүй.
- **Буцааж болох эсэх:** болно. `claude plugin uninstall fm@second-brain-season-2`, `claude plugin marketplace remove second-brain-season-2`, `~/.fmos/config.json` устгах. Нэмсэн файлын жагсаалт, хуучин PATH → `_system/fm/state/install-2026-11-04.txt`.
- Холбоотой: [[Хичээл 03 - Бүгдийг нэг газар цуглуулах]] · [[2026-11-04]]
