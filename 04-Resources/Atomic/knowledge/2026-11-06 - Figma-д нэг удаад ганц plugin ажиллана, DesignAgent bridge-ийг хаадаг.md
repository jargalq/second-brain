---
төрөл: атом
төлөв: идэвхтэй
type: atomic
date: 2026-11-06
ai-first: true
confidence: high
tags: [atomic, figma, fm-bridge, windows]
sources: ["[[_system/logs/2026-11-07]]"]
areas: ["[[03-Areas/AI Team/ai-workers/Creative Director]]"]
aliases: [Figma one plugin at a time, DesignAgent closes Claude Bridge]
---
# Figma-д нэг удаад ганц plugin ажилладаг тул «DesignAgent – Claude Bridge» нь fm-ийн Claude Bridge-ийг хаадаг

## For future agent
2026-11-06-нд PC дээр fm-ийн Figma bridge-ийг асаах үед туршиж олсон баримт. `fig.py status` нь `plugin: False` гэж гарвал эхлээд энэ атомыг унш.

## Баримт
- Энэ PC-д fm-ийн «Claude Bridge» dev plugin import хийгдээгүй байсан. Үүнийг **Plugins → Development → Import plugin from manifest…** цэсээр `D:\code\way-academy-season-2\plugins\fm\tools\figma\bridge\plugin\manifest.json` файлаас import хийсэн.
- Figma-д «DesignAgent – Claude Bridge» (sherizan) гэсэн гуравдагч талын plugin бас суусан. Ctrl+/ дээр «Claude Bridge» гэж хайхад тэр нь нээгддэг. Figma нэг удаад ганц plugin ажиллуулдаг тул тэр нээгдмэгц манай bridge хаагдаж, `plugin: False` болдог.
- Найдвартай арга нь **Plugins → Development → Claude Bridge** цэсээр нээх. «Run last plugin» (Ctrl+Alt+P) ч DesignAgent-ийг нээж магадгүй.
- `open_plugin.ps1` (2026-11-06): мөр 19 нь өөр машины `C:\Users\USER\...` замд screenshot хадгалах гэж алдаа өгдөг. Монгол гарын байрлалд SendKeys `^/` ажиллахгүй. → [[01-GTD/Tasks/fm figma - open_plugin.ps1 DesignAgent plugi]]
- Claude-ийн апп урд байх үед `SetForegroundWindow` Figma-г урд гаргаж чаддаггүй. `WScript.Shell.SendKeys('%')`-ийн дараа `AppActivate` хийхэд ажилласан.

**Холбоос:** [[03-Areas/AI Team/ai-workers/Creative Director]] (Figma bridge-ийг ашигладаг дүр) · [[04-Resources/Atomic/knowledge/2026-11-05 - Figma дизайн файлд PDF шууд орохгүй, SVG болгож буулгана]] (ижил PC дээрх Figma-ийн өөр нэг хязгаар)
