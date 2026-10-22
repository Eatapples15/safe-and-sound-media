import os
exec(open('fissi.py').read().split('POST={')[0])
O="#ff8a1f"
POST={
"edizione-01-vento":("Edizione straordinaria",[
 cover("Edizione straordinaria · Vento forte",[("Con il vento,",W),("il pericolo",W),("arriva",O),("dall'alto.",O)],
  '<span class="mono" style="font-size:22px;color:#a2a6dc">Segui @safe_and_sound_it</span>'),
 f'''<div style="position:absolute;left:72px;right:72px;top:200px;display:grid;gap:40px"><span class="mono" style="font-size:22px;color:#5dea84">Perché</span>
<p style="font-size:60px;line-height:1.15;font-weight:500">Con le raffiche, l'incidente più frequente è la rottura dei rami.</p>
<p style="font-size:36px;line-height:1.4;color:#a2a6dc">Possono colpire chi passa o finire in strada, su auto e moto. Il 21 ottobre a Jesolo un albero caduto su un'auto ha ucciso un uomo di 46 anni.</p>
<p class="mono" style="font-size:20px;color:#6c6ca6">Fonte: Dipartimento della Protezione Civile · ANSA</p></div>''',
 lista("All'aperto",[("1","Cerca un riparo","Lontano da ciò che può cadere: vasi, tegole, insegne"),("2","Evita parchi e viali alberati","I rami si spezzano anche senza che l'albero cada"),("3","Stai lontano da impalcature e gazebo","Teli e tendoni fanno vela: verifica che siano ancorati")]),
 lista("In auto e in casa",[("1","Rallenta, o fermati","Se le raffiche fanno sbandare il veicolo"),("2","Occhio ai punti esposti","Uscita delle gallerie, viadotti, strade costiere"),("3","Furgoni, telonati, caravan","Il vento li sposta anche se non è fortissimo"),("4","Svuota il balcone","Fissa o ritira vasi e oggetti prima che arrivi")]),
 chiusura("Allerta vento? Prima di uscire, svuota il balcone e cambia strada."),
]),
}
for slug,(label,pp) in POST.items():
    d=f"fissi/{slug}"; os.makedirs(d,exist_ok=True); n=len(pp)
    for i,c in enumerate(pp,1):
        open(f"{d}/{i}.html","w").write(P(label,i,n,c,BG5 if i==n else ""))
print("ok")
