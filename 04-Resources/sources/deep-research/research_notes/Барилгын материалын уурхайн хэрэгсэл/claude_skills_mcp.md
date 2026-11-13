---
төрөл: судалгааны тэмдэглэл
төлөв: түүхий
tags: [deep-research, mcp, claude-skills, autocad, qgis, уурхай, аюулгүй-байдал]
огноо: 2026-11-12
---

# Уурхай, геологи, CAD, GIS-д зориулсан Claude skill, plugin, MCP server-ийн бүртгэл (2024–2026)

Тэмдэглэл: GitHub-ийн одны тоо, сүүлийн push огноог GitHub API-аас 2026-11-12-нд шууд татсан. Бусад зүйлийг README эсвэл каталогийн хуудаснаас авсан. Юу ч суулгаагүй, ажиллуулаагүй. «Таамаг» гэж тэмдэглэсэн зүйл баталгаажаагүй.

## 1. Уурхай, геологи, геотехник, хэмжилзүй, уурхайн төлөвлөлтөд тусгайлан зориулсан skill, plugin, MCP server бий юу?

### Takeaway
Ил уурхайн төлөвлөлт (pit design, блок загвар, олборлолтын график)-д зориулсан, боловсорсон нийтийн MCP server эсвэл Claude skill олдсонгүй. Хамгийн ойр нь Seequent-ийн албан ёсны Evo MCP (арилжааны Evo платформ шаарддаг), олон нийтийн geoscience-skills багц, туршилтын GeoAgent (GemPy) юм. Тэд геологийн загварчлалыг хамардаг ч pit design, ТЭЗҮ-ийн зурагт шууд хэрэглэгдэхгүй.

### Cited Findings
- **SeequentEvo/evo-mcp** — https://github.com/SeequentEvo/evo-mcp. Эзэмшигч нь Seequent (Bentley). Лиценз нь «Other/NOASSERTION» буюу стандарт SPDX биш. 12 одтой, 2026-02-02-нд үүсгэсэн, сүүлийн push 2026-10-19. Тайлбар нь: «AI хэрэгсэл ба Evo платформын хооронд аюулгүй интерфейс болох, өөрөө байршуулдаг server» — [GitHub API](https://api.github.com/repos/SeequentEvo/evo-mcp)
- Seequent-ийн нийгэмлэгийн нийтлэлд үүнийг жижиг, хөнгөн server гэж тодорхойлсон. Өөрийн дэд бүтцэд байршуулж, өгөгдлөө өөрийн орчинд хадгалах боломжтой гэжээ — [Seequent Community](https://community.seequent.com/discussion/3417/evo-mcp-model-context-protocol)
- Seequent-ийн блогт агентын демод Evo MCP-ээр kriging хийснийг дурдсан — [Seequent blog](https://www.seequent.com/from-hype-to-impact-seequents-perspective-on-mcp-vibe-coding-and-the-future-of-ai-in-geoscience/)
- Нэрийн төөрөгдөл: Snyk-ийн «Evo» (аюулгүй байдлын бүтээгдэхүүн) болон not-a-feature/evo2-mcp (геномын загвар) нь Seequent-тэй холбоогүй — [evo2-mcp](https://github.com/not-a-feature/evo2-mcp)
- **SteadfastAsArt/geoscience-skills** — https://github.com/SteadfastAsArt/geoscience-skills. MIT лицензтэй, 80 одтой, 2026-01-26-нд үүсгэсэн, сүүлийн push 2026-11-02. Claude Code, Cursor, Copilot-д зориулсан 30 skill: сейсмик, худгийн каротаж, 3D загварчлал, урвуу бодлого, геостатистик, NetCDF — [GitHub API](https://api.github.com/repos/SteadfastAsArt/geoscience-skills)
- **GeoAgent MCP Server** нь цооногийн өгөгдлийг шалгаж, хүний зөвшөөрлийн дараа GemPy-ээр далд 3D загвар үүсгэдэг. Тооцоог LLM биш, детерминист код хийдэг — [Glama](https://glama.ai/mcp/servers/zwhg8siuvm). GitHub URL, од, лицензийг шалгаж амжаагүй.
- **pyvista/pyvista-mcp-server** нь 3D дүрслэлийн server. Хамаарал нь `mcp[cli]>=1.6.0`, `pyvista[all]>=0.44.2` — [Glama pyproject](https://glama.ai/mcp/servers/@pyvista/pyvista-mcp-server/blob/392a1ce5eb0a8ab8f96ee39372f11a4414fb04f8/pyproject.toml)
- Бусад:
  - SGU MCP нь Шведийн геологийн албаны API-г ашигладаг тул Монголд хамааралгүй — [LobeHub](https://lobehub.com/mcp/furrytailapps-sgu-mcp)
  - openvds-mcp-server нь сейсмик эзлэхүүний өгөгдөлтэй ажилладаг — [GitHub](https://github.com/raghujayan/openvds-mcp-server)
  - pouliens «BGS mineral stats» MCP нь Их Британийн геологийн албаны ашигт малтмалын статистикийг өгдөг — [LobeHub](https://lobehub.com/ko/mcp/pouliens-mcp---bgs-mineral-stats)
- **MiningPy** нь MCP биш, уурхайн инженерийн Python сан (блок загварын хэрэгсэл). Ирээдүйд MCP-д ороож болох суурь болно — [PyPI](https://pypi.org/project/miningpy/0.6.1/)
- SKILL.md бүртгэлүүд (claudskills.com) дээр «mining-safety» (налуу тогтворжилт, ground control), «modeling-mining-project-economics» (CaseMark, Apache-2.0), «mining-maintenance» skill бий. Суулгах заавар нь `curl`-оор SKILL.md татах явдал — [mining-safety](https://claudskills.com/skills/mining-safety/SKILL.md), [economics](https://claudskills.com/skills/modeling-mining-project-economics/), [maintenance](https://claudskills.com/skills/mining-maintenance/)
- Soljourner/claude-engineering-skills нь механик, сансар, насосны инженерчлэлийг хамардаг, уурхай биш — [GitHub](https://github.com/Soljourner/claude-engineering-skills)

### Inferences
- Таамаг: Mugi-д аль хэдийн байгаа локал skill-үүд (`mine-planning`, `geo-section-plan`, `dairga`) нь олдсон гуравдагч талын бүх хэрэгслээс зорилгодоо илүү нийцтэй. Гадны зүйл нэмэхээс илүү эдгээрийг хөгжүүлэх нь зөв.
- Evo MCP нь Seequent Evo-ийн бүртгэл, лиценз шаарддаг, өгөгдлийг Evo cloud руу илгээдэг байх магадлалтай (таамаг). Барилгын материалын жижиг уурхайн ТЭЗҮ-д ач холбогдол багатай.
- geoscience-skills нь нефть, газ, сейсмикт чиглэсэн бололтой. Зөвхөн геостатистик (kriging, variogram) хэсэг нь блок загварт хэрэг болж магадгүй. Агуулгыг нь уншиж шалгах шаардлагатай.
- claudskills.com-ийн skill-үүд нэр нь үл мэдэгдэх зохиогчтой, curl-оор татагддаг. Доорх 4-р хэсгийн ToxicSkills судалгааны дагуу эрсдэл өндөр.

### Gaps
- Surpac, Vulcan, Deswik, Whittle, Datamine-ийн албан ёсны MCP server олдсонгүй. Тэдгээрийн вэндорын хуудсыг шууд шалгаагүй.
- GeoAgent-ийн GitHub репо, од, лиценз, сүүлийн commit баталгаажаагүй.
- Монгол хэл эсвэл Монголын стандартад (MNS, уурхайн дүрэм) зориулсан skill олдсонгүй.
- smithery.ai, mcp.so, албан ёсны MCP Registry-д «mining», «geology» гэж шууд хайгаагүй. Хайлтыг хэрэгслийн дуудлагын хязгаараас болж хязгаарласан.

## 2. AutoCAD, DXF, DWG-ийн MCP server эсвэл skill-ээс аль нь байгаа, аль нь арчлагдаж байна вэ?

### Takeaway
Хамгийн идэвхтэй, боловсорсон нь **puran-water/autocad-mcp**: 648 одтой, MIT лицензтэй, 2026-11-07-нд push хийсэн. AutoCAD LT дээр File IPC-ээр, эсвэл AutoCAD-гүйгээр ezdxf-ээр ажилладаг. Гэхдээ дурын AutoLISP ажиллуулах хэрэгсэлтэй. Бусад ихэнх AutoCAD MCP нь жижиг, нэг хүний туршилтын төсөл.

### Cited Findings
- **puran-water/autocad-mcp** — https://github.com/puran-water/autocad-mcp
  - Эзэмшигч нь байгууллага (Puran Water). MIT лицензтэй, 648 одтой, 2025-03-20-нд үүсгэсэн, сүүлийн push 2026-11-07. Архивлагдаагүй — [GitHub API](https://api.github.com/repos/puran-water/autocad-mcp)
  - Тайлбар нь: «AutoCAD LT v3.1: freehand AutoLISP execution, 8 consolidated tools, File IPC + ezdxf backends» — [GitHub API](https://api.github.com/repos/puran-water/autocad-mcp)
  - Хэрэгслүүд нь `drawing`, `entity`, `layer`, `block`, `annotation`, `pid`, `view`, `system`. `system`-ийн `execute_lisp` нь AutoCAD сешн дотор дурын AutoLISP код ажиллуулна (зөвхөн File IPC горимд) — [README](https://github.com/puran-water/autocad-mcp)
  - File IPC горим нь Windows, AutoCAD LT 2024+ шаарддаг. `PostMessageW(WM_CHAR)`-ээр команд илгээж, `C:/temp`-д IPC файл бичдэг. APPLOAD-аар `mcp_dispatch.lsp` ачаалах шаардлагатай. ezdxf горим нь AutoCAD-гүй, matplotlib-ээр дүрс гаргадаг. Суулгахдаа `uv sync` хийнэ — [README](https://github.com/puran-water/autocad-mcp)
  - README-д гадагш сүлжээний дуудлага баримтжуулаагүй. Холболт нь stdio, локал файл, AutoCAD цонх. GitHub-ийн Releases хоосон, `main` дээр 44 commit байна — [README](https://github.com/puran-water/autocad-mcp)
- **vigneshpbmenon/autocad-mcp-server** — https://github.com/vigneshpbmenon/autocad-mcp-server. MIT лицензтэй, Windows дээр ажиллаж буй AutoCAD шаарддаг, энгийн дүрс зурдаг «v0.1» — [Glama readme](https://glama.ai/mcp/servers/@vigneshpbmenon/autocad-mcp-server/blob/e7091ad32a8be68fdc36acfdd37d223c569a8dc9/readme.md)
- **ahmetcemkaraca/AutoCAD_MCP** нь AutoCAD 2025-д зориулагдсан. README нь BarryMcAdams/AutoCAD_MCP руу заадаг тул эх сурвалж нь тодорхойгүй — [GitHub](https://github.com/ahmetcemkaraca/AutoCAD_MCP)
- **Porta048/AutoCad-MCP** нь AutoCAD, GstarCAD, ZWCAD (Windows COM)-тэй ажилладаг — [Glama](https://glama.ai/mcp/servers/@Porta048/AutoCad-MCP/blob/0594df0bb8752f5ff0b915b4436c312fe71e314f/readme-eng.md)
- **U-C4N/Autocad-MCP («AutoCAD MCP Pro»)** нь COM болон ezdxf-ийн хослол. Headless горимд DXF үүсгэж, засаж, шалгадаг — [Glama](https://glama.ai/mcp/servers/U-C4N/Autocad-MCP)
- **Codemod3/CAD-MCP** нь DXF, DWG-г уншиж, шинжилж, засдаг. DWG-г ODA File Converter-ээр DXF болгодог — [Glama](https://glama.ai/mcp/servers/Codemod3/CAD-MCP). GitHub дээр MIT лицензтэй, 1 одтой. 2026-08-12-нд үүсгээд мөн өдөртөө сүүлийн push хийсэн, тайлбаргүй — [GitHub API](https://api.github.com/repos/Codemod3/CAD-MCP)
- **aiblueprint-mcp** (PyPI) нь ezdxf-ээр DXF үүсгэж, LibreCAD dxf2png-ээр урьдчилан харуулдаг — [PyPI](https://pypi.org/project/aiblueprint-mcp/)
- **ranvirw18/autocad-mcp-server** нь зөвхөн каталогт байгаа, GitHub-ийн эх хуудсыг баталгаажуулаагүй — [mcpservers.org](https://mcpservers.org/servers/ranvirw18/autocad-mcp-server.git)
- Зарим каталог `yourusername/autocad-mcp-server` гэх мэт placeholder URL хэрэглэдэг. Суулгахаас өмнө жинхэнэ репог шалгах хэрэгтэй — [WebSearch-ийн хураангуй, mcpservers.org/glama жагсаалт](https://glama.ai/mcp/servers/thepiruthvirajan/autocad-mcp-server)

### Inferences
- Mugi-ийн ТЭЗҮ-ийн DWG урсгалд хамгийн тохиромжтой гуравдагч талын сонголт нь puran-water/autocad-mcp. Гэхдээ ezdxf горимоор, `execute_lisp`-гүйгээр хэрэглэх нь зөв. Mugi бүтэн AutoCAD хэрэглэдэг эсэх нь тодорхойгүй, харин File IPC нь LT 2024+-д зориулагдсан (таамаг: бүтэн AutoCAD дээр ажиллах магадлалтай ч баталгаагүй).
- ezdxf-д суурилсан урсгал (Python → DXF) аль хэдийн `dairga` skill-д байгаа бол MCP нэмэх ашиг бага. Тусгай хэрэгцээ бол AutoCAD-ийн live screenshot, group үүсгэх.
- DWG-г шууд унших бүх зам гуравдагч хөрвүүлэгч (ODA File Converter эсвэл LibreDWG) шаарддаг. ODA нь хаалттай binary, LibreDWG нь GPL.
- 1 одтой, нэг өдрийн commit-тэй, тайлбаргүй Codemod3/CAD-MCP-г итгэлгүй гэж үзнэ.

### Gaps
- LibreDWG-д суурилсан MCP server тусдаа олдсонгүй.
- vigneshpbmenon, Porta048, U-C4N, ahmetcemkaraca репоны од, сүүлийн commit-ийг API-аар шалгаагүй.
- puran-water-ийн хамаарлын хувилбар хэр бэхлэгдсэнийг (uv.lock байгаа эсэх) шалгаагүй.

## 3. QGIS, GIS-ийн ямар MCP server байгаа, хэр боловсорсон бэ?

### Takeaway
**jjsantos01/qgis_mcp** хамгийн алдартай (1152 од) боловч лицензгүй, сүүлийн push нь 2025-10-01 (13 сар гаруйн өмнө). Зөвхөн QGIS 3.22 дээр туршсан, дурын PyQGIS код ажиллуулах `execute_code`-той. **mahdin75/gis-mcp** (205 од, MIT, 2026-08) нь QGIS-гүй, Python GIS сангууд дээр тулгуурласан, илүү шинэ хувилбар.

### Cited Findings
- **jjsantos01/qgis_mcp** — https://github.com/jjsantos01/qgis_mcp
  - 1152 одтой, лиценз нь null (лицензгүй), 2025-03-12-нд үүсгэсэн, сүүлийн push 2025-10-01 — [GitHub API](https://api.github.com/repos/jjsantos01/qgis_mcp)
  - QGIS plugin дотор socket server ажиллаж, MCP server тэр рүү холбогддог. BlenderMCP-д суурилсан. «QGIS 3.X (only tested on 3.22)», Python 3.12+ шаарддаг — [README](https://github.com/jjsantos01/qgis_mcp), [Glama pyproject](https://glama.ai/mcp/servers/@jjsantos01/qgis_mcp/blob/e37bf6f095e1658a8939cb7d8467c1e61d138bd2/pyproject.toml)
  - 15 хэрэгсэлтэй, үүнд `execute_processing`, `render_map`, `execute_code` («Execute arbitrary PyQGIS code») орно. README дэх цорын ганц анхааруулга нь «be very cautious». Нэвтрэлт, хандалтын хяналт, socket-ийн порт, binding-ийн талаар юу ч бичээгүй — [README](https://github.com/jjsantos01/qgis_mcp)
  - Гуравдагч талын дахин багцлалт: PyPI дээрх `mseep-qgis-mcp` албан ёсны биш. getdrio дээрх npx багц `@modelcontextprotocol/server-qgis-mcp-jjsantos01` баталгаажаагүй — [PyPI](https://pypi.org/project/mseep-qgis-mcp/0.1.0/), [getdrio](https://www.getdrio.com/mcp/qgis-mcp-jjsantos01)
  - Fork: kicker315/deepseek_qgis_mcp — [GitHub](https://github.com/kicker315/deepseek_qgis_mcp)
- **mahdin75/gis-mcp** — https://github.com/mahdin75/gis-mcp. MIT лицензтэй, 205 одтой, 2025-05-07-нд үүсгэсэн, сүүлийн push 2026-08-21. «GIS сангуудаар геоорон зайн үйлдэл, координатын хувиргалт хийдэг Python MCP server» — [GitHub API](https://api.github.com/repos/mahdin75/gis-mcp)
- **gmossy/geospatial_mcp_server_experiments** нь туршилтын төсөл: газрын гадаргын дүрслэл, дроны нислэгийн төлөвлөлт, Gradio, FastAPI — [Glama](https://glama.ai/mcp/servers/@gmossy/geospatial_mcp_server_experiments/tree/16aa12b088b5c5c74342522b321f425260782c16)

### Inferences
- qgis_mcp-ийн socket server нэвтрэлтгүй, порт, binding тодорхойгүй. Хэрэв 0.0.0.0-д холбогддог бол дотоод сүлжээнээс QGIS дотор дурын Python ажиллуулах боломж үүснэ (таамаг, кодыг шалгаагүй).
- Лицензгүй тул хууль ёсоор дахин түгээх, засах эрх тодорхойгүй.
- MGRS/UTM 48N–49N, Монголын MSK-тай координатын хувиргалт хийх бол gis-mcp (pyproj-д суурилсан байх магадлалтай, таамаг) нь QGIS-гүйгээр хангалттай байж магадгүй.

### Gaps
- qgis_mcp-ийн plugin кодноос socket-ийн binding (localhost эсвэл 0.0.0.0)-ийг шалгаагүй.
- gis-mcp-ийн хэрэгслийн жагсаалт, хамаарлыг уншаагүй.
- QGIS 3.34/3.40 LTR дээр qgis_mcp ажиллах эсэх тодорхойгүй.

## 4. Гуравдагч талын skill, MCP server суулгахад аюулгүй байдлын эх сурвалжууд ямар шалгуур зөвлөдөг вэ?

### Takeaway
Anthropic-ийн баримт бичигт: «Server бүрт итгэж байгаагаа шалга, гадны агуулга татдаг server нь prompt injection-д өртөмтгий», skill-ийн `allowed-tools` болон `!command` нь зөвшөөрөлгүйгээр ажиллаж болно гэж сануулсан. Бие даасан судалгаагаар (Snyk ToxicSkills 2026-02, Invariant Labs 2025-04) ил skill-үүдийн гуравны нэгээс илүүд аюулгүй байдлын асуудал илэрсэн, мөн MCP tool description-оор хортой заавар нэвтрүүлж болохыг баталсан.

### Cited Findings
- Claude Code MCP docs: «Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection risk.» Project-scoped `.mcp.json` server нь интерактив сешнд зөвшөөрөл асуудаг, харин `claude -p` болон Agent SDK-д асуудаггүй. Clone хийсэн репо өөрийн server-ээ өөрөө зөвшөөрч чадахгүй. Plugin идэвхжүүлэхэд түүний MCP server автоматаар асдаг бөгөөд ердийн server-тэй адил орчны хувьсагчид хандана — [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) (2026-11-12-нд уншсан)
- Claude Code skills docs: workspace trust нь `allowed-tools`-ыг хаадаггүй. «A skill can grant itself broad tool access, so review the allowed-tools...». Skill дэх `` !`command` `` нь Claude-ийн өмнө, зөвшөөрөлгүйгээр ажилладаг. Үүнийг `"disableSkillShellExecution": true` тохиргоогоор хааж болно — [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- Snyk ToxicSkills (2026-02-05 хүртэлх өгөгдөл): ClawHub, skills.sh-ийн 3984 skill-ийг шалгахад 1467 (36.82%) нь ядаж нэг асуудалтай, 534 (13.4%) нь ноцтой асуудалтай, 76 нь баталгаат хортой payload-той байв. Хортой skill-үүд ихэвчлэн shell script биш, байгалийн хэлний заавар дотор нуугддаг. Хортой skill-ийн 91%-д prompt injection ашигласан гэх тоог хоёрдогч эх сурвалж дурдсан — [Snyk blog](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), [DEV хураангуй](https://dev.to/ventureio/are-claude-skills-safe-in-2026-what-the-snyk-toxicskills-audit-actually-found-1315). Анхаар: эдгээр тоог Snyk-ийн эх хуудаснаас шууд шалгаагүй, хайлтын хураангуйгаас авсан.
- Зөрүүтэй тоо: Koi Security ClawHub-ийн 2857 skill-ээс 341 хортойг илрүүлсэн, Antiy 1184 гэж мэдээлсэн. Эдгээр нь өөр арга зүйтэй тул Snyk-ийн 76-тай нийлүүлж болохгүй — [DEV хураангуй](https://dev.to/ventureio/are-claude-skills-safe-in-2026-what-the-snyk-toxicskills-audit-actually-found-1315)
- Claude Code-ийн CVE (хоёрдогч эх сурвалжаас):
  - CVE-2025-59536 (CVSS 8.7) нь clone хийсэн репоны `.claude/settings.json`-оор команд ажиллуулах эмзэг байдал, 1.0.111-д засагдсан.
  - CVE-2026-21852 нь төслийн тохиргоогоор API түлхүүр алдагдах эмзэг байдал, 2.0.65-д засагдсан — [DEV хураангуй](https://dev.to/ventureio/are-claude-skills-safe-in-2026-what-the-snyk-toxicskills-audit-actually-found-1315)
- Invariant Labs (2025-04) «Tool Poisoning Attack»-ийг баримтжуулсан. MCP tool description дотор хэрэглэгчид харагдахгүй заавар нуух боломжтой. Демо дээр «тооны машин» хэрэгслээр SSH түлхүүр хулгайлсан, мөн нэг server нөгөө итгэмжлэгдсэн WhatsApp server-ийн мессежийн хүлээн авагчийг өөрчилсөн — [Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification) (хоёрдогч хураангуйгаар)
- «Rug pull» эрсдэл: зөвшөөрөгдсөн хэрэгсэл хожим зан төлөвөө өөрчилж болно, MCP-д шинэчлэлтийн дараа дахин зөвшөөрөл авах механизм байхгүй — [CSA whitepaper 2026-05](https://labs.cloudsecurityalliance.org/research-rb/csa-whitepaper-mcp-security-tool-poisoning-20260506-csa-styl/)
- CSA-ийн 2026-05-06-ны тайлан SKILL.md-ийг «agent context poisoning» буюу шинэ нийлүүлэлтийн гинжин хэлхээний халдлагын гадаргуу гэж үзсэн — [CSA briefing](https://labs.cloudsecurityalliance.org/research/briefing-csa-research-note-skill-md-agent-context-poisoning/)
- VentureBeat: skill scanner-ууд бүх шалгалтыг давсан ч тестийн файл дотор хортой код нуугдсан тохиолдлыг мэдээлсэн — [VentureBeat](https://venturebeat.com/ai/anthropic-skill-scanners-passed-every-check-malicious-code-test-file) (дэлгэрэнгүйг уншаагүй)

### Inferences
Дээрх эх сурвалжаас нэгтгэсэн практик шалгуурын жагсаалт (зөвлөмж, баримт биш):
1. Эх сурвалж: байгууллага эсвэл нэр хүндтэй зохиогч, 6 сараас дээш түүхтэй, олон хувь нэмэрлэгчтэй, сүүлийн commit 6 сарын дотор хийгдсэн байх. 1 одтой, нэг өдрийн репо бол татгалзана.
2. Лиценз: SPDX стандарт лицензтэй байх. qgis_mcp лицензгүй, evo-mcp NOASSERTION.
3. Дурын код ажиллуулах хэрэгсэл (`execute_lisp`, `execute_code`) байгаа эсэхийг шалгаж, `permissions.deny` эсвэл ask горимоор хязгаарлана.
4. Commit hash-аар бэхэлж суулгана (`git clone` + тодорхой SHA, `uv.lock`). `npx`, `uvx`-ийн хувилбаргүй, «latest» суулгалтаас зайлсхийнэ (rug pull-ийн эсрэг).
5. Сүлжээ: локал stdio server-ийг илүүд үзнэ. Socket server-ийн binding-ийг localhost болгоно.
6. SKILL.md, tool description-ыг бүтнээр нь уншина: `!command`, curl, base64, «ignore previous» гэх мэт заавар байгаа эсэхийг шалгана.
7. Итгэлгүй DWG, DXF, PDF, вэб агуулга нь Claude-д prompt injection-ийн эх болж болно. Энэ нь vault-ийн 8-р дүрэмтэй нийцнэ.
8. Албан ёсны бус дахин багцлалтаас (`mseep-*`, баталгаажаагүй npx багц) зайлсхийнэ.

### Gaps
- Trail of Bits-ийн MCP судалгааг хайж амжаагүй.
- Snyk болон Invariant-ийн эх хуудсыг шууд нээгээгүй. Тоонуудыг хайлтын хураангуй болон хоёрдогч эх сурвалжаас авсан тул эцсийн тайланд эх хуудаснаас шалгах шаардлагатай.
- Anthropic-ийн plugin баримт бичиг (code.claude.com/docs/en/plugins)-ийн аюулгүй байдлын хэсгийг уншаагүй.
- claude-plugins-official, anthropics/skills-д CAD, GIS, геологийн plugin байгаа эсэхийг шууд шалгаагүй. Хайлтын үр дүнд гараагүй тул байхгүй байх магадлалтай (таамаг).
