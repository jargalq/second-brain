# 2025 оны өрөмдлөгийн цооногийн бодит байршлыг XV-017716 талбайд буулгана.
# Эх өгөгдөл: 077 NCGT багц (логийн толгой, shapefile, 2026 оны collar). Эх файлыг өөрчлөхгүй.
import csv, glob, math, os, re, struct, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from pypdf import PdfReader

sys.path.insert(0, r"D:\Seond brain\_system\skills\zurag-shtamp")
from gv_stamp import draw_stamp

ROOT = r"D:\Great Vision project\077 NCGT"
OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams["font.family"] = "Times New Roman"
PW, PH = 420.0, 297.0
RED, GREY, GREEN, BLUE = "#c8102e", "#6b6b6b", "#1a8a3a", "#1f5fa8"


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
        au = [float(m) for m in re.findall(r"^H\d+ [\d.]+ [\d.]+ [\d.]+ ([\d.]+)\s*$", t, re.M)]
        x, y, z = map(int, re.search(r"X=(\d+)\s+Y=(\d+)\s+Z=(\d+)", t).groups())
        rows.append(dict(
            id=re.search(r"(ZK[AB]\d+-\d)", f).group(1), x=x, y=y, z=z,
            depth=float(re.search(r"Өрөмдсөн гүн: *([\d.]+)", t).group(1)),
            start=re.search(r"Нээсэн огноо: *([\d.]+)", t).group(1).rstrip("."),
            end=re.search(r"Хаасан огноо: *([\d.]+)", t).group(1).rstrip("."),
            au=max(au) * 1000 if au else None))
    return sorted(rows, key=lambda r: tuple(int(n) for n in r["start"].split(".")))


lic = dict(zip(["15636", "17717", "17716", "20665"],
               read_polys(os.path.join(ROOT, "01 LICENCE AND BOUNDARIES", "License NCGT.shp"))))
h25 = read_2025()
with open(os.path.join(ROOT, "03 DRILLING 2026 - XV-017716 ONLY", "collar_XV-017716.csv"), encoding="utf-8-sig") as fh:
    h26 = [(r["hole_id"], float(r["x"]), float(r["y"])) for r in csv.DictReader(fh)]
assert len(h25) == 19 and abs(sum(r["depth"] for r in h25) - 1108.5) < 0.01
assert all(inside((r["x"], r["y"]), lic["17716"]) for r in h25)
assert not any(inside((r["x"], r["y"]), lic[k]) for r in h25 for k in ("15636", "17717", "20665"))

fig = plt.figure(figsize=(PW / 25.4, PH / 25.4))
fig.canvas.draw()
fig.add_artist(Rectangle((5 / PW, 5 / PH), 410 / PW, 287 / PH, fill=False, lw=1.2, ec="k", transform=fig.transFigure))


def map_axes(x_mm, y_mm, w_mm, h_mm, xmin, ymin, scale):
    ax = fig.add_axes([x_mm / PW, y_mm / PH, w_mm / PW, h_mm / PH])
    ax.set_xlim(xmin, xmin + w_mm * scale / 1000); ax.set_ylim(ymin, ymin + h_mm * scale / 1000)
    ax.set_aspect("equal"); ax.tick_params(labelsize=7, length=2)
    ax.ticklabel_format(useOffset=False, style="plain")
    return ax


def draw_licences(ax, names=True):
    ax.add_patch(Polygon(lic["17716"], closed=True, fc="#eaf6ec", ec=GREEN, lw=1.6, zorder=1))
    for k in ("15636", "17717", "20665"):
        ax.add_patch(Polygon(lic[k], closed=True, fc="#f1f1f1", ec=GREY, lw=0.8, ls="--", zorder=1))


# Тойм зураг
ov = map_axes(13, 44, 106, 232, 352500, 5080900, 40000)
draw_licences(ov)
ov.scatter([r[1] for r in h26], [r[2] for r in h26], s=6, c=GREY, zorder=3)
ov.scatter([r["x"] for r in h25], [r["y"] for r in h25], s=9, c=RED, zorder=4)
ov.add_patch(Rectangle((352780, 5086700), 2870, 1920, fill=False, ec=BLUE, lw=1, zorder=5))
ov.text(354900, 5083300, "XV-017716", fontsize=11, weight="bold", color=GREEN, ha="center", zorder=6)
ov.text(353700, 5085900, "MV-020665", fontsize=8, color=GREY, ha="center", zorder=6)
ov.text(355000, 5088850, "Томруулсан хэсэг", fontsize=7.5, color=BLUE, ha="center", zorder=6)
ov.set_xticks(range(353000, 357000, 1000)); ov.tick_params(axis="x", labelrotation=0)
for lab in ov.get_yticklabels(): lab.set_rotation(90); lab.set_va("center")
fig.text(66 / PW, 280 / PH, "XV-017716 талбайн тойм, 1:40 000", ha="center", fontsize=10, weight="bold")
fig.text(13 / PW, 34 / PH,
         "Талбайн булангууд: багцын shapefile, WGS84 UTM 47N.\n"
         "Талбай 2 796 га (солбицлоор тооцов).\n"
         "2025 оны 19 цооног бүгд XV-017716 дотор.\n"
         "MV-020665, 17717, 15636 талбайд цооног ороогүй.",
         fontsize=8.5, va="top", linespacing=1.3)

# Томруулсан зураг
ax = map_axes(128, 100, 287 - 3, 186, 352780, 5086700, 10000)
draw_licences(ax)
ax.grid(True, color="#c9c9c9", lw=0.3)
ax.scatter([r[1] for r in h26], [r[2] for r in h26], s=20, c="white", edgecolors=GREY, lw=0.9, zorder=3)
xmax, ymax = ax.get_xlim()[1], ax.get_ylim()[1]
for hid, x, y in h26:
    if x < xmax and 5086700 < y < ymax:
        ax.annotate(hid.replace("GP-26", "GP"), (x, y), xytext=(4, -7), textcoords="offset points", fontsize=6.5, color=GREY, zorder=4)
ax.scatter([r["x"] for r in h25], [r["y"] for r in h25], s=42, c=RED, edgecolors="k", lw=0.4, zorder=5)
for r in h25:
    left = r["id"] == "ZKB14-1"  # зургийн баруун захад ойр
    ax.annotate(r["id"], (r["x"], r["y"]), xytext=(-5 if left else 5, 4), textcoords="offset points", ha="right" if left else "left",
                fontsize=8.5, weight="bold", color=RED, zorder=6)
ax.text(355300, 5088450, "XV-017716", fontsize=12, weight="bold", color=GREEN, zorder=6)
ax.text(353500, 5086725, "MV-020665", fontsize=9, color=GREY, ha="center", zorder=6)
ax.annotate("Баруун хил", (352888, 5088400), fontsize=7.5, color=GREEN, xytext=(5, 0), textcoords="offset points", zorder=6)
ax.annotate("С", (0.975, 0.86), xycoords="axes fraction", ha="center", fontsize=11, weight="bold")
ax.annotate("", (0.975, 0.97), (0.975, 0.87), xycoords="axes fraction", arrowprops=dict(arrowstyle="-|>", color="k"))
ax.plot([354900, 355400], [5086760, 5086760], color="k", lw=2.5, zorder=6)
ax.text(355150, 5086780, "500 м", ha="center", fontsize=8, zorder=6)
fig.text(271 / PW, 288 / PH, "2025 оны цооногийн бодит байршил, 1:10 000", ha="center", fontsize=12, weight="bold")

# Хүснэгт
tb = fig.add_axes([128 / PW, 7 / PH, 98 / PW, 85 / PH]); tb.axis("off")
head = ["Цооног", "Нээсэн", "Хаасан", "X", "Y", "Z", "Гүн, м", "Au, мг/м³"]
cells = [[r["id"], r["start"][5:], r["end"][5:], r["x"], r["y"], r["z"], "%.1f" % r["depth"],
          "%.0f" % r["au"] if r["au"] else "<10"] for r in h25]
cells.append(["Нийт 19", "", "", "", "", "", "%.1f" % sum(r["depth"] for r in h25), ""])
t = tb.table(cellText=cells, colLabels=head, loc="center", cellLoc="center",
             colWidths=[.15, .1, .1, .13, .15, .09, .11, .14], bbox=[0, 0, 1, 1])
t.auto_set_font_size(False); t.set_fontsize(6.8)
for (i, j), c in t.get_celld().items():
    c.set_linewidth(0.3)
    if i == 0 or i == len(cells): c.set_text_props(weight="bold"); c.set_facecolor("#efefef")

# Тайлбар
fig.text(231 / PW, 92 / PH, "Тайлбар", fontsize=9, weight="bold", va="top")
lg = fig.add_axes([231 / PW, 72 / PH, 22 / PW, 15 / PH]); lg.axis("off"); lg.set_xlim(0, 1); lg.set_ylim(0, 3)
lg.scatter([.5], [2.5], s=36, c=RED, edgecolors="k", lw=.4)
lg.scatter([.5], [1.5], s=18, c="white", edgecolors=GREY)
lg.add_patch(Rectangle((.2, .2), .6, .6, fc="#eaf6ec", ec=GREEN, lw=1.2))
fig.text(254 / PW, 84.8 / PH, "2025 оны цооног (19, 1 108.5 м, 5-р сарын 20-6-р сарын 21)", fontsize=8.5, va="center")
fig.text(254 / PW, 79.8 / PH, "2026 оны УКС цооног (25)", fontsize=8.5, va="center")
fig.text(254 / PW, 74.8 / PH, "XV-017716 тусгай зөвшөөрөл (тасархай: NCGT-ийн бусад талбай)", fontsize=8.5, va="center")
fig.text(231 / PW, 70 / PH, "Солбицол, огноо, гүн: 2025 оны логийн толгой, 1 м-ээр тоймлосон. Au: цооногийн хамгийн өндөр дээж.\nZKA логийн ихэнх дээжид утга «-», ZKB логийд «<0.01 г/м³». Логийн гарчгийн «Хуурай талбай» нь нэр,\nбайршлыг солбицлоор шалгав. Газар дээр хэмжээгүй.",
         fontsize=7.8, va="top", linespacing=1.25)

draw_stamp(fig, PW, PH, 415, 5, dict(
    client='"ЭН СИ ЖИ ТИ" ХХК',
    project='Говь-Алтай аймгийн Бигэр сумын нутагт\nорших XV-017716 тусгай зөвшөөрлийн\nталбайн алтны шороон хуримтлал',
    title='2025 оны өрөмдлөгийн цооногийн\nбодит байршлын зураг',
    paper="A3", scale="1:10000", total="1", number="1", license="XV-017716"))

for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, "XV-017716_2025_tsoonog_bairshil." + ext), dpi=200)
for r in h25:
    print(r)
