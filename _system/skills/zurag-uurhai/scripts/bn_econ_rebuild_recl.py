# Баруун наран эдийн засгийн загварыг 10-р бүлгийн хүснэгтээс сэргээх (bn_econ.py олдоогүй)
STONE = [200033,199731,199988,200133,200015,199923,200004,200292,200159,199527,200277,26280]
REV_PER_M3 = 22347/200033          # сая ₮ / м³ цул (НӨАТ-гүй), хүснэгт 10.3-ын 1-р жил
CAPEX = 5975.4
EQUIP = 1768+1358.2+1202+120.2      # 10 жил
BUILD = 679+371                      # 40 жил
INTANG = 477.0
RECL_TOTAL = 3313.38   # 2026-11-06: бүрэн буцаах (8.6 v2)

def model(years, stone, opex_base, recl_years, price=1.0, vol=1.0, opex_f=1.0, capex_f=1.0):
    rows=[]
    recl_old = 102.5  # 11.1 жилд хуваасан (хүснэгт 10.2)
    for t in range(years):
        s = stone[t]
        rev = s*REV_PER_M3*price*vol
        amnat = rev*0.025
        # OPEX: хуучин OPEX - хуучин нөхөн сэргээлт*1.05 + шинэ нөхөн сэргээлт*1.05
        ox = opex_base[t]
        if recl_years:
            ox = ox + (RECL_TOTAL/recl_years - recl_old)*1.05
        ox *= opex_f
        dep = (EQUIP*capex_f/10 if t<10 else 0) + BUILD*capex_f/40 + INTANG*capex_f/(recl_years or 11.13)
        p = rev-amnat-ox-dep
        cit = 0 if p<=0 else (p*0.10 if p<=6000 else 600+(p-6000)*0.25)
        ni = p-cit
        rows.append(dict(rev=rev,amnat=amnat,opex=ox,dep=dep,p=p,cit=cit,ni=ni,cf=ni+dep))
    cfs=[-CAPEX*capex_f]+[r['cf'] for r in rows]
    return rows,cfs

def npv(cfs,r=0.10): return sum(c/(1+r)**i for i,c in enumerate(cfs))
def irr(cfs):
    lo,hi=0.0,50.0
    for _ in range(200):
        m=(lo+hi)/2
        lo,hi=(m,hi) if npv(cfs,m)>0 else (lo,m)
    return m
def payback(cfs):
    cum=cfs[0]
    for i,c in enumerate(cfs[1:],1):
        if cum+c>=0: return i-1 + (-cum)/c
        cum+=c

# --- 1. Хуучныг давтах (12 жил, OPEX 3–9 = 5711.0)
OPEX_OLD=[5906.6,5705]+[39977/7]*7+[5700,5662,960]
rows,cfs=model(12,STONE,OPEX_OLD,None)
print("ХУУЧИН: NPV %.0f (79396) IRR %.0f%% (217) payback %.2f (0.46) total CF %.0f (139461) CIT %.0f (33152) REV %.0f (248718)"%(
 npv(cfs),irr(cfs)*100,payback(cfs),sum(cfs),sum(r['cit'] for r in rows),sum(r['rev'] for r in rows)))

# --- 2. 10 жил
N=10
rows,cfs=model(N,STONE,OPEX_OLD,10)
f=lambda x: f"{x:,.0f}".replace(","," ")
print("\nШИНЭ 10 жил")
for k in ['rev','amnat','opex','dep','p','cit','ni','cf']:
    print(k, [f(r[k]) for r in rows], "Σ", f(sum(r[k] for r in rows)))
cum=0; cl=[]
for c in cfs: cum+=c; cl.append(f(cum))
print("cum",cl)
print("NPV",f(npv(cfs)),"IRR %.0f%%"%(irr(cfs)*100),"payback %.2f"%payback(cfs),"ΣCF",f(sum(cfs)))
print("prod m3 loose/yr1 %.1f"%(STONE[0]*2.69/1.355/1000), "Σ prod mян м3 %.1f"%(sum(STONE[:N])*2.69/1.355/1000))
rev=sum(r['rev'] for r in rows)
print("НӨАТ",f(rev*0.1),"АМНАТ",f(sum(r['amnat'] for r in rows)),"CIT",f(sum(r['cit'] for r in rows)),
      "НДШ",f(144.6+138.4*9),"ТЗ",f(69.5*10))
print("opex yr1 %.1f yr2 %.1f yr3-9 %.1f yr10 %.1f"%(rows[0]['opex'],rows[1]['opex'],rows[2]['opex'],rows[9]['opex']))
# мэдрэмж
for name,kw in [("price",'price'),("vol",'vol'),("opex",'opex_f'),("capex",'capex_f')]:
    print(name,[f(npv(model(N,STONE,OPEX_OLD,10,**{kw:x})[1])) for x in (0.8,0.9,1.0,1.1,1.2)])
lo,hi=0.0,1.0
for _ in range(100):
    m=(lo+hi)/2
    lo,hi=(lo,m) if npv(model(N,STONE,OPEX_OLD,10,price=m)[1])>0 else (m,hi)
print("breakeven %.3f price %.0f vol %.0f"%(m,61900*m,397048*m))
