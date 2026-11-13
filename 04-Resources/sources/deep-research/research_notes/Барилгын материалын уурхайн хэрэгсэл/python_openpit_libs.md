---
төрөл: судалгааны тэмдэглэл
төлөв: түүхий
tags: [deep-research, уурхай, python, pit-optimization, open-source]
огноо: 2026-11-12
---

# Ил уурхайн төлөвлөлтийн нээлттэй эхийн Python сангууд (2024–2026)

> Тэмдэглэл: PyPI/GitHub-ийн мэдээллийг 2026-11-12-нд шалгав. Юу ч суулгаагүй, ажиллуулаагүй. Вэбийн агуулгыг итгэлгүй өгөгдөл гэж үзсэн. «[мэдлэг]» гэсэн тэмдэглэгээтэй зүйлийг энэ сешнд URL-аар шалгаагүй, сургалтын мэдлэгээс бичсэн тул таамаг гэж үз.

## 1. Pit optimization (UPL, Lerchs-Grossmann, pseudoflow): ямар хэрэгслүүд байгаа, засвартай юу, Whittle-тэй тулгасан уу

### Takeaway
Хамгийн найдвартай нээлттэй эх нь **MineFlow** (C++, MIT) ба түүний 2026 оны Python wrapper **PyMineFlow** (MIT, v0.1.0, 2026-10-20). Хамгийн их иш татагддаг PyPI `pseudoflow` багц нь **арилжааны бус лиценз**-тэй тул зөвлөх компанид дотооддоо ч ашиглахад эрсдэлтэй. Блокийн үнэ цэнийг гараар өгдөг тул эдгээр нь агуулгагүй (зөвхөн эзэлхүүн/зардал) эдийн засагт ч ажиллана. Whittle-тэй шууд тулгасан нээлттэй баталгаажуулалт олдсонгүй; MineLib-ийн нийтлэгдсэн оптимумтай тулгасан нь бий.

### Cited Findings
**MineFlow (MineFlowCSM)**
- C++ сан + командын мөрийн хэрэгсэл, ultimate pit limit тооцоолно; Matthew Deutsch хөгжүүлсэн, K. Dağdelen, T. Johnson онолын туслалцаа — [GitHub](https://github.com/MineFlowCSM/MineFlow)
- Лиценз MIT («open source and permissive MIT license»); 26 од, 15 fork, нийт 15 commit; Python binding README-д дурдагдаагүй; `matlab` хавтас бий; Hochbaum pseudoflow-ийн өөрчилсөн хувилбар — [GitHub](https://github.com/MineFlowCSM/MineFlow)
- Блокийн утгыг индексээр `SetBlockValueSI(index, value)`-аар өгнө (жишээнд бүхэл тоо, GMP overflow-ийн тэмдэглэл бий) — [GitHub](https://github.com/MineFlowCSM/MineFlow)
- Байршил, чиглэлээр өөрчлөгдөх налуутай үр ашигтай precedence граф, sub-block ба жигд бус загварыг дэмжинэ — [GitHub](https://github.com/MineFlowCSM/MineFlow)
- Нийтлэл: Deutsch, Dağdelen, Johnson (2022), «An Open-Source Program for Efficiently Computing Ultimate Pit Limits: MineFlow», Natural Resources Research, DOI 10.1007/s11053-022-10035-w — [Springer](https://link.springer.com/article/10.1007/s11053-022-10035-w) (бүтэн текстийг уншиж чадаагүй, redirect)

**PyMineFlow**
- PyPI `pymineflow` 0.1.0, 2026-10-20-нд байршуулсан; MIT; зохиогч Paul Alejandro Espinoza Tenecora; Python 3.10–3.14; repo github.com/MathGeoMineAILab/PyMineFlow; MineFlow C++ solver-ийг ороосон — [PyPI](https://pypi.org/project/pymineflow/0.1.0/)
- Precedence-ийг C++-д үүсгэнэ (minimum search pattern), эсвэл src/dst / CSR хэлбэрээр шууд өгнө; `n_benches` тохиргоо; налуу: тогтмол, азимутын сектороор, домэйноор, блок бүрээр; `slopes=None` үед 1:5 загвар — [PyPI](https://pypi.org/pypi/pymineflow/json)
- Оролт: CSV/GSLIB, Parquet, Feather, pandas/polars DataFrame, MineLib; IX/IY/IZ эсвэл төвийн координат — [PyPI](https://pypi.org/pypi/pymineflow/json)

**`pseudoflow` (PyPI, Hochbaum-ийн pseudoflow-ийн Python интерфейс)**
- Зохиогч Quico Spaen (Berkeley); сүүлийн хувилбар 2022.12.0 (2023-01-01); repo github.com/quic0/pseudoflow — [PyPI JSON](https://pypi.org/pypi/pseudoflow/json)
- **Лиценз: «Non-commercial license. Not an open-source license.»** — [PyPI JSON](https://pypi.org/pypi/pseudoflow/json)
- Parametric minimum cut-д зориулсан ерөнхий граф сан (уурхайн тусгай биш); Python, C, Matlab интерфейстэй — [piwheels/PyPI хайлтын үр дүн](https://www.piwheels.org/project/pseudoflow)

**Бусад жижиг, академик код**
- Avalos & Ortiz (2020, Queen's University), «A guide for pit optimization with pseudoflow in python» — nested pit шинжилгээтэй, зэсийн ордны жишээ — [Queen's](https://qspace.library.queensu.ca/items/beaf3c47-dbe7-46df-b6ee-b54a828610dd), [тайлан PDF](https://queensu.scholaris.ca/server/api/core/bitstreams/55b22e7e-2b19-4d60-b123-e9dc843c5bbf/content)
- luisflarota/Ultimate-Pit-Limit---Pseudoflow: networkx-оор граф үүсгэдэг; ~16 од, aggregator-ийн мэдээллээр 2022-07-25-нд сүүлд шинэчлэгдсэн — [GitHub](https://github.com/luisflarota/Ultimate-Pit-Limit---Pseudoflow), [relatedrepos](https://relatedrepos.com/gh/luisflarota/Ultimate-Pit-Limit---Pseudoflow)
- gPit (GuilhermeMene): MIT, 0 од, 13 commit, release байхгүй; UPL (Hochbaum pseudoflow), revenue factor, pit mesh, NPV ба **эзэлхүүн** тооцоо; хамаарал: pandas, numpy, pyvista, scipy, networkx, **pseudoflow**, meshio; Avalos & Ortiz-ийн кодоос үндэслэсэн — [GitHub](https://github.com/GuilhermeMene/gPit)
- CAOS_PitForge (fsantibanezleal): MIT, 0 од, 163 commit, 2026 copyright; хөтөч дээр TypeScript-ээр ажиллах min-cut (Picard reduction, Dinic + pseudoflow харьцуулалт), Whittle nested shell, MineLib newman1/zuck_small/kd-ийн нийтлэгдсэн оптимумыг ≤2×10⁻⁹ харьцангуй алдаатай давтдаг гэж мэдэгдсэн; CSV-ээр өөрийн блок загвар — [GitHub](https://github.com/fsantibanezleal/CAOS_PitForge)
- Перугийн JAMM сэтгүүлийн нийтлэл: Python дээр LG UPL, 151 898 блоктой синтетик зэсийн загвар, Colab, Python 3.12.12 — [UNITRU](https://revistas.unitru.edu.pe/index.php/jamm/en/article/view/7098)
- MineLib-ийг AMPL/amplpy-аар (UPIT, CPIT, PCPSP) Gurobi-гаар шийдсэн notebook; Newman1-д UPIT ≈ $26.09M, CPIT/PCPSP ≈ $24.18M — [AMPL Colab](https://colab.ampl.com/notebooks/minelib-in-ampl-and-amplpy.html) (AMPL ба Gurobi нь арилжааны solver)

**Баталгаажуулалт / Whittle-тэй харьцуулалт**
- GEOVIA Whittle-ийн pseudoflow engine нь LG-тэй ижил оновчтой pit өгдөг, илүү хурдан, илүү RAM хэрэглэдэг гэж үйлдвэрлэгч мэдэгддэг — [GEOVIA whitepaper](https://www.3ds.com/fileadmin/PRODUCTS-SERVICES/GEOVIA/PDF/whitepaper/GEOVIA-Whittle-Pseudoflow-WhitePaper.pdf)
- Muir (2004) «Pseudoflow, New Life for Lerchs-Grossmann Pit Optimisation»: pseudoflow хувилбарууд LG-ээс мэдэгдэхүйц хурдан — [IIETA нийтлэлийн тойм](https://iieta.org/download/file/fid/137962); Muir-ийн «Pseudoflow, MineFlow, MaxPitLG and Lerchs-Grossmann Mine Designs» ResearchGate дээр бий — [ResearchGate](https://www.researchgate.net/profile/David-Muir/publication/386051102_Pseudoflow_MineFlow_MaxPitLG_and_Lerchs-Grossmann_Mine_Designs/links/67416495b5bd9d17d60013a5/Pseudoflow-MineFlow-MaxPitLG-and-Lerchs-Grossmann-Mine-Designs.pdf) (агуулгыг уншаагүй)
- Deswik-ийн pseudoflow нь блокийн орлого/зардлыг хэрэглэгч өөрөө тооцохыг шаарддаг (Whittle-ийн параметрийн хүснэгт биш) — [Deswik](https://www.deswik.com/?p=4146)

### Inferences
- Max-closure/min-cut аргууд нь блок бүрт ямар ч тоон утга авдаг тул **агуулгагүй** хэрэглээнд (барилгын материал, андезит, дайрга) шууд тохирно: утга = (зарах үнэ − олборлолт − боловсруулалт) × эзэлхүүн/тонн, хөрс/хаягдалд сөрөг утга. Энэ нь онолын дүгнэлт, хэрэгслийн баримт бичигт «grade шаардлагагүй» гэж тусгайлан бичигдээгүй.
- Хүчин чадлаар хязгаарласан pit (CPIT) нь UPL биш — MILP эсвэл Lagrangian/параметрийн аргаар (revenue factor-оор nested shell) шийдэгдэнэ.
- Зөвлөх компанид: PyMineFlow/MineFlow (MIT) нь лицензийн хувьд хамгийн цэвэр сонголт; gPit нь `pseudoflow` (арилжааны бус)-оос хамаардаг тул арилжааны ажилд ашиглахгүй байх нь зөв.
- networkx-ийн `minimum_cut` (BSD-3 [мэдлэг]) эсвэл OR-Tools-ийн `SimpleMaxFlow` (Apache-2.0 [мэдлэг]) ашиглан Picard-ийн бууралтаар UPL-ийг өөрөө бичиж болно; жижиг загварт (<~1 сая блок) хангалттай байх магадлалтай — таамаг.

### Gaps
- MineFlow-ийн сүүлийн commit огноо GitHub хуудсанд харагдаагүй.
- MineFlow нийтлэлд Whittle-тэй шууд харьцуулалт байгаа эсэхийг шалгаж чадаагүй (Springer redirect).
- «OpenPitMiner», «PyLG» нэртэй засвартай сан олдсонгүй.
- PyMineFlow-ийн GitHub од, баримт бичгийн чанарыг шалгаагүй (маш шинэ, 0.1.0).

## 2. Блок загвар ба формат (OMF, PyVista, geoh5py, pygslib, GemPy)

### Takeaway
Блок загвар хадгалах, дүрслэхэд **PyVista (MIT)** + **omfvista (BSD, 0.4.0, 2026-10-29)** хамгийн идэвхтэй. `omf` өөрөө 2019 оноос хойш тогтвортой хувилбаргүй. **geoh5py** (Mira, LGPL-3.0, 0.13.1, 2026-08-21) идэвхтэй. **GemPy** (EUPL-1.2, 2026.0.3) геологийн загварчлалд. pygslib-ийн лиценз тодорхойгүй.

### Cited Findings
- `omf` (Global Mining Guidelines Group): MIT; тогтвортой 1.0.1 (2019-03-01); 2.0.0a0 alpha (2021-07-12) — [PyPI JSON](https://pypi.org/pypi/omf/json); V2 «active development, backwards-incompatible changes» гэж анхааруулсан — [GitHub](https://github.com/gmggroup/omf-python), [docs](https://omf.readthedocs.io/)
- `omfvista`: Bane Sullivan; BSD (classifier); 0.4.0, 2026-10-29; repo github.com/pyvista/omfvista; хамаарал omf>=1.0.0, pyvista, vectormath — [PyPI JSON](https://pypi.org/pypi/omfvista/json)
- `pyvista`: MIT; сүүлийн хувилбар 0.49.2 (огноо харагдаагүй); docs.pyvista.org — [PyPI JSON](https://pypi.org/pypi/pyvista/json)
- `geoh5py`: Mira Geoscience (maintainer Benjamin Kary); LGPL-3.0-or-later; 0.13.1, 2026-08-21; geoh5 нээлттэй формат (Geoscience ANALYST) — [PyPI JSON](https://pypi.org/pypi/geoh5py/json), [docs](https://mirageoscience-geoh5py.readthedocs-hosted.com/)
- `gempy`: EUPL-1.2; 2026.0.3 (2026-06-18), 2026.1.0a1 pre-release (2026-07-02); 3D бүтцийн геологийн загварчлал — [PyPI JSON](https://pypi.org/pypi/gempy/json)
- PyGSLIB (Opengeostat, Adrian Martinez Vargas): нөөцийн үнэлгээ, геостатистик; лиценз MIT/GPL гэж хуучин snapshot ба Wikipedia-д — [GitHub](https://github.com/opengeostat/pygslib), [docs](https://opengeostat.github.io/pygslib), [Wikipedia](https://en.wikipedia.org/wiki/List_of_free_geology_software); PyPI JSON 404 буцаасан — [PyPI](https://pypi.org/pypi/pygslib/json)

### Inferences
- Агуулгагүй ордод (андезит, элс хайрга) GemPy/PyGSLIB-ийн kriging шаардлагагүй байх магадлалтай; литологийн хил (хөрсний ул, давхаргын орой)-ийг гадаргуу болгоод PyVista-ийн `ImageData`/`RectilinearGrid` блок загварт тэмдэглэх нь хангалттай — таамаг.
- LGPL (geoh5py) нь сан болгон ашиглах, дотооддоо хэрэглэхэд хязгаарлалт бага; EUPL-1.2 нь copyleft, гэхдээ түгээхгүй бол дотоод хэрэглээнд үүрэг бараг үүсгэхгүй — [мэдлэг], хуулийн зөвлөгөө биш.

### Gaps
- PyGSLIB-ийн одоогийн LICENSE файл, сүүлийн commit-ийг шалгаагүй.
- PyVista 0.49.2-ийн гарсан огноо, татаж авалтын тоо (pepy/pypistats) шалгаагүй.

## 3. Хоёр гадаргуу хоорондын эзэлхүүн (topo vs pit, хөрсний ул)

### Takeaway
Энэ зорилгод зориулсан бат бөх, засвартай «нэг функц» Python сан олдсонгүй. Практик арга: хоёр гадаргууг нэг grid дээр түүвэрлэж (raster/DEM) зөрүү × нүдний талбай; эсвэл TIN-ийг нэг нэгэн дээр проекцлох. PyVista/trimesh нь битүү (watertight) mesh-ийн эзэлхүүн тооцдог боловч нээлттэй хоёр гадаргууг битүүлэх ажлыг хэрэглэгч хийнэ.

### Cited Findings
- ArcGIS Cut Fill нь хоёр гадаргуугийн эзэлхүүний өөрчлөлтийг тооцдог; raster-ууд ижил origin, мөр/багана, нүдний хэмжээтэй байх ёстой — [Esri](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/3d-analyst/cut-fill.htm) (Python-оос `arcpy`-аар дуудах боломжтой ч арилжааны)
- `volpy`: TIN-ээр илэрхийлсэн DEM-ээс эзэлхүүн тооцох Python төсөл — [GitHub](https://github.com/agu3rra/volpy) (засвар, лицензийг шалгаагүй)
- VTK форумд: нэг TIN-ийг нөгөө рүү проекцлож, босоо шулуунуудын огтлолцлоор гурвалжин бүрийн призмийн эзэлхүүнийг нэмэх арга; mesh boolean-д vtkbool санал болгосон — [VTK Discourse](https://discourse.vtk.org/t/extract-closed-surface-or-generate-3d-mesh-or-volume-from-two-non-closed-surface/3016)
- gPit-д «open-pit volume calculation» функц бий (PyVista дээр) — [GitHub](https://github.com/GuilhermeMene/gPit)
- trimesh: MIT, 5.2.0, Michael Dawson-Haggerty — [PyPI JSON](https://pypi.org/pypi/trimesh/json)
- ezdxf: MIT, 1.4.5, Manfred Moitzi — DXF унших/бичих (контур, 3DFACE/MESH гаргах) — [PyPI JSON](https://pypi.org/pypi/ezdxf/json)

### Inferences
- Нимгэн хөрсөнд (0.3–2 м) TIN-ийн гурвалжны алдаа харьцангуй их тул grid-ийн алхмыг жижиг (0.5–1 м) авч, хоёр гадаргууг `scipy.interpolate.LinearNDInterpolator` эсвэл `matplotlib.tri`-аар ижил grid руу түүвэрлээд `max(top − bottom, 0) × dx × dy`-ийг полигон (нөөцийн хил)-оор маск хийх нь хамгийн энгийн, шалгахад хялбар — таамаг/туршлагын зөвлөмж.
- PyVista-ийн `delaunay_2d()` → `extrude` эсвэл `sample`-аар гадаргуу хооронд өндрийн зөрүү авч болно; битүү эзэлхүүнд `PolyData.volume` — [мэдлэг], баримт бичгээр шалгаагүй.
- shapely (BSD) полигон маскад, rasterio/GDAL (MIT) DEM-д — [мэдлэг].

### Gaps
- PyVista/trimesh-ийн «гадаргуу хоорондын эзэлхүүн»-ий албан ёсны жишээ (example gallery) хайлтаар олдсонгүй.
- Python-ын cut/fill-ийг Surpac/Civil 3D-ийн үр дүнтэй тулгасан нийтлэл олдсонгүй.

## 4. Олборлолтын график (bench-by-bench, MILP)

### Takeaway
Бэлэн, засвартай «уурхайн хуваарь» Python сан алга. Академик код (Gurobipy, AMPL, Pyomo) ба MineLib-ийн benchmark л бий. Барилгын материалын жижиг уурхайд bench-by-bench MILP-ийг OR-Tools / PuLP+CBC / HiGHS-оор өөрөө бичих нь бодит зам.

### Cited Findings
- Lotsu, Bimpong, Boakye (2025, preprint): нээлттэй эхийн Python санд суурилсан, бүрэн давтагдах production scheduling загвар, байгаль орчны торгуулийг objective-д оруулсан — [Preprints.org](https://www.preprints.org/manuscript/202508.1151/v1) (кодын repo холбоосыг шалгаагүй; peer-review хийгдээгүй)
- Pirbalouti & Askari-Nasab (2023, MOL Alberta): minimum mining width-тэй pit design + scheduling MILP, Python Gurobipy дээр; том жишээнд max-flow ба эвристик — [UAlberta MOL PDF](https://sites.ualberta.ca/MOL/DataFiles/2023_Papers/103_Pirbalouti_Pit%20design%20considering%20minimum%20mining%20width.pdf)
- Askari-Nasab нар: том хэмжээний урт хугацааны MILP хуваарь (TOMLAB/CPLEX) — [Scholars' Mine](https://scholarsmine.mst.edu/min_nuceng_facwork/485)
- MineLib: UPIT, CPIT, PCPSP benchmark; AMPL notebook Gurobi 13.0.0 ашигласан — [AMPL Colab](https://colab.ampl.com/notebooks/minelib-in-ampl-and-amplpy.html)
- CAOS_PitForge-ийн «certified scheduling lane»: newman1.cpit-д LP bound-ийг 4×10⁻⁹ алдаатай давтаж, feasible хуваарь 3.81% gap — [GitHub](https://github.com/fsantibanezleal/CAOS_PitForge)
- OpenMines (2024, arXiv 2404.00622): **ачааны машины dispatch**-ийн симуляци, хуваарь биш — [arXiv](https://arxiv.org/html/2404.00622v1); repo github.com/370025263/openmines (шалгаагүй)
- Mining-Gym (QUT): Salabim + Gymnasium дээрх truck dispatch RL — [arXiv](https://arxiv.org/html/2503.19195v2)
- Mine_DigPlan: numpy массиваар 2D/3D уурхай — [GitHub](https://github.com/brownie5253/Mine_DigPlan)

### Inferences
- Агуулгагүй уурхайд хуваарийн гол хязгаар нь жилийн бүтээгдэхүүний тонн (захиалга), хөрс хуулалт, тоног төхөөрөмжийн цаг; NPV-ийн оронд «хөрс хуулалтыг тэгшлэх» эсвэл «хөрсний харьцааг багасгах» objective тохиромжтой — таамаг.
- Bench/polygon түвшинд (блок биш) нэгтгэвэл хувьсагч цөөрч, CBC/HiGHS-оор хурдан шийдэгдэнэ — таамаг.
- Нээлттэй solver-ууд: OR-Tools (Apache-2.0), HiGHS (MIT), CBC (EPL-2.0), PuLP (BSD), Pyomo (BSD) — бүгд [мэдлэг], энэ сешнд шалгаагүй.

### Gaps
- GitHub дээр «open pit scheduling OR-Tools» гэх засвартай repo олдсонгүй (хайлт ердөө нийтлэл буцаасан).
- Lotsu нарын 2025 preprint-ийн кодын байршил, лицензийг шалгаагүй.

## 5. Лицензийн хязгаарлалт (GPL vs MIT) — зөвлөх компанид

### Takeaway
MIT/BSD/Apache бүх хэрэглээнд чөлөөтэй. LGPL/EUPL/GPL нь зөвхөн программыг **гадагш түгээх** үед эх кодын үүрэг үүсгэнэ; дотоод хэрэглээнд бараг асуудалгүй. Хамгийн том эрсдэл: PyPI `pseudoflow` — **арилжааны бус** лиценз, тиймээс төлбөртэй зөвлөх ажилд ашиглаж болохгүй байх магадлал өндөр.

### Cited Findings
- MIT: MineFlow, PyMineFlow, gPit, PitForge, PyVista, trimesh, ezdxf, omf — [MineFlow](https://github.com/MineFlowCSM/MineFlow), [PyMineFlow](https://pypi.org/pypi/pymineflow/json), [gPit](https://github.com/GuilhermeMene/gPit), [PitForge](https://github.com/fsantibanezleal/CAOS_PitForge), [PyVista](https://pypi.org/pypi/pyvista/json), [trimesh](https://pypi.org/pypi/trimesh/json), [ezdxf](https://pypi.org/pypi/ezdxf/json), [omf](https://pypi.org/pypi/omf/json)
- BSD: omfvista — [PyPI](https://pypi.org/pypi/omfvista/json)
- LGPL-3.0+: geoh5py — [PyPI](https://pypi.org/pypi/geoh5py/json)
- EUPL-1.2: GemPy — [PyPI](https://pypi.org/pypi/gempy/json)
- Арилжааны бус: pseudoflow — [PyPI](https://pypi.org/pypi/pseudoflow/json)
- MineLib өгөгдөл: CC BY-SA 3.0 (PitForge-ийн LICENSES.md-д дурдсан) — [PitForge](https://github.com/fsantibanezleal/CAOS_PitForge)
- AMPL ба Gurobi нь арилжааны solver (AMPL notebook Gurobi 13.0.0 ашигласан) — [AMPL Colab](https://colab.ampl.com/notebooks/minelib-in-ampl-and-amplpy.html)

### Inferences
- gPit нь MIT боловч `pseudoflow`-оос хамаардаг тул бүхэлдээ арилжааны бус нөхцөл өвлөнө.
- Зөвлөмжит стек (таамаг): PyMineFlow (UPL) + PyVista/omfvista (блок, дүрслэл) + numpy/scipy/shapely (эзэлхүүн) + OR-Tools/HiGHS (хуваарь) + ezdxf (DWG-д хөрвүүлэх DXF) — бүгд permissive.

### Gaps
- Хуулийн дүгнэлт биш; Монгол Улсын эрх зүйн нөхцөлд лицензийн тайлбар шалгагдаагүй.
- PyGSLIB-ийн одоогийн лиценз тодорхойгүй.
