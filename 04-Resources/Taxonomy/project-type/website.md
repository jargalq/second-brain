---
type: taxonomy
axis: project-type
value: website
label: "Вэбсайт"
icon: "🌐"
date: 2026-10-26
tags: [taxonomy, project-type]
ai-first: true
key-activity: []
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Taxonomy/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 🌐 Вэбсайт

**Тэнхлэг:** `project-type:` — төсөл ямар төрлийн ажил вэ.

## Юу вэ
Клиентийн болон өөрийн вэбсайт: brief, дизайн, build, launch.

## Key Activity
Канвасын activity: өөрийн Key Activity · өөрийн Key Activity. Дүгнэлт: таарна — Дизайн, Хөгжүүлэлт.

## Анхдагч самбар
Preset нь `04-Resources/Taxonomy/project-type/website.json` файлд байна. Төсөл үүсэхэд `_dashboard.json` руу хуулагдана (лавлагаа биш, хуулбар).

## Вэбсайтын талбарууд (2026-10-26, itge.e баталсан)
Төслийн note-ийн frontmatter-т гурван нэмэлт талбар бичнэ. `links` болон `launch`-ийг нэг мөрийн flow хэлбэрээр (JSON шиг) бичдэг, учир нь `fm_goom_sync` олон мөрийн үүрлэсэн бүтцийг уншдаггүй.

- `links:` — `{"staging": "", "prod": "", "figma": "", "framer": "", "repo": ""}`. Нотолгоотой URL л бичнэ; мэдэхгүй бол хоосон.
- `launch:` — `[{"item": "domain", "done": false}, …]`. Ерөнхий жагсаалт: domain, SSL, analytics, SEO meta, OG images, 404, performance, client sign-off.
- `pages:` — CSV sidecar-ийн зам `02-Projects/<P>/Data/pages.csv`. Баганууд: page, path, stage (brief|wireframe|design|build|qa|live), owner, figma, url, seo_title, updated, task. Шийдвэр: .

Апп (Second Brain OS) эдгээрийг төслийн timeline endpoint-ын `site` талбараар уншина.

## Стандарт

### 1. Гаралт ба загвар
| Гаралт | Загвар / байршил | Тэмдэглэл |
|---|---|---|
| Brief + `pages.csv` | `02-Projects/<P>/Data/pages.csv` (stage: brief→wireframe→design→build→qa→live) | дээрх «Вэбсайтын талбарууд» |
| Component library | Нэг unique library; дэлгэц = зөвхөн instance |  |
| Код | GitHub repo (`links.repo`); код vault-д биш, vault-д бичвэр ба шийдвэр |  |
| Staging / prod | Vercel preview → батлалт → prod (`links.staging`, `links.prod`) |  |
| Толгой, хөл | Нэг builder-ээс бүх хуудсанд |  |
| Гаралтын бүртгэл | `Output/YYYY-MM-DD - Гаралтын бүртгэл (Figma · HTML · Vercel).md` (BYD жишиг) | |

### 2. Хэрэгсэл
Figma (зөвхөн `fig.py` bridge, MCP биш) · Stitch (функциональ суурь байгаа бол дахин зохиохгүй) · стек: клиентийн сайт =  (BYD, <өөрийн төсөл> = JukeBox нэг стек), өөрийн static сайт = `build.py` + Vercel (itge.online) · Vercel CLI · fm browse (playwright-core) screenshot QA.

### 3. Шат
1. **Brief, ассет** — клиентийн батлагдсан лого, фонт, палитр эхэнд (шинээр зохиохгүй); `pages.csv` бөглөнө.
2. **Moodboard** — эхлээд vault, дараа нь Pinterest, Dribbble → Figma.
3. **Wireframe → дизайн** — grid-ийг эхэлж тогтоож, давтагдсан хэсэг бүрийг component болгоно; хувилбар бүр clone (v1, v2…), section дотор баруун тийш.
4. **Коммент** — itge.e эсвэл клиент Figma дээр коммент; засварласан frame-ийг @mention-оор хариулна.
5. **Build** — repo-д (тохирох салаа); текстийн эх нэг чиглэлтэй (`content/` → repo).
6. **QA** — 1440 · 430 · 390 · 360 өргөнд screenshot; Figma ↔ код хос зураг.
7. **Preview** — Vercel preview линкээр батлуулна.
8. **Launch** — `launch:` жагсаалт бүгд `done: true`; prod deploy зөвхөн itge.e-ийн зөвшөөрлөөр.

### 4. «Дууссан» шалгуур
- [ ] `pages.csv`-ийн бүх мөр `live`, `links:` бүгд нотолгоотой URL
- [ ] Figma-д non-instance UI ≈ 0 (component audit)
- [ ] Хэвтээ scroll алга, hit area ≥44 px, медиа өөрийн харьцаагаар, lightbox ажиллана
- [ ] `launch:`-ийн 8 зүйл (domain, SSL, analytics, SEO meta, OG, 404, performance, client sign-off)
- [ ] Ө Ү-тэй фонт 1:1 шалгасан
- [ ] Гаралтын бүртгэл ба task `outputs:` шинэчлэгдсэн

### 5. Хориг
- Prod deploy, domain солих — itge.e-ийн зөвшөөрөлгүй хийхгүй.
- Дэлгэц бүрт гараар зурахгүй; Stitch эсвэл батлагдсан бүтцийг дахин зохиохгүй.
- Илгээсэн, батлагдсан хувилбарыг дарж засахгүй.
- Нийтийн repo-д клиентийн нэр, хувийн зам үлдээхгүй.

### 6. Эх сурвалж

### ✅ Шийдсэн (2026-10-29, Architect — itge.e даатгав)
- **Хоёр стек хэвээр:** клиентийн сайт клиентийн стек дээр (JukeBox), өөрийн static сайт `build.py`. Шинэ өөрийн сайт эхлэхэд дахин эргэж харна.
- **Prod deploy-д itge.e-ийн зөвшөөрөл заавал**, itge.online-д ч (preview чөлөөтэй).

## Хэзээ хэрэглэх
Frontmatter-т `project-type: website` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

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
