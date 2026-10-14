import os
exec(open('fissi.py').read().split('POST={')[0])
POST={
"traccia-04-rcp":("Traccia 04",[
 cover("16 ottobre · World Restart a Heart Day",[("Il ritmo",G),("che salva",W),("una vita.",V)],eq("04")),
 lista("Se qualcuno crolla",[("1","Non risponde, non respira normalmente?","Chiama il 112 e metti il vivavoce"),("2","Fatti portare un DAE","Il defibrillatore, se c'è"),("3","Mani al centro del torace","Una sopra l'altra, braccia tese"),("4","Spingi e non fermarti","Fino all'arrivo dei soccorsi")]),
 f'''<div style="position:absolute;left:72px;right:72px;top:200px;display:grid;gap:36px"><span class="mono" style="font-size:22px;color:#5dea84">Il ritmo giusto</span>
<span class="disp" style="font-size:150px;font-weight:700;line-height:.9;white-space:nowrap">100<span style="color:#6c6ca6">–</span>120</span>
<p style="font-size:52px;line-height:1.15;font-weight:500">compressioni al minuto,<br>profonde 5–6 cm.</p>
<p style="font-size:34px;line-height:1.4;color:#a2a6dc">Lascia risalire il torace dopo ogni spinta. Linee guida European Resuscitation Council 2025.</p></div>''',
 lista("Canzoni a tempo",[("103","Stayin' Alive","Bee Gees"),("109","Eye of the Tiger","Survivor"),("113","Can't Stop the Feeling!","Justin Timberlake"),("117","Billie Jean","Michael Jackson"),("119","I Wanna Dance with Somebody","Whitney Houston")],num=False),
 chiusura("Metronomo e playlist: link in bio. Poi fai un corso BLSD."),
]),
}
for slug,(label,pp) in POST.items():
    d=f"fissi/{slug}"; os.makedirs(d,exist_ok=True); n=len(pp)
    for i,c in enumerate(pp,1):
        open(f"{d}/{i}.html","w").write(P(label,i,n,c,BG5 if i==n else ""))
print("ok")
