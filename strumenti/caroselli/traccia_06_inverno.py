import os
exec(open('fissi.py').read().split('POST={')[0])
exec(open('ncap_04_quasi_incidente.py').read().split('\n', 2)[2].split('L = "Non ci avevo pensato"')[0])

def esebox(occ, grande, testo, dom, risp, nota=""):
    n = f'<p style="font-size:24px;line-height:1.4;color:#6c6ca6">{nota}</p>' if nota else ""
    return f"""<div style="position:absolute;left:72px;right:72px;top:190px;display:grid;gap:36px"><span class="mono" style="font-size:22px;color:#ffd43b">{occ}</span>
<p class="disp" style="font-size:66px;line-height:1.02;font-weight:700">{grande}</p>
<p style="font-size:34px;line-height:1.42;color:#a2a6dc">{testo}</p>
<div style="border:2px solid #ffd43b;border-radius:22px;padding:30px 34px;display:grid;gap:12px;background:rgba(255,212,59,.06)">
<span class="mono" style="font-size:20px;color:#ffd43b">E se…?</span>
<span style="font-size:36px;font-weight:600">{dom}</span>
<span style="font-size:30px;line-height:1.38;color:#a2a6dc">{risp}</span></div>{n}</div>"""

L = "Traccia · 06"
POST = {
"traccia-06-inverno": (L, [
 gancio("Traccia · 06 · Guidare d'inverno", [("Da domenica", W), ("ti possono", W), ("multare.", W), ("Le catene", V), ("le hai mai montate?", V)], "Strada facendo · Claudio Baglioni"),
 punto("Dal 15 novembre al 15 aprile", "Gomme invernali o catene a bordo.",
       "Vale sulle strade dove l'ente che le gestisce ha messo l'ordinanza. Te lo dice il cartello all'inizio del tratto.",
       "Fonte: Codice della strada, art. 6 · ACI."),
 lista("Cosa vale", [("01", "Gomme M+S", "La marcatura sul fianco della gomma"), ("02", "Montagna con fiocco", "Il simbolo 3PMSF: ha superato la prova su neve"), ("03", "Catene a bordo", "Della misura delle tue gomme")]),
 esebox("La domanda che ti fai", "Guarda la gomma, non il nome.",
        "Conta la marcatura sul fianco, non il nome commerciale.",
        "E se ho le 4 stagioni?", "Valgono, se sul fianco c'è M+S.", "Fonte: ACI, L'Automobile, 9/11/2026."),
 check("Prima di partire", ["Cerca M+S sul fianco delle gomme", "Metti le catene nel bagagliaio", "Provale una volta a casa, con l'asciutto"], occ="3 cose da fare · salvala"),
 finale("Le catene si imparano in garage, non sotto la neve.", "Mandalo a chi va in montagna"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
