import os
src=open('non_ci_avevo_pensato.py').read().split('L = "Non ci avevo pensato"')[0]
exec(src)
mock = '''<div style="position:absolute;left:72px;right:72px;top:190px;display:grid;grid-template-columns:1fr 400px;gap:40px;align-items:center">
<div style="display:grid;gap:30px"><span class="mono" style="font-size:22px;color:#ffd43b">Come funziona</span>
<p class="disp" style="font-size:62px;line-height:1.02;font-weight:700">Scrivi il tuo Comune. Fatto.</p>
<p style="font-size:34px;line-height:1.4;color:#a2a6dc">Zona sismica, allerta meteo di oggi e domani e tre cose da fare questa settimana. Gratis, senza app, senza registrarti.</p></div>
<div style="border:10px solid #36337a;border-radius:54px;overflow:hidden;height:667px;box-shadow:0 30px 80px rgba(44,66,222,.35)"><img src="app.png" style="width:100%;display:block"></div></div>'''
zone = lista("Cosa vuol dire la zona", [
 ("1", "Zona 1 · la più pericolosa", "Possono verificarsi fortissimi terremoti"),
 ("2", "Zona 2 · pericolosità alta", "Possono verificarsi forti terremoti"),
 ("3", "Zona 3 · pericolosità media", "Forti terremoti possibili ma rari"),
 ("4", "Zona 4 · la meno pericolosa", "I terremoti sono rari"),
], num=False, occ="Rischio sismico")
col = '''<div style="position:absolute;left:72px;right:72px;top:180px;display:grid;gap:30px"><span class="mono" style="font-size:20px;color:#5dea84">Allerta meteo</span>
<h2 class="disp" style="font-size:70px;line-height:.95;font-weight:700">Quattro colori, ogni giorno.</h2>
<div style="display:grid;gap:18px">''' + "".join(f'<div style="display:flex;align-items:center;gap:26px;padding:20px 0;border-top:1.5px solid #36337a"><span style="flex:none;width:60px;height:60px;border-radius:50%;background:{c}"></span><div style="display:grid;gap:4px"><span style="font-size:34px;font-weight:600">{t}</span><span style="font-size:27px;color:#a2a6dc">{d}</span></div></div>' for c,t,d in [
 ("#5dea84","Verde","Nessuna allerta"),("#ffd43b","Gialla","Fenomeni localizzati: informati e fai attenzione"),("#ff8a1f","Arancione","Fenomeni diffusi: segui le indicazioni del Comune"),("#ff4d5e","Rossa","Fenomeni gravi ed estesi: massima prudenza")]) + '''</div>
<p style="font-size:26px;color:#6c6ca6">La pagina si aggiorna da sola col bollettino del Dipartimento della Protezione Civile.</p></div>'''
pp = [
 gancio("Nuovo strumento gratuito", [("Sai in che", W), ("zona sismica", W), ("vivi?", W), ("Scoprilo in", V), ("10 secondi.", V)], "Our House · Madness"),
 mock, zone, col,
 finale("Cerca il tuo Comune: link in bio. Poi crea la card per le Storie.", "Mandalo a chi vive con te"),
]
d = "fissi/lancio-rischio"; n = len(pp)
for i, c in enumerate(pp, 1):
    open(f"{d}/{i}.html", "w").write(P("Il mio rischio sotto casa", i, n, c, BG5 if i == n else ""))
print("ok")
