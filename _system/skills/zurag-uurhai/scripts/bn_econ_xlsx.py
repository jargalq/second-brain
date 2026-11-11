# Баруун наран — 10 жилийн эдийн засгийн загвар (томьёотой Excel)
# Эх сурвалж: БН ТЭЗҮ 10-р бүлэг (хүснэгт 10.1–10.4), bn_econ_rebuild.py, 2026-11-06-ны шийдвэр (10 жил)
# Ажиллуулах: python -I bn_econ_xlsx.py <гаралтын.xlsx>
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.comments import Comment

OUT = sys.argv[1]
BLUE = Font(name="Arial", size=10, color="0000FF")
BLACK = Font(name="Arial", size=10)
GREEN = Font(name="Arial", size=10, color="008000")
BOLD = Font(name="Arial", size=10, bold=True)
H1 = Font(name="Arial", size=12, bold=True)
YEL = PatternFill("solid", fgColor="FFFF00")
HEAD = PatternFill("solid", fgColor="D9E1F2")
thin = Side(style="thin", color="BFBFBF")
BOX = Border(top=thin, bottom=thin, left=thin, right=thin)
NUM = '#,##0.0;(#,##0.0);"-"'
NUM0 = '#,##0;(#,##0);"-"'
PCT = '0.0%;(0.0%);"-"'

wb = Workbook()

# ---------------- Оролт ----------------
s = wb.active; s.title = "Оролт"
s["A1"] = "Баруун наран — эдийн засгийн оролт (10 жил, 2027–2036)"; s["A1"].font = H1
s["A2"] = "Цэнхэр = оролт (засаж болно), шар = гол таамаглал, хар = томьёо. Мөнгөн дүн сая ₮."
s["A2"].font = Font(name="Arial", size=9, italic=True)
inp = {}
def put(r, label, val, unit, src, key, fmt=NUM, key_assump=False):
    s.cell(r, 1, label).font = BLACK
    c = s.cell(r, 2, val); c.font = BLUE if not str(val).startswith("=") else BLACK
    c.number_format = fmt
    if key_assump: c.fill = YEL
    s.cell(r, 3, unit).font = BLACK
    s.cell(r, 4, src).font = Font(name="Arial", size=9, color="595959")
    inp[key] = f"Оролт!$B${r}"
r = 4
s.cell(r, 1, "Ерөнхий").font = BOLD; r += 1
put(r, "Хөнгөлөлтийн хувь", 0.10, "", "ТЭЗҮ 10.6", "disc", PCT, True); r += 1
put(r, "Ашиглалтын хугацаа", 10, "жил", "Шийдвэр 2026-11-06 (Mugi)", "years", NUM0); r += 1
put(r, "Чулууны нягт", 2.69, "т/м³", "ТЭЗҮ 3-р бүлэг", "dens", "0.000"); r += 1
put(r, "Бүтээгдэхүүний овроглог нягт", 1.355, "т/м³ сэвсгэр", "ТЭЗҮ 10.1", "bulk", "0.000"); r += 1
put(r, "НӨАТ", 0.10, "", "Хууль", "vat", PCT); r += 1
put(r, "АМНАТ (орлогоос)", 0.025, "", "ТЭЗҮ 10.3 ⚠ суурь үнэ", "amnat", PCT); r += 1
put(r, "ААНОАТ — доод шат", 0.10, "", "ТЭЗҮ 10.4", "cit1", PCT); r += 1
put(r, "ААНОАТ — дээд шат", 0.25, "", "ТЭЗҮ 10.4", "cit2", PCT); r += 1
put(r, "ААНОАТ — шатны хязгаар", 6000, "сая ₮", "ТЭЗҮ 10.4", "citlim", NUM0); r += 1
put(r, "Өрөмдлөг, тэсэлгээ (гэрээт)", 5000, "₮/м³ цул", "ТЭЗҮ 10.3 ⚠ гүйцэтгэгчийн санал", "drill", NUM0, True); r += 1
put(r, "Бусад зардал (OPEX-ийн)", 0.05, "", "ТЭЗҮ 10.3", "other", PCT); r += 1
r += 1
s.cell(r, 1, "Бүтээгдэхүүн, үнэ (уурхайн ам, НӨАТ-тай)").font = BOLD; r += 1
for j, h in enumerate(["Фракц", "Гарц", "Үнэ, ₮/м³ сэвсгэр", "Жигнэсэн, ₮/м³"]):
    c = s.cell(r, 1 + j, h); c.font = BOLD; c.fill = HEAD
r += 1
fr0 = r
for name, y, p in [("20–40 мм", .526, 70000), ("10–20 мм", .335, 65000), ("5–10 мм", .087, 35000), ("0–5 мм", .052, 5000)]:
    s.cell(r, 1, name).font = BLACK
    c = s.cell(r, 2, y); c.font = BLUE; c.number_format = PCT
    c = s.cell(r, 3, p); c.font = BLUE; c.number_format = NUM0; c.fill = YEL
    c = s.cell(r, 4, f"=B{r}*C{r}"); c.font = BLACK; c.number_format = NUM0
    r += 1
s.cell(r, 1, "Нийт / жигнэсэн").font = BOLD
c = s.cell(r, 2, f"=SUM(B{fr0}:B{r-1})"); c.number_format = PCT; c.font = BOLD
c = s.cell(r, 4, f"=SUM(D{fr0}:D{r-1})"); c.number_format = NUM0; c.font = BOLD
inp["wprice"] = f"Оролт!$D${r}"
s.cell(r, 5, "Шийдвэр 2026-11-05 «Баруун наран бүтээгдэхүүний үнэ». Бүгдийг зарна гэсэн таамаглал 🔴").font = Font(name="Arial", size=9, color="595959")
r += 2
s.cell(r, 1, "Хөрөнгө оруулалт (0-р жил, 2026)").font = BOLD; r += 1
for j, h in enumerate(["Бүлэг", "сая ₮", "Элэгдэл, жил", "Эх сурвалж"]):
    c = s.cell(r, 1 + j, h); c.font = BOLD; c.fill = HEAD
r += 1
cx0 = r
for name, v, life, src in [
    ("Уурхайн техник", 1768.0, 10, "R380LC-9 600 ⚠ · HOWO×4 632 · LG855H×2 376 · SD-13 160 ⚠"),
    ("Бутлан ангилах шугам", 1358.2, 10, "Excel v1 + PVMC-380"),
    ("Кемп (46 ор)", 679.0, 40, "Зүүн нарангийн кемп v5 ⚠"),
    ("Бусад барилга", 371.0, 40, "Excel v1"),
    ("Бусад тоног төхөөрөмж", 1202.0, 10, "Зүүн наран v4.1 ⚠"),
    ("Тооцоологдоогүй 10 %", 120.2, 10, "бусад тоног төхөөрөмжийн"),
    ("Биет бус хөрөнгө", 477.0, 10, "ТЭЗҮ, БОННҮ, хайгуул, зам, сайрын хоолой ⚠"),
]:
    s.cell(r, 1, name).font = BLACK
    c = s.cell(r, 2, v); c.font = BLUE; c.number_format = NUM
    c = s.cell(r, 3, life); c.font = BLUE; c.number_format = NUM0
    s.cell(r, 4, src).font = Font(name="Arial", size=9, color="595959")
    r += 1
cx1 = r - 1
s.cell(r, 1, "Нийт CAPEX").font = BOLD
c = s.cell(r, 2, f"=SUM(B{cx0}:B{cx1})"); c.font = BOLD; c.number_format = NUM
inp["capex"] = f"Оролт!$B${r}"
r += 1
s.cell(r, 1, "Жилийн элэгдэл (1–10-р жил)").font = BLACK
c = s.cell(r, 2, f"=SUMPRODUCT(B{cx0}:B{cx1}/C{cx0}:C{cx1})"); c.number_format = NUM
inp["dep"] = f"Оролт!$B${r}"
s.cell(r, 4, "Шулуун шугамын арга").font = Font(name="Arial", size=9, color="595959")
r += 1
s.cell(r, 1, "2036 оны эцсийн үлдэгдэл өртөг (барилга)").font = BLACK
c = s.cell(r, 2, f"=SUMPRODUCT(B{cx0}:B{cx1}*(C{cx0}:C{cx1}>{'Оролт!$B$6'})*(1-{'Оролт!$B$6'}/C{cx0}:C{cx1}))"); c.number_format = NUM
s.cell(r, 4, "Мэдээллийн зорилгоор, NPV-д ороогүй ⚠").font = Font(name="Arial", size=9, color="595959")
s.column_dimensions["A"].width = 40; s.column_dimensions["B"].width = 12
s.column_dimensions["C"].width = 18; s.column_dimensions["D"].width = 16; s.column_dimensions["E"].width = 40

# ---------------- OPEX ----------------
o = wb.create_sheet("OPEX")
o["A1"] = "Үйл ажиллагааны зардал (сая ₮/жил) — ТЭЗҮ хүснэгт 10.2"; o["A1"].font = H1
for j, h in enumerate(["Зардал", "1-р жил", "2–10-р жил", "Үндэслэл"]):
    c = o.cell(3, 1 + j, h); c.font = BOLD; c.fill = HEAD
items = [
    ("Цалин", 997.4, 954.6, "48 / 46 хүн × 20.78 сая ₮/улирал ⚠"),
    ("НДШ 14.5 %", 144.6, 138.4, "⚠ одоо мөрдөж буй хувь"),
    ("Хүнс", 347.1, 333.9, "35 000 ₮/хүн/хоног; өвөл 6 хүн"),
    ("Түлш (хөдөлгөөнт техник)", 731.7, 639.9, "215 / 188 мян л × 3 400 ₮ ⚠"),
    ("Тос, шүүр", 256.1, 224.0, "түлшний 35 %"),
    ("Цахилгаан (дизель генератор)", 1369.9, 1368.8, "бутлуур 204 000 л + кемп 131 760 л ⚠"),
    ("Дугуй", 43.0, 42.9, "⚠"),
    ("Сэлбэг", 431.2, 430.6, "уурхай, бутлуур 10 %, бусад 5 %"),
    ("ХАБЭА", 66.3, 63.6, "1.38 сая ₮/хүн (7.5)"),
    ("Оффис, орон нутаг, байгаль орчин", 65.7, 65.7, "Зүүн наран v4.1"),
    ("Нөхөн сэргээлт, хаалт", 114.0, 114.0, "1 140.44 сая ₮ / 10 жил ⚠ 28.4 га-д дахин тооцох"),
    ("Татвар, төлбөр (тээврийн, ТЗ, газар, ус)", 69.5, 69.5, "Excel v1"),
]
r = 4
for name, a, b, src in items:
    o.cell(r, 1, name).font = BLACK
    for col, v in ((2, a), (3, b)):
        c = o.cell(r, col, v); c.font = BLUE; c.number_format = NUM
    o.cell(r, 4, src).font = Font(name="Arial", size=9, color="595959")
    r += 1
o.cell(r, 1, "Тогтмол зардлын дүн (өрөмдлөг, бусад 5 %-гүй)").font = BOLD
for col in (2, 3):
    c = o.cell(r, col, f"=SUM({L(col)}4:{L(col)}{r-1})"); c.font = BOLD; c.number_format = NUM
FIX1 = f"OPEX!$B${r}"; FIX2 = f"OPEX!$C${r}"
r += 2
o.cell(r, 1, "Өрөмдлөг, тэсэлгээ = чулуу × Оролтын нэгж үнэ; Бусад 5 % = (тогтмол + өрөмдлөг) × 5 %. Жил бүрээр «Мөнгөн урсгал» хуудсанд.").font = Font(name="Arial", size=9, italic=True)
o.column_dimensions["A"].width = 44; o.column_dimensions["B"].width = 12; o.column_dimensions["C"].width = 12; o.column_dimensions["D"].width = 50

# ---------------- Мөнгөн урсгал ----------------
m = wb.create_sheet("Мөнгөн урсгал")
m["A1"] = "Мөнгөн урсгал (сая ₮) — 0-р жил 2026, 1-р жил 2027, 10-р жил 2036"; m["A1"].font = H1
STONE = [200033, 199731, 199988, 200133, 200015, 199923, 200004, 200292, 200159, 199527]
m.cell(3, 1, "Жил").font = BOLD; m.cell(3, 1).fill = HEAD
m.cell(4, 1, "Он").font = BOLD; m.cell(4, 1).fill = HEAD
for t in range(11):
    col = 2 + t
    c = m.cell(3, col, t); c.font = BOLD; c.fill = HEAD; c.alignment = Alignment(horizontal="center")
    c = m.cell(4, col, str(2026 + t)); c.font = BOLD; c.fill = HEAD; c.alignment = Alignment(horizontal="center")
c = m.cell(3, 13, "Нийт"); c.font = BOLD; c.fill = HEAD
rows = {}
labels = [
    ("stone", "Олборлох чулуу, м³ цул", NUM0),
    ("prod", "Бүтээгдэхүүн, мян м³ сэвсгэр", NUM),
    ("rev", "Орлого (НӨАТ-гүй)", NUM0),
    ("amnat", "АМНАТ", NUM0),
    ("fix", "OPEX — тогтмол", NUM0),
    ("drill", "OPEX — өрөмдлөг, тэсэлгээ", NUM0),
    ("oth", "OPEX — бусад 5 %", NUM0),
    ("opex", "OPEX нийт", NUM0),
    ("dep", "Элэгдэл", NUM0),
    ("ebt", "Татварын өмнөх ашиг", NUM0),
    ("cit", "ААНОАТ", NUM0),
    ("ni", "Цэвэр ашиг", NUM0),
    ("capex", "Хөрөнгө оруулалт", NUM0),
    ("cf", "Цэвэр мөнгөн урсгал", NUM0),
    ("cum", "Хуримтлагдсан", NUM0),
    ("pb", "Нөхөх хугацааны туслах", "0.00"),
    ("vat", "НӨАТ (мэдээлэл)", NUM0),
]
for i, (k, lab, _) in enumerate(labels):
    rows[k] = 5 + i
    m.cell(5 + i, 1, lab).font = BOLD if k in ("cf", "opex", "ni") else BLACK
R = rows
for t in range(11):
    col = 2 + t; X = L(col); P = L(col - 1)
    f = {}
    if t == 0:
        f["capex"] = f"=-{inp['capex']}"
        f["cf"] = f"={X}{R['capex']}"
        f["cum"] = f"={X}{R['cf']}"
    else:
        f["stone"] = STONE[t - 1]
        f["prod"] = f"={X}{R['stone']}*{inp['dens']}/{inp['bulk']}/1000"
        f["rev"] = f"={X}{R['prod']}*1000*{inp['wprice']}/(1+{inp['vat']})/1000000"
        f["amnat"] = f"={X}{R['rev']}*{inp['amnat']}"
        f["fix"] = f"={FIX1 if t == 1 else FIX2}"
        f["drill"] = f"={X}{R['stone']}*{inp['drill']}/1000000"
        f["oth"] = f"=({X}{R['fix']}+{X}{R['drill']})*{inp['other']}"
        f["opex"] = f"={X}{R['fix']}+{X}{R['drill']}+{X}{R['oth']}"
        f["dep"] = f"={inp['dep']}"
        f["ebt"] = f"={X}{R['rev']}-{X}{R['amnat']}-{X}{R['opex']}-{X}{R['dep']}"
        e = f"{X}{R['ebt']}"
        f["cit"] = f"=IF({e}<=0,0,IF({e}<={inp['citlim']},{e}*{inp['cit1']},{inp['citlim']}*{inp['cit1']}+({e}-{inp['citlim']})*{inp['cit2']}))"
        f["ni"] = f"={e}-{X}{R['cit']}"
        f["cf"] = f"={X}{R['ni']}+{X}{R['dep']}"
        f["cum"] = f"={P}{R['cum']}+{X}{R['cf']}"
        f["pb"] = f"=IF(AND({P}{R['cum']}<0,{X}{R['cum']}>=0),{P}3-{P}{R['cum']}/{X}{R['cf']},0)"
        f["vat"] = f"={X}{R['rev']}*{inp['vat']}"
    for k, v in f.items():
        c = m.cell(R[k], col, v)
        c.font = BLUE if k == "stone" else (GREEN if k in ("fix", "dep") or (k == "capex") else BLACK)
        c.number_format = dict((a, b) for a, _, b in labels)[k]
        if k == "cf": c.font = Font(name="Arial", size=10, bold=True)
for k in ("stone", "prod", "rev", "amnat", "opex", "dep", "ebt", "cit", "ni", "capex", "cf", "vat"):
    c = m.cell(R[k], 13, f"=SUM(B{R[k]}:L{R[k]})"); c.font = BOLD; c.number_format = dict((a, b) for a, _, b in labels)[k]
m.cell(R["stone"], 2).comment = Comment("Календарийн зураг №7, №9–13 (ТЭЗҮ 4.7). 10 жилд ≈ 2.0 сая м³; уурхайн хүрээнд 226 557 м³ дараагийн шатанд үлдэнэ.", "Claude")
r = R["vat"] + 2
m.cell(r, 1, "Үр ашгийн үзүүлэлт").font = H1; r += 1
res = {}
for lab, fml, fmt in [
    ("NPV (хөнгөлөлт Оролтод)", f"=B{R['cf']}+NPV({inp['disc']},C{R['cf']}:L{R['cf']})", NUM0),
    ("IRR", f"=IRR(B{R['cf']}:L{R['cf']})", PCT),
    ("Нөхөх хугацаа, жил", f"=SUM(C{R['pb']}:L{R['pb']})", "0.00"),
    ("Нийт цэвэр ашиг", f"=M{R['ni']}", NUM0),
    ("Нийт цэвэр мөнгөн урсгал", f"=M{R['cf']}", NUM0),
]:
    m.cell(r, 1, lab).font = BOLD
    c = m.cell(r, 2, fml); c.font = BOLD; c.number_format = fmt; c.fill = HEAD
    res[lab] = f"'Мөнгөн урсгал'!$B${r}"; r += 1
r += 1
m.cell(r, 1, "Улсын төсөвт (ашиглалтын хугацаанд)").font = H1; r += 1
t0 = r
for lab, fml in [
    ("НӨАТ", f"=M{R['vat']}"),
    ("ААНОАТ", f"=M{R['cit']}"),
    ("АМНАТ", f"=M{R['amnat']}"),
    ("НДШ (ажил олгогчийн)", "=OPEX!B5+OPEX!C5*9"),
    ("ТЗ, газар, ус, тээврийн татвар", "=OPEX!B15+OPEX!C15*9"),
]:
    m.cell(r, 1, lab).font = BLACK
    c = m.cell(r, 2, fml); c.number_format = NUM0; r += 1
m.cell(r, 1, "Нийт").font = BOLD
c = m.cell(r, 2, f"=SUM(B{t0}:B{r-1})"); c.font = BOLD; c.number_format = NUM0
m.column_dimensions["A"].width = 34
for col in range(2, 14): m.column_dimensions[L(col)].width = 10.5
m.freeze_panes = "B5"

# ---------------- Мэдрэмж ----------------
z = wb.create_sheet("Мэдрэмж")
z["A1"] = "Мэдрэмж: NPV (сая ₮). Хүчин зүйл бүрийг тусад нь өөрчилнө."; z["A1"].font = H1
z["A2"] = "Үнэ ба борлуулалтын хэмжээ орлого, АМНАТ-д ижил нөлөөтэй. ААНОАТ-ыг хувилбар бүрд дахин тооцно."
z["A2"].font = Font(name="Arial", size=9, italic=True)
for j, h in enumerate(["Хүчин зүйл", "−20 %", "−10 %", "Суурь", "+10 %", "+20 %"]):
    c = z.cell(4, 1 + j, h); c.font = BOLD; c.fill = HEAD
for j, v in enumerate([0.8, 0.9, 1.0, 1.1, 1.2]):
    c = z.cell(5, 2 + j, v); c.font = BLUE; c.number_format = PCT
z.cell(5, 1, "Коэффициент").font = BLACK
MC = "'Мөнгөн урсгал'!"
def npv_expr(fp, fo, fc):
    # жил бүрийн CF-ийг томьёонд задлан бичнэ
    parts = []
    for t in range(1, 11):
        X = L(2 + t)
        rev = f"{MC}{X}{R['rev']}*{fp}"
        am = f"{MC}{X}{R['amnat']}*{fp}"
        ox = f"{MC}{X}{R['opex']}*{fo}"
        dp = f"{MC}{X}{R['dep']}*{fc}"
        e = f"({rev}-{am}-{ox}-{dp})"
        cit = f"IF({e}<=0,0,IF({e}<={inp['citlim']},{e}*{inp['cit1']},{inp['citlim']}*{inp['cit1']}+({e}-{inp['citlim']})*{inp['cit2']}))"
        parts.append(f"({e}-{cit}+{dp})/(1+{inp['disc']})^{t}")
    return f"=-{inp['capex']}*{fc}+" + "+".join(parts)
for i, (lab, kind) in enumerate([("Үнэ", "p"), ("Борлуулах хэмжээ", "p"), ("OPEX", "o"), ("CAPEX", "c")]):
    r = 6 + i
    z.cell(r, 1, lab).font = BLACK
    for j in range(5):
        k = f"{L(2+j)}$5"
        fp, fo, fc = (k, 1, 1) if kind == "p" else ((1, k, 1) if kind == "o" else (1, 1, k))
        c = z.cell(r, 2 + j, npv_expr(fp, fo, fc)); c.number_format = NUM0
r = 11
z.cell(r, 1, "Өөрийн хувилбар: үнэ/борлуулалтын коэффициент").font = BOLD
c = z.cell(r, 2, 0.311); c.font = BLUE; c.fill = YEL; c.number_format = PCT
z.cell(r, 3, "→ NPV").font = BLACK
c = z.cell(r, 4, npv_expr("$B$11", 1, 1)); c.number_format = NUM0; c.font = BOLD
z.cell(r + 1, 1, "Хугарлын цэг ≈ 31.1 % (NPV ≈ 0) — B11-ийг өөрчилж шалгана. Жигнэсэн үнэ ≈ 19 250 ₮/м³, борлуулалт ≈ 123 500 м³/жил.").font = Font(name="Arial", size=9, italic=True)
z.column_dimensions["A"].width = 44
for col in range(2, 7): z.column_dimensions[L(col)].width = 12

for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if c.font and c.font.name != "Arial":
                c.font = Font(name="Arial", size=c.font.size or 10, bold=c.font.bold, italic=c.font.italic, color=c.font.color)
wb.save(OUT)
print("saved", OUT)
