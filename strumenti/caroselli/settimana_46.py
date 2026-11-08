import os
exec(open('fissi.py').read().split('POST={')[0])
exec(open('ncap_04_quasi_incidente.py').read().split('\n', 2)[2].split('L = "Non ci avevo pensato"')[0])

POST = {
"tech-track-03-ecall": ("Tech Track · 03", [
 gancio("Tech Track · 03", [("Incidente.", W), ("Non riesci", W), ("a chiamare?", W), ("La tua auto", V), ("lo fa da sola.", V)], "Chiamami ancora amore · Roberto Vecchioni"),
 punto("Si chiama eCall", "Chiama il 112 senza che tu tocchi niente.",
       "Se scattano gli airbag o l'urto è forte, l'auto apre una chiamata al 112 e mette in linea l'abitacolo con l'operatore. È obbligatoria sui nuovi modelli di auto e furgoni leggeri omologati dal 31 marzo 2018.",
       "Fonte: Regolamento (UE) 2015/758."),
 lista("Cosa arriva al 112", [("01", "Dove sei", "Posizione da satellite e direzione di marcia"), ("02", "Quando", "Ora esatta dell'incidente"), ("03", "Che auto è", "Tipo di veicolo e carburante"), ("04", "Quante persone", "Il numero di passeggeri")]),
 check("Il tasto SOS", ["Di solito è sul cielo dell'abitacolo, vicino alle luci", "Funziona anche a mano: tienilo premuto", "Usalo anche se vedi un incidente grave", "Non ti segue: i dati partono solo con la chiamata"], occ="Da sapere"),
 finale("Prima di ripartire, cerca il tasto SOS della tua auto.", "Mandalo a chi guida"),
]),
"giornata-vittime-strada-2026": ("Giornata · vittime della strada", [
 gancio("15 novembre · Giornata in memoria", [("2.868", V), ("persone", W), ("morte sulle", W), ("strade italiane", W), ("nel 2025.", W)], "Emozioni · Lucio Battisti"),
 punto("Il dato", "Meno morti del 2024. Più incidenti e più feriti.",
       "Nel 2025 i morti sono scesi del 5,3%, ma gli incidenti con feriti sono saliti a 177.207 e i feriti a 237.822. Dietro ogni numero c'è una famiglia.",
       "Fonte: ACI-Istat, Incidenti stradali in Italia 2025."),
 lista("Chi è più esposto", [("419", "Pedoni", "Morti nel 2025, uno su sette"), ("228", "Ciclisti", "+23% sul 2024"), ("25", "Monopattini", "Conducenti e passeggeri")], num=False),
 check("Cosa dipende da te", ["Telefono fuori portata prima di partire", "Precedenza: rallenta sempre agli incroci", "Velocità adatta alla strada, non al limite", "Cintura anche dietro, sempre"], occ="Gli errori più frequenti secondo Istat"),
 finale("Oggi, prima di partire, metti il telefono dove non arrivi.", "Mandalo a chi guida"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
