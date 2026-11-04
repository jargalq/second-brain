"""Грийтвишн ХХК-ийн зургийн булангийн хүснэгт (штамп), 185 × 55 мм.
Эх загвар: 072 Haitan, 4.zurag/pdf_2026 (2026 онд ЭБМЗ-д өгсөн ТЭЗҮ-ийн хавсралт зураг).

Хэрэглээ (matplotlib):
    import sys; sys.path.insert(0, r"D:\\Seond brain\\_system\\skills\\zurag-shtamp")
    from gv_stamp import draw_stamp
    draw_stamp(fig, page_w_mm=420, page_h_mm=297, right_mm=415, bottom_mm=5, info={...})
right_mm, bottom_mm: хүрээний (рамкийн) баруун доод булан, хуудасны зүүн доод булангаас мм-ээр.
"""
import os
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 185.0, 55.0
FONT = dict(family="Times New Roman", style="italic")

DEFAULT = dict(
    authority="Аж үйлдвэр, эрдэс баялгийн яам\nАшигт малтмал, газрын тосны газар\nЭрдэс баялгийн мэргэжлийн зөвлөл",
    client="",              # Захиалагч, ж: '"ХӨХ ТОЙН" ХХК'
    project="",             # 4 мөр хүртэл: '<аймаг> <сум>-ын нутагт орших "<орд>" ... техник, эдийн засгийн үндэслэл'
    title="",               # Зургийн нэр, 2 мөр хүртэл
    paper="A3", scale="1:1000", total="", number="",
    license="",             # Тусгай зөвшөөрлийн дугаар
    # 6 мөр хүртэл: А.туш, Овог нэр, Г.үсэг, Огноо. Үндсэн утгыг хэрэглэгч 2026-10-30-нд зааж өгсөн.
    signers=[("Инженер", "Т.Давааням", "", ""), ("Инженер", "Ч.Аръяабал", "", "")],
    logo=os.path.join(HERE, "gv_logo.png"),
)

# Баганын хил (штампын зүүн захаас, мм)
XL = [0, 17.5, 46.0, 57.5, 67.5]      # А.туш | Овог, нэр | Г.үсэг | Огноо
XM = 137.5                             # дунд хэсгийн баруун хил
XR = 164.0                             # Цаасны хэмжээ | Масштаб


def draw_stamp(fig, page_w_mm, page_h_mm, right_mm, bottom_mm, info, fs=10):
    d = dict(DEFAULT); d.update(info)
    x0, y0 = right_mm - W, bottom_mm
    ax = fig.add_axes([x0 / page_w_mm, y0 / page_h_mm, W / page_w_mm, H / page_h_mm])
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), W, H, fc="white", ec="none", zorder=0))

    def ln(xa, ya, xb, yb, lw=0.6):
        ax.plot([xa, xb], [ya, yb], color="k", lw=lw, solid_capstyle="butt", clip_on=False)

    rend = fig.canvas.get_renderer()
    mm_per_px = W / ax.get_window_extent(rend).width

    def tx(x, y, s, size=fs, ha="center", maxw=None, **kw):
        """maxw (мм) өгвөл бичвэр нүдэнд багтах хүртэл фонтыг багасгана."""
        t = ax.text(x, y, s, fontsize=size, ha=ha, va="center", linespacing=1.15, **FONT, **kw)
        while maxw and size > 5 and t.get_window_extent(rend).width * mm_per_px > maxw:
            size -= 0.25; t.set_fontsize(size)
        return t

    # шугам
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, lw=1.2, ec="k", clip_on=False))
    ln(0, 35, W, 35)
    ln(XL[4], 15, XM, 15)
    ln(XL[4], 0, XL[4], H); ln(XM, 0, XM, H)
    for y in (30, 25, 20, 15, 10, 5):
        ln(0, y, XL[4], y, 0.4)
    for x in XL[1:4]:
        ln(x, 0, x, 35, 0.4)
    ln(XM, 30, W, 30); ln(XM, 20, W, 20); ln(XM, 15, W, 15)
    ln(XR, 15, XR, 35)

    # Гүйцэтгэгч + лого
    tx(1.5, 52, "Гүйцэтгэгч:", ha="left")
    if d["logo"] and os.path.exists(d["logo"]):
        im = mpimg.imread(d["logo"])
        h_mm = 13.0; w_mm = h_mm * im.shape[1] / im.shape[0]
        if w_mm > XL[4] - 4:
            w_mm = XL[4] - 4; h_mm = w_mm * im.shape[0] / im.shape[1]
        lx = (XL[4] - w_mm) / 2; ly = 36.5
        ax.imshow(im, extent=(lx, lx + w_mm, ly, ly + h_mm), interpolation="lanczos", zorder=2)
    # гарын үсгийн хүснэгт
    for j, s in enumerate(("А.туш", "Овог, нэр", "Г.үсэг", "Огноо")):
        tx((XL[j] + XL[j + 1]) / 2, 32.5, s, size=fs - 0.5, maxw=XL[j + 1] - XL[j] - 0.8)
    for i, row in enumerate(list(d["signers"])[:6]):
        y = 27.5 - 5 * i
        for j, s in enumerate(row):
            if s:
                tx(XL[j] + 0.8, y, s, size=fs - 0.5, ha="left", maxw=XL[j + 1] - XL[j] - 1.2)
    # дунд хэсэг
    cm, wm = (XL[4] + XM) / 2, XM - XL[4] - 3
    tx(cm, 45, d["authority"], size=fs - 0.5, maxw=wm)
    tx(cm, 25, d["project"], size=fs - 0.5, maxw=wm)
    tx(cm, 7.5, d["title"], size=fs, maxw=wm)
    # баруун хэсэг
    cr, wr = (XM + W) / 2, W - XM - 3
    tx(XM + 1.5, 52, "Захиалагч:", ha="left")
    tx(cr, 43, d["client"], size=fs, maxw=wr)
    tx((XM + XR) / 2, 32.5, "Цаасны хэмжээ", size=fs - 1, maxw=XR - XM - 1.5)
    tx((XR + W) / 2, 32.5, "Масштаб", size=fs - 1, maxw=W - XR - 1.5)
    tx((XM + XR) / 2, 25, d["paper"])
    tx((XR + W) / 2, 25, d["scale"])
    tx((XM + XR) / 2, 17.5, "Нийт зураг: %s" % d["total"], size=fs - 1, maxw=XR - XM - 1.5)
    tx((XR + W) / 2, 17.5, "Зураг: №%s" % d["number"], size=fs - 1, maxw=W - XR - 1.5)
    tx(cr, 7.5, "Тусгай зөвшөөрлийн дугаар:\n%s" % d["license"], size=fs - 0.5, maxw=wr)
    return ax
