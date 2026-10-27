import os
exec(open('fissi.py').read().split('POST={')[0])

def gancio(occ, righe, canzone):
    r = "".join(f'<span style="display:block;color:{c}">{t}</span>' for t, c in righe)
    return f"""<div style="position:absolute;left:72px;right:72px;top:200px;display:grid;gap:36px"><span class="mono" style="font-size:20px;color:#ffd43b">{occ}</span>
<h1 class="disp" style="font-size:104px;line-height:.94;font-weight:700">{r}</h1></div>
<div style="position:absolute;left:72px;right:72px;bottom:140px;display:grid;gap:22px">
<span style="font-size:30px;color:#a2a6dc">🎧 {canzone}</span>
<div style="display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid #36337a;padding-top:26px">
<span class="mono" style="font-size:22px;color:#5dea84">Segui @safe_and_sound_it</span><span class="mono" style="font-size:22px">Scorri →</span></div></div>"""

def punto(occ, grande, testo, nota=""):
    n = f'<p style="font-size:28px;line-height:1.4;color:#6c6ca6">{nota}</p>' if nota else ""
    return f"""<div style="position:absolute;left:72px;right:72px;top:190px;display:grid;gap:40px"><span class="mono" style="font-size:22px;color:#ffd43b">{occ}</span>
<p class="disp" style="font-size:66px;line-height:1.02;font-weight:700">{grande}</p>
<p style="font-size:36px;line-height:1.42;color:#a2a6dc">{testo}</p>{n}</div>"""

def finale(frase, invito):
    return f"""<div style="position:absolute;left:72px;right:72px;top:210px"><p class="disp" style="font-size:72px;line-height:1.02;font-weight:700">{frase}</p></div>
<div style="position:absolute;left:72px;right:72px;bottom:150px;display:grid;gap:26px">
<div style="display:flex;gap:16px;flex-wrap:wrap"><span class="mono" style="font-size:20px;background:#5dea84;color:#03001c;border-radius:999px;padding:16px 26px">{invito}</span><span class="mono" style="font-size:20px;border:1.5px solid #a2a6dc;border-radius:999px;padding:16px 26px">Salvalo</span><span class="mono" style="font-size:20px;border:1.5px solid #a2a6dc;border-radius:999px;padding:16px 26px">Segui Safe &amp; Sound</span></div>
<div style="display:flex;align-items:center;gap:22px;border-top:1.5px solid #36337a;padding-top:30px;margin-top:6px"><span class="mono" style="font-size:18px;color:#a2a6dc;white-space:nowrap">Una rubrica di</span><span style="display:flex;align-items:center;gap:18px"><img src="../../pittogramma-fs.svg" style="height:58px"><span class="disp" style="font-size:30px;font-weight:700;line-height:1;color:#f1f2ff">Formazione<br>e Sicurezza</span></span></div></div>"""

L = "Non ci avevo pensato"
POST = {
"ncap-04-quasi-incidente": (L + " · 04", [
 gancio("Non ci avevo pensato · 04", [("Per poco", W), ("non cadi.", W), ("Non è successo", W), ("niente?", W), ("Dillo lo stesso.", V)], "Il secondo secondo me · Caparezza"),
 punto("Il motivo", "Il quasi-incidente ti dice dove succederà.",
       "Si chiama near miss, mancato infortunio: un evento che poteva fare danni e non li ha fatti. È molto più frequente degli infortuni. Il pericolo è lo stesso: questa volta è solo andata bene.",
       "Fonte: INAIL, procedura per la segnalazione dei near miss."),
 check("Come segnalarlo", ["Cosa, dove, quando. Non chi ha sbagliato", "Anche se l'hai solo visto succedere", "Anche se «tanto non si è fatto male nessuno»", "Chiedi cosa è stato corretto: una segnalazione senza risposta non serve"], occ="Due minuti"),
 punto("Non è solo buon senso", "Per la legge è un dato da raccogliere.",
       "La legge 198/2025 prevede linee guida del Ministero del Lavoro, d'intesa con INAIL, per identificare, tracciare e analizzare i mancati infortuni nelle imprese con più di 15 dipendenti.",
       "Fonte: Ministero del Lavoro, conversione del DL 159/2025."),
 finale("L'ultimo «per poco» che hai visto al lavoro? Segnalalo oggi.", "Mandalo a un collega"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
