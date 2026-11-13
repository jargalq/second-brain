---
төрөл: шийдвэр
type: session-decision
төлөв: идэвхтэй
огноо: 2026-11-13
date: 2026-11-13
aliases: [Remove Great Vision project junction]
tags: [decision, PARA, junction, D-диск]
areas: ["[[04-Resources/references/D дискийн PARA индекс (PC)]]"]
---
# Great Vision project junction-ийг устгаж PARA замаар ажиллана

- **Шийдвэр:** `D:\Great Vision project` (→ `D:\PARA\1-Projects\Great Vision project` руу заасан junction)-ийг устгав. Vault-ийн 72 файлын (task, төслийн note, skill, script) замыг `D:\PARA\1-Projects\Great Vision project` болгов. Өдрийн тэмдэглэл, атом, SOUL, лог, `_system/folder-moves`-ийг хөндөөгүй (түүх). `.claude/settings.local.json`-ийн хуучин замтай 5 зөвшөөрлийн мөрийг хасав.
- **Хэн:** Mugi (2026-11-13, «энэний учрыг олоорой алга болгоод vault-aa тохируулаарай»), Architect гүйцэтгэв. Commit `c419a19`, push хийсэн.
- **Яагаад:** 11-11-нд `D:\PROJECT`-ийн junction-уудыг устгасантай ижил журам: нэг файл нэг жинхэнэ замтай байна.
- **Буцааж болох уу:** Тийм. `mklink /J "D:\Great Vision project" "D:\PARA\1-Projects\Great Vision project"`; замыг git-ээр буцаана.
