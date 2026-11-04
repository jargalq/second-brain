# XV-017716 дээр одоогоор өрөмдсөн бүх цооногийг (2025, 2026) нэг зурагт буулгана.
# Эх өгөгдөл: 077 NCGT багц (логийн толгой, 2026 оны CSV, төлөвлөгөөний xlsx, shapefile). Эх файлыг өөрчлөхгүй.
import collections, csv, glob, json, math, os, re, struct, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, Polygon
import openpyxl
from pypdf import PdfReader

sys.path.insert(0, r"D:\Seond brain\_system\skills\zurag-shtamp")
from gv_stamp import draw_stamp

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"D:\Great Vision project\077 NCGT"
D26 = os.path.join(ROOT, "03 DRILLING 2026 - XV-017716 ONLY")
OUT = os.path.dirname(os.path.abspath(__file__))
NAME = "XV-017716_urumdsun_baidal"
plt.rcParams["font.family"] = "Times New Roman"
PW, PH = 420.0, 297.0
GREY, GREEN, BLUE = "#6b6b6b", "#1a8a3a", "#1f5fa8"
BINS = [(100, "#c8102e", "100-аас дээш"), (10, "#e8871a", "10-100"), (0.0001, "#f2c81e", "10-аас доош"), (-1, "#ffffff", "Тоон алтгүй (0, <10 эсвэл үр дүнгүй)")]


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


def read_2025():
    rows = []
    for f in glob.glob(os.path.join(ROOT, "08 DRILLING 2025*", "pic*.pdf")):
        t = PdfReader(f).pages[0].extract_text()
        raw = re.findall(r"^H\d+ ([\d.]+) ([\d.]+) [\d.]+ (\S+)\s*$", t, re.M)  # утга: тоо, «<0.01» эсвэл «-»
        smp = [(float(a), float(b), 0, float(v)) for a, b, v in raw if re.fullmatch(r"[\d.]+", v)]
        lt = sum(1 for _, _, v in raw if v.startswith("<"))
        x, y, z = map(int, re.search(r"X=(\d+)\s+Y=(\d+)\s+Z=(\d+)", t).groups())
        pos = [s for s in smp if s[3] > 0]
        top = max(pos, key=lambda s: s[3]) if pos else None
        rows.append(dict(
            year=2025, id=re.search(r"(ZK[AB]\d+-\d)", f).group(1), x=x, y=y, z=z,
            depth=float(re.search(r"Өрөмдсөн гүн: *([\d.]+)", t).group(1)),
            start=re.search(r"Нээсэн огноо: *([\d.]+)", t).group(1).rstrip("."),
            end=re.search(r"Хаасан огноо: *([\d.]+)", t).group(1).rstrip("."),
            n=len(smp) + lt, lt=lt, au=top[3] * 1000 if top else None, au_from=top[0] if top else None, au_to=top[1] if top else None,
            deepest=max(s[1] for s in pos) if pos else None, end_rock=""))
    return sorted(rows, key=lambda r: tuple(int(n) for n in r["start"].split(".")))


def read_2026():
    def load(n):
        with open(os.path.join(D26, n + "_XV-017716.csv"), encoding="utf-8-sig") as fh:
            return list(csv.DictReader(fh))
    assay = collections.defaultdict(list)
    for r in load("assay"):
        assay[r["hole_id"]].append((float(r["depth_from"]), float(r["depth_to"]), float(r["Au_mg_m3"] or 0)))
    last = {}
    for r in load("lithology"):
        if r["hole_id"] not in last or float(r["depth_to"]) > float(last[r["hole_id"]]["depth_to"]):
            last[r["hole_id"]] = r
    rows = []
    for c in load("collar"):
        s = assay.get(c["hole_id"], [])
        pos = [v for v in s if v[2] > 0]
        top = max(pos, key=lambda v: v[2]) if pos else None
        rows.append(dict(
            year=2026, id=c["hole_id"], x=float(c["x"]), y=float(c["y"]), z=float(c["z"]),
            depth=float(c["max_depth"]), start="", end="", n=len(s), au=top[2] if top else None,
            au_from=top[0] if top else None, au_to=top[1] if top else None,
            deepest=max(v[1] for v in pos) if pos else None, end_rock=last[c["hole_id"]]["rock"]))
    return rows


def read_plan():
    ws = openpyxl.load_workbook(os.path.join(ROOT, "04 DRILL PLAN AND MAPS", "2026_high_piority_drill_plan_on_exploration_license.xlsx"), data_only=True).active
    return [dict(x=r[0], y=r[1], id=r[2], pri=str(r[6])) for r in list(ws.iter_rows(values_only=True))[1:] if r[0]]


lic = dict(zip(["15636", "17717", "17716", "20665"],
               read_polys(os.path.join(ROOT, "01 LICENCE AND BOUNDARIES", "License NCGT.shp"))))
h25, h26, plan = read_2025(), read_2026(), read_plan()
assert len(h25) == 19 and abs(sum(r["depth"] for r in h25) - 1108.5) < 0.01
assert len(h26) == 25 and abs(sum(r["depth"] for r in h26) - 620) < 0.01
assert sum(r["n"] for r in h26) == 95

# Төлөвлөгөөтэй тулгах: 30 м дотор байвал гүйцэтгэсэн гэж тооцно (дугаар нь таарахгүй тул зөвхөн байршлаар)
for p in plan:
    p["near"] = min(h26, key=lambda h: math.hypot(h["x"] - p["x"], h["y"] - p["y"]))
    p["dist"] = math.hypot(p["near"]["x"] - p["x"], p["near"]["y"] - p["y"])
    p["done"] = p["dist"] <= 30
undrilled = [p for p in plan if not p["done"]]
off_plan = [h for h in h26 if not any(p["done"] and math.hypot(p["x"] - h["x"], p["y"] - h["y"]) <= 30 for p in plan)]
short = [h for h in h26 if h["depth"] < 30]
outside = [h["id"] for h in h25 + h26 if not inside((h["x"], h["y"]), lic["17716"])]


def colour(r):
    a = r["au"] if r["au"] is not None else -1
    return next(c for lim, c, _ in BINS if a >= lim)


fig = plt.figure(figsize=(PW / 25.4, PH / 25.4))
fig.canvas.draw()
fig.add_artist(Rectangle((5 / PW, 5 / PH), 410 / PW, 287 / PH, fill=False, lw=1.2, ec="k", transform=fig.transFigure))


def map_axes(x_mm, y_mm, w_mm, h_mm, xmin, ymin, scale):
    ax = fig.add_axes([x_mm / PW, y_mm / PH, w_mm / PW, h_mm / PH])
    ax.set_xlim(xmin, xmin + w_mm * scale / 1000); ax.set_ylim(ymin, ymin + h_mm * scale / 1000)
    ax.set_aspect("equal"); ax.tick_params(labelsize=6.5, length=2)
    ax.ticklabel_format(useOffset=False, style="plain")
    return ax


def draw_licences(ax):
    ax.add_patch(Polygon(lic["17716"], closed=True, fc="#eaf6ec", ec=GREEN, lw=1.5, zorder=1))
    for k in ("15636", "17717", "20665"):
        ax.add_patch(Polygon(lic[k], closed=True, fc="#f1f1f1", ec=GREY, lw=0.7, ls="--", zorder=1))


def draw_holes(ax, s25, s26, s_plan):
    ax.scatter([p["x"] for p in undrilled], [p["y"] for p in undrilled], s=s_plan, marker="x", c=BLUE, lw=0.8, zorder=2)
    ax.scatter([r["x"] for r in h26], [r["y"] for r in h26], s=s26, marker="o", c=[colour(r) for r in h26], edgecolors="k", lw=0.5, zorder=4)
    ax.scatter([r["x"] for r in h25], [r["y"] for r in h25], s=s25, marker="^", c=[colour(r) for r in h25], edgecolors="k", lw=0.5, zorder=4)


# Тойм зураг
ov = map_axes(13, 44, 100, 240, 352500, 5080600, 40000)
draw_licences(ov); draw_holes(ov, 10, 10, 10)
ov.add_patch(Rectangle((352800, 5084140), 3240, 4400, fill=False, ec=BLUE, lw=1, zorder=5))
ov.text(355000, 5082600, "XV-017716", fontsize=11, weight="bold", color=GREEN, ha="center", zorder=6)
ov.text(354200, 5082000, "Өрөмдөөгүй хэсэг", fontsize=8, color=GREEN, ha="center", zorder=6)
ov.text(355400, 5088800, "Томруулсан хэсэг", fontsize=7.5, color=BLUE, ha="center", zorder=6)
ov.set_xticks(range(353000, 357000, 1000))
for lab in ov.get_yticklabels(): lab.set_rotation(90); lab.set_va("center")
fig.text(63 / PW, 286 / PH, "XV-017716 талбайн тойм, 1:40 000", ha="center", fontsize=9.5, weight="bold")

# Томруулсан зураг
ax = map_axes(120, 67, 162, 220, 352800, 5084140, 20000)
draw_licences(ax); ax.grid(True, color="#c9c9c9", lw=0.3); draw_holes(ax, 34, 26, 18)
OFF = {"GP-26013": (-4, 5, "right"), "GP-26007": (6, 3, "left"), "GP-26019": (6, -6, "left"), "GP-26022": (-5, 2, "right"),
       "GP-26023": (-5, -7, "right"), "GP-26020": (-5, 4, "right"), "GP-26015": (5, -6, "left"), "GP-26021": (-5, 4, "right"),
       "GP-26012": (6, 3, "left"), "GP-26018": (6, -7, "left"), "GP-26017": (-5, 2, "right"), "GP-26017a": (5, 2, "left"), "GP-26024": (-5, 3, "right"), "GP-26005": (0, -10, "center")}
for r in h26:
    dx, dy, ha = OFF.get(r["id"], (5, 3, "left"))
    ax.annotate(r["id"].replace("GP-", ""), (r["x"], r["y"]), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=6.5, zorder=6)
OFF25 = {"ZKB12-1": (5, -7, "left"), "ZKB28-1": (5, -5, "left")}
for r in h25:
    dx, dy, ha = OFF25.get(r["id"], (5, 3, "left"))
    ax.annotate(r["id"], (r["x"], r["y"]), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=6.5, weight="bold", zorder=6)
ax.annotate("Х", (0.965, 0.90), xycoords="axes fraction", ha="center", fontsize=10, weight="bold")
ax.annotate("", (0.965, 0.98), (0.965, 0.91), xycoords="axes fraction", arrowprops=dict(arrowstyle="-|>", color="k"))
ax.plot([354900, 355400], [5084190, 5084190], color="k", lw=2.5, zorder=6)
ax.text(355150, 5084215, "500 м", ha="center", fontsize=7.5, zorder=6)
ax.text(353700, 5085900, "MV-020665", fontsize=9, color=GREY, ha="center", zorder=6)
fig.text(201 / PW, 288 / PH, "Өрөмдсөн цооногийн байршил, 1:20 000", ha="center", va="bottom", fontsize=10.5, weight="bold")

# Хүснэгт
tb = fig.add_axes([285 / PW, 62 / PH, 128 / PW, 226 / PH]); tb.axis("off")
head = ["Цооног", "X", "Y", "Гүн, м", "Үр дүн", "Au, мг/м³", "Интервал, м", "Алтны доод, м"]


def fmt(r):
    return [r["id"], "%.0f" % r["x"], "%.0f" % r["y"], "%.1f" % r["depth"], str(r["n"]) if r["n"] else "-",
            "%.1f" % r["au"] if r["au"] else ("<10" if r.get("lt") else ("0" if r["n"] else "-")),
            "%.1f-%.1f" % (r["au_from"], r["au_to"]) if r["au"] else "", "%.1f" % r["deepest"] if r["deepest"] else ""]


cells = [fmt(r) for r in h26] + [["2026: 25", "", "", "620.0", "95", "", "", ""]] + \
        [fmt(r) for r in h25] + [["2025: 19", "", "", "1108.5", str(sum(r["n"] for r in h25)), "", "", ""]]
t = tb.table(cellText=cells, colLabels=head, loc="center", cellLoc="center",
             colWidths=[.16, .12, .14, .09, .08, .11, .15, .15], bbox=[0, 0, 1, 1])
t.auto_set_font_size(False); t.set_fontsize(6.2)
for (i, j), c in t.get_celld().items():
    c.set_linewidth(0.3)
    if i == 0 or cells[i - 1][0].startswith("20") and ":" in cells[i - 1][0]:
        c.set_text_props(weight="bold"); c.set_facecolor("#efefef")

# Тайлбар
fig.text(120 / PW, 58 / PH, "Тайлбар", fontsize=9, weight="bold", va="top")
hs = [Line2D([], [], marker="^", ls="", mfc="w", mec="k", ms=6, label="2025 оны цооног (19)"),
      Line2D([], [], marker="o", ls="", mfc="w", mec="k", ms=5.5, label="2026 оны УКС цооног (25)"),
      Line2D([], [], marker="x", ls="", mec=BLUE, ms=5, label="2026 оны төлөвлөгөөт, өрөмдөөгүй (%d)" % len(undrilled))]
hs += [Line2D([], [], marker="s", ls="", mfc=c, mec="k", ms=5.5, label=("Au " + l + " мг/м³") if lim >= 0 else l) for lim, c, l in BINS]
fig.legend(handles=hs, loc="upper left", bbox_to_anchor=(120 / PW, 55 / PH), ncol=1, fontsize=7.3, frameon=False,
           labelspacing=0.28, handletextpad=0.4, borderaxespad=0, borderpad=0)
fig.text(13 / PW, 41 / PH,
         "Эх сурвалж: NCGT-ийн 2026 оны 10-р сарын багц (assay файл 10-р сарын 29).\n"
         "Солбицол: 2025 логийн толгой, 2026 collar файл, WGS84 UTM 47N.\n"
         "Au: цооногийн хамгийн өндөр дээж. 2026 онд 95 дээж (38 м) л үр дүнтэй.\n"
         "2026 гүйцэтгэгчийн эцсийн тайлан гараагүй. Газар дээр хэмжээгүй.",
         fontsize=7.5, va="top", linespacing=1.3)

draw_stamp(fig, PW, PH, 415, 5, dict(
    client='"ЭН СИ ЖИ ТИ" ХХК',
    project='Говь-Алтай аймгийн Бигэр сумын нутагт\nорших XV-017716 тусгай зөвшөөрлийн\nталбайн алтны шороон хуримтлал',
    title='Өрөмдсөн цооногийн байршил\n(2025, 2026 он), одоогийн байдлаар',
    paper="A3", scale="1:20000", total="1", number="1", license="XV-017716"))

for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, NAME + "." + ext), dpi=200)

# Excel
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Цооног"
ws.append(["Он", "Цооног", "X (UTM47N)", "Y (UTM47N)", "Z", "Гүн, м", "Үр дүнтэй дээж", "Au дээд, мг/м³", "Интервал эхлэх, м", "Интервал дуусах, м", "Хамгийн гүн алт, м", "Сүүлийн лито", "Нээсэн", "Хаасан"])
for r in h25 + h26:
    ws.append([r["year"], r["id"], r["x"], r["y"], r["z"], r["depth"], r["n"], r["au"], r["au_from"], r["au_to"], r["deepest"], r["end_rock"], r["start"], r["end"]])
ws2 = wb.create_sheet("Төлөвлөгөө ба гүйцэтгэл")
ws2.append(["Төлөвлөсөн дугаар", "X", "Y", "Зэрэглэл", "Хамгийн ойр цооног", "Зай, м", "Гүйцэтгэл (30 м дотор)"])
for p in plan:
    ws2.append([p["id"], p["x"], p["y"], p["pri"], p["near"]["id"], round(p["dist"], 1), "Өрөмдсөн" if p["done"] else "Өрөмдөөгүй"])
wb.save(os.path.join(OUT, NAME + ".xlsx"))

summary = dict(
    outside=outside, plan=len(plan), done=[(p["id"], p["near"]["id"], round(p["dist"], 1)) for p in plan if p["done"]],
    undrilled=[(p["id"], p["pri"], round(p["dist"])) for p in undrilled], off_plan=[h["id"] for h in off_plan],
    short=[(h["id"], h["depth"]) for h in short], n25=sum(r["n"] for r in h25),
    gold25=sum(1 for r in h25 if r["au"]), gold26=sum(1 for r in h26 if r["au"]),
    ymin=min(r["y"] for r in h25 + h26), ymax=max(r["y"] for r in h25 + h26), rows=[fmt(r) for r in h26 + h25])
print(json.dumps(summary, ensure_ascii=False, indent=0))
