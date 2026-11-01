import os
exec(open('fissi.py').read().split('POST={')[0])
exec(open('non_ci_avevo_pensato.py').read().split('L = ')[0].split("exec(open('fissi.py')")[1].split('\n',1)[1])

POST = {
"come-funziona-01-scale-sismiche": ("Come funziona · 01", [
 gancio("Come funziona · Terremoti", [("Richter e", W), ("Mercalli", W), ("misurano", W), ("cose diverse.", V)], "Good Vibrations · The Beach Boys"),
 punto("Il perché", "Un terremoto ha una sola magnitudo. Ma tante intensità.",
       "La magnitudo (Richter) misura l'energia liberata alla fonte e si calcola dai sismografi. L'intensità (Mercalli, scala MCS) misura gli effetti in un luogo: su persone, oggetti, edifici. E cambia da paese a paese.",
       "Fonte: INGV."),
 lista("Due scale, due domande", [
   ("5.5", "Magnitudo: quanto è forte alla fonte?", "Un numero con i decimali, uguale per tutti. Lo calcolano gli strumenti."),
   ("VI", "Intensità: cosa ha fatto qui?", "Un grado da I a XII, in numeri romani. Lo dicono gli effetti osservati."),
   ("×32", "Un punto di magnitudo in più", "Vuol dire circa 32 volte l'energia liberata, non il doppio."),
 ], num=False, occ="Magnitudo e intensità").replace("grid-template-columns:170px", "grid-template-columns:200px"),
 punto("Il caso di ottobre", "Tirreno, 23 ottobre: magnitudo 5.5 in mare.",
       "Epicentro a circa 30 km da Alicudi, 9 km di profondità. Una sola magnitudo, ma a Palermo e nei centri della costa ognuno l'ha sentita in modo diverso. Quella differenza è l'intensità.",
       "Fonte: INGV, terremoti.ingv.it."),
 punto("Non ci avevo pensato", "L'intensità la misuri anche tu.",
       "Dopo una scossa l'INGV raccoglie le risposte dei cittadini al questionario «Hai sentito il terremoto?». Per la scossa del 23 ottobre ne sono arrivate 2.778: servono a disegnare la mappa degli effetti.",
       "Fonte: INGV, hsit.it."),
 check("Hai sentito una scossa?", [
   "Prima mettiti al sicuro, il telefono dopo",
   "Apri hsit.it e cerca il terremoto",
   "Racconta cosa hai sentito e visto: persone, oggetti, porte",
   "Rispondi anche se l'hai sentita appena",
 ], occ="Cosa fare dopo"),
 finale("Magnitudo: quanto è forte. Intensità: cosa fa. La seconda la scrivi anche tu.", "Mandalo a chi l'ha sentita"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
