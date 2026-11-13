# -*- coding: utf-8 -*-
"""Тусгай зөвшөөрлийн талбайн 7 зураг (агаарын, сансар, гүний ус, гадаргуу, хөрс, ургамалжилт, УТХГ).

Ажиллуулах:  py -3 -I talbai_zurag.py <config.json> [--only 0,1,...]
config.json: {"name","license","holder","area_ha","out","corners":[["105°55'22.3\"","43°46'34.5\""],...]}
Булангуудыг хэрэглэгчийн дугаарласан дарааллаар (1,2,3,…) өгнө. Аймаг, сумыг солбицлоор автоматаар олно.
"""
import sys, os, re, json, math
sys.stdout.reconfigure(encoding='utf-8')
import warnings; warnings.filterwarnings('ignore')
import geopandas as gpd, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from shapely.geometry import Polygon, box
import rasterio
from rasterio.windows import from_bounds
import contextily as cx

B = 'D:/PARA/3-Resources/ГМС суурь давхарга/'
cfg = json.load(open(sys.argv[1], encoding='utf-8'))
ONLY = None
if '--only' in sys.argv:
    ONLY = {int(x) for x in sys.argv[sys.argv.index('--only') + 1].split(',')}
def want(i): return ONLY is None or i in ONLY

NAME, LIC, HOLDER, AREA = cfg['name'], cfg['license'], cfg.get('holder', ''), cfg.get('area_ha')
OUT = cfg['out']; os.makedirs(OUT, exist_ok=True)
import textwrap
LIC_LBL = cfg.get('license_label', 'Тусгай зөвшөөрөл')          # газрын эрх бол «Нэгж талбар»
BND_LBL = cfg.get('boundary_label', 'Тусгай зөвшөөрлийн талбай')  # газрын эрх бол «Газар эзэмших талбай»

def parse(s):
    if isinstance(s, (int, float)): return float(s)
    n = [float(x) for x in re.findall(r'[\d.]+', s)]
    return n[0] + (n[1] if len(n) > 1 else 0) / 60 + (n[2] if len(n) > 2 else 0) / 3600
LBL = cfg['corners']
PTS = [(parse(x), parse(y)) for x, y in LBL]
site = gpd.GeoDataFrame(geometry=[Polygon(PTS)], crs=4326)
c = site.geometry.iloc[0].centroid
utm = 32600 + int((c.x + 180) // 6) + 1
calc_ha = site.to_crs(utm).area.iloc[0] / 1e4
AREA = AREA or round(calc_ha, 2)
print(f'Талбай: солбицлоор {calc_ha:.2f} га, ТЗ-д {AREA} га')

# ---- засаг захиргаа ----
soums = gpd.read_file(B + 'Boundary/boundary_soums.shp')
aimags = gpd.read_file(B + 'Boundary/boundary_aimag.shp')
csoum = gpd.read_file(B + 'Boundary/center_soums.shp')
soum = soums[soums.contains(c)]
if not len(soum): sys.exit('Талбай аль ч сумын хилд орсонгүй — солбицлоо шалга.')
AIM = soum.AIMAG_ENG.iloc[0]
aimag = aimags[aimags.AIMAG_ENG == AIM]
asoums = soums[soums.AIMAG_ENG == AIM]
def fx(t):  # cp1251-ийн эвдэрсэн монгол нэр
    if not isinstance(t, str): return ''
    t = t.encode('latin1', errors='ignore').decode('cp1251', errors='ignore')
    return t.translate(str.maketrans({'ї': 'ү', 'Ї': 'Ү', 'є': 'ө', 'Є': 'Ө', 'ў': 'ү', 'Ў': 'Ү'})).title()
csoum['MN'] = csoum.SOUMS_MNG.map(fx)
cs = csoum[csoum.AIMAG_ENG == AIM]
AIM_MN = fx(aimag.MNG.iloc[0])
_in = csoum[csoum.within(soum.geometry.iloc[0])]
SOUM_MN = _in.MN.iloc[0] if len(_in) else soum.SOUMS_ENG.iloc[0]
print(f'Байршил: {AIM_MN} аймаг, {SOUM_MN} сум')

sb = site.total_bounds
dx, dy = sb[2] - sb[0], sb[3] - sb[1]
pad = max(dx, dy) * 0.35 + 0.003
db = (sb[0] - pad, sb[1] - pad * 0.7, sb[2] + pad, sb[3] + pad * 0.7)
TITLE = f'«{NAME}» {LIC} · {AIM_MN} аймаг, {SOUM_MN} сум · {AREA} га'

def frame():
    fig = plt.figure(figsize=(14, 9.9), dpi=200)
    fig.patch.set_facecolor('#fdf3c4')
    axA = fig.add_axes([0.03, 0.04, 0.42, 0.92])
    axS = fig.add_axes([0.50, 0.50, 0.42, 0.46])
    axD = fig.add_axes([0.47, 0.06, 0.24, 0.40])
    for a in (axA, axS): a.set_axis_off()
    return fig, axA, axS, axD

def common(axA, axS, axD):
    asoums.boundary.plot(ax=axA, color='#888', lw=0.4)
    soum.boundary.plot(ax=axA, color='yellow', lw=1.2)
    aimag.boundary.plot(ax=axA, color='#333', lw=0.8)
    soum.boundary.plot(ax=axS, color='#333', lw=0.8)
    for ax in (axA, axS):
        site.plot(ax=ax, facecolor='red', edgecolor='red', lw=2)
    for _, r in cs.iterrows():
        axA.plot(r.geometry.x, r.geometry.y, marker='^', color='#1f5fbf', ms=4)
        axA.text(r.geometry.x + 0.03, r.geometry.y, r.MN, fontsize=5)
    for _, r in cs[cs.within(soum.geometry.iloc[0])].iterrows():
        axS.plot(r.geometry.x, r.geometry.y, marker='^', color='#1f5fbf', ms=6)
        axS.text(r.geometry.x + 0.01, r.geometry.y, r.MN, fontsize=8)
    axA.text(c.x, c.y + 0.08, SOUM_MN, fontsize=9, weight='bold')
    axS.text(c.x + 0.02, c.y + 0.02, NAME, fontsize=8, color='darkred')
    site.boundary.plot(ax=axD, color='red', lw=2)
    axD.set_xlim(db[0], db[2]); axD.set_ylim(db[1], db[3])
    axD.tick_params(labelsize=6); axD.set_xlabel('Уртраг', fontsize=7); axD.set_ylabel('Өргөрөг', fontsize=7)
    axD.xaxis.set_major_formatter(lambda v, p: f"{int(v)}°{int(v % 1 * 60):02d}'{v * 3600 % 60:04.1f}\"")
    axD.yaxis.set_major_formatter(lambda v, p: f"{int(v)}°{int(v % 1 * 60):02d}'{v * 3600 % 60:04.1f}\"")
    axD.locator_params(nbins=3)
    for i, (x, y) in enumerate(PTS, 1):
        axD.text(x, y, f' {i}', fontsize=7, color='red', weight='bold')

def legend(fig, extra, fs=10):
    h = [Line2D([], [], marker='^', color='#1f5fbf', ls='', ms=8, label='Сумын төв'),
         Patch(facecolor='none', edgecolor='red', lw=2, label=BND_LBL)] + extra
    fig.legend(handles=h, loc='lower right', bbox_to_anchor=(0.995, 0.06), fontsize=fs,
               title='ТАЙЛБАР', title_fontproperties={'weight': 'bold', 'size': 12}, frameon=False)

def save(fig, name):
    fig.text(0.5, 0.975, TITLE, ha='center', fontsize=12, weight='bold')
    p = f'{OUT}/{name}_{NAME}.jpg'
    fig.savefig(p, facecolor=fig.get_facecolor()); plt.close(fig); print(p)

# ---- 0 Агаарын зураг ----
if want(0):
    s3 = site.to_crs(3857); v = gpd.GeoSeries.from_xy([p[0] for p in PTS], [p[1] for p in PTS], crs=4326).to_crs(3857)
    fig = plt.figure(figsize=(14, 9.9), dpi=220); fig.patch.set_facecolor('#fdf3c4')
    ax = fig.add_axes([0.03, 0.05, 0.62, 0.88])
    b = s3.total_bounds; cxm, cym = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
    asp = 0.62 / 0.88 * 14 / 9.9
    h = max((b[3] - b[1]) * 0.75, (b[2] - b[0]) * 0.75 / asp, 300); w = h * asp
    ax.set_xlim(cxm - w, cxm + w); ax.set_ylim(cym - h, cym + h)
    cx.add_basemap(ax, source=cx.providers.Esri.WorldImagery, attribution=False)
    s3.boundary.plot(ax=ax, color='red', lw=2.5)
    for i, p in enumerate(v, 1):
        ax.plot(p.x, p.y, 'o', color='yellow', ms=6, mec='red')
        right = p.x >= cxm
        ax.text(p.x + (w * 0.03 if right else -w * 0.03), p.y, str(i), color='yellow', fontsize=13, weight='bold',
                ha='left' if right else 'right', va='center')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel(''); ax.set_ylabel('')
    ax.annotate('Х', xy=(0.94, 0.95), xytext=(0.94, 0.86), xycoords='axes fraction', color='white',
                ha='center', fontsize=14, weight='bold', arrowprops=dict(color='white', width=4, headwidth=14))
    k = 1 / math.cos(math.radians(c.y))
    sl = [x for x in (100, 200, 500, 1000, 2000, 5000) if x * k < w * 0.6][-1]; L = sl * k
    x0 = cxm - w * 0.92; y0 = cym - h * 0.92
    ax.plot([x0, x0 + L], [y0, y0], color='white', lw=5); ax.plot([x0, x0 + L / 2], [y0, y0], color='black', lw=5)
    ax.text(x0 + L / 2, y0 + h * 0.03, f'{sl} м' if sl < 1000 else f'{sl // 1000} км', color='white', ha='center', fontsize=11, weight='bold')
    fig.text(0.5, 0.965, f'«{NAME}» {LIC} · агаарын зураг', ha='center', fontsize=15, weight='bold')
    info = f'{LIC_LBL}: {LIC}\n' + ('Эзэмшигч: ' + '\n   '.join(textwrap.wrap(HOLDER, 30)) + '\n' if HOLDER else '') + \
           f'Байршил: {AIM_MN} аймаг,\n   {SOUM_MN} сум\nТалбай: {AREA} га'
    fig.text(0.68, 0.86, info, fontsize=12, va='top', linespacing=1.6)
    n = len(LBL)
    fig.text(0.68, 0.635, '▭ ' + BND_LBL + 'н хил', color='red', fontsize=12)
    fig.text(0.68, 0.585, 'Булангийн цэгийн солбицол (WGS84)', fontsize=12, weight='bold')
    t = fig.add_axes([0.68, 0.06, 0.29, 0.51]); t.axis('off')
    tab = t.table(cellText=[[str(i), x, y] for i, (x, y) in enumerate(LBL, 1)], colLabels=['№', 'Уртраг', 'Өргөрөг'],
                  loc='upper left', cellLoc='center', colWidths=[0.12, 0.44, 0.44])
    tab.auto_set_font_size(False); tab.set_fontsize(11 if n <= 10 else max(6, 11 - (n - 10) * 0.25))
    tab.scale(1, 1.8 if n <= 10 else max(0.9, 1.8 * 11 / (n + 1)))
    fig.text(0.03, 0.02, 'Сансрын зураг: Esri World Imagery', fontsize=8, color='#555')
    p = f'{OUT}/0_агаарын зураг_{NAME}.jpg'; fig.savefig(p, facecolor=fig.get_facecolor()); plt.close(fig); print(p)

# ---- 1 Сансар ----
if want(1):
    fig, axA, axS, axD = frame()
    for ax, g in ((axA, aimag), (axS, soum)):
        g.plot(ax=ax, facecolor='none', edgecolor='none')
        cx.add_basemap(ax, crs=4326, source=cx.providers.Esri.WorldImagery, attribution=False)
    axD.set_xlim(db[0], db[2]); axD.set_ylim(db[1], db[3])
    cx.add_basemap(axD, crs=4326, source=cx.providers.Esri.WorldImagery, attribution=False)
    common(axA, axS, axD); legend(fig, []); save(fig, '1_сансар')

# ---- 2 Гүний ус ----
if want(2):
    gw = gpd.read_file(B + 'groundwater/groundwater.shp').to_crs(4326)
    rivers = gpd.read_file(B + 'surfwater/riverall.shp').to_crs(4326)
    ab = aimag.total_bounds
    rivers_a = gpd.clip(rivers.cx[ab[0]:ab[2], ab[1]:ab[3]], aimag)
    fig, axA, axS, axD = frame()
    gwa = gpd.clip(gw, aimag)
    cats = sorted(gw.typemon.unique())
    cmap = plt.get_cmap('Blues', len(cats) + 2); col = {k: cmap(i + 2) for i, k in enumerate(cats)}
    gwd = gpd.clip(gw, db)
    for ax, g in ((axA, gwa), (axS, gpd.clip(gw, soum)), (axD, gwd)):
        for k, sub in g.groupby('typemon'): sub.plot(ax=ax, color=col[k])
    rivers_a.plot(ax=axA, color='#0033cc', lw=0.5)
    gpd.clip(rivers_a, soum).plot(ax=axS, color='#0033cc', lw=0.8)
    rd = gpd.clip(rivers, db)
    if len(rd): rd.plot(ax=axD, color='#0033cc', lw=1.5)
    common(axA, axS, axD)
    print('Гүний ус (талбай):', list(gwd.typemon.unique()))
    legend(fig, [Patch(color=col[k], label=k) for k in sorted(set(gwa.typemon))] + [Line2D([], [], color='#0033cc', label='Гол')])
    save(fig, '2_гүний ус')

# ---- 3 Гадаргуу ----
def raster(ax, bounds, path, cmap, alpha=1.0):
    with rasterio.open(path) as r:
        w = from_bounds(*bounds, r.transform)
        a = r.read(1, window=w, boundless=True, fill_value=0).astype(float)
        if a.shape[0] > 2500:
            f = a.shape[0] // 1500 + 1
            a = r.read(1, window=w, out_shape=(a.shape[0] // f, a.shape[1] // f), boundless=True).astype(float)
        a[a <= (0 if 'Hill' in path else -1000)] = np.nan
        ax.imshow(a, extent=(bounds[0], bounds[2], bounds[1], bounds[3]), cmap=cmap, alpha=alpha)
        return np.nanmin(a), np.nanmax(a)
if want(3):
    fig, axA, axS, axD = frame()
    for ax, g in ((axA, aimag), (axS, soum)):
        b = g.total_bounds
        raster(ax, b, B + 'Mongolia_DEM_Hill.tif', 'gray')
        raster(ax, b, B + 'mongolian_dem', 'terrain', 0.5)
        gpd.GeoDataFrame(geometry=[box(*b).buffer(0.5).difference(g.geometry.iloc[0])], crs=4326).plot(ax=ax, color='white')
        ax.set_xlim(b[0], b[2]); ax.set_ylim(b[1], b[3])
    raster(axD, db, B + 'Mongolia_DEM_Hill.tif', 'gray')
    dmin, dmax = raster(axD, db, B + 'mongolian_dem', 'terrain', 0.5)
    common(axA, axS, axD)
    print(f'Өндөр (ойрын зураг): {int(dmin)}–{int(dmax)} м')
    legend(fig, [Patch(color=plt.get_cmap('terrain')(0.8), label=f'Өндөр: {int(dmax)} м'),
                 Patch(color=plt.get_cmap('terrain')(0.2), label=f'Нам: {int(dmin)} м')])
    save(fig, '3_гадаргуу')

# ---- 4 Хөрс ----
if want(4):
    soil = gpd.read_file(B + 'soil tsoomoo/soil.shp')
    fig, axA, axS, axD = frame()
    sa = gpd.clip(soil, aimag); sd = gpd.clip(soil, db)
    scats = sorted(soil.groupmon.unique())
    scm = dict(zip(scats, ['#f6cfa6', '#c9a27a', '#f2a983', '#e8d8c8', '#d9b48f', '#b88a5e', '#efc0b0', '#e0b090']))
    for ax, g in ((axA, sa), (axS, gpd.clip(soil, soum)), (axD, sd)):
        for k, sub in g.groupby('groupmon'): sub.plot(ax=ax, color=scm[k])
    common(axA, axS, axD)
    print('Хөрс (талбай):', list(sd.groupmon.unique()))
    legend(fig, [Patch(color=scm[k], label=k) for k in sorted(set(sa.groupmon))])
    save(fig, '4_хөрс')

# ---- 5 Ургамалжилт ----
if want(5):
    def fixu(t):
        try: return t.encode('cp1251').decode('utf-8')
        except Exception: return t
    vg = gpd.read_file(B + 'Urgamal_bulgeer/veggroup.shp', encoding='cp1251').to_crs(4326)
    vg['mn'] = vg.groupmon.map(fixu).str.strip(); vg['geometry'] = vg.buffer(0)
    fig, axA, axS, axD = frame()
    va = gpd.clip(vg, aimag); vd = gpd.clip(vg, db)
    cats = sorted(set(va.mn))
    cm = plt.get_cmap('tab20'); col = {k: mc.to_hex(tuple(0.35 + 0.65 * x for x in cm(i % 20)[:3])) for i, k in enumerate(cats)}
    for ax, g in ((axA, va), (axS, gpd.clip(vg, soum)), (axD, vd)):
        for k, sub in g.groupby('mn'): sub.plot(ax=ax, color=col[k], edgecolor='#999', lw=0.2)
    common(axA, axS, axD)
    print('Ургамалжилт (талбай):', list(vd.mn.unique()))
    legend(fig, [Patch(color=col[k], label=k[:55]) for k in cats], fs=7.5 if len(cats) > 10 else 10)
    save(fig, '5_ургамалжилт')

# ---- 6 Улсын тусгай хамгаалалттай газар ----
if want(6):
    spa = gpd.read_file(B + 'ulsiin tusgai hamgaalalttai gazar nutag/spa.shp').to_crs(4326)
    spa['geometry'] = spa.buffer(0)
    TN = {'ДЦГ': 'Дархан цаазат газар', 'БЦГ': 'Байгалийн цогцолборт газар', 'БНГ': 'Байгалийн нөөц газар',
          'ДГ': 'Дурсгалт газар', 'БДГ': 'Байгалийн дурсгалт газар'}
    spa['tn'] = spa.short_name.map(lambda k: TN.get(k, k))
    COL = {'Дархан цаазат газар': '#2e7d32', 'Байгалийн цогцолборт газар': '#66bb6a', 'Байгалийн нөөц газар': '#c5e1a5',
           'Дурсгалт газар': '#ffb74d', 'Байгалийн дурсгалт газар': '#ffb74d'}
    sp = site.to_crs(utm).geometry.iloc[0]
    spm = spa.to_crs(utm); spm['d'] = spm.distance(sp) / 1000
    near = spm.sort_values('d').drop_duplicates('spa_name').head(3)
    for _, r in near.iterrows(): print(f'УТХГ: {r.spa_name} ({r.short_name}) — {r.d:.1f} км')
    fig, axA, axS, axD = frame()
    va = gpd.clip(spa, aimag)
    for ax, g in ((axA, va), (axS, gpd.clip(spa, soum)), (axD, gpd.clip(spa, db))):
        for k, sub in g.groupby('tn'): sub.plot(ax=ax, color=COL.get(k, '#9ccc65'), alpha=0.85)
    if len(va):
        for _, r in va.dissolve('spa_name').reset_index().iterrows():
            pt = r.geometry.representative_point(); axA.text(pt.x, pt.y, r.spa_name, fontsize=6, color='#1b5e20', weight='bold')
    common(axA, axS, axD)
    fig.text(0.75, 0.42, 'Хамгийн ойр УТХГ:\n' + '\n'.join(f'• {r.spa_name} ({r.short_name}) — {r.d:.1f} км' for _, r in near.iterrows()),
             fontsize=8.5, weight='bold', color='#1b5e20')
    legend(fig, [Patch(color=COL.get(k, '#9ccc65'), label=k) for k in sorted(set(va.tn))] or [Patch(color='white', label='Аймагт УТХГ байхгүй')])
    save(fig, '6_тусгай хамгаалалттай газар')
