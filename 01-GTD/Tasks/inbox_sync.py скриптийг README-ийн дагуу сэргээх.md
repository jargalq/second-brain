---
date: 2026-11-10
type: task
tags:
  - task
ai-first: true
# status: inbox | next-action | in-progress | waiting | someday | completed | cancelled
status: waiting
context: work
owner: "architect"
project:
projects: []
responsible: architect
accountable: me
consulted: []
informed: ["me"]
up: "[[01-GTD/Tasks/Tasks]]"
next_action: "Mugi: Task Scheduler-т «Obsidian Inbox sync»-ийг дахин бүртгэх эсэх"
due:
started:
completed:
priority: medium
aliases:
  - "inbox_sync.py скриптийг README-ийн дагуу сэргээх"
updated: 2026-11-11
---

# inbox_sync.py скриптийг README-ийн дагуу сэргээх

## Шийдэх асуудал / яагаад

`CLAUDE.md`-ийн `inbox` команд `python -I "_system/inbox-sync/inbox_sync.py"`-г эхэлж ажиллуулна гэсэн ч 2026-11-10-ны байдлаар `_system/inbox-sync/`-д зөвхөн `README.md` байна. Иймээс `D:\Inbox`-д орсон файл `01-GTD/Inbox`-д тэмдэглэл болохгүй байж магадгүй. Task Scheduler-ийн «Obsidian Inbox sync» ажил ч мөн скриптгүй ажиллаж байгаа эсэх TBD. Хоёр сешн (Wiki afca42bb, Architect 2f62406b) бие даан анзаарсан.

Холбоотой: [[04-Resources/Atomic/decisions/2026-10-30 - D-Inbox хавтсыг Obsidian Inbox-той холбох]] · [[_system/inbox-sync/README|inbox-sync README]]

## Next action

- Mugi: сэргээх эсэхийг батлах (сешнүүдэд «Architect-д дамжуул» гэсэн сонголт өгсөн, хариу бүртгэгдээгүй).

## Явц
- 2026-11-10 21:57 📌 үүсгэв (Harvester digest afca42bb, 2f62406b-аас)
- 2026-11-11 00:10 📚 Wiki: Mugi «Тийм, сэргээ». Эх скрипт нөөц, _trash-д ч олдоогүй тул README + [[04-Resources/Atomic/decisions/2026-10-30 - D-Inbox хавтсыг Obsidian Inbox-той холбох|шийдвэр]]-ийн дагуу `_system/inbox-sync/inbox_sync.py`-г дахин бичив (WATCH = `D:\Inbox`, дэд хавтас, txt/docx/pdf эхний хэсэг, `state.json`, `--dry-run`, pythonw-д найдвартай). Scratchpad-д туршив: 3 файл → 3 note, дахин ажиллуулахад 0. `D:\Inbox` хавтас алга байсныг дахин үүсгэв. Task Scheduler-ийн «Obsidian Inbox sync» ажил ч алга — дахин бүртгэх нь Mugi-ийн зөвшөөрөл хүлээж байна.
