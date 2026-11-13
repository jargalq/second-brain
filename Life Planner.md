---
date: 2026-11-12
type: dashboard
төрөл: самбар
төлөв: идэвхтэй
ai-first: true
cssclasses:
  - life-planner
tags:
  - home
  - dashboard
aliases:
  - Амьдралын төлөвлөгч
---
![[01-GTD/Inbox/Untitled.base]]

```dataviewjs
await dv.view("_system/views/life-planner")
```

%%
## For future agent
Notion-ий «Life Planner» загварын бараан dashboard (Mugi 2026-11-12). Код: `_system/views/life-planner/view.js`, загвар: `.obsidian/snippets/life-planner.css` (`cssclasses: life-planner`). Шаардлага: Dataview (dataviewjs асаалттай).
Өгөгдөл: 01-GTD/Tasks (status|төлөв, due|хугацаа, completed|дууссан, хүрээ), 01-GTD/Daily (habit_* талбар, «Өнөөдрийн 3 гол зорилт» checkbox, «Санаа», «Тэмдэглэл»), 01-GTD/Events (type: meeting, scheduled), 01-GTD/Inbox, 02-Projects (идэвхтэй төсөл, checkbox-ийн явц), 00-Soul/SOUL «Гурван өндөр». Хуурамч өгөгдөл бүү нэм; хоосон бол «алга» гэж харуулна.
%%
