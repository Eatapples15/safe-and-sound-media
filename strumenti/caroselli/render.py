import json, html, os, random
E = json.load(open("episodi.json"))
esc = html.escape
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;background:#03001c;color:#f1f2ff;font-family:'Instrument Sans',sans-serif;overflow:hidden;position:relative}
.mono{font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:.14em;text-transform:uppercase}
.disp{font-family:'Unbounded',sans-serif;text-transform:uppercase;letter-spacing:-.02em}
.top{position:absolute;top:56px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;font-size:20px;color:#a2a6dc}
.marchio{font-family:'Unbounded';font-weight:700;font-size:30px;letter-spacing:-.01em;color:#f1f2ff}
.marchio b{color:#5dea84}
.piede{position:absolute;bottom:56px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;font-size:18px;color:#a2a6dc}
.pag{color:#f1f2ff}
.alone{position:absolute;inset:0;background:radial-gradient(80% 50% at 85% 0%,rgba(44,66,222,.45),transparent 70%),radial-gradient(60% 40% at 0% 100%,rgba(113,64,252,.22),transparent 70%)}
.eq{display:flex;align-items:flex-end;gap:9px;height:120px}
.eq i{display:block;width:14px;border-radius:7px;background:#36337a}
.eq i.v{background:#5dea84}.eq i.b{background:#2c42de}
.player{border:1.5px solid #36337a;border-radius:20px;padding:30px 34px;background:rgba(11,7,69,.7);display:grid;gap:18px}
.barra{height:6px;border-radius:3px;background:#36337a;position:relative}
.barra::after{content:"";position:absolute;left:0;top:0;bottom:0;width:38%;background:#5dea84;border-radius:3px}
.barra::before{content:"";position:absolute;left:38%;top:50%;width:18px;height:18px;margin:-9px 0 0 -9px;border-radius:50%;background:#f1f2ff}
.tempi{display:flex;justify-content:space-between;font-size:18px;color:#a2a6dc}
"""
def eq(seed, n=26, h=120):
    r = random.Random(seed); out=[]
    for k in range(n):
        v = r.randint(18, h); c = "v" if k%7==3 else ("b" if k%5==1 else "")
        out.append(f'<i class="{c}" style="height:{v}px"></i>')
    return '<div class="eq">'+''.join(out)+'</div>'
def pagina(ep, i, tot, corpo, sfondo=""):
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body style="{sfondo}">
<div class="alone"></div>
<div class="top"><span style="display:flex;align-items:center;gap:14px"><svg width="46" height="42" viewBox="0 0 260 240" style="flex:none"><path d="M44 92 A90 90 0 0 1 186 46" fill="none" stroke="#5dea84" stroke-width="18" stroke-linecap="round"/><path d="M216 148 A90 90 0 0 1 74 194" fill="none" stroke="#2c42de" stroke-width="18" stroke-linecap="round"/><path d="M24 120 H70 L90 88 L108 62 L124 176 L144 96 L160 126 L172 120 H236" fill="none" stroke="#f1f2ff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="marchio">SAFE <b>&amp;</b> SOUND</span></span><span class="mono">Traccia {ep['n']}</span></div>
{corpo}
<div class="piede"><span class="mono">formazionesicurezza.org</span><span class="mono pag">{i:02d} / {tot:02d}</span></div>
</body></html>"""
for ep in E:
    os.makedirs(ep["slug"], exist_ok=True)
    tot=5
    # 1 copertina
    righe="".join(f'<span style="display:block;color:{"#6c6ca6" if k==0 and len(ep["titolo"])>2 else "#f1f2ff"}">{esc(r)}</span>' for k,r in enumerate(ep["titolo"]))
    c1=f"""<div style="position:absolute;left:72px;right:72px;top:190px;display:grid;gap:36px">
<span class="mono" style="font-size:20px;color:#5dea84">{esc(ep['occhiello'])}</span>
<h1 class="disp" style="font-size:132px;line-height:.9;font-weight:700">{righe}</h1></div>
<div style="position:absolute;left:72px;right:72px;bottom:150px;display:grid;gap:28px">{eq(ep['n'])}
<div class="player"><span class="mono" style="font-size:18px;color:#a2a6dc">Now playing</span>
<div style="display:flex;justify-content:space-between;align-items:baseline;gap:20px"><span style="font-size:44px;font-weight:600;line-height:1.1">{esc(ep['brano'])}</span><span class="mono" style="font-size:18px;color:#a2a6dc">{ep['anno']}</span></div>
<span style="font-size:26px;color:#a2a6dc">{esc(ep['artista'])}</span>
<div class="barra"></div><div class="tempi mono"><span>1:08</span><span>{ep['durata']}</span></div></div></div>"""
    # 2 perche
    c2=f"""<div style="position:absolute;left:72px;right:72px;top:220px;display:grid;gap:48px">
<span class="mono" style="font-size:22px;color:#5dea84">Perché questa traccia</span>
<p style="font-size:62px;line-height:1.18;font-weight:500;letter-spacing:-.01em">{esc(ep['perche'])}</p>
<div style="display:flex;gap:20px;align-items:center;border-top:1.5px solid #36337a;padding-top:36px"><span style="width:56px;height:56px;border-radius:50%;background:#5dea84;display:grid;place-items:center;color:#03001c;font-size:24px">▶</span>
<span style="font-size:28px">{esc(ep['brano'])} <span style="color:#a2a6dc">· {esc(ep['artista'])}</span></span></div></div>"""
    # 3 contenuto a punti
    if ep["slug"]=="ep02-allerta-meteo":
        col={"Verde":"#3ddc84","Gialla":"#ffd43b","Arancione":"#ff8a1f","Rossa":"#ff4d5e"}
        voci="".join(f'<div style="display:grid;grid-template-columns:240px 1fr;gap:28px;align-items:center;padding:26px 0;border-top:1.5px solid #36337a"><span class="mono" style="background:{col[t]};color:#03001c;border-radius:999px;padding:14px 22px;font-size:22px;text-align:center">{t}</span><span style="font-size:32px;line-height:1.3">{esc(d)}</span></div>' for t,d in ep["s3"])
    else:
        voci="".join(f'<div style="display:grid;grid-template-columns:90px 1fr;gap:24px;padding:28px 0;border-top:1.5px solid #36337a"><span class="disp" style="font-size:44px;font-weight:700;color:#5dea84">{k+1}</span><div style="display:grid;gap:8px"><span style="font-size:36px;font-weight:600">{esc(t)}</span><span style="font-size:28px;line-height:1.35;color:#a2a6dc">{esc(d)}</span></div></div>' for k,(t,d) in enumerate(ep["s3"]))
    c3=f"""<div style="position:absolute;left:72px;right:72px;top:190px;display:grid;gap:30px">
<h2 class="disp" style="font-size:76px;line-height:.95;font-weight:700">{esc(ep['s3t'])}</h2><div>{voci}</div></div>"""
    # 4 checklist
    v4="".join(f'<li style="display:flex;gap:26px;align-items:center;padding:24px 0;border-top:1.5px solid #36337a;font-size:36px;line-height:1.25"><span style="flex:none;width:40px;height:40px;border:2.5px solid #5dea84;border-radius:8px;display:grid;place-items:center;color:#5dea84;font-size:26px">✓</span>{esc(x)}</li>' for x in ep["s4"])
    c4=f"""<div style="position:absolute;left:72px;right:72px;top:190px;display:grid;gap:30px">
<h2 class="disp" style="font-size:76px;line-height:.95;font-weight:700">{esc(ep['s4t'])}</h2><ul style="list-style:none">{v4}</ul></div>"""
    # 5 chiusura
    c5=f"""<div style="position:absolute;left:72px;right:72px;top:210px;display:grid;gap:48px">
<p class="disp" style="font-size:70px;line-height:1;font-weight:700">{esc(ep['chiusura'])}</p></div>
<div style="position:absolute;left:72px;right:72px;bottom:150px;display:grid;gap:26px">
<div style="display:flex;gap:16px;flex-wrap:wrap"><span class="mono" style="font-size:20px;border:1.5px solid #a2a6dc;border-radius:999px;padding:16px 26px">Salva il post</span><span class="mono" style="font-size:20px;border:1.5px solid #a2a6dc;border-radius:999px;padding:16px 26px">Condividilo</span><span class="mono" style="font-size:20px;background:#5dea84;color:#03001c;border-radius:999px;padding:16px 26px">Segui Safe &amp; Sound</span></div>
<div style="display:flex;align-items:center;gap:22px;border-top:1.5px solid #36337a;padding-top:30px;margin-top:6px"><span class="mono" style="font-size:18px;color:#a2a6dc;white-space:nowrap">Una rubrica di</span><span style="display:flex;align-items:center;gap:18px"><img src="../pittogramma-fs.svg" style="height:58px;width:auto;display:block" alt=""><span class="disp" style="font-size:30px;font-weight:700;line-height:1;color:#f1f2ff">Formazione<br>e Sicurezza</span></span></div></div>"""
    bg5="background:linear-gradient(180deg,#03001c 0%,#060039 45%,#2c42de 130%)"
    for i,(c,bg) in enumerate([(c1,""),(c2,""),(c3,""),(c4,""),(c5,bg5)],1):
        open(f"{ep['slug']}/{i}.html","w").write(pagina(ep,i,tot,c,bg))
print("ok")
