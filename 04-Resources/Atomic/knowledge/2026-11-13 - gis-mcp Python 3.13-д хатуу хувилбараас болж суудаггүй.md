---
date: 2026-11-13
type: atomic
төрөл: атом
төлөв: идэвхтэй
огноо: 2026-11-13
tags: [knowledge, GIS, python, MCP]
ai-first: true
aliases: [gis-mcp fails on Python 3.13 due to pinned deps]
resources:
  - "[[2026-11-12 - Уурхайн зургийн skill судалгаа]]"
---
# gis-mcp 0.15.0 Python 3.13-д шууд суудаггүй, гэхдээ координат хувиргалт нь зөв

## For future agent
- **Баримт (2026-11-13):** gis-mcp 0.15.0 нь `fiona==1.9.6`, `numpy<2`, `rasterio==1.3.9`-ийг хатуу заасан тул Python 3.13-д бинар wheel олдохгүй. Mugi-ийн компьютерт зөвхөн Python 3.13 (64-bit) байна.
- **Тойрсон арга:** `pip install gis-mcp --no-deps` + шинэ хувилбар (numpy 2.5, rasterio 1.5, geopandas 1.2, fastmcp 2.13.1, pillow, tabulate, spreg). esda, giddy, fiona алга — эдгээрт тулгуурласан хэрэгсэл ажиллахгүй байж магадгүй.
- **Шалгалт:** 105°E 45°N → EPSG:32648 = 500 000.0 / 4 982 950.4; эргүүлэх хувиргалт, 0.01° дөрвөлжны геодезийн талбай 876 163 м² — pyproj-тэй яг таарсан.
- **Эрсдэл:** `download_file`, `download_satellite_imagery` зэрэг интернэт рүү хандах хэрэгсэлтэй. MCP болгон бүртгэвэл хаах.
- **PARA:** [[Уурхайн зураг ба төлөвлөлт]]
