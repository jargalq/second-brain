"""20 м-т дээж авах ухмалын тооцоо: эзэлхүүн, Хово рейс, өдөр, зардал.
Арга: 15 м хүртэл 3 шатлалтай ухмал (спираль рамп 12 %), ёроолоос экскаватороор 5 м дээжний нүх.
Үр дүнг calc() dict-ээр буцаана (зураг, PDF хоёулаа ашиглана)."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ukhmal15_geom as G

PRICE = 6700            # ₮ / м³ (цул) — Mugi
SWELL = 1.3             # сулралт (өмнөх тооцоо)
BUCKET = 3.2            # м³ экскаватор (Хятад, 500-р анги)
FILL = 0.9              # шанага дүүргэлт
TRUCK = 18.0            # м³ Хово (2 ширхэг)
N_TRUCK = 2
EXC_CYCLE = 0.5         # мин, нэг шанага (ухах-эргэх-асгах-буцах)
SPOT = 1.0              # мин, Хово солигдож зогсох
V_LOAD, V_EMPTY = 100.0, 200.0   # м/мин (6 ба 12 км/ц) — ачаатай өгсөхөд, хоосон
DUMP = 2.0              # мин, буулгах + эргэх
WAIT = 0.5              # мин
EFF = 0.75              # цагийн ашиглалт (45 мин/цаг)
SHIFT_H = 9.0           # 10 цагийн ээлжээс 1 цаг хоол, түлш
DUMP_ROUTE = 45.0       # м, рампын амнаас овоолго хүртэл
RESERVE = 0.15          # цаг агаар, эвдрэл


# ---- овоолго, нөхөн булалт (Mugi 2026-11-07: «дээж аваад буцааж булах, овоолго үүсгэх зардал») ----
TOPSOIL = 0.2           # м, шимт хөрсний зузаан ⚠
DUMP_AREA = 76 * 48     # м², овоолгын суурь (зураг)
DOZER_PROD = 250.0      # м³/цаг сул, 160 кВт-ийн бульдозер 10–15 м түлхэхэд ⚠
BF_EXC_CYCLE = 0.42     # мин (25 сек): сул овоолгоос ачихад ухахаас хурдан
BF_FILL = 0.95
BF_ROUTE = 70.0         # м, овоолгоос ухмалын ирмэг хүртэл дундаж
BF_DUMP = 1.5           # мин, ирмэгээс асгах
COMPACT = 1.08          # булсан шороо нягтрахад цулаас 8 % их зай эзэлнэ ⚠


n0 = lambda v: f"{v:,.0f}".replace(",", " ")


def backfill(Vb, area_pit, day_rate):
    """day_rate: гэрээлэгчийн 6 700 ₮/м³ үнээс гарах 1 өдрийн (3 техник, 9 цаг) дундаж орлого."""
    hour_fleet = day_rate / SHIFT_H                     # 3 техникийн 1 цаг
    hour_machine = hour_fleet / 3                       # 1 техникийн 1 цаг (бульдозерт хэрэглэнэ) ⚠
    # 1) овоолгын талбайн шимт хөрс
    v_top_dump = DUMP_AREA * TOPSOIL
    v_top_pit = area_pit * TOPSOIL                      # ухалтын дотор орсон, тусад нь хадгална
    # 2) овоолго хэлбэржүүлэх (бульдозер)
    loose = Vb * SWELL
    dozer_form_h = loose / DOZER_PROD
    # 3) нөхөн булах: экскаватор овоолгоос ачиж, Хово ирмэгээс асгана
    passes = int(round(TRUCK / (BUCKET * BF_FILL)))         # овоолсон тэвш: 6 шанага
    load_loose = passes * BUCKET * BF_FILL
    load_bank = load_loose / SWELL
    t_load = passes * BF_EXC_CYCLE + SPOT
    cyc = t_load + BF_ROUTE / 150.0 + BF_DUMP + BF_ROUTE / 250.0 + WAIT
    trips_h = min(N_TRUCK * 60 / cyc, 60 / t_load) * EFF
    prod_h = trips_h * load_bank
    bf_hours = Vb / prod_h
    bf_days = bf_hours / SHIFT_H
    bf_trips = int(np.ceil(loose / load_loose))
    # 4) шимт хөрсийг буцааж дэвсэх, тэгшлэх (бульдозер)
    v_top = v_top_dump + v_top_pit
    dozer_fin_h = v_top * SWELL / DOZER_PROD + 8.0      # + 1 өдөр гадаргуу тэгшлэх
    surplus = Vb * COMPACT - Vb                         # ухмалаас илүү гарах шороо
    items = [
        dict(name="Овоолгын талбайн шимт хөрс хуулах", what=f"{n0(DUMP_AREA)} м² × {TOPSOIL} м = {n0(v_top_dump)} м³",
             cost=v_top_dump * PRICE, days=v_top_dump / 1200, basis="6 700 ₮/м³"),
        dict(name="Овоолго хэлбэржүүлэх (бульдозер)", what=f"{n0(loose)} м³ сул ÷ {DOZER_PROD:.0f} м³/цаг = {dozer_form_h:.0f} цаг",
             cost=dozer_form_h * hour_machine, days=0.0, basis=f"{n0(hour_machine / 1000)} мян. ₮/цаг ⚠"),
        dict(name="Нөхөн булах (экскаватор + 2 Хово)", what=f"{n0(Vb)} м³, {n0(bf_trips)} рейс, {bf_hours:.0f} цаг",
             cost=bf_hours * hour_fleet, days=bf_days, basis=f"{n0(hour_fleet / 1000)} мян. ₮/цаг (3 техник) ⚠"),
        dict(name="Шимт хөрс буцааж дэвсэх, тэгшлэх", what=f"{n0(v_top)} м³ + гадаргуу, {dozer_fin_h:.0f} цаг бульдозер",
             cost=dozer_fin_h * hour_machine, days=dozer_fin_h / SHIFT_H, basis=f"{n0(hour_machine / 1000)} мян. ₮/цаг ⚠"),
    ]
    total = sum(i["cost"] for i in items)
    days = sum(i["days"] for i in items)
    return dict(items=items, total=total, days=days, hour_fleet=hour_fleet, hour_machine=hour_machine,
                v_top_dump=v_top_dump, v_top_pit=v_top_pit, dozer_form_h=dozer_form_h, bf_hours=bf_hours,
                bf_days=bf_days, bf_trips=bf_trips, bf_prod_day=prod_h * SHIFT_H, bf_cycle=cyc, bf_trips_h=trips_h,
                bf_load_bank=load_bank, bf_passes=passes, dozer_fin_h=dozer_fin_h, surplus=surplus,
                cost_bf_per_m3=Vb * PRICE, total_alt=total - bf_hours * hour_fleet + Vb * PRICE)


def calc():
    G.DEPTH = 15.0; G.GRADE = 0.12; G.BERM = 2.0
    Dsp = G.surface("spiral", ext=45)[2]
    V, lay = G.volumes(Dsp)
    area_pit = float((Dsp > 0.02).sum() * G.CELL ** 2)
    hole, hole_top = G.sample_hole(5.0, 3.0, 60.0)
    passes = int(np.floor(TRUCK / (BUCKET * FILL)))           # бүтэн шанага
    load_loose = passes * BUCKET * FILL
    load_bank = load_loose / SWELL
    t_load = passes * EXC_CYCLE + SPOT
    exc_max = 60.0 / t_load                                     # экскаватор цагт ачих дээд рейс
    stages = []
    names = ["1-р шат (0 … −5 м)", "2-р шат (−5 … −10 м)", "3-р шат (−10 … −15 м)", "Дээжний нүх (−15 … −20 м)"]
    vols = list(lay) + [hole]
    depths = [2.5, 7.5, 12.5, 17.5]
    for nm, v, dd in zip(names, vols, depths):
        route = min(dd, 15) / G.GRADE + 15 + DUMP_ROUTE
        kturn = 1.0 if dd > 10 else 0.0                         # ёроолд 3 цэгийн эргэлт
        cyc = t_load + route / V_LOAD + DUMP + route / V_EMPTY + WAIT + kturn
        trips_h = min(N_TRUCK * 60.0 / cyc, exc_max)
        if dd > 15:                                             # нүх: гүнд ухна, шанага дутуу дүүрнэ
            trips_h *= 0.6
        prod_h = trips_h * EFF * load_bank
        prod_day = prod_h * SHIFT_H
        trips = int(np.ceil(v * SWELL / load_loose))
        stages.append(dict(name=nm, V=v, route=route, cycle=cyc, trips_h=trips_h * EFF, prod_h=prod_h,
                           prod_day=prod_day, days=v / prod_day, trips=trips, cost=v * PRICE))
    Vt = sum(s["V"] for s in stages)
    days_work = sum(s["days"] for s in stages)
    setup = 0.5; sample = 0.5
    days_total = days_work + setup + sample
    # хувилбар
    G.GRADE = 0.15; V15, _ = G.volumes(G.surface("spiral", ext=45)[2]); G.GRADE = 0.12
    G.BERM = 0.0; Vnb, _ = G.volumes(G.surface("spiral", ext=45)[2]); G.BERM = 2.0
    G.DEPTH = 20.0; V20, _ = G.volumes(G.surface("spiral", ext=60)[2]); G.DEPTH = 15.0
    Vstr, _ = G.volumes(G.surface("straight", ext=90)[2])
    opts = [
        ("Санал болгож буй: 15 м ухмал + 5 м дээжний нүх, рамп 12 %", Vt, "Аюулгүй, хамгийн бага ухалт"),
        ("Рамп 15 % (эгц)", V15 + hole, "Ачаатай Хово-д хүнд, гулсах эрсдэл"),
        ("Бермгүй (шат хооронд тавцангүй)", Vnb + hole, "Чулуу унах эрсдэл, хатуу чулуулагт л"),
        ("Шулуун рамп (гадна траншей)", Vstr + hole, "Илүү ухалт"),
        ("Хово 20 м-ийн ёроол хүртэл орох бүтэн ухмал", V20, "Хамгийн их ухалт"),
    ]
    bf = backfill(Vt, area_pit, Vt * PRICE / days_work)
    return dict(
        bf=bf, area_pit=area_pit,
        V=Vt, stages=stages, hole=hole, hole_top=hole_top, passes=passes, load_loose=load_loose,
        load_bank=load_bank, t_load=t_load, exc_max=exc_max, days_work=days_work, days_total=days_total,
        days_reserve=days_total * (1 + RESERVE), cost=Vt * PRICE, cost_loose=Vt * SWELL * PRICE,
        trips=sum(s["trips"] for s in stages), loose=Vt * SWELL,
        opts=[dict(name=a, V=b, cost=b * PRICE, note=c) for a, b, c in opts],
        params=dict(PRICE=PRICE, SWELL=SWELL, BUCKET=BUCKET, FILL=FILL, TRUCK=TRUCK, N_TRUCK=N_TRUCK,
                    EXC_CYCLE=EXC_CYCLE, SPOT=SPOT, V_LOAD=V_LOAD, V_EMPTY=V_EMPTY, DUMP=DUMP, WAIT=WAIT,
                    EFF=EFF, SHIFT_H=SHIFT_H, RESERVE=RESERVE, GRADE=0.12))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    r = calc()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ukhmal20_calc.json")
    json.dump(r, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=float)
    for s in r["stages"]:
        print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in s.items()})
    for k in ("V", "passes", "load_loose", "load_bank", "t_load", "exc_max", "days_work", "days_total", "days_reserve", "cost", "cost_loose", "trips"):
        print(k, round(float(r[k]), 2))
    for o in r["opts"]:
        print(o["name"], round(o["V"]), round(o["cost"] / 1e6, 1))
    bf = r["bf"]
    print("area_pit", round(r["area_pit"]))
    for i in bf["items"]:
        print(i["name"], "|", i["what"], "|", round(i["cost"] / 1e6, 1), "M |", round(i["days"], 1), "d |", i["basis"])
    for k in ("total", "days", "hour_fleet", "hour_machine", "bf_prod_day", "bf_cycle", "bf_trips_h", "surplus", "total_alt"):
        print(k, round(float(bf[k]), 2))
