"""15 м гүн, 3 шатлалтай ухмал — план (1:500) + хөндлөн огтлол А-А (1:200), A3, инфографик хэв маяг.
Геометр: ukhmal15_geom.py (12 % спираль рамп, ханан дагуу). Гаралт: PNG + PDF."""
import os as _os
VAULT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))  # vault-ийн үндэс, аль ч компьютерт
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle, FancyArrowPatch
from matplotlib.colors import LightSource, LinearSegmentedColormap
import matplotlib.patheffects as pe

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, _os.path.join(VAULT, "_system", "skills", "zurag-shtamp"))
import ukhmal15_geom as G
from gv_stamp import draw_stamp

G.GRADE = 0.12; G.SWITCH = 0.0
OUT = _os.path.join(VAULT, r"02-Projects\Ажил\Вай эйч графит нэчүрал ХХК\Сүүж уул\Ухмал 20 м\Хуучин хувилбар")
NAME = "Ухмал 15 м 3 шат - план, огтлол"

plt.rcParams["font.family"] = ["Arial", "DejaVu Sans"]
NAVY, NAVY2, YEL, RED, BLUE = "#13306b", "#1f4c9c", "#ffd21f", "#d7261e", "#2a6fdb"
PW, PH = 420.0, 297.0
fig = plt.figure(figsize=(PW / 25.4, PH / 25.4), dpi=200)
fig.patch.set_facecolor("white")
bg = fig.add_axes([0, 0, 1, 1]); bg.set_xlim(0, PW); bg.set_ylim(0, PH); bg.axis("off")

# ---------- тооцоо ----------
X, Y, D = G.surface("spiral", ext=40)
V, lay = G.volumes(D)
ramp = G.ramp_samples("spiral")
VS, layS = G.volumes(G.surface("straight", ext=90)[2])
VN, _ = G.volumes(G.surface("none", ext=40)[2])
G.GRADE = 0.15; V15, _ = G.volumes(G.surface("spiral", ext=40)[2]); G.GRADE = 0.12   # 15 % хувилбар
SW = G.SWELL; TRUCK = 20.0; PROD = 80.0          # Хово 20 м³; экскаватор 80 м³/цаг (⚠ өмнөх зургийн 60–80)
loose = V * SW
crest_ext = (X[D > 0.02].min(), X[D > 0.02].max(), Y[D > 0.02].min(), Y[D > 0.02].max())
print("V", round(V), lay, "loose", round(loose), "crest", np.round(crest_ext, 1), "straight", round(VS), "none", round(VN))

# овоолго: 2 үе, нийт 7 м, налуу 1:1.5
DX0, DX1, DY0, DY1, DH = 37.0, 112.0, -27.0, 21.0, 10.0
def frustum(b, w, h, m=1.5):
    tb, tw = b - 2 * m * h, w - 2 * m * h
    return h / 6 * (b * w + tb * tw + 4 * (b - m * h) * (w - m * h))
Vdump = frustum(DX1 - DX0, DY1 - DY0, DH)
print("dump", round(Vdump), "need", round(loose))


def box(x, y, w, h, title=None, fc="white", tsize=11):
    bg.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=2.2",
                                fc=fc, ec=NAVY, lw=1.6, zorder=1))
    if title:
        bg.add_patch(FancyBboxPatch((x, y + h - 8), w, 8, boxstyle="round,pad=0,rounding_size=2.2",
                                    fc=NAVY, ec=NAVY, lw=1.6, zorder=2))
        bg.add_patch(Rectangle((x, y + h - 8), w, 3, fc=NAVY, ec="none", zorder=2))
        bg.text(x + 3, y + h - 4, title, color="white", fontsize=tsize, fontweight="bold",
                va="center", ha="left", zorder=3)


# ---------- хүрээ, гарчиг ----------
bg.add_patch(Rectangle((20, 5), PW - 25, PH - 10, fill=False, lw=1.2, ec="k"))
bg.add_patch(FancyBboxPatch((24, 279), 388, 14, boxstyle="round,pad=0,rounding_size=3", fc=NAVY, ec=YEL, lw=1.5))
bg.text(30, 286, "10 × 10 м", color=YEL, fontsize=19, fontweight="bold", va="center")
bg.text(73, 286, "ЁРООЛТОЙ, 15 м ГҮН, 3 ШАТЛАЛТАЙ УХМАЛ", color="white", fontsize=17, fontweight="bold", va="center")
bg.text(406, 286, "ПЛАН М 1:500  ·  ОГТЛОЛ А-А М 1:200", color="white", fontsize=12, fontweight="bold",
        va="center", ha="right")

# ======================= ПЛАН =======================
PX0, PY0, PWm, PHm = 22.0, 154.0, 288.0, 122.0
box(PX0, PY0, PWm, PHm, "ПЛАН (ДЭЭРЭЭС ХАРСАН)  ·  М 1:500")
S = 2.0     # мм/м (1:500)
wx0, wy0 = -30.0, -32.0
ax = fig.add_axes([(PX0 + 1) / PW, (PY0 + 1) / PH, (PWm - 2) / PW, (PHm - 10) / PH])
ax.set_xlim(wx0, wx0 + (PWm - 2) / S); ax.set_ylim(wy0, wy0 + (PHm - 10) / S)
ax.set_aspect("equal"); ax.axis("off")

# газар + ухмалын сүүдэрлэлт
ext = (X.min(), X.max(), Y.min(), Y.max())
ls = LightSource(azdeg=315, altdeg=40)
cm = LinearSegmentedColormap.from_list("e", ["#8a6a48", "#b38b5d", "#d9bc8c", "#ead7b2"])
Z = -D
rgb = ls.shade(Z, cmap=cm, vert_exag=2.5, blend_mode="soft", dx=G.CELL, dy=G.CELL,
               vmin=-15, vmax=0)
ax.add_patch(Rectangle((wx0 - 5, wy0 - 5), 200, 100, fc="#ead7b2", ec="none", zorder=0))
# газрын бүдэг хээ
rng = np.random.default_rng(3)
pts = rng.uniform([wx0, wy0], [wx0 + 145, wy0 + 55], size=(900, 2))
ax.scatter(pts[:, 0], pts[:, 1], s=0.6, c="#b89a6c", zorder=0.5, lw=0)
ax.imshow(rgb, extent=ext, origin="lower", zorder=1, interpolation="bilinear")
mask = np.where(D > 0.02, 1.0, np.nan)
ax.imshow(np.where(D > 0.02, 0, np.nan)[..., None] * 0 + 0, extent=ext, origin="lower", alpha=0)
# ухмалаас гадуурх газрыг дахин будна (сүүдэрлэлтийн хүрээ)
outside = np.zeros(D.shape + (4,)); outside[..., :3] = matplotlib.colors.to_rgb("#ead7b2")
outside[..., 3] = (D <= 0.02) * 1.0
ax.imshow(outside, extent=ext, origin="lower", zorder=1.1)
# шатны ирмэг: дээд (бүдүүн), доод (нарийн)
for lv, lw, c, ls_ in [(0.03, 2.2, RED, "-"), (4.97, 1.0, "white", (0, (5, 2))), (5.03, 0.6, "#5a4630", "-"),
                       (9.97, 1.0, "white", (0, (5, 2))), (10.03, 0.6, "#5a4630", "-"), (14.97, 0.8, "#5a4630", "-")]:
    ax.contour(X, Y, D, levels=[lv], colors=[c], linewidths=lw, linestyles=[ls_], zorder=3)
# рампын тэнхлэг
ax.plot(ramp[:, 0], ramp[:, 1], color=BLUE, lw=1.4, ls=(0, (6, 3)), zorder=4)
for i in (60, 200, 340, 470):
    p0, p1 = ramp[i], ramp[i + 6]
    ax.annotate("", xy=p0[:2], xytext=p1[:2], arrowprops=dict(arrowstyle="-|>", color="white", lw=1.6), zorder=5)
# тээврийн зам: рампын амнаас овоолго руу (6 м)
ex, ey = ramp[-1, 0], ramp[-1, 1]
road = Polygon([(ex, ey - 3), (DX0 + 8, ey - 3), (DX0 + 8, ey + 3), (ex, ey + 3)], fc="#e3c78f", ec="#6b5434",
               lw=0.8, zorder=2)
ax.add_patch(road)
ax.plot([ex, DX0 + 8], [ey, ey], color=BLUE, lw=1.2, ls=(0, (6, 3)), zorder=4)
ax.annotate("", xy=(DX0 + 6, ey), xytext=(ex + 6, ey), arrowprops=dict(arrowstyle="-|>", color="white", lw=1.6), zorder=5)

# овоолго (шороо буулгах талбай)
m = 1.5 * DH
ax.add_patch(Rectangle((DX0, DY0), DX1 - DX0, DY1 - DY0, fc="#c79a5b", ec="#6b4a22", lw=1.2, ls=(0, (8, 2, 2, 2)), zorder=2))
ax.add_patch(Rectangle((DX0 + m, DY0 + m), DX1 - DX0 - 2 * m, DY1 - DY0 - 2 * m, fc="#e2c08a", ec="#6b4a22",
                       lw=1.4, hatch="////", zorder=2.2))
for t in np.arange(DX0 + 2, DX1 - 1, 3.0):     # налуугийн зураас (урт/богино)
    ll = m if int((t - DX0) / 3) % 2 == 0 else m / 2
    for yy, sgn in ((DY1, -1), (DY0, 1)):
        ax.plot([t, t], [yy + sgn * 0, yy + sgn * ll * 0.9], color="#6b4a22", lw=0.5, zorder=2.3)
for t in np.arange(DY0 + 2, DY1 - 1, 3.0):
    ll = m if int((t - DY0) / 3) % 2 == 0 else m / 2
    for xx, sgn in ((DX0, 1), (DX1, -1)):
        ax.plot([xx, xx + sgn * ll * 0.9], [t, t], color="#6b4a22", lw=0.5, zorder=2.3)
# овоолго дээр гарах налуу зам (2-р үе)
ax.add_patch(Polygon([(DX0, ey - 3), (DX0 + m, ey - 3), (DX0 + m, ey + 3), (DX0, ey + 3)], fc="#e3c78f",
                     ec="#6b5434", lw=0.8, zorder=2.4))
ax.text((DX0 + DX1) / 2, 8, "ШОРОО БУУЛГАХ\nТАЛБАЙ", ha="center", va="center", fontsize=11, fontweight="bold",
        color=NAVY, zorder=6, bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=NAVY, lw=1))
ax.text((DX0 + DX1) / 2, -4.5, f"V ≈ {Vdump/1000:.1f} мян. м³ (сул)\nH = 10 м (2 үе × 5 м) · налуу 1:1.5",
        ha="center", va="center", fontsize=7.5, color="#3b2a14", zorder=6,
        bbox=dict(boxstyle="round,pad=0.25", fc="#fff6e2", ec="none", alpha=0.9))
# овоолгын зай
ax.annotate("", xy=(crest_ext[1], -9), xytext=(DX0, -9), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=0.9), zorder=6)
ax.text((crest_ext[1] + DX0) / 2, -7.8, f"{DX0 - crest_ext[1]:.0f} м", ha="center", fontsize=7.5, color=NAVY, zorder=6,
        fontweight="bold")


# техник (план, бодит хэмжээ)
def truck_plan(ax, x, y, ang, z=7):
    """Хово 8×4: 9.5 × 2.5 м, (x,y) = арын төв, ang = урд чиглэл."""
    ca, sa = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    def T(pts): return [(x + px * ca - py * sa, y + px * sa + py * ca) for px, py in pts]
    ax.add_patch(Polygon(T([(0, -1.25), (6.6, -1.25), (6.6, 1.25), (0, 1.25)]), fc="#f2b705", ec="k", lw=0.7, zorder=z))
    ax.add_patch(Polygon(T([(0.4, -0.9), (6.2, -0.9), (6.2, 0.9), (0.4, 0.9)]), fc="#a07b45", ec="#5b4220", lw=0.4, zorder=z))
    ax.add_patch(Polygon(T([(7.0, -1.25), (9.5, -1.25), (9.5, 1.25), (7.0, 1.25)]), fc="#f2b705", ec="k", lw=0.7, zorder=z))
    ax.add_patch(Polygon(T([(8.6, -1.1), (9.3, -1.1), (9.3, 1.1), (8.6, 1.1)]), fc="#2b3a4a", ec="none", zorder=z))


def exc_plan(ax, x, y, ang, sw, z=7):
    """500-р анги экскаватор: явах эрхтэн 5.4 × 3.4 м, их бие 3.8 × 3.2, сум ~10 м."""
    ca, sa = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    def T(pts, a_c=ca, a_s=sa): return [(x + px * a_c - py * a_s, y + px * a_s + py * a_c) for px, py in pts]
    for s in (-1, 1):
        ax.add_patch(Polygon(T([(-2.7, s * 1.7 - 0.45), (2.7, s * 1.7 - 0.45), (2.7, s * 1.7 + 0.45), (-2.7, s * 1.7 + 0.45)]),
                             fc="#333", ec="k", lw=0.5, zorder=z))
    cb, sb = np.cos(np.radians(sw)), np.sin(np.radians(sw))
    ax.add_patch(Polygon(T([(-2.4, -1.6), (1.4, -1.6), (1.4, 1.6), (-2.4, 1.6)], cb, sb), fc="#f2b705", ec="k", lw=0.7, zorder=z + 0.1))
    ax.add_patch(Polygon(T([(-0.2, 0.3), (1.4, 0.3), (1.4, 1.5), (-0.2, 1.5)], cb, sb), fc="#2b3a4a", ec="k", lw=0.4, zorder=z + 0.2))
    ax.add_patch(Polygon(T([(1.2, -0.45), (8.6, -0.3), (8.6, 0.3), (1.2, 0.45)], cb, sb), fc="#f2b705", ec="k", lw=0.6, zorder=z + 0.2))
    ax.add_patch(Polygon(T([(8.4, -0.9), (9.8, -0.9), (9.8, 0.9), (8.4, 0.9)], cb, sb), fc="#555", ec="k", lw=0.5, zorder=z + 0.2))


exc_plan(ax, 1.5, 2.0, 90, -95)
truck_plan(ax, 1.0, -8.0, 180)   # ёроолд ухарч орсон: арын тал экскаватор руу
truck_plan(ax, 24, ey, 0, z=7)   # гарч буй ачаатай Хово
# шошго
def tag(x, y, s, fs=7.5, **kw):
    ax.text(x, y, s, fontsize=fs, ha="center", va="center", zorder=9, color=NAVY, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=NAVY, lw=0.7, alpha=0.95), **kw)
tag(-12, 19.5, "500 экскаватор (3 м³)", fs=6.8)
ax.plot([-12, 1.5], [18.5, 3.5], color=NAVY, lw=0.6, zorder=8)
tag(30, ey + 7.5, "Хово 20 м³", fs=6.8)
tag(20, -29.3, "Орох, гарах рамп: 6 м, 12 % (6.8°), L = 125 м", fs=6.8)
ax.annotate("", xy=(6, ey + 1), xytext=(8, -28.3), arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.6), zorder=8)
# ёроолын хэмжээ
ax.annotate("", xy=(-5, -4.4), xytext=(5, -4.4), arrowprops=dict(arrowstyle="<->", color="white", lw=0.9), zorder=8)
ax.text(0, -3.2, "10 м", color="white", fontsize=7, ha="center", fontweight="bold", zorder=8)
ax.annotate("", xy=(-4.4, -5), xytext=(-4.4, 5), arrowprops=dict(arrowstyle="<->", color="white", lw=0.9), zorder=8)
ax.text(-3.2, 0, "10 м", color="white", fontsize=7, rotation=90, va="center", fontweight="bold", zorder=8)
# шатны тэмдэг
for (x, y, s) in [(-12.5, -12.0, "−15"), (-21.5, 1, "−5"), (-16.5, 5, "−10")]:
    pass
# огтлолын шугам А-А
ax.plot([wx0 + 1, crest_ext[1] + 5], [0, 0], color="k", lw=0.7, ls=(0, (10, 2, 2, 2)), zorder=8)
for xx in (wx0 + 1, crest_ext[1] + 5):
    ax.plot([xx, xx], [0, 3], color="k", lw=1.8, zorder=8)
    ax.text(xx, 4.6, "А", fontsize=10, fontweight="bold", ha="center", zorder=8)
# хойд зүг
nx, ny = 30.5, 12.0
ax.add_patch(Polygon([(nx, ny + 6), (nx - 1.8, ny), (nx, ny + 1.5)], fc="k", zorder=9))
ax.add_patch(Polygon([(nx, ny + 6), (nx + 1.8, ny), (nx, ny + 1.5)], fc="white", ec="k", lw=0.6, zorder=9))
ax.text(nx, ny + 7.8, "Х", fontsize=11, fontweight="bold", ha="center", zorder=9)
# масштаб шугам
for i in range(5):
    ax.add_patch(Rectangle((wx0 + 2 + i * 5, wy0 + 0.8), 5, 1, fc="k" if i % 2 == 0 else "white", ec="k", lw=0.5, zorder=9))
for i in (0, 5, 25):
    ax.text(wx0 + 2 + i, wy0 + 2.7, f"{i}", fontsize=6, ha="center", zorder=9)
ax.text(wx0 + 30, wy0 + 1.3, "м", fontsize=6.5, va="center", zorder=9)

# ======================= ОГТЛОЛ А-А =======================
SX0, SY0, SWm, SHm = 22.0, 63.0, 288.0, 88.0
box(SX0, SY0, SWm, SHm, "ХӨНДЛӨН ОГТЛОЛ А-А  ·  М 1:200")
S2 = 5.0
ax2 = fig.add_axes([(SX0 + 1) / PW, (SY0 + 1) / PH, (SWm - 2) / PW, (SHm - 9) / PH])
w_m, h_m = (SWm - 2) / S2, (SHm - 9) / S2
x_left = -28.0
ax2.set_xlim(x_left, x_left + w_m); ax2.set_ylim(-15.7, -15.7 + h_m); ax2.set_aspect("equal"); ax2.axis("off")
j = np.argmin(np.abs(Y[:, 0] - 0.0))
xs = X[j]; zs = -D[j]
xr = xs[(xs > x_left) & (xs < x_left + w_m)]; zr = zs[(xs > x_left) & (xs < x_left + w_m)]
ax2.add_patch(Rectangle((x_left, 0), w_m, 2, fc="#e8f1fb", ec="none", zorder=0))     # тэнгэр
# чулуулаг (давхаргаар)
poly = np.r_[np.c_[xr, zr], [[xr[-1], -17], [xr[0], -17]]]
ax2.add_patch(Polygon(poly, fc="#9c8a76", ec="none", zorder=1))
ax2.add_patch(Polygon(np.r_[np.c_[xr, np.maximum(zr, -5)], [[xr[-1], -5], [xr[0], -5]]], fc="#c9a26b", ec="none", zorder=1.2))
ax2.add_patch(Polygon(poly, fill=False, hatch="..", ec="#7a6a58", lw=0, zorder=1.1))
ax2.plot(xr, zr, color="k", lw=1.6, zorder=3)
ax2.plot([x_left, x_left + w_m], [-5, -5], color="#6b5434", lw=0.5, ls=(0, (4, 3)), zorder=1.5)
ax2.text(x_left + w_m - 0.5, -3.6, "Хөрс,\nөгөршсөн", ha="right", fontsize=7.5, color="#4a3420", zorder=4, style="italic")
ax2.text(x_left + w_m - 0.5, -13.5, "Чулуулаг", ha="right", fontsize=7.5, color="white", zorder=4, style="italic")
# түвшний шугам
for lv in (0, -5, -10, -15):
    ax2.plot([x_left, x_left + 2.2], [lv, lv], color="k", lw=0.8, zorder=4)
    ax2.text(x_left + 2.6, lv - (0.55 if lv == 0 else 0), f"{lv} м" if lv else "0 м", fontsize=8, va="center", fontweight="bold", zorder=4)
    ax2.plot([x_left + 6, xr[np.argmax(zr <= lv)] if lv < 0 else x_left + 6], [lv, lv], color="white", lw=0.6, ls=(0, (4, 3)), zorder=2)
# шатны шошго (зүүн хана, бермтэй хэсэг)
_, XX = G.pit_depth(0)
def lbl(x, y, s, fs=7.2):
    ax2.text(x, y, s, fontsize=fs, ha="center", va="center", zorder=6, color=NAVY, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=NAVY, lw=0.7))
xe = 5.0  # баруун ханын ёроолын ирмэг (зүүн хана дээр рамп таарсан тул баруун хананд тэмдэглэнэ)
# баруун талын профайлын онцлог цэгийг олох
right = (xr > 5)
lbl(13.5, -2.6, "1-р шат (0…−5 м)\nналуу 45°")
lbl(21.5, -8.3, "2-р шат (−5…−10 м)\nналуу 60° ⚠")
lbl(-15.0, -12.6, "3-р шат (−10…−15 м)\nналуу 60° ⚠")
# ёроолын хэмжээ
ax2.annotate("", xy=(-5, -15.3), xytext=(5, -15.3), arrowprops=dict(arrowstyle="<->", color="white", lw=1), zorder=6)
ax2.text(0, -15.52, "ёроол 10 м", fontsize=6.5, ha="center", va="center", color="white", fontweight="bold", zorder=6)
# хажуугийн дүрс: экскаватор, Хово
def exc_side(ax, x, y, flip=1, z=7):
    f = flip
    def T(p): return [(x + f * a, y + b) for a, b in p]
    ax.add_patch(FancyBboxPatch((x - 2.7, y), 5.4, 1.1, boxstyle="round,pad=0,rounding_size=0.5", fc="#333", ec="k", lw=0.6, zorder=z))
    ax.add_patch(Polygon(T([(-2.4, 1.2), (1.4, 1.2), (1.4, 2.6), (-2.4, 2.9)]), fc="#f2b705", ec="k", lw=0.6, zorder=z))
    ax.add_patch(Polygon(T([(0.0, 2.6), (1.4, 2.6), (1.4, 4.2), (0.1, 4.2)]), fc="#9fc3e6", ec="k", lw=0.6, zorder=z))
    ax.add_patch(Polygon(T([(1.0, 2.0), (1.6, 2.6), (5.2, 6.2), (5.8, 5.6)]), fc="#f2b705", ec="k", lw=0.6, zorder=z))
    ax.add_patch(Polygon(T([(5.2, 6.2), (5.8, 5.6), (8.2, 1.4), (7.6, 1.2)]), fc="#f2b705", ec="k", lw=0.6, zorder=z))
    ax.add_patch(Polygon(T([(7.4, 1.6), (8.6, 1.2), (8.8, 0.1), (7.4, 0.3)]), fc="#555", ec="k", lw=0.6, zorder=z))
def truck_side(ax, x, y, flip=1, z=6, alpha=1):
    f = flip
    def T(p): return [(x + f * a, y + b) for a, b in p]
    ax.add_patch(Polygon(T([(0, 1.0), (9.5, 1.0), (9.5, 1.4), (0, 1.4)]), fc="#333", ec="k", lw=0.5, zorder=z, alpha=alpha))
    ax.add_patch(Polygon(T([(0.0, 1.4), (6.6, 1.4), (6.6, 3.3), (0.6, 3.3), (0.0, 2.6)]), fc="#f2b705", ec="k", lw=0.6, zorder=z, alpha=alpha))
    ax.add_patch(Polygon(T([(7.0, 1.4), (9.5, 1.4), (9.5, 2.8), (9.1, 3.4), (7.0, 3.4)]), fc="#f2b705", ec="k", lw=0.6, zorder=z, alpha=alpha))
    ax.add_patch(Polygon(T([(8.0, 2.5), (9.2, 2.5), (8.9, 3.2), (8.0, 3.2)]), fc="#9fc3e6", ec="k", lw=0.4, zorder=z, alpha=alpha))
    for wx in (1.4, 2.8, 7.3, 8.6):
        ax.add_patch(Circle((x + f * wx, y + 0.55), 0.55, fc="#222", ec="k", lw=0.4, zorder=z + 0.1, alpha=alpha))
def truck_rear(ax, x, y, z=6):
    ax.add_patch(Polygon([(x - 1.25, y + 1.0), (x + 1.25, y + 1.0), (x + 1.25, y + 3.3), (x - 1.25, y + 3.3)], fc="#f2b705", ec="k", lw=0.6, zorder=z))
    ax.add_patch(Polygon([(x - 1.15, y + 3.3), (x + 1.15, y + 3.3), (x + 0.6, y + 4.0), (x - 0.6, y + 4.0)], fc="#a07b45", ec="#5b4220", lw=0.5, zorder=z))
    for wx in (-0.95, -0.4, 0.4, 0.95):
        ax.add_patch(Rectangle((x + wx - 0.26, y), 0.52, 1.1, fc="#222", ec="k", lw=0.3, zorder=z + 0.1))
    ax.text(x, y + 5.0, "Хово 20 м³\n(рамп дээр, араас)", fontsize=6.2, ha="center", color="#333", zorder=6, style="italic")
exc_side(ax2, 2.5, -15, flip=-1)
truck_rear(ax2, 9.6, zr[np.argmin(np.abs(xr - 9.6))])
# рамп огтлолд (баруун, зүүн хананд)
for xx in (xr[np.argmin(np.abs(xr + 13.5))],):
    pass
# рампын тавцан: профайл дахь хэвтээ хэсгийг тэмдэглэх
dz = np.abs(np.gradient(zr, xr))
flat = (dz < 0.2) & (zr < -0.3) & (zr > -14.7) & (np.abs(zr + 5) > 0.3) & (np.abs(zr + 10) > 0.3)
segs = np.split(np.where(flat)[0], np.where(np.diff(np.where(flat)[0]) > 1)[0] + 1)
for sg in segs:
    if len(sg) < 8: continue
    x0s, x1s, zz = xr[sg[0]], xr[sg[-1]], zr[sg].mean()
    ax2.plot([x0s, x1s], [zz + 0.12, zz + 0.12], color=BLUE, lw=3, solid_capstyle="butt", zorder=4)
    lbl((x0s + x1s) / 2 + (0 if x0s < 0 else 7.5), zz + (1.4 if x0s < 0 else 2.2), f"рамп −{abs(zz):.1f} м", fs=6.3)
# өргөний хэмжээс (дээд)
cx0, cx1 = xr[np.argmax(zr < -0.02)], xr[len(zr) - 1 - np.argmax(zr[::-1] < -0.02)]
ax2.annotate("", xy=(cx0 + 0.8, -0.8), xytext=(cx1 - 0.8, -0.8), arrowprops=dict(arrowstyle="<->", color=RED, lw=1))
ax2.text((cx0 + cx1) / 2, -0.25, f"ухмалын дээд өргөн ≈ {cx1 - cx0:.0f} м (А-А)", fontsize=7.5, ha="center",
         color=RED, fontweight="bold", zorder=6)
# бермийн өргөн
lbl(-8.5, -9.0, "берм 2 м ⚠", fs=6)

# ======================= БАРУУН БАГАНА =======================
RX, RWd = 314.0, 96.0
# --- ажлын хэмжээ ---
box(RX, 154, RWd, 122, "АЖЛЫН ХЭМЖЭЭ")
rows = [("1-р шат\n0…−5 м", lay[0]), ("2-р шат\n−5…−10 м", lay[1]), ("3-р шат\n−10…−15 м", lay[2])]
cols = [RX + 2, RX + 22, RX + 41, RX + 60, RX + 77, RX + RWd - 2]
hdr = ["Шат", "Цул,\nм³", "Сул,\nм³", "Хово,\nэргэлт", "Цаг"]
yT = 262
def cell(i, y, s, h=9, fc="white", bold=False, col="k", fs=7.6):
    bg.add_patch(Rectangle((cols[i], y - h), cols[i + 1] - cols[i], h, fc=fc, ec="#9aa7c0", lw=0.5, zorder=3))
    bg.text((cols[i] + cols[i + 1]) / 2, y - h / 2, s, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", color=col, zorder=4, linespacing=1.05)
for i, s in enumerate(hdr): cell(i, yT, s, h=10, fc="#dfe7f5", bold=True, col=NAVY)
y = yT - 10
fmt = lambda v: f"{v:,.0f}".replace(",", " ")
for name, v in rows:
    vals = [name, fmt(v), fmt(v * SW), fmt(np.ceil(v * SW / TRUCK)), f"{v / PROD:.0f}"]
    for i, s in enumerate(vals): cell(i, y, s, h=11)
    y -= 11
tot = [("НИЙТ"), fmt(V), fmt(loose), fmt(np.ceil(loose / TRUCK)), f"{V / PROD:.0f}"]
for i, s in enumerate(tot): cell(i, y, s, h=10, fc=YEL, bold=True, col=NAVY, fs=8.4)
y -= 10
bg.text(RX + RWd / 2, y - 6.5, f"500 экскаватор · Хово 20 м³\n≈ {np.ceil(loose / TRUCK):.0f} эргэлт · ≈ {V / PROD / 10:.0f} ээлж (10 цаг)",
        ha="center", va="center", fontsize=8.2, fontweight="bold", color=NAVY, zorder=4)
bg.text(RX + RWd / 2, y - 17, f"Цулыг газарт 0.25 м тороор тоолсон. Сулралт ×{SW}.\nБүтээмж {PROD:.0f} м³/цаг (⚠ өмнөх зургийн 60–80).",
        ha="center", va="center", fontsize=6.4, color="#333", zorder=4)
# хувилбарын харьцуулалт
yy = y - 26
bg.text(RX + 3, yy, "Рампын хувилбар (хөрс хуулалт):", fontsize=7.4, fontweight="bold", color=NAVY, va="center")
cmp = [("Рампгүй (зөвхөн ухмал)", VN, "#888"), ("Шулуун гадна траншей, 12 %", VS, "#888"),
       ("Ханан дагуу спираль, 15 %", V15, "#888"), ("Ханан дагуу спираль, 12 % ✔", V, NAVY)]
for k, (s, v, c) in enumerate(cmp):
    yk = yy - 5.2 - k * 4.6
    bg.text(RX + 4, yk, s, fontsize=6.7, color=c, va="center", fontweight="bold" if c == NAVY else "normal")
    bg.text(RX + RWd - 4, yk, fmt(v) + " м³", fontsize=6.7, color=c, va="center", ha="right",
            fontweight="bold" if c == NAVY else "normal")

# --- тэмдэглэгээ ---
box(RX, 104, RWd, 47, "ТЭМДЭГЛЭГЭЭ", tsize=10)
leg = [("line", RED, "-", 2.2, "Ухмалын хил (дээд ирмэг)"),
       ("line", BLUE, (0, (6, 3)), 1.4, "Рампын тэнхлэг (6 м, 12 %)"),
       ("line", "#888", (0, (5, 2)), 1.0, "Шатны ирмэг (берм)"),
       ("rect", "#c79a5b", None, None, "Шороо буулгах талбай"),
       ("line", "k", (0, (10, 2, 2, 2)), 0.8, "Огтлолын шугам А-А")]
for k, (t, c, lsy, lw, s) in enumerate(leg):
    yk = 137 - k * 7.0
    if t == "line":
        bg.plot([RX + 4, RX + 20], [yk, yk], color=c, ls=lsy, lw=lw, zorder=4)
    else:
        bg.add_patch(Rectangle((RX + 4, yk - 2), 16, 4, fc=c, ec="#6b4a22", hatch="////", lw=0.6, zorder=4))
    bg.text(RX + 24, yk, s, fontsize=7.6, va="center", zorder=4)

# --- хөрс хуулалтыг багасгасан шийдэл ---
box(RX, 63, RWd, 38, "ХӨРС ХУУЛАЛТЫГ БАГАСГАСАН", tsize=8.6)
pts_ = ["Рамп ханан дагуу спираль: шулуун\nтраншейгаас " + fmt(VS - V) + " м³ бага",
        "Ёроол 10 × 10 м: экскаватор + ухарч\nорох Хово-д хүрэлцэх хамгийн бага",
        "2, 3-р шат 60°, берм 2 м (⚠ батлах)",
        "Овоолго рампын амнаас ойр, 1 зам"]
for k, s in enumerate(pts_):
    yk = 90 - k * 7.2
    bg.add_patch(Circle((RX + 5, yk + (1.2 if "\n" in s else 0)), 1.7, fc="#2e9e44", ec="none", zorder=4))
    bg.text(RX + 5, yk + (1.2 if "\n" in s else 0), "✓", color="white", fontsize=7, ha="center", va="center", fontweight="bold", zorder=5)
    bg.text(RX + 8.5, yk, s, fontsize=6.6, va="center", zorder=4, linespacing=1.1)

# ======================= ДООД МӨР =======================
box(22, 7, 205, 53, "АЖЛЫН ДАРААЛАЛ · АНХААРАХ", tsize=10)
steps = [("1", "Шимт хөрс хуулж, хил тэмдэглэнэ.\n1-р шатыг (0…−5 м, 45°) газрын\nтүвшнээс ухна, Хово дээр ачна."),
         ("2", "Рампын эхний тойргийг зүсэж,\n2-р шатыг (−5…−10 м) ухна.\nБерм 2 м үлдээнэ."),
         ("3", "3-р шат (−10…−15 м), ёроол 10×10.\nХово рампын хөлөөс ёроол руу\nухарч орж ачигдана."),
         ("4", "Шороог буулгах талбайд 2 үеэр\n(2 × 5 м) асгаж, бульдозероор\nтэгшилнэ.")]
for k, (n, s) in enumerate(steps):
    x = 25 + k * 50.5
    bg.add_patch(Circle((x + 3.5, 46), 3, fc=NAVY, ec="none", zorder=4))
    bg.text(x + 3.5, 46, n, color="white", fontsize=9, ha="center", va="center", fontweight="bold", zorder=5)
    bg.text(x + 8, 46, s, fontsize=6.3, va="center", zorder=4, linespacing=1.15)
    if k < 3:
        bg.annotate("", xy=(x + 50, 46), xytext=(x + 47.5, 46), arrowprops=dict(arrowstyle="-|>", color=YEL, lw=2), zorder=5)
bg.add_patch(FancyBboxPatch((25, 9.5), 199, 25, boxstyle="round,pad=0,rounding_size=1.5", fc="#fdecea", ec=RED, lw=1, zorder=3))
warn = ["⚠ Таамаг: 2, 3-р шатны 60°, берм 2 м — геотехникийн дүгнэлтээр батлах. Хэрэв бүх шат 45° бол эзэлхүүн өснө.",
        "⚠ Рамп 12 % (6.8°): ачаатай Хово-д зөвшөөрөгдөх дээд хязгаарт ойр; гадна ирмэгт 1 м хамгаалалтын далан хийнэ.",
        "⚠ 6 м рамп нэг эгнээтэй: дээр, доор зөрөх талбай (≥ 10 м) гаргана. Ёроолд Хово эргэхгүй — ухарч орно.",
        "⚠ Овоолгын хормой ухмалын ирмэгээс ≥ 13 м зайтай (нурах призм). Ус зайлуулах зумф ёроолын нэг буланд."]
for k, s in enumerate(warn):
    bg.text(28, 30.5 - k * 5.6, s, fontsize=6.5, va="center", color="#7a1010", zorder=4)

draw_stamp(fig, PW, PH, right_mm=PW - 5, bottom_mm=5, info=dict(
    client="",
    project="15 м гүн, 3 шатлалтай ухмалын\nзохион байгуулалт (10 × 10 м ёроол,\nспираль рамп, шороо буулгах талбай)",
    title="Ухмалын план, хөндлөн огтлол А-А",
    paper="A3", scale="1:500; 1:200", total="1", number="1", license=""), fs=9)

os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, NAME + ".png"), dpi=200)
fig.savefig(os.path.join(OUT, NAME + ".pdf"))
print("ok")
