import os
exec(open('fissi.py').read().split('POST={')[0])
exec(open('non_ci_avevo_pensato.py').read().split('L = ')[0].split("exec(open('fissi.py')")[1].split('\n',1)[1])

POST = {
"tech-track-02-magnitudo": ("Tech Track · 02", [
 gancio("Tech Track · Etna, 21 ottobre", [("Prima 3.9,", W), ("poi 3.8.", W), ("Nessuno ha", V), ("sbagliato.", V)], "Confusa e felice · Carmen Consoli"),
 punto("Il motivo", "Nei primi 2 minuti decide un computer. Poi un sismologo.",
       "La stima automatica usa i dati arrivati fino a quel momento e dà un intervallo, non un numero preciso. Poi un sismologo di turno rivede i segnali e il dato rivisto sostituisce quello provvisorio.",
       "Fonte: INGV, Sala di sorveglianza sismica."),
 lista("Dopo la scossa", [
   ("2′", "Stima automatica", "Intervallo di magnitudo, epicentro, profondità"),
   ("5′", "Localizzazione automatica finale", "Sono arrivati i dati di più stazioni"),
   ("15′", "Revisione del sismologo", "Di solito 12–15 minuti, al massimo 30"),
   ("Poi", "Altre magnitudo, come la Mw", "Calcoli più lunghi, a volte valori diversi"),
 ], num=False, occ="La sala INGV, minuto per minuto"),
 punto("Non ci avevo pensato", "Lo stesso terremoto può avere più magnitudo.",
       "Ci sono scale diverse: l'INGV di solito dà subito la magnitudo locale (ML), la magnitudo momento (Mw) arriva più tardi. Ed enti diversi possono ottenere valori un po' diversi. Per questo i siti a volte non coincidono.",
       "Oltre 500 stazioni sismiche, sale operative a Roma, Napoli e Catania, 24 ore su 24."),
 finale("Senti una scossa? Il dato giusto è su terremoti.ingv.it. Salvalo oggi.", "Mandalo a chi ha sentito la scossa"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
