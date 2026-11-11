"""20 м-т дээж авах ухмал — ТАНИЛЦУУЛГА, МОНГОЛ + 中文, ЗАРДАЛГҮЙ хувилбар (хятад захиралд).
Мөнгөн дүн (₮, үнэ, зардал) огт орохгүй: эзэлхүүн, рейс, хугацаа, арга, аюулгүй ажиллагаа, зураг.
Ажиллуулах: python -I ukhmal20_report_cn.py
Тооцоо: ukhmal20_calc.py, зураг: ukhmal20_draw_cn.py (ukhmal20_draw.py-оос үүсгэсэн)."""
import os as _os
VAULT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))  # vault-ийн үндэс, аль ч компьютерт
import pathlib as _pl
LOGO_URI = _pl.Path(VAULT, "_system", "skills", "zurag-shtamp", "gv_logo.png").as_uri()
import os, sys, subprocess, tempfile, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8")
import ukhmal20_calc as C
from pypdf import PdfReader, PdfWriter
import pymupdf

OUT = _os.path.join(VAULT, r"02-Projects\Ажил\Вай эйч графит нэчүрал ХХК\Сүүж уул\Ухмал 20 м\Сүүж уул - 20 м-т дээж авах ухмал - танилцуулга (MN-CN).pdf")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TMP = tempfile.mkdtemp(prefix="u20cn_")
R = C.calc()
st = R["stages"]
bf = R["bf"]
f0 = lambda v: f"{v:,.0f}".replace(",", "\u00a0")
f1 = lambda v: f"{v:.1f}"
days_total = math.ceil(R["days_total"]); days_res = math.ceil(R["days_reserve"])
days_2sh = math.ceil(R["days_work"] / 2 + 1)
days_all = math.ceil(R["days_total"] + bf["days"])
days_all_res = math.ceil((R["days_total"] + bf["days"]) * 1.15)
full = R["opts"][-1]["V"]
save = full - R["V"]

def cn(s):
    return f"<span class='cn'>{s}</span>"
def bi(mn, zh, br=True):
    return f"{mn}{'<br>' if br else ' · '}{cn(zh)}"

MN_ST = ["1-р шат", "2-р шат", "3-р шат", "Дээжний нүх"]
CN_ST = ["第1台阶", "第2台阶", "第3台阶", "取样坑"]
DEP = ["0 … −5 м", "−5 … −10 м", "−10 … −15 м", "−15 … −20 м"]
ENDS = ["−5 м", "−10 м", "−15 м", "−20 м"]

# ---------- өдрийн хуваарь ----------
def progress(c):
    acc = 0.0
    for k, s_ in enumerate(st):
        if c < acc + s_["V"] - 1:
            pct = (c - acc) / s_["V"] * 100
            if pct < 99.5:
                return bi(f"{MN_ST[k]} {pct:.0f} %", f"{CN_ST[k]} {pct:.0f}%")
            return bi(f"{ENDS[k]} хүрсэн", f"到达{ENDS[k].replace(' м', '米')}")
        acc += s_["V"]
    return bi("−20 м хүрсэн ✔", "到达−20米 ✔")

sched, day, left, cum = [], 1, [s["V"] for s in st], 0.0
cap, i = 0.5, 0
while i < len(st):
    works, trips, c = [], 0, cap
    while c > 1e-6 and i < len(st):
        use = min(c, left[i] / st[i]["prod_day"])
        vol = use * st[i]["prod_day"]
        left[i] -= vol; cum += vol; c -= use
        trips += vol * C.SWELL / R["load_loose"]
        works.append(i)
        if left[i] <= 1e-6:
            i += 1
    ks = list(dict.fromkeys(works))
    mn = " + ".join(MN_ST[k] for k in ks); zh = " + ".join(CN_ST[k] for k in ks)
    if day == 1:
        mn = "Бэлтгэл (хил, рамп тэмдэглэх) + " + mn; zh = "准备(放线、标出坡道)+ " + zh
    sched.append(dict(day=day, work=bi(mn, zh), trips=trips, cum=cum, depth=progress(cum)))
    day += 1; cap = 1.0
sched.append(dict(day=day, work=bi("Дээж авах, тэмдэглэх; техник гаргах", "取样、标记;设备撤出"), trips=0, cum=cum,
                  depth=bi("−20 м хүрсэн ✔", "到达−20米 ✔")))

CSS = """
@page { size: A4; margin: 11mm 13mm 12mm 13mm; }
* { box-sizing: border-box; }
body { font-family: Arial, "Microsoft YaHei", sans-serif; color: #1d2433; font-size: 9.8pt; line-height: 1.24; margin: 0; }
.cn { color: #1f4e9a; font-family: "Microsoft YaHei", Arial, sans-serif; font-size: 0.93em; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
.hdr { background: #13306b; color: #fff; border: 2px solid #ffd21f; border-radius: 6px; padding: 7px 14px; margin-bottom: 8px; }
.hdr h1 { margin: 0; font-size: 16pt; } .hdr h1 b { color: #ffd21f; font-weight: 700; } b, strong { font-weight: 700; }
.hdr h1 .cn { color: #ffd21f; font-size: 13pt; font-weight: bold; }
.hdr p { margin: 3px 0 0; font-size: 9.5pt; color: #dfe7f5; } .hdr p .cn { color: #ffe680; }
h2 { background: #13306b; color: #fff; font-size: 11pt; padding: 4px 10px; border-radius: 5px 5px 0 0; margin: 7px 0 0; }
h2 .cn { color: #ffe680; font-size: 10pt; }
.box { border: 1.5px solid #13306b; border-top: none; border-radius: 0 0 6px 6px; padding: 5px 9px; }
.box p { margin: 2px 0 5px; }
.big { display: grid; grid-template-columns: repeat(4, 1fr); gap: 7px; margin: 8px 0 4px; }
.k { border: 2px solid #13306b; border-radius: 8px; padding: 8px 6px; text-align: center; background: #f3f6fc; }
.k .n { font-size: 21pt; font-weight: bold; color: #13306b; line-height: 1.1; }
.k .u { font-size: 9pt; color: #333; }
.k.y { background: #ffd21f; }
table { width: 100%; border-collapse: collapse; font-size: 9.1pt; }
th { background: #dfe7f5; color: #13306b; } th, td { border: 1px solid #9aa7c0; padding: 2px 5px; text-align: center; }
td.l, th.l { text-align: left; }
tr.tot td { background: #ffd21f; font-weight: bold; color: #13306b; }
td.r { text-align: right; white-space: nowrap; font-weight: bold; }
.nw { white-space: nowrap; }
.step { display: grid; grid-template-columns: 30px 1fr; gap: 8px; margin: 5px 0; align-items: start; }
.step .c { width: 27px; height: 27px; border-radius: 50%; background: #13306b; color: #fff; font-weight: bold; font-size: 12pt;
           display: flex; align-items: center; justify-content: center; }
.step .c.r { background: #d7261e; }
.warn { background: #fdecea; border: 1.5px solid #d7261e; border-radius: 6px; padding: 6px 10px; margin-top: 8px; color: #6d0f0f; }
.ok { background: #eaf6ec; border: 1.5px solid #2e9e44; border-radius: 6px; padding: 6px 10px; margin-top: 7px; }
small { color: #555; }
ul, ol { margin: 2px 0; padding-left: 20px; } li { margin: 2px 0; }
.cover { display: flex; flex-direction: column; height: 268mm; }
.cv-top { display: flex; align-items: center; gap: 14px; border-bottom: 3px solid #13306b; padding-bottom: 10px; }
.cv-mid { flex: 1; display: flex; flex-direction: column; justify-content: center; }
.cv-kind { font-size: 13pt; font-weight: bold; color: #fff; background: #13306b; display: inline-block; padding: 5px 14px; border-radius: 4px; align-self: flex-start; }
.cv-kind .cn { color: #ffe680; }
.cv-title { font-size: 25pt; font-weight: bold; color: #13306b; line-height: 1.2; margin-top: 14px; }
.cv-title b { color: #c8102e; }
.cv-title .cn { font-size: 20pt; }
.cv-sub { font-size: 12pt; color: #333; margin-top: 10px; }
.cv-city { text-align: center; color: #555; margin-top: 10px; }
table.sign td { padding: 6px 8px; font-size: 10.5pt; }
"""

cover = f"""
<div class="page cover">
<div class="cv-top"><img src="{LOGO_URI}" style="height:70px"></div>
<div class="cv-mid">
 <div class="cv-kind">ТАНИЛЦУУЛГА · {cn('项目说明')}</div>
 <div class="cv-sub" style="font-size:14pt;color:#13306b;font-weight:bold;margin:12px 0 0">Сүүж уулын бал чулууны орд · {cn('Сүүж уул 石墨矿床')}</div>
 <div class="cv-title"><b>20 м</b> гүнд дээж авах<br>ухмалын зохион байгуулалт,<br>нөхөн булалт, хугацаа
  <div class="cn" style="margin-top:10px"><b>20米</b>深取样坑施工布置、<br>回填及工期</div></div>
 <div class="cv-sub">15 м шатлалтай ухмал + 5 м дээжний нүх · Экскаватор 3.2 м³ × 1, Хово 18 м³ × 2<br>
  {cn('15米台阶式采坑 + 5米取样小坑 · 挖掘机(3.2 m³铲斗)1台,豪沃自卸车(18 m³)2台')}</div>
 <div class="big" style="margin-top:22px">
  <div class="k"><div class="n">{f0(R['V'])}</div><div class="u">м³ ухалт (цул)<br>{cn('挖方 m³(实方)')}</div></div>
  <div class="k"><div class="n">{f0(R['trips'])}</div><div class="u">Хово рейс<br>{cn('自卸车车次')}</div></div>
  <div class="k"><div class="n">{days_total}</div><div class="u">өдөр: ухах, дээж авах<br>{cn('开挖及取样(天)')}</div></div>
  <div class="k y"><div class="n">{days_all}</div><div class="u">өдөр нийт (булалттай)<br>{cn('总工期含回填(天)')}</div></div>
 </div>
</div>
<table class="sign">
<tr><td class="l" style="width:32%">{bi('Захиалагч', '业主', False)}</td><td class="l">«Вай эйч графит нэчүрал» ХХК</td></tr>
<tr><td class="l">{bi('Тусгай зөвшөөрөл', '采矿许可证', False)}</td><td class="l">MV-018976 «Дарцагт» (ашиглалтын · {cn('采矿')})</td></tr>
<tr><td class="l">{bi('Боловсруулсан', '编制', False)}</td><td class="l">«Грийтвишн» ХХК · Инженер Т.Давааням · Инженер Ч.Аръяабал</td></tr>
<tr><td class="l">{bi('Огноо', '日期', False)}</td><td class="l">2026 оны 11 сарын 7 · {cn('2026年11月7日')}</td></tr>
</table>
<div class="cv-city">Улаанбаатар · {cn('乌兰巴托')} · 2026</div>
</div>
"""

summary = f"""
<div class="page">
<div class="hdr"><h1>Хураангуй · {cn('摘要')}</h1><p>Юу хийх, хэдэн куб, хэд хоног · {cn('做什么、挖多少、需要多少天')}</p></div>
<h2>Санал болгож буй арга · {cn('推荐方案')}</h2>
<div class="box">
<p>20 м гүнээс дээж авахын тулд Хово-г 20 м хүртэл оруулах бүтэн ухмал хийвэл <b>{f0(full)} м³</b> ухна. Иймд дараах аргыг санал болгож байна:<br>
{cn(f'若让自卸车下到20米坑底,需开挖 <b>{f0(full)} m³</b>。因此推荐以下方案:')}</p>
<ul>
<li><b>0 → −15 м:</b> 3 шатлалтай ухмал (5 м-ийн шат), ханан дагуу эргэлдэх 6 м өргөн, 12 %-ийн налуу замтай. Хово ёроол хүртэл орж ачигдана.<br>
{cn('<b>0 → −15米:</b>3个台阶(每阶5米),沿坑壁螺旋布置宽6米、坡度12%的坡道。自卸车下到坑底装车。')}</li>
<li><b>−15 → −20 м:</b> экскаватор 15 м-ийн ёроол дээр зогсож 3 × 3 м ёроолтой нүх ухна. Дээжийг шанаганаас авна, нүхэнд хүн орохгүй.<br>
{cn('<b>−15 → −20米:</b>挖掘机站在15米坑底,向下挖底面3×3米的小坑。从铲斗中取样,人员不进入小坑。')}</li>
</ul>
<table>
<tr><th class="l">Үзүүлэлт · {cn('指标')}</th><th>Утга · {cn('数值')}</th></tr>
<tr><td class="l">{bi('Нийт ухалт (цул)', '总挖方(实方)', False)}</td><td><b>{f0(R['V'])} м³</b></td></tr>
<tr><td class="l">{bi('Хово рейс (2 машин)', '自卸车车次(2台)', False)}</td><td><b>{f0(R['trips'])}</b> · 1 рейс ≈ {R['load_bank']:.1f} м³ цул</td></tr>
<tr><td class="l">{bi('Ухах, дээж авах хугацаа: 1 ээлж', '开挖及取样工期:单班', False)}</td><td><b>{days_total} өдөр</b> (нөөцтэй {days_res}) · {cn(f'{days_total}天(含储备{days_res}天)')}</td></tr>
<tr><td class="l">{bi('Өдөр, шөнө 2 ээлжээр', '昼夜两班', False)}</td><td>≈ {days_2sh} өдөр · {cn(f'约{days_2sh}天')}</td></tr>
<tr><td class="l">{bi('Бүтэн 20 м ухмалаас хэмнэх ухалт', '比20米全深采坑少挖', False)}</td><td><b>{f0(save)} м³</b> ({save / full * 100:.0f} %)</td></tr>
<tr><td class="l">{bi('Овоолго үүсгэх, нөхөн булах', '排土场整形及回填', False)}</td><td>{f1(bf['days'])} өдөр · {cn(f'{f1(bf["days"])}天')}</td></tr>
<tr class="tot"><td class="l">{bi('НИЙТ ХУГАЦАА (ухах + булах)', '总工期(开挖 + 回填)', False)}</td><td>{days_all} өдөр (нөөцтэй {days_all_res}) · {cn(f'{days_all}天(含储备{days_all_res}天)')}</td></tr>
<tr><td class="l">{bi('Шороо буулгах талбай', '排土场', False)}</td><td>76 × 48 м, 10 м өндөр, ухмалаас 14 м · {cn('高10米,距采坑14米')}</td></tr>
</table>
</div>

<h2>1.1 Анхны өгөгдөл · {cn('原始数据')}</h2>
<div class="box"><table>
<tr><td class="l" style="width:34%">{bi('Зорилго', '目的', False)}</td><td class="l"><b>20 м гүнээс дээж авах</b>, хамгийн бага ухалтаар<br>{cn('从20米深处取样,开挖量最小')}</td></tr>
<tr><td class="l">{bi('Ухмалын хэлбэр', '采坑形式', False)}</td><td class="l">3 шатлалтай (5 м-ийн шат), ёроол 10 × 10 м, 1-р шат 45°<br>{cn('3个台阶(每阶5米),坑底10×10米,第1台阶坡面角45°')}</td></tr>
<tr><td class="l">{bi('Экскаватор', '挖掘机', False)}</td><td class="l">1 ширхэг, Хятад, 500-р анги, шанага 3.2 м³<br>{cn('1台,国产500级,铲斗3.2 m³')}</td></tr>
<tr><td class="l">{bi('Автосамосвал', '自卸车', False)}</td><td class="l">2 ширхэг Хово, тэвш 18 м³<br>{cn('豪沃2台,车厢18 m³')}</td></tr>
<tr><td class="l">{bi('Ажлын горим', '作业制度', False)}</td><td class="l">1 ээлж = 10 цаг (9 цаг бодит ажил)<br>{cn('每班10小时(实际作业9小时)')}</td></tr>
</table></div>
</div>
"""

method = f"""
<div class="page">
<div class="hdr"><h1>1. Сонгосон <b>арга</b> · {cn('施工方案')}</h1><p>Ямар дарааллаар, яагаад ингэж хийх вэ · {cn('施工顺序及理由')}</p></div>
<h2>1.2 «15 м ухмал + 5 м дээжний нүх» · {cn('“15米采坑 + 5米取样小坑”')}</h2>
<div class="box">
<p>Хово-г 20 м-ийн ёроол хүртэл оруулах гэвэл ухмал хэт томорно: <b>{f0(full)} м³</b>. Тэгэхээр Хово-г зөвхөн <b>15 м</b> хүртэл оруулаад, сүүлийн 5 м-ийг экскаватор өөрөө жижиг нүх болгож ухна. Ингэснээр <b>{f0(save)} м³</b> бага ухна.<br>
{cn(f'若让自卸车下到20米坑底,采坑过大:<b>{f0(full)} m³</b>。因此自卸车只下到<b>15米</b>,最后5米由挖掘机挖一个小坑。这样可少挖<b>{f0(save)} m³</b>。')}</p>
<div class="step"><div class="c">1</div><div><b>1-р шат: 0 → −5 м</b> · {f1(st[0]['days'])} өдөр · {f0(st[0]['V'])} м³<br>
Хамгийн том хэсэг. Хөрс сул тул хана 45° налуу. Рампын (налуу замын) эхний тойргийг зүснэ.<br>
{cn(f'<b>第1台阶:0 → −5米</b> · {f1(st[0]["days"])}天 · {f0(st[0]["V"])} m³。工程量最大。表土松软,坡面角45°。开挖坡道第一圈。')}</div></div>
<div class="step"><div class="c">2</div><div><b>2-р шат: −5 → −10 м</b> · {f1(st[1]['days'])} өдөр · {f0(st[1]['V'])} м³<br>
Чулуулаг эхэлнэ, хана 60°. Шат хооронд 2 м өргөн тавцан үлдээнэ (чулуу өнхрөхийг тосно).<br>
{cn(f'<b>第2台阶:−5 → −10米</b> · {f1(st[1]["days"])}天 · {f0(st[1]["V"])} m³。进入基岩,坡面角60°。台阶之间留2米宽平台(拦挡滚石)。')}</div></div>
<div class="step"><div class="c">3</div><div><b>3-р шат: −10 → −15 м</b> · {f1(st[2]['days'])} өдөр · {f0(st[2]['V'])} м³<br>
Ёроол 10 × 10 м. Хово ёроолд урагш-ухрах-урагш гэж 3 цэгээр эргэж, экскаваторт ухарч ирнэ.<br>
{cn(f'<b>第3台阶:−10 → −15米</b> · {f1(st[2]["days"])}天 · {f0(st[2]["V"])} m³。坑底10×10米。自卸车在坑底三点掉头,倒车靠近挖掘机。')}</div></div>
<div class="step"><div class="c r">4</div><div><b>Дээжний нүх: −15 → −20 м</b> · ≈ 1 өдөр · {f0(st[3]['V'])} м³<br>
Экскаватор ёроол дээр зогсож 3 × 3 м нүх ухна. <b>Нүхэнд хүн орохгүй.</b> Дээжийг 20 м-ээс гарсан шанаганаас авна.<br>
{cn(f'<b>取样小坑:−15 → −20米</b> · 约1天 · {f0(st[3]["V"])} m³。挖掘机站在坑底挖3×3米小坑。<b>人员严禁进入小坑。</b>从20米处挖出的铲斗中取样。')}</div></div>
</div>

<h2>1.3 Хувилбарын харьцуулалт · {cn('方案比较')}</h2>
<div class="box"><table>
<tr><th class="l">Нөхцөл · {cn('方案')}</th><th>Ухалт, м³<br>{cn('挖方 m³')}</th><th>Хугацаа<br>{cn('工期')}</th><th class="l">Тайлбар · {cn('说明')}</th></tr>
<tr><td class="l"><b>Санал болгож буй</b><br>{cn('<b>推荐方案</b>')}</td><td><b>{f0(R['V'])}</b></td><td>{days_total} өдөр<br>{cn(f'{days_total}天')}</td><td class="l">Аюулгүй, хамгийн бага ухалт<br>{cn('安全,开挖量最小')}</td></tr>
<tr><td class="l">Өдөр, шөнө 2 ээлжээр<br>{cn('昼夜两班作业')}</td><td>{f0(R['V'])}</td><td>≈ {days_2sh} өдөр<br>{cn(f'约{days_2sh}天')}</td><td class="l">Гэрэлтүүлэг, 2 дахь оператор хэрэгтэй<br>{cn('需照明及第二班司机')}</td></tr>
<tr><td class="l">Рамп 15 % (эгц)<br>{cn('坡道15%(较陡)')}</td><td>{f0(R['opts'][1]['V'])}</td><td>≈ 1 өдөр бага<br>{cn('约少1天')}</td><td class="l">Ачаатай Хово гулсах эрсдэл<br>{cn('重载自卸车有打滑风险')}</td></tr>
<tr><td class="l">Шат хооронд тавцангүй<br>{cn('台阶间不留平台')}</td><td>{f0(R['opts'][2]['V'])}</td><td>≈ 1.5 өдөр бага<br>{cn('约少1.5天')}</td><td class="l">Зөвхөн хатуу чулуунд; чулуу унах эрсдэл<br>{cn('仅适用于坚硬岩石;有落石风险')}</td></tr>
<tr><td class="l">Шулуун рамп (гадна траншей)<br>{cn('直坡道(外部堑沟)')}</td><td>{f0(R['opts'][3]['V'])}</td><td>≈ 2 өдөр илүү<br>{cn('约多2天')}</td><td class="l">{f0(R['opts'][3]['V'] - R['V'])} м³ илүү ухалт<br>{cn(f'多挖{f0(R["opts"][3]["V"] - R["V"])} m³')}</td></tr>
<tr><td class="l">Хово 20 м хүртэл орох бүтэн ухмал<br>{cn('自卸车下到20米的全深采坑')}</td><td>{f0(full)}</td><td>≈ {math.ceil(full / (R['V'] / R['days_work']) + 1)} өдөр<br>{cn(f'约{math.ceil(full / (R["V"] / R["days_work"]) + 1)}天')}</td><td class="l">{f0(save)} м³ илүү ухалт<br>{cn(f'多挖{f0(save)} m³')}</td></tr>
</table></div>
</div>
"""

stage_rows = "".join(
    f"<tr><td class='l nw'>{MN_ST[k]} <small>({DEP[k]})</small><br>{cn(CN_ST[k])}</td><td class='nw'><b>{f0(s['V'])}</b></td><td class='nw'>{f0(s['V'] * C.SWELL)}</td><td>{f0(s['trips'])}</td>"
    f"<td>{f0(s['route'])}</td><td>{f1(s['cycle'])}</td><td>{f1(s['trips_h'])}</td><td class='nw'>{f0(s['prod_day'])}</td><td><b>{f1(s['days'])}</b></td></tr>"
    for k, s in enumerate(st))
calcpage = f"""
<div class="page">
<div class="hdr"><h1>2. Ажлын хэмжээ, <b>хугацаа</b> · {cn('工程量与工期')}</h1><p>Энгийн арифметик, тоо бүрийг шалгаж болно · {cn('简单算术,每个数字都可核对')}</p></div>
<h2>2.1 Хэдэн куб ухах вэ · {cn('挖方量')}</h2>
<div class="box">
<p>Ухмалыг 5 м-ээр давхарлаж, компьютераар 25 × 25 см-ийн нүдээр тоолсон. Дээд давхарга хамгийн өргөн тул хамгийн их ухалттай.<br>
{cn('采坑按5米分层,用电脑以25×25厘米网格计算。上层最宽,挖方量最大。')}</p>
<table><tr><th class="l">Давхарга<br>{cn('分层')}</th><th>Цул м³<br>{cn('实方')}</th><th>Сул м³ (×1.3)<br>{cn('松方')}</th><th>Хово рейс<br>{cn('车次')}</th><th>Зам, м<br>{cn('运距')}</th><th>1 эргэлт, мин<br>{cn('循环(分)')}</th><th>Рейс / цаг<br>{cn('车次/时')}</th><th>м³ / өдөр<br>{cn('m³/天')}</th><th>Өдөр<br>{cn('天')}</th></tr>
{stage_rows}
<tr class="tot"><td class="l">Нийт · 合计</td><td class="nw">{f0(R['V'])}</td><td class="nw">{f0(R['loose'])}</td><td>{f0(R['trips'])}</td><td></td><td></td><td></td><td></td><td>{f1(R['days_work'])}</td></tr></table>
<small>Цул м³ = газарт байгаа хөрс. Ухаад тэвшинд хийхэд сулраад 1.3 дахин томордог (сул м³).</small><br>
<small>{cn('实方 = 原状土体积;挖出装车后松散,体积增大1.3倍(松方)。')}</small>
</div>

<h2>2.2 Нэг Хово хэдэн куб зөөх вэ · {cn('每车装多少')}</h2>
<div class="box"><table>
<tr><td class="l">{bi('Шанага 3.2 м³, дүүргэлт 90 % → 1 шанага', '铲斗3.2 m³,满斗率90% → 每斗')}</td><td class="r">3.2 × 0.9 = {C.BUCKET * C.FILL:.2f} м³ сул</td></tr>
<tr><td class="l">{bi('Тэвш 18 м³ → бүтэн шанагын тоо', '车厢18 m³ → 斗数')}</td><td class="r">18 ÷ 2.88 = 6.25 → {R['passes']}</td></tr>
<tr><td class="l">{bi('1 рейс', '每车')}</td><td class="r">{R['passes']} × 2.88 = {R['load_loose']:.1f} м³ сул = {R['load_bank']:.1f} м³ цул</td></tr>
<tr><td class="l">{bi(f"Ачих хугацаа: {R['passes']} шанага × 30 сек + Хово солигдох 1 мин", f"装车时间:{R['passes']}斗 × 30秒 + 换车1分钟")}</td><td class="r">≈ {R['t_load']:.0f} мин</td></tr>
</table></div>

<h2>2.3 Цагт, өдөрт хэдийг ухах вэ · {cn('每小时、每天挖多少')}</h2>
<div class="box"><table>
<tr><td class="l">{bi('Хово 1 эргэлт = ачих 4 + өгсөх (6 км/ц) + буулгах, эргэх 2 + буцах (12 км/ц) + хүлээх 0.5 мин. Гүн рүү орох тусам зам уртасна.', '自卸车一个循环 = 装车4 + 上坡(6公里/时)+ 卸车掉头2 + 返回(12公里/时)+ 等待0.5分钟。越深运距越长。')}</td><td class="r">7.7 → 10.3 мин</td></tr>
<tr><td class="l">{bi('2 Хово цагт хэдэн рейс хийх вэ (экскаватор цагт 15-аас ихийг ачиж чадахгүй)', '2台自卸车每小时车次(挖掘机每小时最多装15车)')}</td><td class="r">12 – 15</td></tr>
<tr><td class="l">{bi('Бодит ажил: цагт 45 мин (75 %) — зогсолт, тос, хүлээлт', '实际作业:每小时45分钟(75%)——停机、加油、等待')}</td><td class="r">9 – 11 рейс/цаг</td></tr>
<tr><td class="l">{bi('10 цагийн ээлжид 1 цаг хоол, түлш → 9 цаг бодит ажил', '每班10小时,扣除1小时用餐、加油 → 实际9小时')}</td><td class="r">{f0(st[2]['prod_day'])} – {f0(st[0]['prod_day'])} м³/өдөр</td></tr>
</table></div>

<h2>2.4 Хэд хоног · {cn('工期')}</h2>
<div class="box"><table>
<tr><td class="l">{bi('Ухах ажил (давхарга бүрийг өөрийн хурдаар)', '开挖(各分层按各自效率计算)')}</td><td class="r">{f1(R['days_work'])} өдөр</td></tr>
<tr><td class="l">{bi('+ бэлтгэл 0.5 өдөр + дээж авах 0.5 өдөр', '+ 准备0.5天 + 取样0.5天')}</td><td class="r">{f1(R['days_total'])} → {days_total} өдөр</td></tr>
<tr><td class="l">{bi('+ цаг агаар, эвдрэлийн нөөц 15 %', '+ 天气、故障储备15%')}</td><td class="r">≈ {days_res} өдөр</td></tr>
</table></div>
<div class="ok"><b>Шалгах арга:</b> Өдөр бүр Хово-гийн рейсийг тоолоод {R['load_bank']:.1f}-аар үржүүл → тэр өдрийн ухсан цул м³ (ойролцоо). Хүснэгтийн «м³ / өдөр»-тэй харьцуул.<br>
{cn(f'<b>核对方法:</b>每天统计自卸车车次,乘以{R["load_bank"]:.1f} → 当天挖方(实方,近似值)。与表中“m³/天”对比。')}</div>
</div>
"""

sched_rows = "".join(
    f"<tr><td>{s['day']}</td><td class='l'>{s['work']}</td><td>{'—' if not s['trips'] else f0(s['trips'])}</td><td>{f0(s['cum'])}</td><td>{s['depth']}</td></tr>"
    for s in sched)
schedpage = f"""
<div class="page">
<div class="hdr"><h1>3. Ажлын <b>хуваарь</b>, операторын заавар · {cn('施工进度及司机须知')}</h1><p>1 ээлж (10 цаг) · Экскаватор 1 + Хово 2 · {cn('单班(10小时)· 挖掘机1台 + 自卸车2台')}</p></div>
<h2>3.1 Өдөр бүрийн зорилт · {cn('每日目标')}</h2>
<div class="box"><table>
<tr><th>Өдөр<br>{cn('天')}</th><th class="l">Ажил · {cn('工作内容')}</th><th>Рейс<br>{cn('车次')}</th><th>Нийт ухсан, м³ цул<br>{cn('累计挖方(实方)')}</th><th>Өдрийн эцэст<br>{cn('当日完成')}</th></tr>
{sched_rows}
</table>
<small>Гүйцэтгэлийг тухайн шатны эзэлхүүнээр (м³) бодсон. Хоцорвол нөөц өдрүүд ({days_res - days_total}) ашиглана. · {cn(f'完成率按各台阶体积计算。如滞后,使用储备天数({days_res - days_total}天)。')}</small></div>

<h2>3.2 Оператор өдөр бүр · {cn('司机每日须知')}</h2>
<div class="box"><ul>
<li>Ажил эхлэхээс өмнө хана, ирмэгт ан цав, нуралт байгаа эсэхийг харна. Байвал ажил эхлэхгүй.<br>{cn('开工前检查坑壁、坑边有无裂缝、坍塌。若有,不得开工。')}</li>
<li>Рейсийг тоолж бичнэ (Хово тус бүр). Орой нийлбэрийг өдрийн зорилттой харьцуулна.<br>{cn('记录每台自卸车车次。晚上将合计与当日目标对比。')}</li>
<li>Шатны гүнг шон, түвшин хэмжигчээр шалгана: −5, −10, −15 м. Хэт гүн ухахгүй.<br>{cn('用标杆、水准仪检查台阶深度:−5、−10、−15米。不得超挖。')}</li>
<li>Хана: 1-р шат 45° (1 м доош = 1 м хойш), 2, 3-р шат 60° (1 м доош = 0.6 м хойш).<br>{cn('坡面:第1台阶45°(下1米退1米),第2、3台阶60°(下1米退0.6米)。')}</li>
<li>Рамп 6 м өргөн, 12 % (8 м явахад 1 м өгсөнө). Гадна ирмэгт 1 м шороон далан.<br>{cn('坡道宽6米,坡度12%(每走8米升高1米)。外侧筑1米高土挡。')}</li>
<li>Шороог зөвхөн буулгах талбайд, ухмалын ирмэгээс 13 м-ээс цааш асгана.<br>{cn('土只能卸在排土场,距采坑边缘13米以外。')}</li>
<li>−15 м-ээс доош экскаватор ёроол дээр зогсож нүх ухна. <b>Нүхэнд хүн орохгүй.</b><br>{cn('−15米以下,挖掘机站在坑底挖小坑。<b>人员严禁进入小坑。</b>')}</li>
<li>−20 м-т хүрмэгц шанагаар дээж гаргаж, уут бүрт гүн, огноо, цагийг бичнэ. Зураг авна.<br>{cn('到达−20米后,用铲斗取出样品,每袋注明深度、日期、时间,并拍照。')}</li>
</ul></div>

</div>
"""

v_top_dump = C.DUMP_AREA * C.TOPSOIL
v_top = v_top_dump + R["area_pit"] * C.TOPSOIL
it = bf["items"]
bf_rows = [
    (bi("Овоолгын талбайн шимт хөрс хуулах", "剥离排土场表土"), f"{f0(C.DUMP_AREA)} м² × {C.TOPSOIL} м = {f0(v_top_dump)} м³", f1(it[0]["days"])),
    (bi("Овоолго хэлбэржүүлэх (бульдозер)", "排土场整形(推土机)"), bi(f"{f0(R['loose'])} м³ сул, ≈ {bf['dozer_form_h']:.0f} цаг", f"{f0(R['loose'])} m³松方,约{bf['dozer_form_h']:.0f}小时"), bi("ухахтай зэрэг", "与开挖同时")),
    (bi("Нөхөн булах (экскаватор + 2 Хово)", "回填(挖掘机 + 2台自卸车)"), bi(f"{f0(R['V'])} м³, {f0(bf['bf_trips'])} рейс, {bf['bf_hours']:.0f} цаг", f"{f0(R['V'])} m³,{f0(bf['bf_trips'])}车次,{bf['bf_hours']:.0f}小时"), f1(it[2]["days"])),
    (bi("Шимт хөрс буцааж дэвсэх, тэгшлэх", "表土回铺、平整"), bi(f"{f0(v_top)} м³ + гадаргуу, {bf['dozer_fin_h']:.0f} цаг", f"{f0(v_top)} m³ + 地表平整,{bf['dozer_fin_h']:.0f}小时"), f1(it[3]["days"])),
]
bf_html = "".join(f"<tr><td class='l'>{a}</td><td class='l'>{b}</td><td>{c}</td></tr>" for a, b, c in bf_rows)
bfpage = f"""
<div class="page">
<div class="hdr"><h1>4. Овоолго үүсгэх, <b>нөхөн булах</b> · {cn('排土及回填')}</h1><p>Дээж авсны дараа ухмалыг буцааж булах хүртэлх ажил · {cn('取样后至回填完毕的全部工作')}</p></div>
<h2>4.1 Ажлын дараалал · {cn('施工顺序')}</h2>
<div class="box">
<div class="step"><div class="c">А</div><div><b>Ухахаас өмнө:</b> овоолгын талбай (76 × 48 м) ба ухмалын талбайн (≈ {f0(R['area_pit'])} м²) шимт хөрсийг 20 см зузаанаар хуулж, <b>тусад нь</b> жижиг овоо болгоно. Сүүлд буцааж дэвсэнэ.<br>
{cn(f'<b>开挖前:</b>剥离排土场(76×48米)及采坑范围(约{f0(R["area_pit"])} m²)厚20厘米的表土,<b>单独</b>堆放,最后回铺。')}</div></div>
<div class="step"><div class="c">Б</div><div><b>Ухах үед:</b> Хово шороог овоолгод асгана. Бульдозер түүнийг 5 м-ээр 2 үе болгож тэгшилнэ (ухах ажилтай зэрэг явна).<br>
{cn('<b>开挖时:</b>自卸车将土卸到排土场。推土机按每层5米分2层推平(与开挖同时进行)。')}</div></div>
<div class="step"><div class="c r">В</div><div><b>Дээж авсны дараа:</b> экскаватор овоолгоос ачиж, Хово эхлээд рампаар ёроол руу орж асгана. Дүүрэхийн хэрээр ухмалын ирмэгээс асгана. 1 рейс {bf['bf_passes']} шанага ≈ {bf['bf_load_bank']:.1f} м³ цул, 1 эргэлт ≈ {bf['bf_cycle']:.1f} мин.<br>
{cn(f'<b>取样后:</b>挖掘机从排土场装车,自卸车先沿坡道下到坑底卸土,随着回填升高,改在坑边卸土。每车{bf["bf_passes"]}斗约{bf["bf_load_bank"]:.1f} m³实方,一个循环约{bf["bf_cycle"]:.1f}分钟。')}</div></div>
<div class="step"><div class="c">Г</div><div><b>Сүүлд:</b> бульдозер гадаргууг тэгшилж, шимт хөрсийг буцааж дэвсэнэ. Булсан шороо ≈ {f0(bf['surplus'])} м³ илүү гарна; ухмалын дээр бага зэрэг овон болгож үлдээвэл суултаар тэгширнэ.<br>
{cn(f'<b>最后:</b>推土机平整地表并回铺表土。回填后约多出{f0(bf["surplus"])} m³土,在采坑上方略微堆高,沉降后自然平整。')}</div></div>
</div>
<h2>4.2 Хэмжээ, хугацаа · {cn('工程量与工期')}</h2>
<div class="box"><table>
<tr><th class="l">Ажил · {cn('工作')}</th><th class="l">Хэмжээ · {cn('工程量')}</th><th>Өдөр<br>{cn('天')}</th></tr>
{bf_html}
<tr class="tot"><td class="l" colspan="2">Овоолго + нөхөн булалт · 排土 + 回填</td><td>{f1(bf['days'])}</td></tr>
</table></div>
<h2>4.3 Бүх ажлын нийт хугацаа · {cn('全部工作总工期')}</h2>
<div class="box"><table>
<tr><th class="l">Ажил · {cn('工作')}</th><th>Өдөр · {cn('天')}</th></tr>
<tr><td class="l">{bi('Ухах, дээж авах (2-р бүлэг)', '开挖及取样(第2章)', False)}</td><td>{f1(R['days_total'])}</td></tr>
<tr><td class="l">{bi('Овоолго үүсгэх, нөхөн булах (4.2)', '排土及回填(4.2)', False)}</td><td>{f1(bf['days'])}</td></tr>
<tr class="tot"><td class="l">НИЙТ · 合计</td><td>{days_all} өдөр (нөөцтэй {days_all_res}) · {days_all}天(含储备{days_all_res}天)</td></tr>
</table></div>
<div class="warn"><b>Анхаарах:</b><ul>
<li>Лабораторийн хариуг хүлээж байгаад булах бол техник сул зогсоно. Ухсан даруйд дээжээ аваад шууд булах нь хурдан.<br>{cn('若等化验结果再回填,设备将闲置。取样后立即回填更快。')}</li>
<li>Бульдозер энэ 3 техникт ороогүй. Түүнийг ≈ {f0(bf['dozer_form_h'] + bf['dozer_fin_h'])} цаг тусад нь ажиллуулна.<br>{cn(f'推土机不在这3台设备之内,需另外安排约{f0(bf["dozer_form_h"] + bf["dozer_fin_h"])}小时。')}</li></ul></div>
</div>
"""

sec56 = f"""
<div class="page">
<div class="hdr"><h1>5. Аюулгүй ажиллагаа, <b>таамаг</b> · {cn('安全及假设条件')}</h1><p>Ажил эхлэхээс өмнө · {cn('开工前')}</p></div>
<h2>5.1 Ажлыг хүлээн авах · {cn('验收')}</h2>
<div class="box"><ul>
<li>Ухалтыг маркшейдерийн хэмжилтээр, цул м³-ээр тооцно.<br>{cn('挖方量以测量为准,按实方 m³ 计算。')}</li>
<li>Ажлыг шатаар хүлээн авна: −5, −10, −15 м-т хэмжилт хийнэ.<br>{cn('分台阶验收:在−5、−10、−15米处测量。')}</li>
</ul></div>
<h2>5.2 Аюулгүй ажиллагаа · {cn('安全')}</h2>
<div class="box"><ul>
<li>Дээжний нүхэнд (−15 … −20 м) хүн орохгүй. Дээжийг шанаганаас авна.<br>{cn('取样小坑(−15…−20米)内严禁人员进入,从铲斗中取样。')}</li>
<li>Рампын гадна ирмэгт 1 м шороон далан. Ачаатай Хово 1-р араагаар өгсөнө.<br>{cn('坡道外侧筑1米高土挡。重载自卸车用一档上坡。')}</li>
<li>Ухмалын ирмэгээс 13 м дотор шороо асгахгүй, техник зогсоохгүй. Ирмэгийг тууз, тэмдгээр хашина.<br>{cn('距采坑边缘13米内不得堆土、停放设备。坑边用警示带和标志围挡。')}</li>
<li>Хана нурах, ан цав гарах, ус орох, Хово гулсах үед ажлыг зогсооно.<br>{cn('坑壁坍塌、出现裂缝、涌水、自卸车打滑时立即停工。')}</li>
</ul></div>
<h2>5.3 Таамаг (батлах шаардлагатай) · {cn('假设条件(需确认)')}</h2>
<div class="box"><table>
<tr><th class="l">Таамаг · {cn('假设')}</th><th class="l">Өөр байвал · {cn('若不同')}</th></tr>
<tr><td class="l">{bi('2, 3-р шатны налуу 60°, шат хооронд 2 м тавцан (хатуу чулуулаг)', '第2、3台阶坡面角60°,平台2米(坚硬岩石)')}</td><td class="l">{bi('Сул чулуулагт 45° → ухалт, хугацаа өснө', '岩石松软时改为45° → 挖方、工期增加')}</td></tr>
<tr><td class="l">{bi('Экскаватор ёроолоос ≈ 7 м хүртэл ухаж чадна', '挖掘机可从坑底向下挖约7米')}</td><td class="l">{bi('Маркийн үзүүлэлтээр шалгана', '按机型参数核实')}</td></tr>
<tr><td class="l">{bi('Сулралт 1.3; шанага 90 % дүүрнэ; 1 шанага 30 сек', '松散系数1.3;满斗率90%;每斗30秒')}</td><td class="l">{bi('Том чулуу, хөлдсөн хөрсөнд удааширна', '遇大块岩石、冻土时变慢')}</td></tr>
<tr><td class="l">{bi('Газрын ус гарахгүй', '无地下水')}</td><td class="l">{bi('Зумф, насос → хугацаа өснө', '需集水坑、水泵 → 工期增加')}</td></tr>
</table></div>

<div class="hdr" style="margin-top:10px"><h1>6. Дүгнэлт, <b>санал</b> · {cn('结论及建议')}</h1></div>
<div class="box" style="border-top:1.5px solid #13306b; border-radius:6px"><ol style="margin:2px 0; padding-left:20px">
<li>20 м-т хүрэх хамгийн бага ухалттай арга нь <b>15 м шатлалтай ухмал + 5 м дээжний нүх</b>: {f0(R['V'])} м³, {days_total} ажлын өдөр.<br>
{cn(f'到达20米开挖量最小的方案为<b>15米台阶式采坑 + 5米取样小坑</b>:{f0(R["V"])} m³,{days_total}个工作日。')}</li>
<li>Энэ нь Хово-г 20 м хүртэл оруулахаас {f0(save)} м³ ({save / full * 100:.0f} %) бага ухалттай.<br>
{cn(f'比自卸车下到20米的方案少挖{f0(save)} m³({save / full * 100:.0f}%)。')}</li>
<li>Овоолго үүсгэх, дээж авсны дараа буцааж булах нь ≈ {f1(bf['days'])} өдөр. <b>Бүх ажил ≈ {days_all} ажлын өдөр</b> (нөөцтэй {days_all_res}).<br>
{cn(f'排土及取样后回填约{f1(bf["days"])}天。<b>全部工作约{days_all}个工作日</b>(含储备{days_all_res}天)。')}</li>
<li>Рампыг 15 % болгох эсвэл тавцангүй хийх нь 1–1.5 өдөр хэмнэх ч Хово гулсах, чулуу унах эрсдэлтэй тул санал болгохгүй.<br>
{cn('坡道改为15%或不留平台可节省1–1.5天,但有自卸车打滑、落石风险,不建议采用。')}</li>
<li>Дараагийн алхам: (1) газар дээр хил, рамп, овоолгын талбайг тэмдэглэх, (2) 1-р шатны эхний 2 өдрийн гүйцэтгэлээр бүтээмжийг шалгаж, хуваарийг тодотгох, (3) бульдозер бэлтгэх.<br>
{cn('下一步:(1)现场标出采坑边界、坡道和排土场;(2)根据第1台阶前2天的完成情况核实效率、调整进度;(3)准备推土机。')}</li>
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

parts = [html(x, f"p{k}") for k, x in enumerate([cover, summary, method, calcpage, schedpage, bfpage, sec56])]
subprocess.run([sys.executable, "-I", os.path.join(HERE, "ukhmal20_draw_cn.py"), TMP], check=True, capture_output=True, timeout=900)
w = PdfWriter()
for f in parts + [os.path.join(TMP, "drawings.pdf")]:
    for pg in PdfReader(f).pages:
        w.add_page(pg)
w.add_metadata({"/Title": "20 м-т дээж авах ухмал — танилцуулга (MN-CN) / 20米深取样坑说明", "/Author": "Грийтвишн ХХК"})
mid = os.path.join(TMP, "merged.pdf")
with open(mid, "wb") as fh:
    w.write(fh)
doc = pymupdf.open(mid)
n = len(doc)
n_a4 = sum(1 for pg in doc if pg.rect.width < 1000)
YH = r"C:\Windows\Fonts\arial.ttf"
for i, pg in enumerate(doc):
    if i == 0:
        continue
    r = pg.rect
    txt = f"Хуудас {i + 1} / {n}"
    if r.width > 1000:
        pg.insert_text(pymupdf.Point(r.width - 175, 12), f"Хавсралт {i + 1 - n_a4} · " + txt, fontname="yh", fontfile=YH, fontsize=8, color=(0.3, 0.3, 0.3))
    else:
        pg.insert_text(pymupdf.Point(r.width - 100, r.height - 14), txt, fontname="yh", fontfile=YH, fontsize=8, color=(0.4, 0.4, 0.4))
        pg.insert_text(pymupdf.Point(37, r.height - 14), "«Грийтвишн» ХХК · Сүүж уул · 20 м-т дээж авах ухмал · танилцуулга (MN-CN)",
                       fontname="yh", fontfile=YH, fontsize=8, color=(0.4, 0.4, 0.4))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT, garbage=3, deflate=True)
for f in parts:
    print(os.path.basename(f), len(PdfReader(f).pages), "pages")
print("OUT", OUT, n, "pages", "TMP", TMP)
