import os
exec(open('fissi.py').read().split('POST={')[0])
O = "#ff8a1f"
L = "Come funziona"
slug = "come-funziona-02-allerta"
segui = '<span class="mono" style="font-size:22px;color:#a2a6dc">Segui @safe_and_sound_it</span>'
pp = [
 cover("Come funziona · Allerta meteo",
       [("Ieri la", W), ("Basilicata", W), ("era tutta", W), ("arancione.", O), ("Chi l'ha", G), ("deciso?", G)],
       segui),
 f'''<div style="position:absolute;left:72px;right:72px;top:220px;display:grid;gap:48px"><span class="mono" style="font-size:22px;color:#5dea84">La cosa che sorprende</span>
<p class="disp" style="font-size:76px;line-height:1;font-weight:700">Il colore non misura <span style="color:{O}">la pioggia.</span></p>
<p style="font-size:44px;line-height:1.3;font-weight:500">Misura gli effetti che quella pioggia può avere sul territorio: frane, allagamenti, fiumi che si alzano.</p>
<p style="font-size:34px;line-height:1.4;color:#a2a6dc">Per questo la stessa perturbazione può essere gialla in una zona e arancione in quella accanto.</p></div>''',
 lista("Chi fa cosa", [
   ("01", "Centro Funzionale", "I tecnici della Regione incrociano previsioni meteo, terreno e corsi d'acqua, zona per zona."),
   ("02", "Regione", "Ogni giorno nel pomeriggio pubblica il bollettino con l'allerta per oggi e domani."),
   ("03", "Comune", "Il sindaco attiva la fase operativa e il piano di protezione civile."),
   ("04", "Dipartimento", "La Protezione Civile nazionale coordina la rete e pubblica il quadro di tutta Italia.")]),
 (lambda rows: f'''<div style="position:absolute;left:72px;right:72px;top:180px;display:grid;gap:30px"><h2 class="disp" style="font-size:70px;line-height:.95;font-weight:700">I quattro colori</h2><div>{"".join(f'<div style="display:grid;grid-template-columns:56px 1fr;gap:30px;align-items:start;padding:30px 0;border-top:1.5px solid #36337a"><span style="width:56px;height:56px;border-radius:14px;background:{c};margin-top:4px"></span><div style="display:grid;gap:8px"><span class="disp" style="font-size:40px;font-weight:700;color:{c}">{t}</span><span style="font-size:32px;font-weight:600">{k}</span><span style="font-size:28px;line-height:1.35;color:#a2a6dc">{d}</span></div></div>' for c,t,k,d in rows)}</div></div>''')([
   ("#5dea84","Verde","Nessuna allerta","Nessuna criticità significativa prevista."),
   ("#ffd43b","Gialla","Criticità ordinaria","Fenomeni localizzati: allagamenti e frane in punti precisi."),
   ("#ff8a1f","Arancione","Criticità moderata","Fenomeni diffusi: frane, allagamenti, piene dei corsi d'acqua."),
   ("#ff4d5e","Rossa","Criticità elevata","Fenomeni estesi e gravi, anche per persone ed edifici.")]),
 f'''<div style="position:absolute;left:72px;right:72px;top:200px;display:grid;gap:40px"><span class="mono" style="font-size:22px;color:#5dea84">Non ci avevo pensato</span>
<p class="disp" style="font-size:66px;line-height:1.02;font-weight:700">L'allerta è una <span style="color:{O}">previsione</span>, non l'allarme.</p>
<p style="font-size:36px;line-height:1.4;color:#d9dbf7">Dice cosa potrebbe succedere. Poi è il Comune a decidere come muoversi: <b>attenzione</b>, <b>preallarme</b>, <b>allarme</b>.</p>
<div class="player" style="gap:14px"><span class="mono" style="font-size:18px;color:#a2a6dc">La regola nazionale</span><span style="font-size:32px;line-height:1.35">Con allerta gialla o arancione, almeno la fase di <b>attenzione</b>. Con la rossa, almeno il <b>preallarme</b>.</span></div></div>''',
 f'''<div style="position:absolute;left:72px;right:72px;top:200px;display:grid;gap:40px"><span class="mono" style="font-size:22px;color:#5dea84">Le zone di allerta</span>
<p class="disp" style="font-size:70px;line-height:1;font-weight:700">Il colore è per <span style="color:#5dea84">zona</span>, non per regione.</p>
<p style="font-size:38px;line-height:1.38">Ogni regione è divisa in zone che rispondono allo stesso modo alla pioggia. La Basilicata ne ha <b>7</b>: A1, A2, B, C, D, E1, E2.</p>
<p style="font-size:34px;line-height:1.4;color:#a2a6dc">Ecco perché oggi una parte della regione è arancione e un'altra gialla.</p></div>''',
 check("Da fare oggi", [
   "Scopri in che zona di allerta è il tuo comune",
   "Guarda il bollettino ogni pomeriggio, per il giorno dopo",
   "Leggi il piano di protezione civile del tuo Comune",
   "Con l'arancione: niente cantine, sottopassi e argini"], occ="5 minuti"),
 chiusura("Il colore lo decide chi studia il territorio. Cosa fare, lo decidi tu."),
]
d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
for i, c in enumerate(pp, 1):
    open(f"{d}/{i}.html", "w").write(P(L, i, n, c, BG5 if i == n else ""))
print(n)
