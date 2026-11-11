"""20 м-т дээж авах ухмал — нэг PDF: энгийн тайлбар (A4) + инженерийн зураг (A3 × 2) + тооцоо, хуваарь (A4).
Ажиллуулах: python -I ukhmal20_report.py
Edge headless-ээр HTML-ийг PDF болгож, pypdf-ээр нийлүүлнэ."""
import os as _os
VAULT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))  # vault-ийн үндэс, аль ч компьютерт
import pathlib as _pl
LOGO_URI = _pl.Path(VAULT, "_system", "skills", "zurag-shtamp", "gv_logo.png").as_uri()
import os, sys, subprocess, shutil, tempfile, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8")
import ukhmal20_calc as C
from pypdf import PdfReader, PdfWriter

OUT = _os.path.join(VAULT, r"02-Projects\Ажил\Вай эйч графит нэчүрал ХХК\Сүүж уул\Ухмал 20 м\Сүүж уул - 20 м-т дээж авах ухмал - нэгдсэн тайлан.pdf")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TMP = tempfile.mkdtemp(prefix="u20_")
R = C.calc()
st = R["stages"]
f0 = lambda v: f"{v:,.0f}".replace(",", " ")
f1 = lambda v: f"{v:.1f}"
mln = lambda v: f"{v / 1e6:.1f}"
days_total = math.ceil(R["days_total"]); days_res = math.ceil(R["days_reserve"])

# ---------- өдрийн хуваарь ----------
sched, day, left, cum = [], 1, [s["V"] for s in st], 0.0
SHORT = ["1-р шат", "2-р шат", "3-р шат", "Нүх"]
ENDS = ["−5 м", "−10 м", "−15 м", "−20 м"]
def progress(c):
    acc = 0.0
    for k, s_ in enumerate(st):
        if c < acc + s_["V"] - 1:
            pct = (c - acc) / s_["V"] * 100
            return f"{SHORT[k]} {pct:.0f} %" if pct < 99.5 else f"{ENDS[k]} хүрсэн"
        acc += s_["V"]
    return "−20 м хүрсэн ✔"
sched.append(dict(day=1, work="Бэлтгэл (хил, рамп тэмдэглэх) + 1-р шат эхэлнэ", trips=None, cum=0, depth="0"))
cap = 0.5                      # 1-р өдрийн хагас нь бэлтгэл
i = 0
depth_txt = ["−5 м", "−10 м", "−15 м", "−20 м"]
while i < len(st):
    works, trips = [], 0
    c = cap
    while c > 1e-6 and i < len(st):
        need_days = left[i] / st[i]["prod_day"]
        use = min(c, need_days)
        vol = use * st[i]["prod_day"]
        left[i] -= vol; cum += vol; c -= use
        trips += vol * C.SWELL / R["load_loose"]
        works.append(st[i]["name"].split(" (")[0])
        if left[i] <= 1e-6:
            i += 1
    if day == 1:
        sched[0].update(trips=trips, cum=cum, depth=progress(cum))
    else:
        # хүрсэн гүн
        acc, dep = 0, 0.0
        for k, s in enumerate(st):
            if cum >= acc + s["V"] - 1:
                acc += s["V"]; dep = 5.0 * (k + 1)
            else:
                dep += 5.0 * (cum - acc) / s["V"]; break
        sched.append(dict(day=day, work=" + ".join(dict.fromkeys(works)), trips=trips, cum=cum, depth=progress(cum)))
    day += 1; cap = 1.0
last = sched[-1]
sched.append(dict(day=day, work="Дээж авах, тэмдэглэх; техник гаргах", trips=0, cum=cum, depth="−20 м хүрсэн ✔"))

CSS = """
@page { size: A4; margin: 12mm 13mm 12mm 13mm; }
* { box-sizing: border-box; }
body { font-family: Arial, sans-serif; color: #1d2433; font-size: 11pt; line-height: 1.32; margin: 0; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
.hdr { background: #13306b; color: #fff; border: 2px solid #ffd21f; border-radius: 6px; padding: 9px 14px; margin-bottom: 10px; }
.hdr h1 { margin: 0; font-size: 18pt; } .hdr h1 b { color: #ffd21f; }
.hdr p { margin: 3px 0 0; font-size: 10pt; color: #dfe7f5; }
h2 { background: #13306b; color: #fff; font-size: 12pt; padding: 5px 10px; border-radius: 5px 5px 0 0; margin: 8px 0 0; }
.box { border: 1.5px solid #13306b; border-top: none; border-radius: 0 0 6px 6px; padding: 6px 10px; }
.big { display: grid; grid-template-columns: repeat(4, 1fr); gap: 7px; margin: 8px 0 4px; }
.k { border: 2px solid #13306b; border-radius: 8px; padding: 8px 6px; text-align: center; background: #f3f6fc; }
.k .n { font-size: 21pt; font-weight: bold; color: #13306b; line-height: 1.1; }
.k .u { font-size: 9.5pt; color: #333; }
.k.y { background: #ffd21f; }
table { width: 100%; border-collapse: collapse; font-size: 10pt; }
th { background: #dfe7f5; color: #13306b; } th, td { border: 1px solid #9aa7c0; padding: 3px 6px; text-align: center; }
td.l, th.l { text-align: left; }
tr.tot td { background: #ffd21f; font-weight: bold; color: #13306b; }
.step { display: grid; grid-template-columns: 34px 1fr; gap: 8px; margin: 6px 0; align-items: start; }
.step .c { width: 30px; height: 30px; border-radius: 50%; background: #13306b; color: #fff; font-weight: bold; font-size: 13pt;
           display: flex; align-items: center; justify-content: center; }
.step .c.r { background: #d7261e; }
.warn { background: #fdecea; border: 1.5px solid #d7261e; border-radius: 6px; padding: 7px 11px; margin-top: 10px; color: #6d0f0f; }
.ok { background: #eaf6ec; border: 1.5px solid #2e9e44; border-radius: 6px; padding: 7px 11px; margin-top: 8px; }
.calc { font-size: 9.6pt; } .calc table { font-size: 9.3pt; } .calc td, .calc th { padding: 3px 5px; } .nw { white-space: nowrap; } .calc td { text-align: left; } .calc td.r { text-align: right; white-space: nowrap; font-weight: bold; }
.eq { font-family: Consolas, monospace; background: #f3f6fc; padding: 1px 4px; border-radius: 3px; }
small { color: #555; }
ul { margin: 4px 0; padding-left: 20px; } li { margin: 2px 0; }
.cover { display: flex; flex-direction: column; height: 268mm; }
.cv-top { display: flex; align-items: center; gap: 14px; border-bottom: 3px solid #13306b; padding-bottom: 10px; }
.cv-org { font-size: 20pt; font-weight: bold; color: #c8102e; letter-spacing: 1px; }
.cv-mid { flex: 1; display: flex; flex-direction: column; justify-content: center; }
.cv-kind { font-size: 13pt; font-weight: bold; color: #fff; background: #13306b; display: inline-block; padding: 5px 14px; border-radius: 4px; align-self: flex-start; }
.cv-title { font-size: 27pt; font-weight: bold; color: #13306b; line-height: 1.2; margin-top: 14px; }
.cv-title b { color: #c8102e; }
.cv-sub { font-size: 12pt; color: #333; margin-top: 10px; }
.cv-city { text-align: center; color: #555; margin-top: 10px; }
table.sign td { padding: 7px 8px; font-size: 11pt; }
table.toc td { padding: 6px 8px; } table.toc td:last-child { width: 50px; font-weight: bold; color: #13306b; }
.foot { font-size: 8.5pt; color: #666; margin-top: 8px; border-top: 1px solid #ccc; padding-top: 4px; }
"""

p = R["params"]
summary = f"""
<div class="page">
<div class="hdr"><h1>1. Даалгавар, <b>сонгосон арга</b></h1><p>Юу хийх, ямар техникээр, яагаад ингэж хийх вэ</p></div>

<h2>1.1 Анхны өгөгдөл</h2>
<div class="box"><table>
<tr><td class="l" style="width:42%">Зорилго</td><td class="l"><b>20 м гүнээс дээж авах</b>, хамгийн бага зардлаар</td></tr>
<tr><td class="l">Ухмалын хэлбэр</td><td class="l">3 шатлалтай (5 м-ийн шат), ёроол 10 × 10 м, 1-р шат 45°</td></tr>
<tr><td class="l">Экскаватор</td><td class="l">1 ширхэг, Хятад, 500-р анги, шанага 3.2 м³</td></tr>
<tr><td class="l">Автосамосвал</td><td class="l">2 ширхэг Хово, тэвш 18 м³</td></tr>
<tr><td class="l">Үнэ</td><td class="l">1 м³ ухалт = {f0(C.PRICE)} ₮ (захиалагч төлнө)</td></tr>
<tr><td class="l">Ажлын горим</td><td class="l">1 ээлж = 10 цаг (9 цаг бодит ажил)</td></tr>
</table></div>
<h2>1.2 Сонгосон арга: «15 м ухмал + 5 м дээжний нүх»</h2>
<div class="box">
<p style="margin:2px 0 6px">Хово-г 20 м-ийн ёроол хүртэл оруулах гэвэл ухмал хэт томорно:
<b>{f0(R['opts'][-1]['V'])} м³ = {mln(R['opts'][-1]['cost'])} сая ₮</b>.
Тэгэхээр Хово-г зөвхөн <b>15 м</b> хүртэл оруулаад, сүүлийн 5 м-ийг экскаватор өөрөө жижиг нүх болгож ухна.
Ингэснээр <b>{f0(R['opts'][-1]['V'] - R['V'])} м³, ≈ {mln(R['opts'][-1]['cost'] - R['cost'])} сая ₮ хэмнэнэ</b>.</p>
<div class="step"><div class="c">1</div><div><b>1-р шат: 0 → −5 м</b> · {f1(st[0]['days'])} өдөр · {f0(st[0]['V'])} м³<br>
Хамгийн том хэсэг. Хөрс сул тул хана 45° налуу. Рампын (налуу замын) эхний тойргийг зүснэ.</div></div>
<div class="step"><div class="c">2</div><div><b>2-р шат: −5 → −10 м</b> · {f1(st[1]['days'])} өдөр · {f0(st[1]['V'])} м³<br>
Чулуулаг эхэлнэ, хана 60°. Шат хооронд 2 м өргөн тавцан үлдээнэ (чулуу өнхрөхийг тосно).</div></div>
<div class="step"><div class="c">3</div><div><b>3-р шат: −10 → −15 м</b> · {f1(st[2]['days'])} өдөр · {f0(st[2]['V'])} м³<br>
Ёроол 10 × 10 м. Хово ёроолд урагш-ухрах-урагш гэж 3 цэгээр эргэж, экскаваторт ухарч ирнэ.</div></div>
<div class="step"><div class="c r">4</div><div><b>Дээжний нүх: −15 → −20 м</b> · ≈ 1 өдөр · {f0(st[3]['V'])} м³<br>
Экскаватор ёроол дээр зогсож 3 × 3 м нүх ухна. <b>Нүхэнд хүн орохгүй.</b> Дээжийг 20 м-ээс гарсан шанаганаас авна.</div></div>
</div>

<h2>1.3 Хувилбарын харьцуулалт («хэрвээ… бол»)</h2>
<div class="box"><table>
<tr><th class="l">Нөхцөл</th><th>Ухалт, м³</th><th>Зардал</th><th>Хугацаа</th></tr>
<tr><td class="l"><b>Санал болгож буй</b> (дээрх)</td><td>{f0(R['V'])}</td><td><b>{mln(R['cost'])} сая ₮</b></td><td>{days_total} өдөр</td></tr>
<tr><td class="l">Өдөр, шөнө 2 ээлжээр ажиллавал</td><td>{f0(R['V'])}</td><td>{mln(R['cost'])} сая ₮</td><td>≈ {math.ceil(R['days_work'] / 2 + 1)} өдөр</td></tr>
<tr><td class="l">Гэрээлэгч Хово-гийн тоогоор (сул м³) тооцвол</td><td>{f0(R['loose'])}</td><td style="color:#d7261e"><b>{mln(R['cost_loose'])} сая ₮</b></td><td>адил</td></tr>
<tr><td class="l">Рамп 15 % (эгц, Хово-д хүнд)</td><td>{f0(R['opts'][1]['V'])}</td><td>{mln(R['opts'][1]['cost'])} сая ₮</td><td>≈ 1 өдөр бага</td></tr>
<tr><td class="l">Шат хооронд тавцангүй (зөвхөн хатуу чулуунд)</td><td>{f0(R['opts'][2]['V'])}</td><td>{mln(R['opts'][2]['cost'])} сая ₮</td><td>≈ 1.5 өдөр бага</td></tr>
<tr><td class="l">Хово 20 м хүртэл орох бүтэн ухмал</td><td>{f0(R['opts'][4]['V'])}</td><td>{mln(R['opts'][4]['cost'])} сая ₮</td><td>≈ {math.ceil(R['opts'][4]['V'] / (R['V'] / R['days_work']) + 1)} өдөр</td></tr>
</table></div>

</div>
"""

stage_rows = "".join(
    f"<tr><td class='l nw'>{s['name'].replace(' (', '<br><small>(').replace(')', ')</small>')}</td><td class='nw'>{f0(s['V'])}</td><td class='nw'>{f0(s['V'] * C.SWELL)}</td><td>{f0(s['trips'])}</td>"
    f"<td>{f0(s['route'])}</td><td>{f1(s['cycle'])}</td><td>{f1(s['trips_h'])}</td><td class='nw'>{f0(s['prod_day'])}</td><td>{f1(s['days'])}</td><td>{mln(s['cost'])}</td></tr>"
    for s in st)
calcpage = f"""
<div class="page">
<div class="hdr"><h1>2. Ажлын хэмжээ, хугацаа, <b>зардал</b></h1><p>Энгийн арифметик. Тоо бүрийг шалгаж болно.</p></div>

<h2>2.1 Хэдэн куб ухах вэ</h2>
<div class="box calc">
<p style="margin:0 0 4px">Ухмалыг 5 м-ээр давхарлаж, компьютераар 25 × 25 см-ийн нүдээр тоолсон. Дээд давхарга хамгийн өргөн тул хамгийн их ухалттай.</p>
<table><tr><th class="l">Давхарга</th><th>Цул м³</th><th>Сул м³<br>(×1.3)</th><th>Хово рейс</th><th>Зам, м</th><th>1 эргэлт, мин</th><th>Рейс / цаг</th><th>м³ / өдөр</th><th>Өдөр</th><th>Сая ₮</th></tr>
{stage_rows}
<tr class="tot"><td class="l">Нийт</td><td class="nw">{f0(R['V'])}</td><td class="nw">{f0(R['loose'])}</td><td>{f0(R['trips'])}</td><td></td><td></td><td></td><td></td><td>{f1(R['days_work'])}</td><td>{mln(R['cost'])}</td></tr></table>
<small>Цул м³ = газарт байгаа хөрс. Ухаад тэвшинд хийхэд сулраад 1.3 дахин томордог (сул м³).</small>
</div>

<h2>2.2 Нэг Хово хэдэн куб зөөх вэ</h2>
<div class="box calc"><table>
<tr><td>Шанага 3.2 м³, дүүргэлт 90 % → 1 шанага</td><td class="r">3.2 × 0.9 = {C.BUCKET * C.FILL:.2f} м³ сул</td></tr>
<tr><td>Тэвш 18 м³ → бүтэн шанагын тоо</td><td class="r">18 ÷ 2.88 = 6.25 → {R['passes']} шанага</td></tr>
<tr><td>1 рейс</td><td class="r">{R['passes']} × 2.88 = {R['load_loose']:.1f} м³ сул = {R['load_bank']:.1f} м³ цул</td></tr>
<tr><td>Ачих хугацаа: {R['passes']} шанага × 30 сек + Хово солигдох 1 мин</td><td class="r">≈ {R['t_load']:.0f} мин</td></tr>
</table></div>

<h2>2.3 Цагт, өдөрт хэдийг ухах вэ</h2>
<div class="box calc"><table>
<tr><td>Хово 1 эргэлт = ачих 4 + өгсөх (6 км/ц) + буулгах, эргэх 2 + буцах (12 км/ц) + хүлээх 0.5 мин. Гүн рүү орох тусам зам уртасна.</td><td class="r">7.7 → 10.3 мин</td></tr>
<tr><td>2 Хово цагт хэдэн рейс хийх вэ (экскаватор цагт 15-аас ихийг ачиж чадахгүй)</td><td class="r">12 – 15 рейс</td></tr>
<tr><td>Бодит ажил: цагт 45 мин (75 %) — зогсолт, тос, хүлээлт</td><td class="r">9 – 11 рейс/цаг</td></tr>
<tr><td>10 цагийн ээлжид 1 цаг хоол, түлш → 9 цаг бодит ажил</td><td class="r">{f0(st[2]['prod_day'])} – {f0(st[0]['prod_day'])} м³/өдөр</td></tr>
</table></div>

<h2>2.4 Хэд хоног, хэдэн төгрөг</h2>
<div class="box calc"><table>
<tr><td>Ухах ажил (давхарга бүрийг өөрийн хурдаар)</td><td class="r">{f1(R['days_work'])} өдөр</td></tr>
<tr><td>+ бэлтгэл 0.5 өдөр + дээж авах 0.5 өдөр</td><td class="r">{f1(R['days_total'])} → {days_total} өдөр</td></tr>
<tr><td>+ цаг агаар, эвдрэлийн нөөц 15 %</td><td class="r">≈ {days_res} өдөр</td></tr>
<tr><td>Зардал: {f0(R['V'])} м³ × {f0(C.PRICE)} ₮</td><td class="r">{f0(R['cost'])} ₮ ≈ {mln(R['cost'])} сая ₮</td></tr>
<tr><td>1 өдрийн дундаж зардал</td><td class="r">≈ {R['cost'] / R['days_total'] / 1e6:.1f} сая ₮</td></tr>
</table></div>
<div class="ok"><b>Шалгах арга:</b> Өдөр бүр Хово-гийн рейсийг тоолоод 13.3-аар үржүүл → тэр өдрийн ухсан цул м³ (ойролцоо). Хүснэгтийн «м³ / өдөр»-тэй харьцуул. Их зөрвөл шалтгааныг ол (Хово хүлээх, экскаватор зогсох).</div>
</div>
"""

sched_rows = "".join(
    f"<tr><td>{s['day']}</td><td class='l'>{s['work']}</td><td>{'—' if not s['trips'] else f0(s['trips'])}</td><td>{f0(s['cum'])}</td><td>{s['depth']}</td><td>{mln(s['cum'] * C.PRICE)}</td></tr>"
    for s in sched)
schedpage = f"""
<div class="page">
<div class="hdr"><h1>3. Ажлын <b>хуваарь</b>, операторын заавар</h1><p>1 ээлж (10 цаг) · Экскаватор 1 + Хово 2</p></div>
<h2>3.1 Өдөр бүрийн зорилт</h2>
<div class="box"><table>
<tr><th>Өдөр</th><th class="l">Ажил</th><th>Рейс<br>(зорилт)</th><th>Нийт ухсан,<br>м³ цул</th><th>Өдрийн эцэст<br>гүйцэтгэл</th><th>Нийт зардал,<br>сая ₮</th></tr>
{sched_rows}
</table>
<small>Гүйцэтгэлийг тухайн шатны эзэлхүүнээр (м³) бодсон. Дээд шат хамгийн өргөн тул удаан, доод шатууд хурдан дуусна. Хоцорвол нөөц өдрүүд ({days_res - days_total} өдөр) ашиглана.</small></div>

<h2>3.2 Оператор өдөр бүр</h2>
<div class="box"><ul>
<li>Ажил эхлэхээс өмнө: хана, ирмэгт ан цав, нуралт байгаа эсэхийг харна. Байвал ажил эхлэхгүй.</li>
<li>Рейсийг тоолж бичнэ (Хово тус бүр). Орой нийлбэрийг өдрийн зорилттой харьцуулна.</li>
<li>Шатны гүнг шон, түвшин хэмжигчээр шалгана: −5, −10, −15 м. Хэт гүн ухахгүй (илүү мөнгө).</li>
<li>Хана: 1-р шат 45° (1 м доош = 1 м хойш), 2, 3-р шат 60° (1 м доош = 0.6 м хойш). Хэт эгц бол нурна, хэт налуу бол илүү ухалт.</li>
<li>Рамп 6 м өргөн, 12 % (8 м явахад 1 м өгсөнө). Гадна ирмэгт 1 м шороон далан.</li>
<li>Шороог зөвхөн буулгах талбайд, ухмалын ирмэгээс 13 м-ээс цааш асгана.</li>
<li>−15 м-ээс доош: экскаватор ёроол дээр зогсож нүх ухна. <b>Нүхэнд хүн орохгүй.</b></li>
<li>−20 м-т хүрмэгц: шанагаар дээж гаргаж, уут бүрт гүн, огноо, цагийг бичнэ. Зураг авна.</li>
</ul></div>
<div class="warn"><b>Ажлыг зогсоох:</b> хана нурах, ан цав гарах, ус орох, Хово рампаар өгсөж чадахгүй гулсах, хүн ухмалын ирмэгээр явах.</div>
</div>
"""



bf = R["bf"]
GRAND = R["cost"] + bf["total"]
GRAND_ALT = R["cost"] + bf["total_alt"]
days_all = math.ceil(R["days_total"] + bf["days"])
days_all_res = math.ceil((R["days_total"] + bf["days"]) * 1.15)
bf_rows = "".join(
    f"<tr><td class='l'>{it['name']}</td><td class='l'>{it['what']}</td><td>{it['basis']}</td><td>{'зэрэг' if it['days'] == 0 else f1(it['days'])}</td><td><b>{mln(it['cost'])}</b></td></tr>"
    for it in bf["items"])
bfpage = f"""
<div class="page">
<div class="hdr"><h1>4. Овоолго үүсгэх, <b>нөхөн булах</b></h1><p>Дээж авсны дараа ухмалыг буцааж булах хүртэлх бүх ажил, зардал</p></div>
<h2>4.1 Ажлын дараалал</h2>
<div class="box">
<div class="step"><div class="c">А</div><div><b>Ухахаас өмнө:</b> овоолгын талбай (76 × 48 м) ба ухмалын талбайн (≈ {f0(R['area_pit'])} м²) шимт хөрсийг 20 см зузаанаар хуулж, <b>тусад нь</b> жижиг овоо болгоно. Сүүлд буцааж дэвсэнэ.</div></div>
<div class="step"><div class="c">Б</div><div><b>Ухах үед:</b> Хово шороог овоолгод асгана. Бульдозер түүнийг 5 м-ээр 2 үе болгож тэгшилнэ (ухах ажилтай зэрэг явна, тусдаа өдөр шаардахгүй).</div></div>
<div class="step"><div class="c r">В</div><div><b>Дээж авсны дараа:</b> экскаватор овоолгоос ачиж, Хово эхлээд рампаар ёроол руу орж асгана. Дүүрэхийн хэрээр ухмалын ирмэгээс асгана. 1 рейс {bf['bf_passes']} шанага ≈ {bf['bf_load_bank']:.1f} м³ цул, 1 эргэлт ≈ {bf['bf_cycle']:.1f} мин (зам богино, ухах шаардлагагүй).</div></div>
<div class="step"><div class="c">Г</div><div><b>Сүүлд:</b> бульдозер гадаргууг тэгшилж, шимт хөрсийг буцааж дэвсэнэ. Булсан шороо нягтарч ≈ {f0(bf['surplus'])} м³ илүү гарна. Үүнийг ухмалын дээр бага зэрэг овон болгож үлдээвэл суултаар тэгширнэ.</div></div>
</div>
<h2>4.2 Зардал</h2>
<div class="box"><table>
<tr><th class="l">Ажил</th><th class="l">Хэмжээ</th><th>Үнэлгээ</th><th>Өдөр</th><th>Сая ₮</th></tr>
{bf_rows}
<tr class="tot"><td class="l" colspan="3">Овоолго + нөхөн булалт</td><td>{f1(bf['days'])}</td><td>{mln(bf['total'])}</td></tr>
</table>
<small>⚠ Үнэлгээ: зөвхөн 6 700 ₮/м³ гэсэн үнэ мэдэгдэж байгаа. Гэрээлэгч өдөрт ≈ {f0(R['cost'] / R['days_work'])} ₮ (3 техник, 9 цаг) олно гэж үзээд 3 техникийн 1 цаг ≈ {f0(bf['hour_fleet'])} ₮, 1 техник (бульдозер) ≈ {f0(bf['hour_machine'])} ₮ гэж тооцсон. Бодит үнийг гэрээлэгчээс авна.</small></div>

<h2>4.3 Бүх ажлын нийт зардал</h2>
<div class="box"><table>
<tr><th class="l">Ажил</th><th>Өдөр</th><th>Сая ₮</th></tr>
<tr><td class="l">Ухах, дээж авах (2-р бүлэг)</td><td>{f1(R['days_total'])}</td><td>{mln(R['cost'])}</td></tr>
<tr><td class="l">Овоолго үүсгэх, нөхөн булах (4.2)</td><td>{f1(bf['days'])}</td><td>{mln(bf['total'])}</td></tr>
<tr class="tot"><td class="l">НИЙТ</td><td>{days_all} өдөр (нөөцтэй {days_all_res})</td><td>{mln(GRAND)}</td></tr>
<tr><td class="l">Хэрвээ гэрээлэгч булалтыг ч мөн {f0(C.PRICE)} ₮/м³-ээр авбал</td><td>адил</td><td style="color:#d7261e"><b>{mln(GRAND_ALT)}</b></td></tr>
</table></div>
<div class="warn"><b>Анхаарах:</b>
<ul><li>Булалт нь ухалтаас хялбар (сул шороо ачна, зам богино). Тиймээс <b>булалтыг 1 м³-ээр биш, цагаар эсвэл хямд үнээр</b> тохирох нь ашигтай. Ялгаа нь ≈ {mln(GRAND_ALT - GRAND)} сая ₮.</li>
<li>Лабораторийн хариу хүлээж байгаад булах бол техник хоосон зогсох хөлсийг гэрээнд тусгана. Эсвэл ухсан даруйд дээжээ аваад шууд булна.</li>
<li>Бульдозер энэ 3 техникт ороогүй. Түүнийг ≈ {f0(bf['dozer_form_h'] + bf['dozer_fin_h'])} цаг тусад нь түрээслэнэ.</li></ul></div>
</div>
"""

cover = f"""
<div class="page cover">
<div class="cv-top">
 <img src="{LOGO_URI}" style="height:70px">

</div>
<div class="cv-mid">
 <div class="cv-kind">НЭГДСЭН ТАЙЛАН</div>
 <div class="cv-sub" style="font-size:14pt;color:#13306b;font-weight:bold;margin:12px 0 0">Сүүж уулын бал чулууны орд</div>
 <div class="cv-title"><b>20 м</b> гүнд дээж авах<br>ухмалын зохион байгуулалт,<br>нөхөн булалт, хугацаа, зардал</div>
 <div class="cv-sub">15 м шатлалтай ухмал + 5 м дээжний нүх · Экскаватор 3.2 м³ × 1, Хово 18 м³ × 2</div>
 <div class="big" style="margin-top:22px">
  <div class="k"><div class="n">{f0(R['V'])}</div><div class="u">м³ ухалт (цул)</div></div>
  <div class="k"><div class="n">{mln(R['cost'])}</div><div class="u">сая ₮ ухах</div></div>
  <div class="k y"><div class="n">{mln(GRAND)}</div><div class="u">сая ₮ нийт<br>(овоолго, булалттай)</div></div>
  <div class="k"><div class="n">{days_all}</div><div class="u">ажлын өдөр<br>(нөөцтэй {days_all_res})</div></div>
 </div>
</div>
<table class="sign">
<tr><td class="l" style="width:35%">Захиалагч</td><td class="l">«Вай эйч графит нэчүрал» ХХК</td></tr>
<tr><td class="l">Тусгай зөвшөөрөл</td><td class="l">MV-018976 «Дарцагт» (ашиглалтын)</td></tr>
<tr><td class="l">Боловсруулсан</td><td class="l">«Грийтвишн» ХХК · Инженер Т.Давааням · Инженер Ч.Аръяабал</td></tr>
<tr><td class="l">Огноо</td><td class="l">2026 оны 11 сарын 7</td></tr>
</table>
<div class="cv-city">Улаанбаатар · 2026</div>
</div>
"""

toc = f"""
<div class="page">
<div class="hdr"><h1>Агуулга, <b>хураангуй</b></h1><p>Тайлан нь 7 хуудас бичвэр, 2 хуудас A3 зургаас бүрдэнэ</p></div>
<h2>Агуулга</h2>
<div class="box"><table class="toc">
<tr><td class="l">Хураангуй</td><td>2</td></tr>
<tr><td class="l"><b>1. Даалгавар, сонгосон арга</b> — анхны өгөгдөл, арга, хувилбарын харьцуулалт</td><td>3</td></tr>
<tr><td class="l"><b>2. Ажлын хэмжээ, хугацаа, зардал</b> — куб, рейс, бүтээмж, өдөр, төгрөг</td><td>4</td></tr>
<tr><td class="l"><b>3. Ажлын хуваарь, операторын заавар</b> — өдөр бүрийн зорилт</td><td>5</td></tr>
<tr><td class="l"><b>4. Овоолго үүсгэх, нөхөн булах</b> — дараалал, зардал, нийт зардал</td><td>6</td></tr>
<tr><td class="l"><b>5. Гэрээ, аюулгүй ажиллагаа, таамаг</b></td><td>7</td></tr>
<tr><td class="l"><b>6. Дүгнэлт, санал</b></td><td>7</td></tr>
<tr><td class="l">Хавсралт 1. Ухмалын план, ажлын хэмжээ (A3, М 1:500)</td><td>8</td></tr>
<tr><td class="l">Хавсралт 2. Хөндлөн огтлол А-А, дээжний нүх (A3, М 1:200)</td><td>9</td></tr>
</table></div>
<h2>Хураангуй</h2>
<div class="box">
<p style="margin:2px 0 6px">20 м гүнээс дээж авахын тулд Хово-г 20 м хүртэл оруулах бүтэн ухмал хийвэл
<b>{f0(R['opts'][-1]['V'])} м³ буюу {mln(R['opts'][-1]['cost'])} сая ₮</b> болно. Иймд дараах аргыг санал болгож байна:</p>
<ul>
<li><b>0 → −15 м:</b> 3 шатлалтай ухмал (5 м-ийн шат), ханан дагуу эргэлдэх 6 м өргөн, 12 %-ийн налуу замтай. Хово ёроол хүртэл орж ачигдана.</li>
<li><b>−15 → −20 м:</b> экскаватор 15 м-ийн ёроол дээр зогсож 3 × 3 м ёроолтой нүх ухна. Дээжийг шанаганаас авна, нүхэнд хүн орохгүй.</li>
</ul>
<table>
<tr><th class="l">Үзүүлэлт</th><th>Утга</th></tr>
<tr><td class="l">Нийт ухалт (цул)</td><td><b>{f0(R['V'])} м³</b></td></tr>
<tr><td class="l">Зардал ({f0(C.PRICE)} ₮/м³)</td><td><b>{f0(R['cost'])} ₮ ≈ {mln(R['cost'])} сая ₮</b></td></tr>
<tr><td class="l">Хугацаа (1 ээлж / 2 ээлж)</td><td><b>{days_total} ажлын өдөр</b> (нөөцтэй {days_res}) / ≈ {math.ceil(R['days_work'] / 2 + 1)} өдөр</td></tr>
<tr><td class="l">Хэмнэлт (бүтэн 20 м ухмалтай харьцуулахад)</td><td>{f0(R['opts'][-1]['V'] - R['V'])} м³ · ≈ {mln(R['opts'][-1]['cost'] - R['cost'])} сая ₮</td></tr>
<tr><td class="l">Овоолго үүсгэх, нөхөн булах</td><td><b>{mln(bf['total'])} сая ₮</b> · {f1(bf['days'])} өдөр</td></tr>
<tr class="tot"><td class="l">НИЙТ ЗАРДАЛ (ухах + булах)</td><td>{mln(GRAND)} сая ₮ · {days_all} өдөр</td></tr>
<tr><td class="l">Хамгийн их зардалтай хэсэг</td><td>1-р шат (0 … −5 м): {mln(st[0]['cost'])} сая ₮</td></tr>
<tr><td class="l">Шороо буулгах талбай</td><td>76 × 48 м, 10 м өндөр, ухмалаас 14 м зайтай</td></tr>
</table>
<div class="warn" style="margin-top:8px"><b>Гол эрсдэл:</b> гэрээлэгч Хово-гийн тоогоор (сул м³) тооцвол зардал
<b>{mln(R['cost_loose'])} сая ₮</b> болж {mln(R['cost_loose'] - R['cost'])} сая ₮-өөр өснө. Гэрээнд маркшейдерийн хэмжилтээр, цул м³-ээр тооцохыг заавал бичнэ.</div>
</div>
</div>
"""

sec45 = f"""
<div class="page">
<div class="hdr"><h1>5. Гэрээ, аюулгүй ажиллагаа, <b>таамаг</b></h1><p>Мөнгө төлөхөөс өмнө, ажил эхлэхээс өмнө</p></div>
<h2>5.1 Гэрээнд заавал тусгах</h2>
<div class="box"><ul>
<li>Ухалтыг <b>маркшейдерийн хэмжилтээр, цул м³-ээр</b> тооцно. Хово тоолбол 30 %-иар ({mln(R['cost_loose'] - R['cost'])} сая ₮) их төлнө.</li>
<li>{f0(C.PRICE)} ₮-нд юу орсныг тодорхой бич: ухах, зөөх, буулгах, түлш, оператор, буулгах талбайн тэгшилгээ.</li>
<li>Нөхөн булалт энэ үнэд ороогүй. Булалтыг цагаар эсвэл хямд үнээр тусад нь тохирно (4-р бүлэг).</li>
<li>Ажлыг шатаар хүлээн авна: −5, −10, −15 м-т хэмжилт хийж, гүйцэтгэлээр төлнө.</li>
</ul></div>
<h2>5.2 Аюулгүй ажиллагаа</h2>
<div class="box"><ul>
<li>Дээжний нүхэнд (−15 … −20 м) хүн орохгүй. Дээжийг шанаганаас авна.</li>
<li>Рампын гадна ирмэгт 1 м шороон далан. Ачаатай Хово 1-р араагаар өгсөнө.</li>
<li>Ухмалын ирмэгээс 13 м дотор шороо асгахгүй, техник зогсоохгүй. Ирмэгийг тууз, тэмдгээр хашина.</li>
<li>Хана нурах, ан цав гарах, ус орох, Хово гулсах үед ажлыг зогсооно.</li>
</ul></div>
<h2>5.3 Таамаг (батлах шаардлагатай)</h2>
<div class="box"><table>
<tr><th class="l">Таамаг</th><th class="l">Өөр байвал</th></tr>
<tr><td class="l">2, 3-р шатны налуу 60°, шат хооронд 2 м тавцан (хатуу чулуулаг)</td><td class="l">Сул чулуулагт 45° → ухалт, зардал өснө</td></tr>
<tr><td class="l">Экскаватор ёроолоос ≈ 7 м хүртэл ухаж чадна</td><td class="l">Маркийн үзүүлэлтээр шалгана</td></tr>
<tr><td class="l">Сулралт 1.3; шанага 90 % дүүрнэ; 1 шанага 30 сек</td><td class="l">Том чулуу, хөлдсөн хөрсөнд удааширна</td></tr>
<tr><td class="l">Газрын ус гарахгүй</td><td class="l">Зумф, насос → хугацаа өснө</td></tr>
<tr><td class="l">Бульдозер, булалтын цагийн үнэ ≈ гэрээлэгчийн ухалтын өдрийн орлогоор</td><td class="l">Бодит үнийн санал авна</td></tr>
</table></div>

<div class="hdr" style="margin-top:12px"><h1>6. Дүгнэлт, <b>санал</b></h1></div>
<div class="box" style="border-top:1.5px solid #13306b; border-radius:6px"><ol style="margin:2px 0; padding-left:20px">
<li>20 м-т хүрэх хамгийн бага зардалтай арга нь <b>15 м шатлалтай ухмал + 5 м дээжний нүх</b>: {f0(R['V'])} м³, ≈ {mln(R['cost'])} сая ₮, {days_total} ажлын өдөр.</li>
<li>Энэ нь Хово-г 20 м хүртэл оруулахаас {mln(R['opts'][-1]['cost'] - R['cost'])} сая ₮ хямд.</li>
<li>Овоолго үүсгэх, дээж авсны дараа буцааж булах нь ≈ {mln(bf['total'])} сая ₮, {f1(bf['days'])} өдөр. <b>Бүх ажил ≈ {mln(GRAND)} сая ₮, {days_all} ажлын өдөр.</b> Булалтыг 1 м³-ээр тооцуулбал {mln(GRAND_ALT)} сая ₮ болох тул цагаар тохирно.</li>
<li>Рампыг 15 % болгох эсвэл тавцангүй хийх нь 7–12 сая ₮ хэмнэх ч Хово гулсах, чулуу унах эрсдэлтэй тул санал болгохгүй.</li>
<li>Дараагийн алхам: (1) ухалтыг цул м³-ээр, булалт ба бульдозерыг цагаар тохирох, (2) газар дээр хил, рамп, овоолгын талбайг тэмдэглэх, (3) 1-р шатны эхний 2 өдрийн гүйцэтгэлээр бүтээмжийг шалгаж, хуваарийг тодотгох.</li>
</ol></div>
</div>
"""

def html(body, name):
    path = os.path.join(TMP, name + ".html")
    open(path, "w", encoding="utf-8").write(f"<!doctype html><html lang='mn'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    pdf = os.path.join(TMP, name + ".pdf")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", path],
                   check=True, capture_output=True, timeout=120)
    return pdf

import pymupdf
p0 = html(cover + toc, "p0")
p1 = html(summary + calcpage + schedpage + bfpage + sec45, "p1")
subprocess.run([sys.executable, "-I", os.path.join(HERE, "ukhmal20_draw.py"), TMP], check=True, capture_output=True, timeout=900)
w = PdfWriter()
for f in (p0, p1, os.path.join(TMP, "drawings.pdf")):
    for pg in PdfReader(f).pages:
        w.add_page(pg)
w.add_metadata({"/Title": "20 м-т дээж авах ухмал — нэгдсэн тайлан", "/Author": "Грийтвишн ХХК"})
mid = os.path.join(TMP, "merged.pdf")
with open(mid, "wb") as fh:
    w.write(fh)
# хуудасны дугаар (нүүрээс бусад)
doc = pymupdf.open(mid)
n = len(doc)
for i, pg in enumerate(doc):
    if i == 0:
        continue
    r = pg.rect
    txt = f"Хуудас {i + 1} / {n}"
    if r.width > 1000:      # A3 хавсралт: штампын дээд талд, баруун
        pt = pymupdf.Point(r.width - 150, 12)
        pg.insert_text(pt, f"Хавсралт {i - 6} · " + txt, fontname="ar", fontfile=r"C:\Windows\Fonts\arial.ttf", fontsize=8, color=(0.3, 0.3, 0.3))
    else:
        pt = pymupdf.Point(r.width - 100, r.height - 14)
        pg.insert_text(pt, txt, fontname="ar", fontfile=r"C:\Windows\Fonts\arial.ttf", fontsize=8, color=(0.4, 0.4, 0.4))
        pg.insert_text(pymupdf.Point(37, r.height - 14), "«Грийтвишн» ХХК · Сүүж уул · 20 м-т дээж авах ухмал · нэгдсэн тайлан",
                       fontname="ar", fontfile=r"C:\Windows\Fonts\arial.ttf", fontsize=8, color=(0.4, 0.4, 0.4))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT, garbage=3, deflate=True)
for f in (p0, p1):
    print(f, len(PdfReader(f).pages), "pages")
print("OUT", OUT, n, "pages", "TMP", TMP)
