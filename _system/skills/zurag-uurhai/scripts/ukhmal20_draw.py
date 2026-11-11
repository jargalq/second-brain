"""20 м-т дээж авах ухмал — 2 хуудас A3 (инфографик хэв маяг):
  1) План М 1:500 + ажлын хэмжээ, өдөр, зардал
  2) Хөндлөн огтлол А-А М 1:200 + дээжний нүх, техник
Геометр: ukhmal15_geom.py, тооцоо: ukhmal20_calc.py. Гаралт: PDF (2 хуудас) + PNG."""
import os as _os
VAULT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))  # vault-ийн үндэс, аль ч компьютерт
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle
from matplotlib.colors import LightSource, LinearSegmentedColormap
from matplotlib.backends.backend_pdf import PdfPages

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, _os.path.join(VAULT, "_system", "skills", "zurag-shtamp"))
import ukhmal15_geom as G
import ukhmal20_calc as C
from gv_stamp import draw_stamp

OUTDIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "_out")
os.makedirs(OUTDIR, exist_ok=True)
plt.rcParams["font.family"] = ["Arial", "DejaVu Sans"]
NAVY, YEL, RED, BLUE, GREEN = "#13306b", "#ffd21f", "#d7261e", "#2a6fdb", "#2e9e44"
PW, PH = 420.0, 297.0
fmt = lambda v: f"{v:,.0f}".replace(",", " ")

R = C.calc()
G.DEPTH = 15.0; G.GRADE = 0.12; G.BERM = 2.0; G.SWITCH = 0.0
X, Y, D = G.surface("spiral", ext=40)
ramp = G.ramp_samples("spiral")
crest = (X[D > 0.02].min(), X[D > 0.02].max(), Y[D > 0.02].min(), Y[D > 0.02].max())
HOLE_TOP, HOLE_BOT, HOLE_C = R["hole_top"], 3.0, (0.0, 0.6)
DX0, DX1, DY0, DY1, DH = 37.0, 113.0, -27.0, 21.0, 10.0
def frustum(b, w, h, m=1.5):
    return h / 6 * (b * w + (b - 2 * m * h) * (w - 2 * m * h) + 4 * (b - m * h) * (w - m * h))
Vdump = frustum(DX1 - DX0, DY1 - DY0, DH)
print("V", round(R["V"]), "loose", round(R["loose"]), "dump", round(Vdump), "crest", np.round(crest, 1))

STAMP = dict(client="«ВАЙ ЭЙЧ ГРАФИТ\nНЭЧҮРАЛ» ХХК",
             project="Сүүж уулын бал чулууны орд:\n20 м гүнд дээж авах ухмалын\nзохион байгуулалт (15 м шатлалтай\nухмал + 5 м дээжний нүх)",
             paper="A3", total="2", license="MV-018976")


def new_sheet(title_y, title_w, scale_txt):
    fig = plt.figure(figsize=(PW / 25.4, PH / 25.4), dpi=200)
    fig.patch.set_facecolor("white")
    bg = fig.add_axes([0, 0, 1, 1]); bg.set_xlim(0, PW); bg.set_ylim(0, PH); bg.axis("off")
    bg.add_patch(Rectangle((20, 5), PW - 25, PH - 10, fill=False, lw=1.2, ec="k"))
    bg.add_patch(FancyBboxPatch((24, 279), 388, 14, boxstyle="round,pad=0,rounding_size=3", fc=NAVY, ec=YEL, lw=1.5))
    bg.text(30, 286, title_y, color=YEL, fontsize=19, fontweight="bold", va="center")
    bg.text(30 + 9 * len(title_y) * 0.62 + 4, 286, title_w, color="white", fontsize=17, fontweight="bold", va="center")
    bg.text(406, 286, scale_txt, color="white", fontsize=12, fontweight="bold", va="center", ha="right")
    return fig, bg


def box(bg, x, y, w, h, title=None, fc="white", tsize=11, ec=NAVY):
    bg.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=2.2", fc=fc, ec=ec, lw=1.6, zorder=1))
    if title:
        bg.add_patch(FancyBboxPatch((x, y + h - 8), w, 8, boxstyle="round,pad=0,rounding_size=2.2", fc=ec, ec=ec, lw=1.6, zorder=2))
        bg.add_patch(Rectangle((x, y + h - 8), w, 3, fc=ec, ec="none", zorder=2))
        bg.text(x + 3, y + h - 4, title, color="white", fontsize=tsize, fontweight="bold", va="center", ha="left", zorder=3)


# ---------- техникийн дүрс ----------
def truck_plan(ax, x, y, ang, z=7):
    ca, sa = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    T = lambda pts: [(x + px * ca - py * sa, y + px * sa + py * ca) for px, py in pts]
    ax.add_patch(Polygon(T([(0, -1.25), (6.6, -1.25), (6.6, 1.25), (0, 1.25)]), fc="#f2b705", ec="k", lw=0.7, zorder=z))
    ax.add_patch(Polygon(T([(0.4, -0.9), (6.2, -0.9), (6.2, 0.9), (0.4, 0.9)]), fc="#a07b45", ec="#5b4220", lw=0.4, zorder=z))
    ax.add_patch(Polygon(T([(7.0, -1.25), (9.5, -1.25), (9.5, 1.25), (7.0, 1.25)]), fc="#f2b705", ec="k", lw=0.7, zorder=z))
    ax.add_patch(Polygon(T([(8.6, -1.1), (9.3, -1.1), (9.3, 1.1), (8.6, 1.1)]), fc="#2b3a4a", ec="none", zorder=z))


def exc_plan(ax, x, y, ang, sw, z=7):
    ca, sa = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    def T(pts, c=ca, s=sa): return [(x + px * c - py * s, y + px * s + py * c) for px, py in pts]
    for s in (-1, 1):
        ax.add_patch(Polygon(T([(-2.7, s * 1.7 - 0.45), (2.7, s * 1.7 - 0.45), (2.7, s * 1.7 + 0.45), (-2.7, s * 1.7 + 0.45)]), fc="#333", ec="k", lw=0.5, zorder=z))
    cb, sb = np.cos(np.radians(sw)), np.sin(np.radians(sw))
    ax.add_patch(Polygon(T([(-2.4, -1.6), (1.4, -1.6), (1.4, 1.6), (-2.4, 1.6)], cb, sb), fc="#f2b705", ec="k", lw=0.7, zorder=z + 0.1))
    ax.add_patch(Polygon(T([(-0.2, 0.3), (1.4, 0.3), (1.4, 1.5), (-0.2, 1.5)], cb, sb), fc="#2b3a4a", ec="k", lw=0.4, zorder=z + 0.2))
    ax.add_patch(Polygon(T([(1.2, -0.45), (7.6, -0.3), (7.6, 0.3), (1.2, 0.45)], cb, sb), fc="#f2b705", ec="k", lw=0.6, zorder=z + 0.2))
    ax.add_patch(Polygon(T([(7.4, -0.9), (8.8, -0.9), (8.8, 0.9), (7.4, 0.9)], cb, sb), fc="#555", ec="k", lw=0.5, zorder=z + 0.2))


def exc_side(ax, x, y, flip=1, z=7, alpha=1.0):
    f = flip
    T = lambda p: [(x + f * a, y + b) for a, b in p]
    kw = dict(ec="k", lw=0.6, zorder=z, alpha=alpha)
    ax.add_patch(FancyBboxPatch((x - 2.7, y), 5.4, 1.1, boxstyle="round,pad=0,rounding_size=0.5", fc="#333", **kw))
    ax.add_patch(Polygon(T([(-2.4, 1.2), (1.4, 1.2), (1.4, 2.6), (-2.4, 2.9)]), fc="#f2b705", **kw))
    ax.add_patch(Polygon(T([(0.0, 2.6), (1.4, 2.6), (1.4, 4.2), (0.1, 4.2)]), fc="#9fc3e6", **kw))
    ax.add_patch(Polygon(T([(1.0, 2.0), (1.6, 2.6), (4.6, 5.4), (5.2, 4.8)]), fc="#f2b705", **kw))
    ax.add_patch(Polygon(T([(4.6, 5.4), (5.2, 4.8), (6.9, -1.8), (6.3, -2.0)]), fc="#f2b705", **kw))
    ax.add_patch(Polygon(T([(6.1, -1.6), (7.3, -2.0), (7.5, -3.1), (6.1, -2.9)]), fc="#555", **kw))


def truck_rear(ax, x, y, z=6, label=True):
    ax.add_patch(Polygon([(x - 1.25, y + 1.0), (x + 1.25, y + 1.0), (x + 1.25, y + 3.3), (x - 1.25, y + 3.3)], fc="#f2b705", ec="k", lw=0.6, zorder=z))
    ax.add_patch(Polygon([(x - 1.15, y + 3.3), (x + 1.15, y + 3.3), (x + 0.6, y + 4.0), (x - 0.6, y + 4.0)], fc="#a07b45", ec="#5b4220", lw=0.5, zorder=z))
    for wx in (-0.95, -0.4, 0.4, 0.95):
        ax.add_patch(Rectangle((x + wx - 0.26, y), 0.52, 1.1, fc="#222", ec="k", lw=0.3, zorder=z + 0.1))
    if label:
        ax.text(x, y + 5.0, "Хово 18 м³\n(рамп дээр, араас)", fontsize=6.5, ha="center", color="#333", zorder=6, style="italic")


# ===================================================================== ХУУДАС 1: ПЛАН
fig1, bg = new_sheet("20 м", "ГҮНД ДЭЭЖ АВАХ УХМАЛ · ЗОХИОН БАЙГУУЛАЛТ", "ПЛАН М 1:500")
PX0, PY0, PWm, PHm = 22.0, 154.0, 288.0, 122.0
box(bg, PX0, PY0, PWm, PHm, "ПЛАН (ДЭЭРЭЭС ХАРСАН)  ·  М 1:500")
S = 2.0
wx0, wy0 = -30.0, -32.0
ax = fig1.add_axes([(PX0 + 1) / PW, (PY0 + 1) / PH, (PWm - 2) / PW, (PHm - 10) / PH])
ax.set_xlim(wx0, wx0 + (PWm - 2) / S); ax.set_ylim(wy0, wy0 + (PHm - 10) / S); ax.set_aspect("equal"); ax.axis("off")
ext = (X.min(), X.max(), Y.min(), Y.max())
cm = LinearSegmentedColormap.from_list("e", ["#8a6a48", "#b38b5d", "#d9bc8c", "#ead7b2"])
rgb = LightSource(azdeg=315, altdeg=40).shade(-D, cmap=cm, vert_exag=2.5, blend_mode="soft", dx=G.CELL, dy=G.CELL, vmin=-15, vmax=0)
ax.add_patch(Rectangle((wx0 - 5, wy0 - 5), 200, 100, fc="#ead7b2", ec="none", zorder=0))
pts = np.random.default_rng(3).uniform([wx0, wy0], [wx0 + 145, wy0 + 58], size=(900, 2))
ax.scatter(pts[:, 0], pts[:, 1], s=0.6, c="#b89a6c", zorder=0.5, lw=0)
ax.imshow(rgb, extent=ext, origin="lower", zorder=1, interpolation="bilinear")
outside = np.zeros(D.shape + (4,)); outside[..., :3] = matplotlib.colors.to_rgb("#ead7b2"); outside[..., 3] = (D <= 0.02) * 1.0
ax.imshow(outside, extent=ext, origin="lower", zorder=1.1)
for lv, lw, c, ls_ in [(0.03, 2.2, RED, "-"), (4.97, 1.0, "white", (0, (5, 2))), (5.03, 0.6, "#5a4630", "-"),
                       (9.97, 1.0, "white", (0, (5, 2))), (10.03, 0.6, "#5a4630", "-"), (14.97, 0.8, "#5a4630", "-")]:
    ax.contour(X, Y, D, levels=[lv], colors=[c], linewidths=lw, linestyles=[ls_], zorder=3)
ax.plot(ramp[:, 0], ramp[:, 1], color=BLUE, lw=1.4, ls=(0, (6, 3)), zorder=4)
for i in (60, 200, 340, 470):
    ax.annotate("", xy=ramp[i, :2], xytext=ramp[i + 6, :2], arrowprops=dict(arrowstyle="-|>", color="white", lw=1.6), zorder=5)
ex, ey = ramp[-1, 0], ramp[-1, 1]
ax.add_patch(Polygon([(ex, ey - 3), (DX0 + 8, ey - 3), (DX0 + 8, ey + 3), (ex, ey + 3)], fc="#e3c78f", ec="#6b5434", lw=0.8, zorder=2))
ax.plot([ex, DX0 + 8], [ey, ey], color=BLUE, lw=1.2, ls=(0, (6, 3)), zorder=4)
ax.annotate("", xy=(DX0 + 6, ey), xytext=(ex + 6, ey), arrowprops=dict(arrowstyle="-|>", color="white", lw=1.6), zorder=5)
# дээжний нүх
hc = HOLE_C
ax.add_patch(Rectangle((hc[0] - HOLE_TOP / 2, hc[1] - HOLE_TOP / 2), HOLE_TOP, HOLE_TOP, fc="#6d5638", ec="k", lw=1.0, zorder=4))
ax.add_patch(Rectangle((hc[0] - HOLE_BOT / 2, hc[1] - HOLE_BOT / 2), HOLE_BOT, HOLE_BOT, fc="#3d2f1e", ec="white", lw=0.8, zorder=4.1))
for a in np.linspace(0, 2 * np.pi, 9)[:-1]:
    ax.plot([hc[0] + HOLE_BOT / 2 * np.sign(np.cos(a)) * min(1, abs(np.cos(a)) * 1.5), hc[0] + HOLE_TOP / 2 * np.sign(np.cos(a)) * min(1, abs(np.cos(a)) * 1.5)],
            [hc[1] + HOLE_BOT / 2 * np.sign(np.sin(a)) * min(1, abs(np.sin(a)) * 1.5), hc[1] + HOLE_TOP / 2 * np.sign(np.sin(a)) * min(1, abs(np.sin(a)) * 1.5)],
            color="#d9c19a", lw=0.5, zorder=4.05)
ax.text(hc[0], hc[1], "−20", color="white", fontsize=6.5, ha="center", va="center", fontweight="bold", zorder=4.2)
# овоолго
m = 1.5 * DH
ax.add_patch(Rectangle((DX0, DY0), DX1 - DX0, DY1 - DY0, fc="#c79a5b", ec="#6b4a22", lw=1.2, ls=(0, (8, 2, 2, 2)), zorder=2))
ax.add_patch(Rectangle((DX0 + m, DY0 + m), DX1 - DX0 - 2 * m, DY1 - DY0 - 2 * m, fc="#e2c08a", ec="#6b4a22", lw=1.4, hatch="////", zorder=2.2))
for t in np.arange(DX0 + 2, DX1 - 1, 3.0):
    ll = m if int((t - DX0) / 3) % 2 == 0 else m / 2
    for yy, sgn in ((DY1, -1), (DY0, 1)):
        ax.plot([t, t], [yy, yy + sgn * ll * 0.9], color="#6b4a22", lw=0.5, zorder=2.3)
for t in np.arange(DY0 + 2, DY1 - 1, 3.0):
    ll = m if int((t - DY0) / 3) % 2 == 0 else m / 2
    for xx, sgn in ((DX0, 1), (DX1, -1)):
        ax.plot([xx, xx + sgn * ll * 0.9], [t, t], color="#6b4a22", lw=0.5, zorder=2.3)
ax.add_patch(Polygon([(DX0, ey - 3), (DX0 + m, ey - 3), (DX0 + m, ey + 3), (DX0, ey + 3)], fc="#e3c78f", ec="#6b5434", lw=0.8, zorder=2.4))
ax.text((DX0 + DX1) / 2, 8, "ШОРОО БУУЛГАХ\nТАЛБАЙ", ha="center", va="center", fontsize=11, fontweight="bold", color=NAVY, zorder=6,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=NAVY, lw=1))
ax.text((DX0 + DX1) / 2, -4.5, f"{DX1 - DX0:.0f} × {DY1 - DY0:.0f} м, өндөр 10 м (2 үе × 5 м)\nбагтаамж ≈ {Vdump / 1000:.1f} мян. м³ (сул шороо)",
        ha="center", va="center", fontsize=7.5, color="#3b2a14", zorder=6, bbox=dict(boxstyle="round,pad=0.25", fc="#fff6e2", ec="none", alpha=0.9))
ax.annotate("", xy=(crest[1], -9), xytext=(DX0, -9), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=0.9), zorder=6)
ax.text((crest[1] + DX0) / 2, -7.8, f"{DX0 - crest[1]:.0f} м", ha="center", fontsize=7.5, color=NAVY, zorder=6, fontweight="bold")
# техник
exc_plan(ax, -1.0, -8.0, 0, 90)
truck_plan(ax, 4.5, -8.4, 0)
truck_plan(ax, 24, ey, 0)
def tag(x, y, s, fs=6.8):
    ax.text(x, y, s, fontsize=fs, ha="center", va="center", zorder=9, color=NAVY, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=NAVY, lw=0.7, alpha=0.95))
tag(-12, 19.5, "Дээжний нүх: −15 → −20 м\n(дээд 8.8 × 8.8, ёроол 3 × 3 м)")
ax.plot([-12, -0.5], [17.7, 4.5], color=NAVY, lw=0.6, zorder=8)
tag(-17, -29.6, "Экскаватор 3.2 м³ (ёроолд)")
ax.plot([-17, -2], [-28.6, -9.5], color=NAVY, lw=0.6, zorder=8)
tag(30, ey + 7.5, "Хово 18 м³ × 2")
tag(17, -29.6, "Рамп: 6 м, 12 % (6.8°), L = 125 м")
ax.annotate("", xy=(8, ey + 1), xytext=(13, -28.6), arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.6), zorder=8)
ax.plot([wx0 + 1, crest[1] + 5], [0, 0], color="k", lw=0.7, ls=(0, (10, 2, 2, 2)), zorder=8)
for xx in (wx0 + 1, crest[1] + 5):
    ax.plot([xx, xx], [0, 3], color="k", lw=1.8, zorder=8)
    ax.text(xx, 4.6, "А", fontsize=10, fontweight="bold", ha="center", zorder=8)
nx, ny = 30.5, 12.0
ax.add_patch(Polygon([(nx, ny + 6), (nx - 1.8, ny), (nx, ny + 1.5)], fc="k", zorder=9))
ax.add_patch(Polygon([(nx, ny + 6), (nx + 1.8, ny), (nx, ny + 1.5)], fc="white", ec="k", lw=0.6, zorder=9))
ax.text(nx, ny + 7.8, "Х", fontsize=11, fontweight="bold", ha="center", zorder=9)
for i in range(5):
    ax.add_patch(Rectangle((wx0 + 2 + i * 5, wy0 + 0.8), 5, 1, fc="k" if i % 2 == 0 else "white", ec="k", lw=0.5, zorder=9))
for i in (0, 5, 25):
    ax.text(wx0 + 2 + i, wy0 + 2.7, f"{i}", fontsize=6, ha="center", zorder=9)
ax.text(wx0 + 30, wy0 + 1.3, "м", fontsize=6.5, va="center", zorder=9)

# --- баруун: ажлын хэмжээ ---
RX, RWd = 314.0, 96.0
box(bg, RX, 154, RWd, 122, "АЖЛЫН ХЭМЖЭЭ, ӨДӨР, ЗАРДАЛ", tsize=9.5)
cols = [RX + 2, RX + 30, RX + 47, RX + 61, RX + 75, RX + RWd - 2]
def cell(i, y, s, h=9, fc="white", bold=False, col="k", fs=7.4):
    bg.add_patch(Rectangle((cols[i], y - h), cols[i + 1] - cols[i], h, fc=fc, ec="#9aa7c0", lw=0.5, zorder=3))
    bg.text((cols[i] + cols[i + 1]) / 2, y - h / 2, s, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", color=col, zorder=4, linespacing=1.05)
y = 265
for i, s in enumerate(["Шат", "Ухалт,\nм³ (цул)", "Хово\nрейс", "Өдөр", "Сая ₮"]):
    cell(i, y, s, h=10, fc="#dfe7f5", bold=True, col=NAVY, fs=7)
y -= 10
for st in R["stages"]:
    nm = st["name"].replace(" (", "\n(")
    for i, s in enumerate([nm, fmt(st["V"]), fmt(st["trips"]), f"{st['days']:.1f}", f"{st['cost'] / 1e6:.1f}"]):
        cell(i, y, s, h=10.5, fs=6.6 if i == 0 else 7.6)
    y -= 10.5
for i, s in enumerate(["НИЙТ", fmt(R["V"]), fmt(R["trips"]), f"{R['days_work']:.1f}", f"{R['cost'] / 1e6:.1f}"]):
    cell(i, y, s, h=10, fc=YEL, bold=True, col=NAVY, fs=8.2)
y -= 10
bg.text(RX + RWd / 2, y - 5.5, f"Бэлтгэл, дээж авах +1 өдөр → ≈ {np.ceil(R['days_total']):.0f} ажлын өдөр\n"
        f"Цаг агаар, эвдрэлийн нөөц 15 % → ≈ {np.ceil(R['days_reserve']):.0f} өдөр",
        ha="center", va="center", fontsize=7.6, fontweight="bold", color=NAVY)
bg.text(RX + RWd / 2, y - 14.5, f"1 ээлж = 10 цаг (9 цаг бодит ажил) · 1 м³ = {C.PRICE:,} ₮\n"
        f"Хово 1 рейс = {R['passes']} шанага = {R['load_loose']:.1f} м³ сул = {R['load_bank']:.1f} м³ цул".replace(",", " "),
        ha="center", va="center", fontsize=6.5, color="#333")
yy = y - 22
bg.text(RX + 3, yy, "Хувилбар (ухалт → зардал):", fontsize=7.3, fontweight="bold", color=NAVY, va="center")
short = ["Санал болгосон ✔", "Рамп 15 % (эгц)", "Бермгүй", "Шулуун рамп", "Хово 20 м-т орох"]
for k, (o, sn) in enumerate(zip(R["opts"], short)):
    yk = yy - 4.2 - k * 3.9
    c = NAVY if k == 0 else "#666"
    bw = "bold" if k == 0 else "normal"
    bg.text(RX + 4, yk, sn, fontsize=6.8, color=c, va="center", fontweight=bw)
    bg.text(RX + 62, yk, fmt(o["V"]) + " м³", fontsize=6.8, color=c, va="center", ha="right", fontweight=bw)
    bg.text(RX + RWd - 4, yk, f"{o['cost'] / 1e6:.0f} сая ₮", fontsize=6.8, color=c, va="center", ha="right", fontweight=bw)

# --- доод зүүн: ажлын дараалал ---
box(bg, 22, 63, 288, 87, "АЖЛЫН ДАРААЛАЛ (ОПЕРАТОРТ)", tsize=10)
st = R["stages"]
steps = [("0", "Бэлтгэл · 0.5 өдөр", "Хил, рампын тэнхлэгийг\nшон хатгаж тэмдэглэнэ.\nОвоолгын талбайг сонгоно."),
         ("1", f"1-р шат · {st[0]['days']:.1f} өдөр", f"0 → −5 м ухна (налуу 45°).\n{fmt(st[0]['V'])} м³, {fmt(st[0]['trips'])} рейс.\nРампын 1-р тойргийг зүснэ."),
         ("2", f"2-р шат · {st[1]['days']:.1f} өдөр", f"−5 → −10 м (налуу 60°).\n{fmt(st[1]['V'])} м³, {fmt(st[1]['trips'])} рейс.\nХананд 2 м тавцан үлдээнэ."),
         ("3", f"3-р шат · {st[2]['days']:.1f} өдөр", f"−10 → −15 м, ёроол 10 × 10.\n{fmt(st[2]['V'])} м³, {fmt(st[2]['trips'])} рейс.\nХово ёроолд 3 цэгээр эргэнэ."),
         ("4", f"Нүх, дээж · 1 өдөр", f"Ёроолоос −20 м хүртэл\n3 × 3 м нүх ({fmt(st[3]['V'])} м³).\nДээжийг шанаганаас авна.")]
for k, (n, h, s) in enumerate(steps):
    x = 26 + k * 57
    bg.add_patch(FancyBboxPatch((x, 70), 52, 68, boxstyle="round,pad=0,rounding_size=1.8", fc="#f3f6fc", ec="#9aa7c0", lw=0.8, zorder=2))
    bg.add_patch(Circle((x + 7, 131), 4.2, fc=NAVY if n != "4" else RED, ec="none", zorder=4))
    bg.text(x + 7, 131, n, color="white", fontsize=12, ha="center", va="center", fontweight="bold", zorder=5)
    bg.text(x + 13, 131, h, fontsize=7.6, va="center", fontweight="bold", color=NAVY, zorder=4)
    bg.text(x + 3, 114, s, fontsize=8, va="center", zorder=4, linespacing=1.3)
    # жижиг дүрс: давхарга
    dep = [0, 1, 2, 3, 4][k]
    gx, gy = x + 6, 74
    for j in range(4):
        fcj = "#c9a26b" if j == 0 else ("#9c8a76" if j < 3 else "#7d6a55")
        done = j < dep
        bg.add_patch(Rectangle((gx + j * 2.2, gy + 22 - (j + 1) * 5), 40 - j * 4.4, 5,
                               fc="white" if done else fcj, ec="#6b5434", lw=0.4, zorder=3,
                               hatch=None if done else "..."))
        if j == dep - 1 or (dep == 0 and j == 0):
            pass
    if dep >= 1:
        j = dep - 1
        bg.add_patch(Rectangle((gx + j * 2.2, gy + 22 - (j + 1) * 5), 40 - j * 4.4, 5, fc=YEL, ec=NAVY, lw=0.9, zorder=3.5))
    if k < 4:
        bg.annotate("", xy=(x + 56.5, 104), xytext=(x + 52.5, 104), arrowprops=dict(arrowstyle="-|>", color=YEL, lw=2.5), zorder=5)

# --- баруун: тэмдэглэгээ ---
box(bg, RX, 63, RWd, 87, "ТЭМДЭГЛЭГЭЭ", tsize=10)
leg = [("line", RED, "-", 2.2, "Ухмалын хил (дээд ирмэг)"), ("line", BLUE, (0, (6, 3)), 1.4, "Рамп (6 м, 12 %)"),
       ("line", "#888", (0, (5, 2)), 1.0, "Шатны ирмэг, 2 м тавцан"), ("rect", "#c79a5b", None, None, "Шороо буулгах талбай"),
       ("hole", "#3d2f1e", None, None, "Дээжний нүх (−20 м)"), ("line", "k", (0, (10, 2, 2, 2)), 0.8, "Огтлолын шугам А-А")]
for k, (t, c, lsy, lw, s) in enumerate(leg):
    yk = 134 - k * 10
    if t == "line":
        bg.plot([RX + 4, RX + 20], [yk, yk], color=c, ls=lsy, lw=lw, zorder=4)
    elif t == "rect":
        bg.add_patch(Rectangle((RX + 4, yk - 2.5), 16, 5, fc=c, ec="#6b4a22", hatch="////", lw=0.6, zorder=4))
    else:
        bg.add_patch(Rectangle((RX + 7, yk - 3), 10, 6, fc="#6d5638", ec="k", lw=0.6, zorder=4))
        bg.add_patch(Rectangle((RX + 10, yk - 1), 4, 2, fc=c, ec="white", lw=0.5, zorder=4.1))
    bg.text(RX + 24, yk, s, fontsize=7.8, va="center", zorder=4)

# --- доод зүүн: анхаарах ---
box(bg, 22, 7, 205, 53, "АНХААРАХ", tsize=10, ec=RED)
warn = ["• Хэмжилтийг Хово-гийн тоогоор биш, ухмалын хэмжилтээр (цул м³) тооцохоор гэрээ хий.",
        f"   Хово тоолбол сул м³ болж ≈ {R['cost_loose'] / 1e6:.0f} сая ₮ (30 %-иар их) гарна.",
        "• Дээжний нүхэнд хүн орохгүй. Дээжийг шанагаас авна, гүнийг шанаганы тэмдгээр хэмжинэ.",
        "• Хово ачаатай рампаар 1-р араагаар өгсөнө. Рампын гадна ирмэгт 1 м шороон далан хийнэ.",
        "• Ухмалын ирмэгээс 13 м дотор шороо асгахгүй, техник зогсоохгүй.",
        "• Ус орвол ёроолын буланд зумф ухаж шавхана. Хана нурж эхэлбэл ажлыг зогсооно.",
        "• Дээж авсны дараа нөхөн булах ажил энэ үнэд ороогүй (тусдаа тохирно)."]
for k, s in enumerate(warn):
    bg.text(25, 48 - k * 5.6, s, fontsize=7.1, va="center", color="#7a1010" if k < 2 else "#222", zorder=4)

draw_stamp(fig1, PW, PH, right_mm=PW - 5, bottom_mm=5, info=dict(STAMP, title="Ухмалын план, ажлын хэмжээ", scale="1:500", number="1"), fs=9)

# ===================================================================== ХУУДАС 2: ОГТЛОЛ
fig2, bg = new_sheet("20 м", "ГҮНД ДЭЭЖ АВАХ УХМАЛ · ОГТЛОЛ", "ХӨНДЛӨН ОГТЛОЛ А-А М 1:200")
SX0, SY0, SWm, SHm = 22.0, 122.0, 390.0, 154.0
box(bg, SX0, SY0, SWm, SHm, "ХӨНДЛӨН ОГТЛОЛ А-А  ·  М 1:200")
S2 = 5.0
ax2 = fig2.add_axes([(SX0 + 1) / PW, (SY0 + 1) / PH, (SWm - 2) / PW, (SHm - 9) / PH])
w_m, h_m = (SWm - 2) / S2, (SHm - 9) / S2
x_left = -38.0
ax2.set_xlim(x_left, x_left + w_m); ax2.set_ylim(-21.5, -21.5 + h_m); ax2.set_aspect("equal"); ax2.axis("off")
j = np.argmin(np.abs(Y[:, 0] - 0.0))
xs, zs = X[j], -D[j]
x_right = x_left + w_m
xr = np.r_[x_left, xs[(xs > x_left) & (xs < x_right)], x_right]
zr = np.r_[0, zs[(xs > x_left) & (xs < x_right)], 0]
# дээжний нүхийг профайлд оруулах
hb, ht = HOLE_BOT / 2, HOLE_TOP / 2
zr = np.where(np.abs(xr - hc[0]) <= ht, np.minimum(zr, -15 - 5 * np.clip((ht - np.abs(xr - hc[0])) / (ht - hb), 0, 1)), zr)
ax2.add_patch(Rectangle((x_left, 0), w_m, 10, fc="#e8f1fb", ec="none", zorder=0))
poly = np.r_[np.c_[xr, zr], [[x_right, -23], [x_left, -23]]]
ax2.add_patch(Polygon(poly, fc="#9c8a76", ec="none", zorder=1))
ax2.add_patch(Polygon(np.r_[np.c_[xr, np.maximum(zr, -5)], [[x_right, -5], [x_left, -5]]], fc="#c9a26b", ec="none", zorder=1.2))
ax2.add_patch(Polygon(poly, fill=False, hatch="..", ec="#7a6a58", lw=0, zorder=1.1))
ax2.plot(xr, zr, color="k", lw=1.6, zorder=3)
ax2.plot([x_left, x_right], [-5, -5], color="#6b5434", lw=0.5, ls=(0, (4, 3)), zorder=1.5)
ax2.text(x_right - 1, -2.5, "Хөрс, өгөршсөн давхарга", ha="right", fontsize=8.5, color="#4a3420", zorder=4, style="italic")
ax2.text(x_right - 1, -12, "Чулуулаг", ha="right", fontsize=8.5, color="white", zorder=4, style="italic")
for lv in (0, -5, -10, -15, -20):
    ax2.plot([x_left, x_left + 2.2], [lv, lv], color="k", lw=0.8, zorder=4)
    ax2.text(x_left + 2.6, lv + (0.5 if lv == 0 else 0), f"{lv} м", fontsize=9, va="center", fontweight="bold", zorder=4)
    xe = xr[np.argmax(zr <= lv + 0.01)] if lv < 0 else x_left + 6
    ax2.plot([x_left + 6.5, xe], [lv, lv], color="white" if lv < 0 else "#888", lw=0.6, ls=(0, (4, 3)), zorder=2)
def lbl(x, y, s, fs=8, fc="white", ec=NAVY, col=NAVY):
    ax2.text(x, y, s, fontsize=fs, ha="center", va="center", zorder=6, color=col, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.3", fc=fc, ec=ec, lw=0.8))
lbl(14.5, -2.6, "1-р шат (0 … −5 м)\nналуу 45°")
lbl(22.5, -8.5, "2-р шат (−5 … −10 м)\nналуу 60° ⚠")
lbl(-16.5, -12.8, "3-р шат (−10 … −15 м)\nналуу 60° ⚠")
lbl(-8.5, -9.0, "тавцан 2 м", fs=6.8)
lbl(10.5, -18.2, "ДЭЭЖНИЙ НҮХ\n−15 → −20 м\nёроол 3 × 3 м, хана 60°", fs=7.5, fc="#fdecea", ec=RED, col=RED)
ax2.annotate("", xy=(1.4, -18.6), xytext=(6.6, -18.4), arrowprops=dict(arrowstyle="-|>", color=RED, lw=1), zorder=6)
ax2.add_patch(Polygon([(-1.0, -20), (1.0, -20), (0.8, -19.6), (-0.8, -19.6)], fc=YEL, ec="k", lw=0.6, zorder=6))
ax2.annotate("ДЭЭЖ\n(шанагаас авна)", xy=(0, -19.8), xytext=(-12, -18.7), fontsize=7.5, color=NAVY, fontweight="bold",
             ha="center", va="center", arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=0.9), zorder=7)
ax2.annotate("", xy=(-hb, -20.7), xytext=(hb, -20.7), arrowprops=dict(arrowstyle="<->", color="white", lw=0.9), zorder=6)
ax2.text(0, -21.2, "3 м", fontsize=7, ha="center", va="center", color="white", fontweight="bold", zorder=6)
ax2.annotate("", xy=(-5, -14.6), xytext=(5, -14.6), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=0.9), zorder=6)
ax2.text(2.6, -14.0, "ёроол 10 м", fontsize=7.2, ha="center", color=NAVY, fontweight="bold", zorder=6)
exc_side(ax2, -4.6, -15, flip=1, alpha=0.55, z=5)
ax2.text(-11.5, -16.3, "экскаватор (ар талд,\nрампын хөлд)", fontsize=6.5, ha="center", color="#333", style="italic", zorder=6)
truck_rear(ax2, 9.6, zr[np.argmin(np.abs(xr - 9.6))])
dz = np.abs(np.gradient(zr, xr))
flat = (dz < 0.2) & (zr < -0.3) & (zr > -14.7) & (np.abs(zr + 5) > 0.3) & (np.abs(zr + 10) > 0.3)
idx = np.where(flat)[0]
for sg in np.split(idx, np.where(np.diff(idx) > 1)[0] + 1):
    if len(sg) < 8: continue
    x0s, x1s, zz = xr[sg[0]], xr[sg[-1]], zr[sg].mean()
    ax2.plot([x0s, x1s], [zz + 0.12, zz + 0.12], color=BLUE, lw=3, solid_capstyle="butt", zorder=4)
    lbl((x0s + x1s) / 2 + (0 if x0s < 0 else 8), zz + (1.3 if x0s < 0 else 2.4), f"рамп −{abs(zz):.1f} м", fs=6.8)
cx0 = xr[np.argmax(zr < -0.02)]; cx1 = xr[len(zr) - 1 - np.argmax(zr[::-1] < -0.02)]
ax2.annotate("", xy=(cx0 + 0.8, 1.0), xytext=(cx1 - 0.8, 1.0), arrowprops=dict(arrowstyle="<->", color=RED, lw=1))
ax2.text((cx0 + cx1) / 2, 1.6, f"ухмалын дээд өргөн ≈ {cx1 - cx0:.0f} м", fontsize=8.5, ha="center", color=RED, fontweight="bold", zorder=6)
# гүний сум
ax2.annotate("", xy=(30, 0), xytext=(30, -20), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=1.2), zorder=6)
ax2.text(30.8, -10, "20 м", fontsize=10, rotation=90, va="center", color=NAVY, fontweight="bold", zorder=6)
ax2.plot([1.5, 31], [-20, -20], color=NAVY, lw=0.6, ls=(0, (3, 2)), zorder=5)

# --- доод: техник, тооцоо ---
p = R["params"]
box(bg, 22, 63, 128, 54, "ТЕХНИК (3 ШИРХЭГ)", tsize=10)
tech = [("Экскаватор (Хятад, 500-р анги)", ""), ("Шанага", "3.2 м³"), ("1 шанага ≈", f"{C.BUCKET * C.FILL:.2f} м³ сул (90 %)"),
        ("1 шанагын хугацаа", "≈ 30 сек"), ("Хово (2 ширхэг)", ""), ("Тэвш", "18 м³"),
        ("1 рейс", f"{R['passes']} шанага = {R['load_loose']:.1f} м³ сул"), ("Ачих хугацаа", f"≈ {R['t_load']:.0f} мин")]
for k, (a, b) in enumerate(tech):
    yk = 103.5 - k * 4.9
    bold = b == ""
    bg.text(26, yk, a, fontsize=7.6, va="center", fontweight="bold" if bold else "normal", color=NAVY if bold else "#222")
    bg.text(146, yk, b, fontsize=7.6, va="center", ha="right", color="#222")
box(bg, 154, 63, 156, 54, "НЭГ ӨДӨРТ ХЭДИЙГ УХАХ ВЭ", tsize=10)
calc_lines = [
    "Хово 1 эргэлт = ачих 4 мин + өгсөх + буулгах 2 мин + буцах ≈ 8–10 мин",
    "2 Хово → цагт ≈ 12–15 рейс (экскаватор цагт 15-аас ихийг ачиж чадахгүй)",
    "Бодит ашиглалт 75 % (цагт 45 мин) → цагт ≈ 9–11 рейс",
    f"1 рейс ≈ {R['load_bank']:.1f} м³ цул → цагт ≈ 120–150 м³",
    "Өдөрт 9 цаг бодит ажил → өдөрт ≈ 1 100–1 350 м³",
    f"{fmt(R['V'])} м³ ÷ ≈ 1 250 м³/өдөр ≈ {R['days_work']:.0f} өдөр (+1 бэлтгэл, дээж)"]
for k, s in enumerate(calc_lines):
    bg.text(158, 103.5 - k * 6.6, s, fontsize=7.4, va="center", color="#222" if k < 5 else NAVY, fontweight="bold" if k == 5 else "normal")
box(bg, 314, 63, 98, 54, "ЯАГААД ИНГЭЖ ХИЙВ", tsize=10)
why = [f"Хово 20 м хүртэл орвол\n{fmt(R['opts'][-1]['V'])} м³ = {R['opts'][-1]['cost'] / 1e6:.0f} сая ₮",
       f"15 м-ээс доош зөвхөн экскаватор\nухна → {fmt(R['opts'][-1]['V'] - R['V'])} м³ хэмнэнэ",
       f"Рамп ханан дагуу эргэлдэнэ →\nшулуун рампаас {fmt(R['opts'][3]['V'] - R['V'])} м³ бага"]
for k, s in enumerate(why):
    yk = 100 - k * 13
    bg.add_patch(Circle((318.5, yk), 2.0, fc=GREEN, ec="none", zorder=4))
    bg.text(318.5, yk, "✓", color="white", fontsize=7.5, ha="center", va="center", fontweight="bold", zorder=5)
    bg.text(322.5, yk, s, fontsize=7.2, va="center", zorder=4, linespacing=1.2)
box(bg, 22, 7, 205, 53, "ТААМАГ (ГЭРЭЭНИЙ ӨМНӨ БАТЛАХ)", tsize=10, ec=RED)
assum = ["• 2, 3-р шатны 60° налуу, 2 м тавцан — чулуулаг хатуу гэж үзсэн. Сул бол налууг 45° болгоно.",
         "• Ёроол 10 × 10 м — Хово 3 цэгээр эргэх, экскаватор зогсох хамгийн бага талбай.",
         "• Дээжний нүх 5 м гүн: экскаватор ёроолоос ≈ 7 м хүртэл ухаж чадна (маркаар шалгах).",
         "• Сулралт 1.3: 1 м³ цул шороо тэвшинд 1.3 м³ болно.",
         "• 1 м³ = " + fmt(C.PRICE) + " ₮ — ухах, зөөх, буулгах бүгд орсон гэж үзсэн (түлш орсон эсэхийг тохир).",
         "• Газрын ус, том чулуу, хөлдсөн хөрс гарвал хугацаа уртасна."]
for k, s in enumerate(assum):
    bg.text(25, 48 - k * 6.3, s, fontsize=7.0, va="center", color="#222", zorder=4)
draw_stamp(fig2, PW, PH, right_mm=PW - 5, bottom_mm=5, info=dict(STAMP, title="Хөндлөн огтлол А-А, дээжний нүх", scale="1:200", number="2"), fs=9)

pdf_path = os.path.join(OUTDIR, "drawings.pdf")
with PdfPages(pdf_path) as pdf:
    pdf.savefig(fig1); pdf.savefig(fig2)
fig1.savefig(os.path.join(OUTDIR, "sheet1.png"), dpi=110)
fig2.savefig(os.path.join(OUTDIR, "sheet2.png"), dpi=110)
print("ok", pdf_path)
