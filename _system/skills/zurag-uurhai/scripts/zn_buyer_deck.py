"""Зүүн наран — 30 000 м³ худалдан авагчийн танилцуулга (A4 хэвтээ, графит хэв маяг).
Ажиллуулах: python -I zn_buyer_deck.py
Тоо бүр vault-ийн ТЭЗҮ (индекс, 3, 5, 11-р бүлэг)-ээс; байхгүйг TBD гэж тэмдэглэнэ.
Edge headless-ээр HTML-ийг PDF болгоно."""
import os as _os
VAULT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))  # vault-ийн үндэс, аль ч компьютерт
import os, sys, subprocess, tempfile, shutil
sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = _os.path.join(VAULT, r"02-Projects\Ажил\Хөхтойн ХХК\Зүүн наран\05 Зах зээл")
OUT = os.path.join(OUT_DIR, "Зүүн наран - 30 000 м³ худалдан авагчийн танилцуулга 2026-11-08.pdf")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# ---------- эх тоо (ТЭЗҮ индекс, 5.5) ----------
BULK = 1.336          # т/м³ асгаасны эзэлхүүн жин (индекс #6)
ORDER = 30_000        # м³ сэвсгэр
DAYS = 180            # ажлын улирал 5–10 сар (индекс #11)
P20 = 177_890         # 10–20 мм м³/жил (ТЭЗҮ 5.5)
P10 = 77_619          # 5–10 мм
P05 = 46_511          # 0–5 мм
P520 = P20 + P10
order_t = ORDER * BULK
share = ORDER / P520 * 100
day_520 = P520 / DAYS
days_needed = ORDER / day_520
f0 = lambda v: f"{v:,.0f}".replace(",", " ")
print(f"30 000 м³ = {order_t:.0f} т; 5–20 мм-ийн {share:.1f} %; өдөрт {day_520:.0f} м³; {days_needed:.1f} өдөр")

STONE = """<svg xmlns='http://www.w3.org/2000/svg' width='600' height='600'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' seed='7'/><feColorMatrix values='0 0 0 0 0.55  0 0 0 0 0.55  0 0 0 0 0.56  0 0 0 0.55 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"""
STONE_URI = "data:image/svg+xml;utf8," + STONE.replace("#", "%23").replace("\n", "")

CSS = f"""
@page {{ size: 297mm 210mm; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{ --g0:#1E2124; --g1:#2A2E33; --g2:#3A3F45; --g3:#6B7178; --g4:#A9AEB3; --g5:#E6E7E8; --paper:#F4F4F2; --cu:#C2703D; }}
body {{ font-family: 'Segoe UI', Arial, sans-serif; color: var(--g1); background: var(--paper); }}
.s {{ width:297mm; height:210mm; position:relative; overflow:hidden; page-break-after: always; background: var(--paper); }}
.s:last-child {{ page-break-after: auto; }}
.hd {{ height:30mm; background: var(--g0) url("{STONE_URI}"); background-size: 300px; color:#fff; padding: 8mm 14mm 0; position:relative; }}
.hd::after {{ content:''; position:absolute; left:14mm; bottom:0; width:24mm; height:1.6mm; background:var(--cu); }}
.hd .k {{ font-size:8.5pt; letter-spacing:.18em; text-transform:uppercase; color: var(--g4); }}
.hd h2 {{ font-size:21pt; font-weight:600; margin-top:1.5mm; }}
.bd {{ padding: 9mm 14mm 0; }}
.ft {{ position:absolute; bottom:0; left:0; right:0; height:10mm; border-top:0.3mm solid var(--g4); display:flex; justify-content:space-between; align-items:center; padding: 0 14mm; font-size:7.5pt; color: var(--g3); }}
.ft b {{ color: var(--cu); font-weight:600; }}
.kpis {{ display:flex; gap:5mm; margin-bottom:8mm; }}
.kpi {{ flex:1; background:#fff; border-top:1.2mm solid var(--g1); padding:4mm 4.5mm; }}
.kpi.cu {{ border-top-color: var(--cu); }}
.kpi .v {{ font-size:20pt; font-weight:700; color: var(--g0); line-height:1.1; }}
.kpi .v small {{ font-size:10pt; font-weight:500; color: var(--g3); }}
.kpi .l {{ font-size:8.5pt; color: var(--g3); margin-top:1.5mm; line-height:1.35; }}
table {{ border-collapse: collapse; width:100%; font-size:9.5pt; }}
th {{ text-align:left; background: var(--g1); color:#fff; font-weight:600; padding:2.2mm 3mm; font-size:8.5pt; }}
td {{ padding:2mm 3mm; border-bottom:0.25mm solid var(--g5); background:#fff; }}
td.n, th.n {{ text-align:right; font-variant-numeric: tabular-nums; white-space:nowrap; }}
.ok {{ color:#2F7D4F; font-weight:700; }}
.cols {{ display:flex; gap:9mm; }}
.cols > div {{ flex:1; }}
h3 {{ font-size:11pt; font-weight:600; color: var(--g0); margin-bottom:3mm; padding-bottom:1.5mm; border-bottom:0.4mm solid var(--cu); display:inline-block; }}
p, li {{ font-size:10pt; line-height:1.5; color: var(--g2); }}
ul {{ padding-left:4.5mm; }} li {{ margin-bottom:1.6mm; }}
.note {{ font-size:8pt; color: var(--g3); margin-top:3mm; line-height:1.4; }}
.tbd {{ display:inline-block; background:#FBEBDD; color:#8A4518; font-size:8pt; font-weight:700; padding:0.3mm 1.6mm; border-radius:1mm; }}
.bar {{ height:5mm; background: var(--g5); position:relative; margin:1.2mm 0 3mm; }}
.bar i {{ position:absolute; left:0; top:0; bottom:0; background: var(--g1); }}
.bar i.cu {{ background: var(--cu); }}
.cover {{ background: var(--g0) url("{STONE_URI}"); background-size: 300px; color:#fff; }}
.cover .in {{ position:absolute; left:18mm; top:40mm; right:18mm; }}
.cover .k {{ font-size:10pt; letter-spacing:.22em; color: var(--g4); text-transform:uppercase; }}
.cover h1 {{ font-size:40pt; font-weight:700; line-height:1.1; margin-top:5mm; }}
.cover .sub {{ font-size:15pt; color: var(--g5); margin-top:5mm; max-width:200mm; line-height:1.4; }}
.cover .ln {{ width:30mm; height:1.8mm; background: var(--cu); margin-top:9mm; }}
.cover .meta {{ position:absolute; left:18mm; bottom:16mm; font-size:9.5pt; color: var(--g4); line-height:1.6; }}
.cover .big {{ position:absolute; right:18mm; bottom:14mm; text-align:right; }}
.cover .big .v {{ font-size:46pt; font-weight:700; color: var(--cu); line-height:1; }}
.cover .big .l {{ font-size:10pt; color: var(--g4); margin-top:2mm; }}
.step {{ display:flex; gap:4mm; margin-bottom:4.5mm; }}
.step .no {{ width:9mm; height:9mm; flex:none; background: var(--g1); color:#fff; font-weight:700; display:flex; align-items:center; justify-content:center; font-size:11pt; }}
.step .no.cu {{ background: var(--cu); }}
.step b {{ color: var(--g0); font-size:10.5pt; }}
"""

def slide(no, kicker, title, body):
    return f"""<section class="s"><div class="hd"><div class="k">{kicker}</div><h2>{title}</h2></div>
<div class="bd">{body}</div>
<div class="ft"><span>«Хөхтойн» ХХК · «Зүүн наран» андезитын орд · Өмнөговь, Цогтцэций</span><span><b>{no:02d}</b> / 08</span></div></section>"""

TBD = '<span class="tbd">TBD</span>'
S = []

# 1 нүүр
S.append(f"""<section class="s cover"><div class="in">
<div class="k">Худалдан авагчид зориулсан танилцуулга</div>
<h1>«Зүүн наран»<br>андезит дайрга</h1>
<div class="sub">Бетон, авто зам, тэсэлгээний дүүргэлтэд зориулсан 5–10, 10–20 мм-ийн буталсан дайргыг уурхайн ам дээрээс нийлүүлнэ.</div>
<div class="ln"></div></div>
<div class="meta">«Хөхтойн» ХХК · Өмнөговь аймаг, Цогтцэций сум<br>Ашиглалтын тусгай зөвшөөрөл MV-46000368 · 2026 оны 11 сар</div>
<div class="big"><div class="v">30 000 м³</div><div class="l">сэвсгэр дайрганы санал · ≈ {f0(order_t)} т</div></div>
</section>""")

# 2 орд
S.append(slide(2, "Орд", "Тавантолгойн бүсэд, засмал замын ойролцоо", f"""
<div class="kpis">
<div class="kpi cu"><div class="v">6.80 <small>сая м³</small></div><div class="l">Геологийн нөөц A+B+C (18.3 сая т), ЭБМЗ XX-18-03, 2025</div></div>
<div class="kpi"><div class="v">15 <small>жил</small></div><div class="l">Ашиглалтын тусгай зөвшөөрөл MV-46000368</div></div>
<div class="kpi"><div class="v">40 <small>км</small></div><div class="l">Тавантолгойн нүүрсний бүлэг ордын төв хүртэл</div></div>
<div class="kpi"><div class="v">15 <small>км</small></div><div class="l">Хармагтайн төмөр замын өртөө хүртэл</div></div>
</div>
<div class="cols"><div>
<h3>Байршил</h3>
<table><tr><th>Чиглэл</th><th class="n">Зай</th></tr>
<tr><td>Засмал зам (Тавантолгой–Гашуунсухайт)</td><td class="n">500 м</td></tr>
<tr><td>Хармагтайн төмөр замын өртөө</td><td class="n">15 км</td></tr>
<tr><td>Цогтцэций сумын төв</td><td class="n">28 км</td></tr>
<tr><td>Тавантолгойн бүлэг орд</td><td class="n">40 км</td></tr>
<tr><td>Даланзадгад</td><td class="n">128 км</td></tr>
</table></div><div>
<h3>Ордын тухай</h3>
<ul>
<li>Пенсильваны Дөшийн овоо формацын <b>андезит</b>: хөхөвтөр саарал, цул нягт (2.69 т/м³).</li>
<li>Давхарга хэвтээ, гадаргаас ойр. Хуулалт бага (0.187 м³/м³), 20 м-ийн гүнд газрын доорх ус илрээгүй.</li>
<li>Эхний шатанд 5 жилд 750 104 м³ үйлдвэрлэлийн нөөцийг ил аргаар олборлоно.</li>
<li>Солбицол: 105°54′31″ E, 43°46′44″ N, өндөршил 1 585–1 617 м.</li>
</ul></div></div>"""))

# 3 бүтээгдэхүүн
def barrow(name, use, v, pct, cu=False):
    return f"""<tr><td><b>{name}</b></td><td>{use}</td><td class="n">{f0(v)}</td><td class="n">{pct}</td></tr>"""
S.append(slide(3, "Бүтээгдэхүүн", "Гурван фракц, хаалттай циклээр бутална", f"""
<div class="cols"><div style="flex:1.35">
<table><tr><th>Фракц</th><th>Хэрэглээ</th><th class="n">м³/жил*</th><th class="n">Гарц</th></tr>
{barrow("10–20 мм", "Бетоны том дүүргэгч, тэсэлгээний цооногийн дүүргэлт, зам", P20, "58.9 %")}
{barrow("5–10 мм", "Бетоны дүүргэгч, тэсэлгээний дүүргэлт", P10, "25.7 %")}
{barrow("0–5 мм", "Буталсан элс: зуурмаг, замын суурь, далан", P05, "15.4 %")}
</table>
<div style="margin-top:6mm">
<p style="font-size:8.5pt">10–20 мм · 58.9 %</p><div class="bar"><i class="cu" style="width:58.9%"></i></div>
<p style="font-size:8.5pt">5–10 мм · 25.7 %</p><div class="bar"><i style="width:25.7%"></i></div>
<p style="font-size:8.5pt">0–5 мм · 15.4 %</p><div class="bar"><i style="width:15.4%;background:var(--g3)"></i></div>
</div>
<p class="note">* Жилд 150 000 м³ цул андезит (403 500 т) боловсруулахад гарах сэвсгэр бүтээгдэхүүн (1.336 т/м³). Гарц нь лабораторийн бутлалтын ордын дундаж; ашиглалтын эхний жилд хэмжиж баталгаажуулна.</p>
</div><div>
<h3>Захиалгад тохируулах</h3>
<ul>
<li>5–10 ба 10–20 мм-ийн харьцааг конусан бутлуурын гаргалтын завсраар (19–51 мм) тохируулж болно.</li>
<li>20–40 мм хэрэгтэй бол шигшүүрийн торыг сольж гаргана. Хэмжээ, үнэ {TBD}</li>
<li>Тусгай ширхэгийн бүрэлдэхүүн (жишээ нь 8–25 мм) шаардлагатай бол урьдчилан тохирно.</li>
<li>0–5 мм буталсан элсийг тусад нь санал болгоно. Үнэ {TBD}</li>
</ul></div></div>"""))

# 4 чанар
Q = [("Бутлагдсан хэсэгт дайрганы эзлэх хувь","%","90–100","100"),("Нимгэн, үзүүрлэг хэсэг","%","≤ 15","4.4"),
     ("Бутрамтгай чанар","%","≤ 8","6.5 (Б-8)"),("Элэгдэх чанар","%","≤ 25","15.1"),("Тоос, шаврын хэмжээ","%","≤ 2","0.2"),
     ("Элсэрхэг хэсэг","%","≤ 10","2.1"),("Бүхэл шавар","%","≤ 0.25","байхгүй"),("Хүйтэн тэсвэрлэлт (Na₂SO₄, 5 мөчлөг)","%","≤ 10","1.2 (ХТ-25)"),
     ("Уусдаг цахиур (SiO₂)","ммоль/л","< 50","25.8"),("Цацраг идэвх (Ra экв.)","Бк/кг","< 370","85"),("Ус шингээлт","%","< 2","0.58")]
rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td class="n">{c}</td><td class="n"><b>{d}</b></td><td class="ok">✓</td></tr>' for a,b,c,d in Q)
S.append(slide(4, "Чанар", "MNS 2803:2004, MNS 0390:1998-ийн шаардлагыг бүрэн хангана", f"""
<div class="cols"><div style="flex:1.5">
<table style="font-size:8.8pt"><tr><th>Үзүүлэлт</th><th>Нэгж</th><th class="n">Стандарт</th><th class="n">Ордын дундаж</th><th></th></tr>{rows}</table>
<p class="note">Эх сурвалж: хайгуулын тайлан (хүснэгт 6-17), ЭБМЗ-ийн 2025.12.11-ний XX-18-03 дүгнэлт.</p>
</div><div>
<div class="kpi cu" style="margin-bottom:5mm"><div class="v">М400</div><div class="l">хүртэлх маркийн хүнд бетоны том дүүргэгч болох нь технологийн туршилтаар батлагдсан</div></div>
<div class="kpi" style="margin-bottom:5mm"><div class="v">3-1 <small>төрөл</small></div><div class="l">Элэгдлээр авто замын далангийн хучилтын материалын шаардлагыг хангана</div></div>
<h3>Нэмэлт үзүүлэлт</h3>
<ul style="font-size:9pt"><li>Ширхэгийн нягт 2.67 г/см³, сүвэрхэг чанар 0.5 %</li><li>Хлор 0.0041 %, чийг 0.3 %</li><li>SiO₂ 60.86 %, Al₂O₃ 13.12 %, SO₃ 0.20 %</li></ul>
</div></div>"""))

# 5 үйлдвэрлэл
S.append(slide(5, "Үйлдвэрлэлийн чадал", "30 000 м³ бол жилийн үйлдвэрлэлийн жижиг хэсэг", f"""
<div class="kpis">
<div class="kpi"><div class="v">150 000 <small>м³ цул</small></div><div class="l">Жилийн олборлолт (403 500 т)</div></div>
<div class="kpi"><div class="v">{f0(P520)} <small>м³</small></div><div class="l">Жилд гарах 5–20 мм дайрга (сэвсгэр)</div></div>
<div class="kpi cu"><div class="v">{share:.1f} <small>%</small></div><div class="l">30 000 м³ нь 5–20 мм-ийн жилийн гарцын хувь</div></div>
<div class="kpi"><div class="v">≈ {days_needed:.0f} <small>өдөр</small></div><div class="l">30 000 м³-ийг үйлдвэрлэх хугацаа (өдөрт ≈ {f0(day_520)} м³)**</div></div>
</div>
<div class="cols"><div>
<h3>Бутлан ангилах шугам</h3>
<table><tr><th>Шат</th><th>Тоног төхөөрөмж</th></tr>
<tr><td>1-р шат</td><td>Хацарт бутлуур PE900×1200 (оролт ≤ 750 мм)</td></tr>
<tr><td>2-р шат</td><td>Конусан бутлуур CS220B (200–400 т/цаг)</td></tr>
<tr><td>Ангилалт</td><td>Чичиргээт шигшүүр 4YK-1860 (4 давхар), +20 мм буцна</td></tr>
<tr><td>Тоос</td><td>Тоос барих PVMC-380-2.5 (95 %), ус шүршилт</td></tr>
</table></div><div>
<h3>Ажлын горим</h3>
<ul>
<li>Олборлолт, бутлалт 5–10 сард (180 хоног), 2 ээлжээр.</li>
<li>Ил уурхай, бутлуур, бүтээгдэхүүний овоолго нэг талбайд: налуу замын амнаас бутлуур 161 м.</li>
<li>Өрөмдлөг, тэсэлгээг гэрээт гүйцэтгэгч хийнэ. Ачилт R380LC-9 экскаватор, ачигчаар.</li>
<li>Ажилтан 44 хүн, уурхайн кемптэй.</li>
</ul>
<p class="note">** Тооцоо: жилийн 5–20 мм-ийн гарц ÷ 180 ажлын өдөр. Бодит хуваарийг бусад хэрэглэгчийн захиалгатай уялдуулж гэрээгээр тогтооно.</p>
</div></div>"""))

# 6 нөхцөл
S.append(slide(6, "Нийлүүлэлтийн нөхцөл", "Уурхайн ам дээр ачиж өгнө", f"""
<div class="kpis">
<div class="kpi cu"><div class="v">55 000 <small>₮/м³</small></div><div class="l">Сэвсгэр м³, НӨАТ орсон (НӨАТ-гүй 50 000 ₮/м³)</div></div>
<div class="kpi"><div class="v">{f0(ORDER*55_000/1e6)} <small>сая ₮</small></div><div class="l">30 000 м³-ийн дүн, НӨАТ орсон</div></div>
<div class="kpi"><div class="v">≈ {f0(order_t)} <small>т</small></div><div class="l">30 000 м³ сэвсгэрийн жин (1.336 т/м³)</div></div>
</div>
<table><tr><th style="width:55mm">Нөхцөл</th><th>Агуулга</th></tr>
<tr><td><b>Үнийн суурь</b></td><td>Уурхайн ам дээр: уурхайн талбайд худалдан авагчийн машинд ачиж өгнө</td></tr>
<tr><td><b>Тээвэр</b></td><td>Худалдан авагч хариуцна. Уурхайгаас засмал зам хүртэл 500 м</td></tr>
<tr><td><b>Хэмжилт</b></td><td>Сэвсгэр м³-ээр. Талбайд 60 т-ын автомашины жинтэй</td></tr>
<tr><td><b>Нийлүүлэх улирал</b></td><td>5–10 сард шууд үйлдвэрлэлээс. Өвлийн нийлүүлэлтийг нөөцөөс урьдчилан тохирно</td></tr>
<tr><td><b>Нийлүүлэлт эхлэх</b></td><td>2027 он (ТЭЗҮ батлагдаж, ашиглалт эхэлсний дараа). Яг огноо {TBD}</td></tr>
<tr><td><b>Төлбөрийн нөхцөл</b></td><td>{TBD}</td></tr>
<tr><td><b>Фракцаар үнэ</b></td><td>5–10, 10–20 мм ижил үнээр тооцсон. 0–5 мм, 20–40 мм-ийн үнэ {TBD}</td></tr>
</table>
<p class="note">Үнэ урьдчилсан бөгөөд гэрээгээр эцэслэнэ.</p>"""))

# 7 яагаад
S.append(slide(7, "Давуу тал", "Яагаад «Зүүн наран»", """
<div class="cols" style="gap:7mm">
<div><div class="step"><div class="no cu">1</div><div><b>Ойр байршил</b><p>Тавантолгойн бүсээс 40 км, Хармагтайн өртөөнөөс 15 км, засмал замаас 500 м. Тээврийн зардал бага.</p></div></div>
<div class="step"><div class="no">2</div><div><b>Батлагдсан чанар</b><p>11 үзүүлэлтээр MNS стандартыг хангасан. М400 хүртэлх бетон, замын хучилтад тохирно.</p></div></div>
<div class="step"><div class="no">3</div><div><b>Хууль ёсны эрх</b><p>Ашиглалтын тусгай зөвшөөрөл MV-46000368 (15 жил). Нөөцийг ЭБМЗ хүлээн авсан.</p></div></div></div>
<div><div class="step"><div class="no">4</div><div><b>Урт хугацааны нөөц</b><p>Геологийн нөөц 6.8 сая м³. Жилд 150 000 м³ олборлоход олон жилийн нийлүүлэлтийг хангана.</p></div></div>
<div class="step"><div class="no">5</div><div><b>Тогтвортой фракц</b><p>Хоёр шаттай бутлалт, хаалттай цикл: 20 мм-ээс том ширхэгийг дахин бутална.</p></div></div>
<div class="step"><div class="no">6</div><div><b>Хариуцлагатай үйл ажиллагаа</b><p>Тоос барих төхөөрөмж, ус шүршилт, тэсэлгээний аюулгүйн бүс, нөхөн сэргээлтийн төлөвлөгөөтэй.</p></div></div></div>
</div>"""))

# 8 дараагийн алхам
S.append(slide(8, "Хамтран ажиллах", "Дараагийн алхам", f"""
<div class="cols"><div>
<div class="step"><div class="no cu">1</div><div><b>Хэрэгцээгээ илгээх</b><p>Хэмжээ (м³), фракц, нийлүүлэх сар, хүлээн авах цэг.</p></div></div>
<div class="step"><div class="no">2</div><div><b>Санамж бичиг</b><p>Хэмжээ, үнэ, хуваарийг урьдчилан баталгаажуулна.</p></div></div>
<div class="step"><div class="no">3</div><div><b>Нийлүүлэх гэрээ</b><p>Ашиглалт эхлэхэд нийлүүлэлтийн хуваарийг гэрээгээр тогтооно.</p></div></div>
<div class="step"><div class="no">4</div><div><b>Сорьц, чанарын гэрчилгээ</b><p>Фракц бүрээс сорьц авч ширхэгийн бүрэлдэхүүн, тоос шавар, бутрамтгай чанарыг шалгана.</p></div></div>
</div><div>
<div class="kpi cu" style="padding:7mm">
<div class="l" style="margin:0 0 2mm;letter-spacing:.15em;text-transform:uppercase">Холбоо барих</div>
<div class="v" style="font-size:17pt">«Хөхтойн» ХХК</div>
<p style="margin-top:3mm">Захирал Э.Жавхлант-Од</p>
<p>Утас: {TBD}</p><p>Имэйл: {TBD}</p><p>Хаяг: {TBD}</p>
</div>
<p class="note">Тоо бүрийн эх сурвалж: «Зүүн наран» ордын ТЭЗҮ (2026, «Грийтвишн» ХХК), хайгуулын тайлан, ЭБМЗ-ийн XX-18-03 дүгнэлт.</p>
</div></div>"""))

html = f"<!doctype html><html lang='mn'><head><meta charset='utf-8'><title>Зүүн наран — худалдан авагчийн танилцуулга</title><style>{CSS}</style></head><body>{''.join(S)}</body></html>"
tmp = tempfile.mkdtemp(prefix="znb_")
hp = os.path.join(tmp, "deck.html")
open(hp, "w", encoding="utf-8").write(html)
pdf = os.path.join(tmp, "deck.pdf")
subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", hp], check=True, capture_output=True)
shutil.move(pdf, OUT)
print("OK", OUT, os.path.getsize(OUT))
print("HTML", hp)
