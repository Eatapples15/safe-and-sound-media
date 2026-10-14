import html, os, re
exec(open('render.py').read().split('for ep in E:')[0].replace('E = json.load(open("episodi.json"))','E=[]'))
def P(label,i,tot,corpo,sf=""):
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body style="{sf}">
<div class="alone"></div><div class="top"><span style="display:flex;align-items:center;gap:14px"><svg width="46" height="42" viewBox="0 0 260 240" style="flex:none"><path d="M44 92 A90 90 0 0 1 186 46" fill="none" stroke="#5dea84" stroke-width="18" stroke-linecap="round"/><path d="M216 148 A90 90 0 0 1 74 194" fill="none" stroke="#2c42de" stroke-width="18" stroke-linecap="round"/><path d="M24 120 H70 L90 88 L108 62 L124 176 L144 96 L160 126 L172 120 H236" fill="none" stroke="#f1f2ff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="marchio">SAFE <b>&amp;</b> SOUND</span></span><span class="mono">{label}</span></div>
{corpo}<div class="piede"><span class="mono">formazionesicurezza.org</span><span class="mono pag">{i:02d} / {tot:02d}</span></div></body></html>"""
def cover(occ,righe,sotto=""):
    r="".join(f'<span style="display:block;color:{c}">{t}</span>' for t,c in righe)
    return f"""<div style="position:absolute;left:72px;right:72px;top:210px;display:grid;gap:36px"><span class="mono" style="font-size:20px;color:#5dea84">{occ}</span>
<h1 class="disp" style="font-size:118px;line-height:.92;font-weight:700">{r}</h1></div>
<div style="position:absolute;left:72px;right:72px;bottom:150px;display:grid;gap:28px">{sotto}</div>"""
def lista(tit,voci,num=True,occ=""):
    v="".join(f'<div style="display:grid;grid-template-columns:{"170px" if not num else "90px"} 1fr;gap:24px;padding:26px 0;border-top:1.5px solid #36337a"><span class="disp" style="font-size:{44 if num else 52}px;font-weight:700;color:#5dea84">{k}</span><div style="display:grid;gap:8px"><span style="font-size:34px;font-weight:600">{t}</span><span style="font-size:27px;line-height:1.35;color:#a2a6dc">{d}</span></div></div>' for k,t,d in voci)
    o=f'<span class="mono" style="font-size:20px;color:#5dea84">{occ}</span>' if occ else ''
    return f"""<div style="position:absolute;left:72px;right:72px;top:170px;display:grid;gap:26px">{o}<h2 class="disp" style="font-size:70px;line-height:.95;font-weight:700">{tit}</h2><div>{v}</div></div>"""
def check(tit,voci,occ=""):
    v="".join(f'<li style="display:flex;gap:26px;align-items:center;padding:24px 0;border-top:1.5px solid #36337a;font-size:34px;line-height:1.25"><span style="flex:none;width:40px;height:40px;border:2.5px solid #5dea84;border-radius:8px;display:grid;place-items:center;color:#5dea84;font-size:26px">✓</span>{x}</li>' for x in voci)
    o=f'<span class="mono" style="font-size:20px;color:#5dea84">{occ}</span>' if occ else ''
    return f"""<div style="position:absolute;left:72px;right:72px;top:180px;display:grid;gap:26px">{o}<h2 class="disp" style="font-size:72px;line-height:.95;font-weight:700">{tit}</h2><ul style="list-style:none">{v}</ul></div>"""
def chiusura(frase):
    return f"""<div style="position:absolute;left:72px;right:72px;top:210px"><p class="disp" style="font-size:76px;line-height:1;font-weight:700">{frase}</p></div>
<div style="position:absolute;left:72px;right:72px;bottom:150px;display:grid;gap:26px">
<div style="display:flex;gap:16px;flex-wrap:wrap"><span class="mono" style="font-size:20px;border:1.5px solid #a2a6dc;border-radius:999px;padding:16px 26px">Salva il post</span><span class="mono" style="font-size:20px;border:1.5px solid #a2a6dc;border-radius:999px;padding:16px 26px">Condividilo</span><span class="mono" style="font-size:20px;background:#5dea84;color:#03001c;border-radius:999px;padding:16px 26px">Segui Safe &amp; Sound</span></div>
<div style="display:flex;align-items:center;gap:22px;border-top:1.5px solid #36337a;padding-top:30px;margin-top:6px"><span class="mono" style="font-size:18px;color:#a2a6dc;white-space:nowrap">Una rubrica di</span><span style="display:flex;align-items:center;gap:18px"><img src="../../pittogramma-fs.svg" style="height:58px"><span class="disp" style="font-size:30px;font-weight:700;line-height:1;color:#f1f2ff">Formazione<br>e Sicurezza</span></span></div></div>"""
BG5="background:linear-gradient(180deg,#03001c 0%,#060039 45%,#2c42de 130%)"
W="#f1f2ff";G="#6c6ca6";V="#5dea84";Y="#ffd43b";R="#ff4d5e"
POST={
"00-benvenuto":("Inizia da qui",[
 cover("Benvenuto in Safe &amp; Sound",[("La",G),("sicurezza",W),("a tempo",W),("di musica.",V)],eq("00")),
 f'''<div style="position:absolute;left:72px;right:72px;top:220px;display:grid;gap:48px"><span class="mono" style="font-size:22px;color:#5dea84">Cos'è</span>
<p style="font-size:60px;line-height:1.18;font-weight:500">Ogni settimana un tema di sicurezza e protezione civile, e una canzone che lo racconta.</p>
<p style="font-size:38px;line-height:1.35;color:#a2a6dc">Niente allarmismi: cose utili da sapere, spiegate in modo semplice. Da salvare, da condividere, da fare.</p></div>''',
 lista("Le rubriche",[("01","Traccia","Un tema, una canzone. La guida completa da salvare."),("02","Lato B","Miti da sfatare e curiosità sulla sicurezza."),("03","Edizione straordinaria","Quando succede qualcosa: cosa sapere, subito."),("04","Tech Track","La tecnologia che ci protegge: IT-alert, app, sensori.")]),
 chiusura("Una traccia a settimana. Premi play sulla prevenzione."),
]),
"01-numeri-utili":("Info",[
 cover("Da salvare",[("I numeri",W),("da sapere",W),("a memoria.",V)],'<div class="player" style="gap:10px"><span class="mono" style="font-size:18px;color:#a2a6dc">Il più importante</span><span class="disp" style="font-size:150px;font-weight:700;line-height:1;color:#5dea84">112</span><span style="font-size:30px;color:#a2a6dc">Numero unico di emergenza europeo</span></div>'),
 f'''<div style="position:absolute;left:72px;right:72px;top:200px;display:grid;gap:40px"><span class="disp" style="font-size:260px;font-weight:700;line-height:.9;color:#5dea84">112</span>
<p style="font-size:54px;line-height:1.18;font-weight:500">Il numero unico di emergenza europeo.</p>
<p style="font-size:36px;line-height:1.4;color:#a2a6dc">Funziona in tutta Italia e in tutti i Paesi dell'Unione Europea, anche senza credito. Se non sai chi chiamare, chiama il 112.</p></div>''',
 lista("Gli altri numeri",[("113","Polizia di Stato","Soccorso pubblico"),("115","Vigili del Fuoco","Incendi, crolli, fughe di gas, soccorso tecnico"),("118","Emergenza sanitaria","Malori, incidenti, ferite gravi"),("1530","Guardia Costiera","Emergenze in mare")],num=False),
 lista("Quando chiami",[("1","Chi sei","Nome e numero da cui chiami"),("2","Cosa è successo","Poche parole, chiare"),("3","Dove sei","Indirizzo, Comune, un punto di riferimento"),("4","Quante persone","Feriti, persone in pericolo"),("5","Non riattaccare","Chiude per primo l'operatore")]),
 chiusura("Salvalo adesso. In emergenza non avrai tempo di cercarlo."),
]),
"02-terremoto":("Guida",[
 cover("Prima · durante · dopo",[("Terremoto:",W),("cosa fare",W),("in 3 tempi.",V)],eq("02")),
 check("Prima",["Scopri se il tuo Comune è in zona sismica e qual è la tua area di attesa","Fissa alle pareti mobili alti e pesanti","Sai dove chiudere acqua, luce e gas","Prepara il piano di emergenza di casa"],occ="Adesso, con calma"),
 check("Durante",["In casa: riparati sotto un tavolo robusto o vicino a un muro portante","Stai lontano da finestre, vetri e mobili che possono cadere","Non usare l'ascensore, non correre per le scale","All'aperto: lontano da edifici, alberi, lampioni e linee elettriche"],occ="Pochi secondi"),
 check("Dopo",["Esci con prudenza, con le scarpe ai piedi","Raggiungi l'area di attesa del tuo Comune","Usa il telefono solo per le emergenze","Segui le indicazioni delle autorità e della protezione civile"],occ="Quando la scossa è finita"),
 chiusura("Prepararsi è l'unica scossa che puoi decidere tu."),
]),
}
for slug,(label,pp) in POST.items():
    d=f"fissi/{slug}"; os.makedirs(d,exist_ok=True); n=len(pp)
    for i,c in enumerate(pp,1):
        open(f"{d}/{i}.html","w").write(P(label,i,n,c,BG5 if i==n else ""))
print("ok")
