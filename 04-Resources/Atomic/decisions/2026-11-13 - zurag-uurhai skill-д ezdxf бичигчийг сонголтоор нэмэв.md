---
date: 2026-11-13
type: session-decision
төрөл: шийдвэр
төлөв: идэвхтэй
огноо: 2026-11-13
tags: [decision, зураг, skill, zurag-uurhai, ezdxf, autocad]
ai-first: true
aliases: [Add optional ezdxf DXF writer to zurag-uurhai skill]
resources:
  - "[[2026-11-12 - Уурхайн зургийн skill судалгаа]]"
  - "[[_system/skills/zurag-uurhai/SKILL|zurag-uurhai]]"
related:
  - "[[2026-11-12 - Skill-ийг эвдэхгүй, зөвхөн сайжруулна]]"
  - "[[2026-11-13 - CAD, GIS багцыг тусдаа venv-д, хуулбар дээр туршина]]"
---

# zurag-uurhai skill-д ezdxf бичигчийг сонголтоор нэмэв

**Шийдвэр:** `zurag-uurhai` skill-д ezdxf-ээр DXF R2013 бичдэг `zn_dxfw_ez.py`-г нэмэв. Ажиллуулахдаа `ZN_DXF=ezdxf` гэж заана. Хувьсагчгүй үед хуучин R12 бичигч хэвээр ажиллана.

- **Хэн:** Mugi зөвшөөрөв («Тийм, нэвтрүүл»), Wiki сешн хийв.
- **Яагаад:**
  - Group, handle DXF дотроо байдаг тул DWG-г AutoCAD-аар нэг л удаа хадгалж гаргана (`dxf2dwg_ez.ps1`). Ерөнхий дэвсгэр 105 с-ээс 50 с болсон.
  - Кирилл, Ө, Ү, ³ тэмдэгт `\U+` кодгүй шууд бичигдэнэ. Hatch (`'HA'`) нэмэгдэв.
- **Шалгалт:**
  - Анхдагч горимд 6 паспортын DXF байт бүрээрээ ижил гарав. Жинхэнэ skill дээр дахин шалгав.
  - ezdxf горимд 6 паспорт ба `zn_dxf.py`-ийн ерөнхий дэвсгэр (2 634 объект, 36 group) хуучинтай ±1 мм дотор таарав. Давхарга, group ижил. AutoCAD group-ийг танив.
  - `zn_reclaim`, `zn_year1`, `zn_year10`, `bn_*`-ээр шалгаагүй.
- **Буцаах:** болно. `zn_dxfw.py`-д нэмсэн 4 мөрийг хасах, эсвэл `_trash/skill-zurag-uurhai-2026-11-13/`-ийн нөөцийг сэргээнэ.
- **Нөхцөл:** ezdxf зөвхөн `C:\Users\Hp\.venvs\ezdxf` venv-д суусан. Шинэ горимыг тэр venv-ийн python-оор ажиллуулна.

## For future agent
Шинэ горимыг анхдагч болгохоос өмнө `zn_year*`, `zn_reclaim`, `bn_*`-ийг `compare.py` маягийн тулгалтаар шалга.
