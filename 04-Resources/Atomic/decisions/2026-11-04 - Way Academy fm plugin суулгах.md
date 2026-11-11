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

## 2026-11-05 шинэчлэл: 0.10.3 → 0.10.7

- **Хэн:** Mugi «repo update», «бүгдийг бич» гэж баталсан. Claude (📥 GTD · PC) хийв.
- **Хийсэн:** репог `git pull`, marketplace `second-brain-season-2`-ийг шинэчилж fm 0.10.7 болгов. Vault-д: `fm_migrate` (дэд хавтсан дахь 6 base-ийг PARA дээд хавтас руу, 5 холбоос), `fm_bases update` (17 base загвараар солив), `fm_rules update` (BOOT, 6 дүрийн note, template, `CLAUDE.md`-д «Хамтрагчийн зарчим»), `check/shinechlel.py` (дутуу 4 файл). Хуучин хувь → `_trash/bases-2026-11-05/`, `_trash/rules-2026-11-05/`.
- **Цэвэрлэгээ:** `fm_bases` `04-Resources/Taxonomy/Ангилал.base`-ийг дахин үүсгэсэн (дээд хавтас дахьтай яг ижил) → `_trash` руу зөөж, 17 note дахь бичвэр замыг `04-Resources/Ангилал.base` болгов. Хуучин «📥 GTD» сешнийг архивлав.
- **Үлдсэн:** `04-Resources/library/repos/Багаж ба skill.base` дэд хавтаст (base байршлын дүрэмтэй зөрчилдөнө), `01-GTD/Untitled*.base` 2, эзэнгүй base 46. `check.py` 6/7 (Б7 гаралт дутуу). Figma bridge ирсэн, Figma desktop суугаагүй.
- **Буцааж болох эсэх:** болно — `_trash/*-2026-11-05/`-аас сэргээнэ.

- Холбоотой: [[Хичээл 03 - Бүгдийг нэг газар цуглуулах]] · [[2026-11-04]]
