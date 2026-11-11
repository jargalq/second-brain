---
type: taxonomy
axis: project-type
value: software
label: "Систем, хэрэгсэл"
icon: "🛠"
date: 2026-10-26
tags: [taxonomy, project-type]
ai-first: true
key-activity: []
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 🛠 Систем, хэрэгсэл

**Тэнхлэг:** `project-type:` — төсөл ямар төрлийн ажил вэ.

## Юу вэ
Өөрийн програм, plugin, bridge, vault-ийн хөдөлгүүр бүтээх төсөл.

## Key Activity
Канвасын activity: өөрийн Key Activity. Дүгнэлт: шинэ — «Өөрийн систем, хэрэгсэл хөгжүүлэх» (Revenue: Product).

## Анхдагч самбар
Preset нь `04-Resources/Taxonomy/project-type/software.json` файлд байна. Төсөл үүсэхэд `_dashboard.json` руу хуулагдана (лавлагаа биш, хуулбар).

## Стандарт
> Суурь =  §1–5 (бүтнээр нь уншина). Энд зөвхөн software төслийн шахмал. Нотолгоо: Inai Operation App / Second Brain OS (goomnet), founder-matrix-os.

### 1. Гаралт ба загвар
| Гаралт | Загвар / байршил |
|---|---|
| Spec | `goomnet/docs/superpowers/specs/YYYY-MM-DD-<сэдэв>-design.md` |
| Plan | superpowers:writing-plans → task-ийн «Өөрчлөлтийн түүх»-д холбоос (PLAN.md шиг гурав дахь эх үүсгэхгүй) |
| Дизайн | moodboard → wireframe (clone хувилбар) → 🧩 component; Stitch v2 = чадварын суурь (`02-Projects/Inai Operation App/Output/stitch-projects-v2/`) |
| Код | goomnet: зөвхөн `feat/second-brain-platform` · founder-matrix-os: `main` (CI ногоон) |
| Харагдац | Нэг төрөл = нэг component (`AppHeader`, `CalendarView`, kanban, гаралтын component, `openChat`, Ctrl K) |
| Run note | `<төсөл>/Chat/runs` |
| Багаж | `04-Resources/library/repos/<нэр>.md` (`type: tool`, cover, url, status) |

### 2. Хэрэгсэл
superpowers (brainstorming → writing-plans → subagent-driven-development → verification-before-completion; systematic-debugging) · `.claude/skills/better-*` · `variant` (сонголт тодорхойгүй үед) · `interface-review` (дуусгахад) · fm browse screenshot · `fm_goom_dispatch`.

### 3. Шат
1. Task (itge.e-ийн эх үг «Шаардлага»-д) → claim.
2. Brainstorm → spec (itge.e батлана).
3. Plan → subagent-driven хэрэгжүүлэлт; subagent бүр task-тай хоёр талдаа холбоотой.
4. Дизайн хэрэгтэй бол Figma эсвэл прототип → itge.e коммент → component.
5. Код: better-* дүрэм; хуурамч өгөгдөлгүй («удахгүй», «unknown»).
6. QA: бүх хуудсыг screenshot, прототип ↔ апп хос зураг, урсгалаар дайрч алдаа засна — тэгээд л харуулна.
7. `interface-review` → commit (зөв салаа) → task `completed` + «## Хүргэсэн».

### 4. «Дууссан» шалгуур
- [ ] Тест, CI ногоон; verification-before-completion хийсэн
- [ ] Screenshot QA хос зураг task-д хавсаргасан
- [ ] Шинэ харагдац байгаа component-ийг давтаагүй
- [ ] Хуурамч 0 алга; холбогдоогүй үйлдэл = «удахгүй»
- [ ] Commit hash, файл task-ийн `outputs:`, «Хүргэсэн»-д; урт run бол thread-д явц бичигдсэн
- [ ] Шинэ багаж бол `type: tool` note

### 5. Хориг
- goomnet-ийн өөр салаа руу push хийхгүй; хувийн зам commit хийхгүй.
- Шинэ repo үүсгэхгүй (founder-matrix-os-ийг томруулна).
- Тестгүйгээр «болсон» гэхгүй.
- CLAUDE.md, hook өөрчилдөг гадны хэрэгсэл (AgentTrail г.м.) суулгахгүй.

### 6. Эх сурвалж
(дотоод жишээ) ·  ·  · 

### ✅ Шийдсэн (2026-10-29)
- **Дизайны эх үнэн = Figma → component** (itge.e). HTML прототип нь туслах хэрэгсэл болж үлдэнэ, эх үнэн биш; 10-27-ны шийдвэрийг энэ орлоно.
- `better-*` skill-ийг `04-Resources/library/repos/better UI skill-үүд (kargulstudio).md` бүртгэнэ (Architect шийдэв).

## Хэзээ хэрэглэх
Frontmatter-т `project-type: software` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

Шийдвэр: 

## 🔗 Хэрэглэсэн газар

```base
filters:
  and:
    - '!file.inFolder("_trash")'
    - or:
        - list(tool).contains(this)
        - list(task-type).contains(this)
        - list(project-type).contains(this)
views:
  - type: table
    name: Хэрэглэсэн газар
    groupBy:
      property: type
      direction: ASC
    order: [file.name, type, status, project]
```
