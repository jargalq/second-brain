---
date: 2026-11-13
type: atomic
төрөл: атом
төлөв: идэвхтэй
огноо: 2026-11-13
tags: [knowledge, AutoCAD, MCP, аюулгүй-байдал]
ai-first: true
aliases: [autocad-mcp-pro COM mode safety gaps]
resources:
  - "[[2026-11-12 - Уурхайн зургийн skill судалгаа]]"
---
# autocad-mcp-pro-гийн COM горим ажилладаг, гэхдээ энгийн командыг хаадаггүй, хаахдаа асуулгүй хадгалдаг

## For future agent
- **Баримт (2026-11-13, autocad-mcp-pro 1.8.0, AutoCAD 2024, `ZuunNaran.dwg`-ийн хуулбар):** DWG нээх, давхарга үүсгэх, `drawing_save_as`, `drawing_export_pdf` (706 КБ) ажилласан. Эх файлын md5 өөрчлөгдөөгүй.
- **Цоорхой:**
  1. `DANGEROUS_COMMANDS_ENABLED=false` нь зөвхөн `security.py`-ийн жагсаалтыг хаадаг; `system_run_command "_LINE …"` ажилласан.
  2. `drawing_close` өөрчлөлтийг асуулгүй хадгалсан.
  3. `LISP_POLICY`-ийн зөв утга: `read`, `denylist`, `off` (`deny` биш).
  4. `analysis_layer_stats` 2 808 объекттой файлд 180 сек-д гараагүй; ezdxf горимд хормын дотор.
  5. PDF-д plot тохиргоо өгөхгүй бол зураг хуудасны доод хэсэгт шахагдана.
- **Хэрэглэх журам:** үргэлж хуулбар дээр; `ALLOWED_PATHS`-ийг туршилтын хавтсаар; `TOOL_DENYLIST=system_run_command,system_run_lisp` эсвэл `READ_ONLY=true`.
- **Хаана хэрэгтэй:** олон DWG-ээс PDF бөөнөөр гаргах, давхарга шалгах. Python → DXF → `dxf2dwg_groups.ps1` урсгалыг орлохгүй.
- **PARA:** [[Уурхайн зураг ба төлөвлөлт]] · [[Зураг - шийдвэр, асуудлын нэгтгэл]]
