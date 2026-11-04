---
type: taxonomy
axis: project-type
value: content
label: "Контент"
icon: "📣"
date: 2026-10-26
tags: [taxonomy, project-type]
ai-first: true
key-activity: []
up: "[[04-Resources/Taxonomy/Ангилал]]"
status: active
---

> **itge.e-ийн ангилал.** Төрөл бүр нь юу болохыг тодорхойлсон note. `04-Resources/Taxonomy/Ангилал.base` дээр бүгд хүснэгт болж харагдана. Өөрийн ажилд тохирохгүйг нь устгаад, дутууг нь ижил хэлбэрээр нэм.

# 📣 Контент

**Тэнхлэг:** `project-type:` — төсөл ямар төрлийн ажил вэ.

## Юу вэ
Пост, carousel, reel, newsletter, брэндийн визуал гаргах төсөл.

## Key Activity
Канвасын activity: өөрийн Key Activity · өөрийн Key Activity. Дүгнэлт: таарна — Контент, брэндинг.

## Анхдагч самбар
Preset нь `04-Resources/Taxonomy/project-type/content.json` файлд байна. Төсөл үүсэхэд `_dashboard.json` руу хуулагдана (лавлагаа биш, хуулбар).

## Стандарт (itge-content)

### 1. Гаралт ба загвар
| Гаралт | Загвар (эх) | Хэмжээ / формат | Фонт (Ө Ү шалгасан) |
|---|---|---|---|
| Inspired remake reel | (дотоод жишээ) | 9:16; VO −18 LUFS, хөгжим VO-гоос −10 dB | SF Pro Bold/Heavy (sei карт) |
| Carousel | How-to стандарт §6 · `fm:post` | 1080×1350, 10 слайд, margin 96, слайд ≤25 үг | Montserrat 64–72 гарчиг |
| Poster / пост | давхаргатай урсгал (v15) · `fm:post` · `03-Areas/Studio/poster-maker/` | 1080×1350 (4:5) | төслийн DS |
| Short video (ерөнхий) | How-to reel загвар · Хичээл 03 `make_video.py` | 9:16 | — |

**Нэршил ба хувилбар:** Figma `<Төсөл>_<Гаралт>_<Хэмжээ>_vNN`, бичвэр `NNN - бичвэр (vN).md`; «final» гэж бичихгүй. Засвар бүр clone, хуучныг дарахгүй (жижиг засвар л газар дээр нь). Нэг гаралт = нэг карт, хувилбарууд дотроо; олон төсөлд PARA холбоосоор ().

### 2. Хэрэгсэл
`fm:post` · `fm:figma` (`fig.py` bridge) · `fm:watch` (эх бичлэг задлах) · Premiere (MOGRT, Essential Sound — Claude рендер биш) · faster-whisper (үгийн цаг) · `vo_sync.py`, `vo_cards.py`, `aud.py` · NotebookLM (Journal brainstorm) · `build_lesson.py`, `export_html.py` · Vercel (`itge-intro`).

### 3. Шат (бүх гаралтад нийтлэг)
1. **Brief, эх** — эхлээд vault, дараа нь вэб; эх сурвалжийн URL бүрийг тэмдэглэнэ.
2. **Бичвэр** — no ego, редакцийн монгол; Journal бол brainstorm + редакторын шат.
3. **Загвар сонгох** — дээрх хүснэгтээс; «өөрөөр найруул» = бичвэр, бүтэц, дизайн биш.
4. **Зураг, кадр** — Figma-д загварын instance-аар (постер: wireframe → plate → foreground → layer control).
5. **Хөдөлгөөн, дуу** — VO → whisper → карт; Premiere-д угсарна.
6. **QA** — тусдаа шалгалт (доорх), 100% томруулж.
7. **Батлалт** — itge.e Figma коммент; батлагдсан frame-ийг түгжиж, Output note-д `батлагдсан · YYYY-MM-DD · vNN`.
8. **Нийтлэл** — HTML бол `02-Projects/itge.online/Output/site/` (`articles/<slug>/`, `lessons/NN/`) → Vercel; сошиал постыг itge.e өөрөө нийтэлнэ.

### 3б. Техникээр сэтгэх (Creative workflow v2, itge.e 2026-10-29)
Визуал гаралт бүр (пост, постер, carousel, cover, Journal-ын визуал) [[04-Resources/Taxonomy/Workflow/creative-technique-loop|🧭 техникийн тойрог]]-оор явна:
- **Moodboard** — техникээр бүлэглэнэ (мөр бүр нэг техник), харагдах байдлаар биш. Сан: [[04-Resources/Taxonomy/Technique]] · Figma «🧭 Техникийн сан».
- **Brief** — 3-р шатын 1-д «ямар алхам тус болох вэ» гэж үйлдэл › талбар › **1–3 техник** нэрлэнэ (жишээ: carousel нүүр = Масштабын зөрүү + Ханасан өнгөн талбай; дотор = Хэмжээний шатлал). itge.e сонгоно.
- **QA** — 6-р шатад нэрлэсэн техник бүр 360 px-д нүдэнд харагдаж байгааг шалгана.
- **Бүртгэл** — Output note-д `technique:` + `technique-evidence: observed`; гаралт техникийн сангийн шинэ жишээ болно.

### 4. «Дууссан» шалгуур
- [ ] Brief-д нэрлэсэн 1–3 техник 360 px thumbnail-д харагдана; Output note-д `technique:` бичигдсэн
- [ ] Ө Ү 1:1 зургаар шалгасан («хүмүүс төрөхөөсөө Үргэлж Өөр»)
- [ ] Reel: safe zone, нэг кадр = нэг accent, кадр ≤4 с
- [ ] Бичвэр тасраагүй, placeholder бүр vault-д нотолгоотой
- [ ] Journal: slideshow ≥3, 3 с mp4, contain-fit, 390 ба 1280 px-д хэвтээ scroll алга, хайрцаг бүрт эх URL
- [ ] Хичээл: самбарын screenshot алга — component болгож дахин зурсан
- [ ] Постер hero-д гарчиг давхардаагүй
- [ ] Task `outputs:` + Output note-д хувилбар, батлалт

### 5. Хориг
- Unbounded, Playfair Display, Mona Sans (Ө Ү алга).
- Journal-ын дизайныг өөрчлөхгүй; social дизайныг вэб хуудсанд тэр чигт нь хуулахгүй.
- Хичээлийн HTML-ийг artifact болгохгүй.
- Зургийн хувилбарыг чатаар явуулахгүй — Figma-д.
- Кино footage = зөвхөн өөрийн IG; эх reel-ийг хуулахгүй, санааг авна.
- Төлбөртэй зураг үүсгэлт = itge.e-ийн OK.

### 6. Эх сурвалж

### ✅ Шийдсэн (2026-10-29, Architect — itge.e даатгав)
- **Reel-ийн анхдагч фонт = Montserrat** (Ө Ү зөв); SF Pro-г зөвхөн Apple UI дуурайсан sei картад.
- **Бүртгэл:** гаралт бүр Output note + нийтлэгдвэл itge.online мөрөнд (PARA цагийн шугамын itge.online эгнээ).
- Short video = How-to reel загвараар; Хичээл 03-ын `make_video.py`-ийг анхны загвар болгоно.

## Хэзээ хэрэглэх
Frontmatter-т `project-type: content` гэж бичнэ. Талбаргүй бол `generic` гэж үзнэ, таамаглахгүй.

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
