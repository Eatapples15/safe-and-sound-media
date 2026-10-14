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
"ncap-01-gas": (L + " · 01", [
 gancio("Non ci avevo pensato · 01", [("Senti odore", W), ("di gas?", W), ("Non accendere", V), ("la luce.", V)], "Breathe · Pink Floyd"),
 punto("Il motivo", "Un interruttore fa una scintilla. Basta quella.",
       "Niente interruttori, campanelli, telefono o accendini nella stanza. Apri le finestre, chiudi la valvola del gas vicino al contatore ed esci. Chiama il 115 o il 112 da fuori casa."),
 punto("Il gas che non senti", "Il monossido di carbonio non ha odore e non ha colore.",
       "Mal di testa, nausea, sonnolenza, confusione. Se in casa state male tutti insieme mentre la caldaia o la stufa sono accese, pensa al CO: esci all'aria aperta e vai al pronto soccorso.",
       "Fonte: Istituto Superiore di Sanità, EpiCentro."),
 check("Prima di accendere il riscaldamento", ["Caldaia, stufa e canna fumaria controllate ogni anno", "Mai forno, fornelli o braciere per scaldare casa", "Mai generatori o barbecue al chiuso", "Prese d'aria libere: non tapparle per il freddo", "Un rilevatore di monossido vicino a caldaia e camere"], occ="Adesso, con calma"),
 finale("Sai dov'è la valvola del gas di casa tua? Vai a vederlo adesso.", "Mandalo a chi vive con te"),
]),
"ncap-02-elettricita": (L + " · 02", [
 gancio("Non ci avevo pensato · 02", [("Qualcuno prende", W), ("la scossa?", W), ("Non toccarlo.", V)], "Electric Avenue · Eddy Grant"),
 punto("Il motivo", "Il primo istinto è afferrarlo. Così le vittime diventano due.",
       "Prima stacca la corrente: salvavita o interruttore generale. Se non puoi, allontanalo dalla fonte con un oggetto asciutto e isolante, di legno o plastica. Poi chiama il 112."),
 punto("Il salvavita", "Ha un tasto di prova. Lo hai mai premuto?",
       "Premi il tasto «T»: la levetta deve scattare e in casa salta la corrente. Rialzala e torna tutto come prima. Se non scatta, il salvavita non ti sta proteggendo: chiama un elettricista.",
       "Ogni quanto: lo indica il produttore. Almeno una volta l'anno."),
 lista("Altre tre cose", [("01", "Telefono in carica sul bordo della vasca", "Acqua e corrente: basta che scivoli"), ("02", "Ciabatte una dentro l'altra", "Sovraccarico: si scaldano fino a fondere"), ("03", "Cavi sotto il tappeto", "Si schiacciano e si rovinano dove non li vedi")]),
 finale("Oggi premi il tasto T. Ci vogliono dieci secondi.", "Mandalo a chi vive con te"),
]),
"ncap-03-locali": (L + " · 03", [
 gancio("Non ci avevo pensato · 03", [("Entri in", W), ("discoteca?", W), ("Conta", V), ("le uscite.", V)], "Disco Inferno · The Trammps"),
 punto("Il motivo", "Nel panico torni alla porta da cui sei entrato.",
       "Anche se ce n'è una più vicina. Appena entri cerca i cartelli verdi delle uscite di sicurezza: dieci secondi, e in caso di emergenza sai già dove andare."),
 check("Se la folla spinge", ["Braccia davanti al petto, come un pugile: ti lasciano spazio per respirare", "Muoviti in diagonale verso i lati, non contro la corrente", "Stai lontano da muri, transenne e porte chiuse", "Se cadi, rialzati subito. Se non ci riesci, rannicchiati sul fianco e proteggi la testa"], occ="Pochi secondi"),
 lista("Altre tre cose", [("01", "C'è fumo?", "Stai basso: l'aria respirabile è vicina al pavimento"), ("02", "Uscita chiusa o bloccata?", "Segnalalo subito al personale del locale"), ("03", "Un punto di ritrovo fuori", "Decidetelo all'arrivo, così nessuno torna dentro a cercarvi")]),
 finale("Sabato esci? Prima di ballare, guarda dove sono le uscite.", "Mandalo a chi esce con te"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
