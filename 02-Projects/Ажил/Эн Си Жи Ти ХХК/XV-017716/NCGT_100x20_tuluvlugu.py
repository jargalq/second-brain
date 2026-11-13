# XV-017716 алтны шороон хуримтлалын 100×20 м хайгуулын цооногийн санал.
# Шугамыг GP-26020-оор дамжуулж az 135°-аар татна (2026 оны 7 цооног энэ шугам дээр бараг байна).
# Гаралт: csv, xlsx, dxf, pdf, png. Эх багцын файлыг өөрчлөхгүй.
import csv, glob, math, os, re, struct, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from pypdf import PdfReader

sys.path.insert(0, r"D:\Seond brain\_system\skills\zurag-shtamp")
from gv_stamp import draw_stamp

ROOT = r"D:\PARA\1-Projects\Great Vision project\077 NCGT"
OUT = os.path.dirname(os.path.abspath(__file__))
NAME = "XV-017716_100x20_tuluvlugu"
OX, OY = 354703.081, 5085364.816     # GP-26020
S = math.sqrt(0.5)
MAX_DEPTH = 30                       # м, 2026 оны алт 28.8 м хүртэл
AVG_DEPTH = 24.8                     # м, 2026 оны дундаж (620 м / 25)
EXIST_TOL = 12                       # м, үүнээс ойр зангилаанд цооног нэмэхгүй
EDGE = 10                            # м, лицензийн хилээс дотогш
PHASE = {1: "1-р ээлж", 2: "2-р ээлж", 3: "3-р ээлж (нөхцөлтэй)"}
COL = {1: "#c8102e", 2: "#e88a00", 3: "#1f5fa8"}


def to_xy(u, v):
    return OX + (u + v) * S, OY + (u - v) * S


def to_uv(x, y):
    dx, dy = x - OX, y - OY
    return (dx + dy) * S, (dx - dy) * S


def read_polys(path):
    b = open(path, "rb").read(); i = 100; out = []
    while i < len(b):
        _, ln = struct.unpack(">2i", b[i:i + 8])
        np_, npt = struct.unpack("<2i", b[i + 44:i + 52])
        s = i + 52 + 4 * np_
        v = struct.unpack("<%dd" % (2 * npt), b[s:s + 16 * npt])
        out.append([(v[j], v[j + 1]) for j in range(0, len(v), 2)])
        i += 8 + 2 * ln
    return out


def inside(p, poly):
    x, y = p; c = False
    for a, b in zip(poly, poly[1:]):
        if (a[1] > y) != (b[1] > y) and x < (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]:
            c = not c
    return c


def edge_dist(p, poly):
    best = 1e9
    for a, b in zip(poly, poly[1:]):
        t = max(0, min(1, ((p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])) / ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)))
        best = min(best, math.dist(p, (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))))
    return best


def utm47_to_ll(e, n):
    """WGS84 UTM 47N -> өргөрөг, уртраг (Крюгерийн цуваа)."""
    a, f, k0 = 6378137.0, 1 / 298.257223563, 0.9996
    m = f / (2 - f)
    A = a / (1 + m) * (1 + m ** 2 / 4 + m ** 4 / 64)
    be = [m / 2 - 2 * m ** 2 / 3 + 37 * m ** 3 / 96, m ** 2 / 48 + m ** 3 / 15, 17 * m ** 3 / 480]
    de = [2 * m - 2 * m ** 2 / 3 - 2 * m ** 3, 7 * m ** 2 / 3 - 8 * m ** 3 / 5, 56 * m ** 3 / 15]
    xi, eta = n / (k0 * A), (e - 500000) / (k0 * A)
    xi1, eta1 = xi, eta
    for j, b in enumerate(be, 1):
        xi1 -= b * math.sin(2 * j * xi) * math.cosh(2 * j * eta)
        eta1 -= b * math.cos(2 * j * xi) * math.sinh(2 * j * eta)
    chi = math.asin(math.sin(xi1) / math.cosh(eta1))
    lat = chi + sum(d * math.sin(2 * j * chi) for j, d in enumerate(de, 1))
    return math.degrees(lat), 99 + math.degrees(math.atan2(math.sinh(eta1), math.cos(xi1)))


lic = dict(zip(["15636", "17717", "17716", "20665"],
               read_polys(os.path.join(ROOT, "01 LICENCE AND BOUNDARIES", "License NCGT.shp"))))
base = os.path.join(ROOT, "03 DRILLING 2026 - XV-017716 ONLY")
with open(os.path.join(base, "collar_XV-017716.csv"), encoding="utf-8-sig") as fh:
    collars = {r["hole_id"]: (float(r["x"]), float(r["y"]), float(r["max_depth"])) for r in csv.DictReader(fh)}
au = {k: 0.0 for k in collars}
with open(os.path.join(base, "assay_XV-017716.csv"), encoding="utf-8-sig") as fh:
    for r in csv.DictReader(fh):
        au[r["hole_id"]] = max(au[r["hole_id"]], float(r["Au_mg_m3"]))

# Зангилаа: (блок, шугамын дугаар, u, v-ийн хүрээ, 0 дугаарын v)
LINES = [("T", i + 1, u, range(-320, 101, 20), 100) for i, u in enumerate(range(-200, 301, 100))]
LINES += [("Z", i + 1, u, range(440, 641, 20), 640) for i, u in enumerate(range(-200, 201, 100))]
LINES += [("H", 1, 0, range(120, 421, 20), 420)]
CORE_U = (-100, 0, 100)

plan, tied, clipped = [], [], 0
for blk, ln, u, vs, v0 in LINES:
    for v in vs:
        x, y = to_xy(u, v)
        if not inside((x, y), lic["17716"]) or edge_dist((x, y), lic["17716"]) < EDGE:
            clipped += 1
            continue
        near = [k for k, c in collars.items() if math.dist((x, y), c[:2]) < EXIST_TOL]
        if near:
            tied.append((blk, ln, v, near[0]))
            continue
        first = v % 40 == 0
        phase = 3 if not first else (1 if blk == "H" or u in CORE_U else 2)
        num = (v0 - v) // 10           # тайлангийн IV.1: урсгал уруу харж зүүн гараас, 10 м-т 1 дугаар
        lat, lon = utm47_to_ll(x, y)
        plan.append(dict(id="%s%d-%02d" % (blk, ln, num), blk=blk, line=ln, num=num, phase=phase,
                         x=round(x, 1), y=round(y, 1), lat=round(lat, 6), lon=round(lon, 6)))

# Шалгалт
assert len({p["id"] for p in plan}) == len(plan)
for p in plan:
    assert inside((p["x"], p["y"]), lic["17716"])
    assert not any(inside((p["x"], p["y"]), lic[k]) for k in ("15636", "17717", "20665"))
    assert min(math.dist((p["x"], p["y"]), c[:2]) for c in collars.values()) >= EXIST_TOL - 0.1
with open(os.path.join(ROOT, "01 LICENCE AND BOUNDARIES", "XV-017716 licence corners - WGS84.csv"), encoding="utf-8-sig") as fh:
    err = max(max(abs(a - b) for a, b in zip(utm47_to_ll(float(r["easting_UTM47N_m"]), float(r["northing_UTM47N_m"])),
                                             (float(r["latitude"]), float(r["longitude"])))) for r in csv.DictReader(fh))
assert err < 2e-5, err

count = {(b, f): sum(1 for p in plan if p["blk"] == b and p["phase"] == f) for b in "TZH" for f in (1, 2, 3)}
tot = {f: sum(count[b, f] for b in "TZH") for f in (1, 2, 3)}
print("clipped", clipped, "tied", tied)
print("counts", count, "tot", tot, "all", len(plan), "ll err", err)

# CSV
with open(os.path.join(OUT, NAME + ".csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["hole_id", "block", "line", "number", "phase", "x_UTM47N", "y_UTM47N", "latitude", "longitude", "max_depth_m"])
    for p in plan:
        w.writerow([p["id"], p["blk"], p["line"], p["num"], p["phase"], p["x"], p["y"], p["lat"], p["lon"], MAX_DEPTH])

# Excel
wb = Workbook(); ws = wb.active; ws.title = "Хураангуй"
hd = PatternFill("solid", fgColor="E6E6E6"); B = Font(bold=True)
d = wb.create_sheet("Цооног")
d.append(["Цооног", "Блок", "Шугам", "Дугаар", "Ээлж", "X (UTM 47N)", "Y (UTM 47N)", "Өргөрөг", "Уртраг", "Дээд гүн, м"])
for p in plan:
    d.append([p["id"], p["blk"], p["line"], p["num"], p["phase"], p["x"], p["y"], p["lat"], p["lon"], MAX_DEPTH])
for c in d[1]: c.font = B; c.fill = hd
d.freeze_panes = "A2"; d.auto_filter.ref = d.dimensions
for col, wd in zip("ABCDEFGHIJ", (10, 7, 7, 8, 7, 13, 13, 11, 11, 11)): d.column_dimensions[col].width = wd
e = wb.create_sheet("2026 холбох цооног")
e.append(["Торлолын зангилаа", "2026 оны цооног", "Au дээд, мг/м³", "Гүн, м"])
for blk, ln, v, k in tied:
    e.append(["%s%d, v=%d" % (blk, ln, v), k, round(au[k], 1), collars[k][2]])
for c in e[1]: c.font = B; c.fill = hd
for col, wd in zip("ABCD", (20, 16, 15, 8)): e.column_dimensions[col].width = wd

ws["A1"] = "XV-017716, 100×20 м хайгуулын цооногийн санал"; ws["A1"].font = Font(bold=True, size=13)
ws["A3"] = "Дээд гүн, м"; ws["B3"] = MAX_DEPTH
ws["A4"] = "Дундаж гүн, м (2026 оны бодит)"; ws["B4"] = AVG_DEPTH
for c in (ws["B3"], ws["B4"]): c.font = Font(color="0000FF")
ws.append([])
ws.append(["Ээлж", "T блок", "Z блок", "H холбох", "Нийт цооног", "Нийт, т/м (дундаж)", "Нийт, т/м (дээд)", "Ажил"])
for c in ws[6]: c.font = B; c.fill = hd; c.alignment = Alignment(wrap_text=True, vertical="center")
TXT = {1: "Гол шугамууд, 40 м алхам", 2: "Захын шугамууд, 40 м алхам", 3: "Алт илэрсэн хэсэгт 20 м болгож нягтруулах"}
for f in (1, 2, 3):
    r = 6 + f
    ws.append([PHASE[f]] + ['=COUNTIFS(Цооног!$B:$B,"%s",Цооног!$E:$E,%d)' % (b, f) for b in "TZH"] +
              ["=SUM(B%d:D%d)" % (r, r), "=E%d*$B$4" % r, "=E%d*$B$3" % r, TXT[f]])
ws.append(["Нийт"] + ["=SUM(%s7:%s9)" % (c, c) for c in "BCDEFG"])
for c in ws[10]: c.font = B
for r in ws.iter_rows(min_row=7, max_row=10, min_col=6, max_col=7):
    for c in r: c.number_format = "#,##0"
notes = [
    "Тайлбар",
    "T: GP-26007, 26013, 26015, 26020, 26022 орчим. Z: GP-26012, 26018, 26021 орчим. H: хоёр блокийг L0 шугамаар холбоно.",
    "Шугамын чиглэл az 135°, шугам хоорондын зай 100 м (az 45°-ын дагуу), цооног хоорондын эцсийн зай 20 м.",
    "Дугаарлалт: 2025 оны тайлангийн IV.1 — урсгал уруу харж зүүн гараас, 10 м-т 1 дугаар.",
    "Гүн: улаан хүрэн цул шаварт 2 м орсны дараа эсвэл 30 м-т зогсооно (саналын шалгуур, геологич батална).",
    "Өндөр (Z) ороогүй: газар дээр GPS-ээр хэмжинэ. Газрын байдал, зам, хамгаалалтын бүсийг шалгаагүй.",
]
for i, t in enumerate(notes):
    ws.cell(row=12 + i, column=1, value=t).font = B if i == 0 else Font()
for col, wd in zip("ABCDEFGH", (31, 8, 8, 9, 9, 11, 11, 42)): ws.column_dimensions[col].width = wd
wb.save(os.path.join(OUT, NAME + ".xlsx"))

# DXF (R12)
out = ["0", "SECTION", "2", "ENTITIES"]


def dx_line(a, b, layer):
    out.extend(["0", "LINE", "8", layer, "10", "%.2f" % a[0], "20", "%.2f" % a[1], "30", "0", "11", "%.2f" % b[0], "21", "%.2f" % b[1], "31", "0"])


def dx_pt(p, layer):
    out.extend(["0", "CIRCLE", "8", layer, "10", "%.2f" % p[0], "20", "%.2f" % p[1], "30", "0", "40", "2.5"])


def dx_text(p, s, layer, h=3):
    out.extend(["0", "TEXT", "8", layer, "10", "%.2f" % (p[0] + 3), "20", "%.2f" % p[1], "30", "0", "40", str(h), "1", s])


for k, poly in lic.items():
    for a, b in zip(poly, poly[1:]):
        dx_line(a, b, "LIC_" + k)
for p in plan:
    dx_pt((p["x"], p["y"]), "PLAN_P%d" % p["phase"]); dx_text((p["x"], p["y"]), p["id"], "PLAN_TEXT")
for k, c in collars.items():
    dx_pt(c[:2], "HOLE_2026"); dx_text(c[:2], k, "HOLE_2026")
for blk, ln, u, vs, v0 in LINES:
    dx_line(to_xy(u, vs[0]), to_xy(u, vs[-1]), "LINES")
out.extend(["0", "ENDSEC", "0", "EOF"])
with open(os.path.join(OUT, NAME + ".dxf"), "w", encoding="ascii", newline="\r\n") as fh:
    fh.write("\n".join(out) + "\n")

# Зураг
plt.rcParams["font.family"] = "Times New Roman"
PW, PH = 420.0, 297.0
fig = plt.figure(figsize=(PW / 25.4, PH / 25.4)); fig.canvas.draw()
fig.add_artist(Rectangle((5 / PW, 5 / PH), 410 / PW, 287 / PH, fill=False, lw=1.2, ec="k", transform=fig.transFigure))


def map_axes(x_mm, y_mm, w_mm, h_mm, xmin, ymin, scale):
    ax = fig.add_axes([x_mm / PW, y_mm / PH, w_mm / PW, h_mm / PH])
    ax.set_xlim(xmin, xmin + w_mm * scale / 1000); ax.set_ylim(ymin, ymin + h_mm * scale / 1000)
    ax.set_aspect("equal"); ax.tick_params(labelsize=7, length=2)
    ax.ticklabel_format(useOffset=False, style="plain")
    return ax


def draw_lic(ax):
    ax.add_patch(Polygon(lic["17716"], closed=True, fc="#eaf6ec", ec="#1a8a3a", lw=1.6, zorder=1))
    for k in ("15636", "17717", "20665"):
        ax.add_patch(Polygon(lic[k], closed=True, fc="#f1f1f1", ec="#6b6b6b", lw=0.8, ls="--", zorder=1))


ax = map_axes(14, 10, 212, 268, 354290, 5084620, 5000)
draw_lic(ax); ax.grid(True, color="#c9c9c9", lw=0.3)
ax.text(354390, 5085500, "MV-020665", fontsize=10, color="#6b6b6b", ha="center", rotation=90, zorder=2)
for blk, ln, u, vs, v0 in LINES:
    xs, ys = zip(*[to_xy(u, v) for v in vs if inside(to_xy(u, v), lic["17716"])])
    ax.plot(xs, ys, color="#999999", lw=0.5, zorder=2)
    if blk != "H":
        ax.annotate("%s%d" % (blk, ln), (xs[-1], ys[-1]), xytext=(6, 6), textcoords="offset points", fontsize=8.5, weight="bold", zorder=7)
for f, sz in ((3, 9), (2, 15), (1, 15)):
    pts = [p for p in plan if p["phase"] == f]
    ax.scatter([p["x"] for p in pts], [p["y"] for p in pts], s=sz, c=COL[f], lw=0, zorder=4)
for p in plan:
    if p["phase"] == 1:
        ax.annotate("%d" % p["num"], (p["x"], p["y"]), xytext=(0, 3), textcoords="offset points", fontsize=4.8, ha="center", color="#7a0a1c", zorder=5)
x0, x1, y0, y1 = ax.get_xlim()[0], ax.get_xlim()[1], ax.get_ylim()[0], ax.get_ylim()[1]
OFF = {"GP-26023": (-30, -9), "GP-26019": (6, -8), "GP-26013": (6, 5), "GP-26022": (-36, 5), "GP-26015": (6, -8), "GP-26020": (-34, 6),
       "GP-26021": (-34, 6), "GP-26012": (6, 3), "GP-26018": (6, -8), "GP-26007": (-38, 4)}
for k, c in collars.items():
    if x0 < c[0] < x1 and y0 < c[1] < y1:
        hit = au[k] > 0
        ax.scatter([c[0]], [c[1]], s=34, c="#ffd400" if hit else "white", edgecolors="k", lw=0.7, zorder=6)
        ax.annotate("%s (%.0f)" % (k.replace("GP-26", ""), au[k]), c[:2], xytext=OFF.get(k, (6, 4)), textcoords="offset points", fontsize=6.8, weight="bold", zorder=7,
                    bbox=dict(fc="white", ec="none", pad=0.4, alpha=0.75))
ax.text(354905, 5085160, "H холбох шугам\n(L0)", fontsize=7.5, color="#7a0a1c", zorder=7, ha="left")
ax.annotate("С", (0.96, 0.86), xycoords="axes fraction", ha="center", fontsize=11, weight="bold")
ax.annotate("", (0.96, 0.97), (0.96, 0.87), xycoords="axes fraction", arrowprops=dict(arrowstyle="-|>", color="k"))
ax.plot([354340, 354540], [5084680, 5084680], color="k", lw=2.5, zorder=7)
ax.text(354440, 5084692, "200 м", ha="center", fontsize=8, zorder=7)
fig.text(120 / PW, 281 / PH, "100×20 м хайгуулын цооногийн санал, 1:5 000", ha="center", fontsize=12, weight="bold")

ov = map_axes(236, 110, 65, 165, 352500, 5080900, 60000)
draw_lic(ov)
ov.scatter([c[0] for c in collars.values()], [c[1] for c in collars.values()], s=4, c="#555555", zorder=3)
ov.scatter([p["x"] for p in plan], [p["y"] for p in plan], s=2, c=COL[1], zorder=4)
xy25 = []
for f in glob.glob(os.path.join(ROOT, "08 DRILLING 2025*", "pic*.pdf")):
    m = re.search(r"X=(\d+)\s+Y=(\d+)", PdfReader(f).pages[0].extract_text())
    xy25.append((int(m.group(1)), int(m.group(2))))
assert len(xy25) == 19
ov.scatter([c[0] for c in xy25], [c[1] for c in xy25], s=9, marker="x", c="k", lw=0.7, zorder=4)
ov.text(354900, 5088950, "× 2025 оны цооног", fontsize=7, ha="center", zorder=5)
ov.text(354900, 5083000, "• 2026 оны цооног", fontsize=7, color="#555555", ha="center", zorder=5)
ov.add_patch(Rectangle((354290, 5084620), 1060, 1340, fill=False, ec="#1f5fa8", lw=1, zorder=5))
ov.set_xticks([353000, 355000]); ov.tick_params(labelsize=6)
for lab in ov.get_yticklabels(): lab.set_rotation(90); lab.set_va("center")
fig.text(268 / PW, 279 / PH, "Талбайн тойм, 1:60 000", ha="center", fontsize=9.5, weight="bold")

fig.text(308 / PW, 283 / PH, "Цооногийн тоо", fontsize=10, weight="bold", va="top")
tb = fig.add_axes([308 / PW, 232 / PH, 105 / PW, 45 / PH]); tb.axis("off")
cells = [[PHASE[f].split(" (")[0], count["T", f], count["Z", f], count["H", f], tot[f], "{:,.0f}".format(tot[f] * AVG_DEPTH), "{:,}".format(tot[f] * MAX_DEPTH)] for f in (1, 2, 3)]
all_n = sum(tot.values())
cells.append(["Нийт", sum(count["T", f] for f in tot), sum(count["Z", f] for f in tot), sum(count["H", f] for f in tot), all_n, "{:,.0f}".format(all_n * AVG_DEPTH), "{:,}".format(all_n * MAX_DEPTH)])
t = tb.table(cellText=cells, colLabels=["Ээлж", "T", "Z", "H", "Нийт", "т/м\n24.8 м", "т/м\n30 м"], loc="center", cellLoc="center",
             colWidths=[.26, .1, .1, .1, .12, .16, .16], bbox=[0, 0, 1, 1])
t.auto_set_font_size(False); t.set_fontsize(8)
for (i, j), c in t.get_celld().items():
    c.set_linewidth(0.3)
    if i == 0 or i == 4: c.set_text_props(weight="bold"); c.set_facecolor("#efefef")

fig.text(308 / PW, 227 / PH, "Тайлбар", fontsize=10, weight="bold", va="top")
lg = fig.add_axes([308 / PW, 188 / PH, 8 / PW, 32 / PH]); lg.axis("off"); lg.set_xlim(0, 1); lg.set_ylim(0, 5)
lg.scatter([.5] * 3, [4.5, 3.5, 2.5], s=[18, 18, 10], c=[COL[1], COL[2], COL[3]], lw=0)
lg.scatter([.5, .5], [1.5, .5], s=30, c=["#ffd400", "white"], edgecolors="k", lw=.7)
for i, s in enumerate(["1-р ээлж: гол шугам, 40 м алхам", "2-р ээлж: захын шугам, 40 м алхам", "3-р ээлж: алт илэрвэл 20 м болгож нягтруулна",
                       "2026 оны цооног, алт илэрсэн (мг/м³ дээд дээж)", "2026 оны цооног, алт илрээгүй эсвэл дээжгүй"]):
    fig.text(317 / PW, (216.8 - 6.4 * i) / PH, s, fontsize=8.2, va="center")
fig.text(308 / PW, 186 / PH,
         "Шугам az 135°, хоорондоо 100 м, цооног 20 м.\n"
         "T, Z дугаар нь шугамын дагуух дугаар (10 м-т 1).\n"
         "Хилээс 10 м дотогш, 2026 оны цооногоос 12 м-ээс\nойр зангилаанд цооног нэмээгүй.\n"
         "Гүн: улаан хүрэн цул шаварт 2 м орсны дараа\nэсвэл 30 м-т зогсооно (геологич батална).\n\n"
         "Хэсэг, шугамын чиглэл нь 2026 оны цооног,\nалтны утга, өндрийн налуугаар гаргасан санал.\n"
         "Газрын байдал, зам, урсгалыг газар дээр шалгаагүй.\n"
         "Эцсийн торлолыг шинжээчтэй тохирно.",
         fontsize=8.2, va="top", linespacing=1.3)

draw_stamp(fig, PW, PH, 415, 5, dict(
    client='"ЭН СИ ЖИ ТИ" ХХК',
    project='Говь-Алтай аймгийн Бигэр сумын нутагт\nорших XV-017716 тусгай зөвшөөрлийн\nталбайн алтны шороон хуримтлал',
    title='Хайгуулын цооногийн төлөвлөгөөний\nзураг (100×20 м), санал',
    paper="A3", scale="1:5000", total="1", number="1", license="XV-017716"))
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, NAME + "." + ext), dpi=200)

# Сансрын зурагтай тулгах шалгалт (дотоод)
try:
    from PIL import Image
    im = Image.open(os.path.join(ROOT, "04 DRILL PLAN AND MAPS", "GPPL_2026_drillplan_on_exploration_license_satellite.png")).convert("RGB")
    sx = (777 - 170) / (355500 - 353250); sy = (1257 - 45) / (5088750 - 5084250)
    f2, a2 = plt.subplots(figsize=(10, 10))
    x_lo, y_hi = 353250 - 170 / sx, 5088750 + 45 / sy
    a2.imshow(im, extent=(x_lo, x_lo + im.width / sx, y_hi - im.height / sy, y_hi), interpolation="lanczos")
    for f in (3, 2, 1):
        pts = [p for p in plan if p["phase"] == f]
        a2.scatter([p["x"] for p in pts], [p["y"] for p in pts], s=6, c=COL[f], lw=0)
    a2.set_xlim(354290, 355400); a2.set_ylim(5084620, 5085960)
    f2.savefig(sys.argv[1], dpi=110) if len(sys.argv) > 1 else None
except OSError as ex:
    print("satellite check skipped", ex)
