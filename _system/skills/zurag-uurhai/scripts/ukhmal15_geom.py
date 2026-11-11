"""Жижиг шатлалтай ухмал + налуу зам (рамп): геометр, эзэлхүүн (DEPTH = 15, 20 … м, 5 м-ийн шат).
Хувилбарыг тоон аргаар (0.25 м тор) харьцуулна: шулуун гадна траншей vs хананд зүсэх спираль.
Нэгж: м. Ёроолын төв (0,0). Гүн эерэг (0 = газрын гадарга)."""
import numpy as np

# ---- параметр (таамаг нь ⚠) ----
DEPTH = 15.0         # ухмалын (рамп хүрэх) гүн
BOT = 10.0           # ёроол 10 × 10 м (лавлагаа зураг)
H = 5.0              # шатны өндөр
A1 = 45.0            # 1-р шат (0…-5 м), хөрс/өгөршсөн — даалгавар
A23 = 60.0           # доод шатууд, чулуулаг — ⚠ таамаг
BERM = 2.0           # хамгаалалтын тавцан — ⚠ таамаг
RW = 6.0             # рампын өргөн (лавлагаа зураг)
GRADE = 0.12         # рампын налуу
SWELL = 1.3          # сулралт
CELL = 0.25
SWITCH = 0.0         # энэ гүнээс дээш рамп шулуун гадагш гарна (0 = бүтэн спираль)

t1, t23 = 1 / np.tan(np.radians(A1)), 1 / np.tan(np.radians(A23))


def wall_depth(d0, r):
    """d0 гүнтэй тавцангаас r м гадагш: налуу хананы гүн (бермгүй, хөрс 45°, чулуу 60°)."""
    r = np.maximum(r, 0)
    rock = max(d0 - H, 0)
    r_rock = rock * t23
    return np.where(r <= r_rock, d0 - r / t23, H - (r - r_rock) / t1)


def profile():
    """(r, гүн) тасархай шугам: ёроолоос гадагш, шат бүр H, доод шатууд 60°, дээд 45°, берм."""
    n = int(round(DEPTH / H))
    r, d = [0.0], [DEPTH]
    for i in range(n):
        top = DEPTH - (i + 1) * H
        r.append(r[-1] + H * (t1 if top <= 0 + 1e-9 else t23)); d.append(top)
        if top > 0:
            r.append(r[-1] + BERM); d.append(top)
    return np.array(r), np.array(d)


def pit_depth(r):
    R, Dp = profile()
    r = np.maximum(r, 0)
    return np.interp(r, R, Dp, right=0.0), tuple(R[1:])


def rect_dist(X, Y, half):
    dx = np.maximum(np.abs(X) - half, 0); dy = np.maximum(np.abs(Y) - half, 0)
    return np.hypot(dx, dy)


def r_wall(dd):
    """Тухайн гүн дэх (рампгүй) ханын хөлийн зай. Берм дээр дотор ирмэгийг авна."""
    R, Dp = profile()
    # гүн буурах дарааллаар: interp-д өсөх x хэрэгтэй тул -Dp
    return np.interp(-dd, -Dp, R)


def ramp_samples(kind):
    L = DEPTH / GRADE
    s = np.arange(0, L + 0.25, 0.25)
    d = DEPTH - GRADE * s
    if kind == "straight":
        return np.c_[-BOT / 2 - s, np.zeros_like(s), d]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    k = 0
    half0 = BOT / 2 + r_wall(DEPTH) + RW / 2
    x, y = -BOT / 2, -half0
    pts = [(x, y, DEPTH)]
    ds = s[1] - s[0]
    for dd in d[1:]:
        half = BOT / 2 + r_wall(dd) + RW / 2
        dx, dy = dirs[k]
        x += dx * ds; y += dy * ds
        if dd < SWITCH:
            pts.append((x, y, dd)); continue
        if k == 0: y = -half
        elif k == 1: x = half
        elif k == 2: y = half
        else: x = -half
        if (k == 0 and x >= half) or (k == 1 and y >= half) or (k == 2 and x <= -half) or (k == 3 and y <= -half):
            k = (k + 1) % 4
        pts.append((x, y, dd))
    return np.array(pts)


def surface(kind, ext=90):
    xs = np.arange(-ext, ext, CELL)
    X, Y = np.meshgrid(xs, xs)
    D, _ = pit_depth(rect_dist(X, Y, BOT / 2))
    if kind != "none":
        for x, y, dd in ramp_samples(kind)[::2]:
            r = np.hypot(X - x, Y - y) - RW / 2
            m = r < 45
            Dr = np.where(r <= 0, dd, wall_depth(dd, r))
            D = np.where(m, np.maximum(D, np.maximum(Dr, 0)), D)
    return X, Y, np.maximum(D, 0)


def volumes(D):
    a = CELL ** 2
    tot = D.sum() * a
    layers = [np.clip(D - lo, 0, H).sum() * a for lo in np.arange(0, DEPTH, H)]
    return tot, layers


def sample_hole(depth=5.0, bot=3.0, ang=60.0):
    """Ёроолоос экскаватороор ухах дээжний нүх: дөрвөлжин зүсэгдсэн пирамид."""
    top = bot + 2 * depth / np.tan(np.radians(ang))
    a1, a2 = bot ** 2, top ** 2
    return depth / 3 * (a1 + a2 + np.sqrt(a1 * a2)), top


if __name__ == "__main__":
    import sys
    DEPTH = float(sys.argv[1]) if len(sys.argv) > 1 else 15.0
    for g in (0.12, 0.15):
        GRADE = g
        X, Y, D = surface("spiral")
        tot, lay = volumes(D)
        print(f"depth {DEPTH} grade {g:.0%} spiral V={tot:8.0f}  layers={[round(v) for v in lay]}")
