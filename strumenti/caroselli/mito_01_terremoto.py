import os
exec(open('fissi.py').read().split('POST={')[0])
exec(open('non_ci_avevo_pensato.py').read().split('L = ')[0].split("exec(open('fissi.py')")[1].split('\n',1)[1])

POST = {
"mito-01-terremoto": ("Mito o verità · 01", [
 gancio("Mito o verità · Terremoti", [("I terremoti", W), ("si possono", W), ("prevedere?", W), ("No.", V)], "Che sarà · Ricchi e Poveri"),
 punto("La risposta", "Nessuno sa dire giorno, ora, luogo e magnitudo.",
       "Una previsione così, oggi, non esiste. Esistono stime di probabilità, ma sono approssimative e non si possono usare per dare l'allarme alla popolazione.",
       "Fonte: INGV, domande frequenti sui terremoti."),
 lista("Mito o verità?", [
   ("MITO", "«C'è tempo da terremoto»", "I terremoti avvengono dentro la Terra, con qualsiasi tempo."),
   ("MITO", "«Ha previsto la scossa del giorno X»", "Chi annuncia data e ora non ha basi scientifiche. Non condividerlo."),
   ("VERITÀ", "Sappiamo dove è più probabile", "Le mappe di pericolosità indicano le zone più esposte ai terremoti forti."),
 ], num=False, occ="Tre frasi che girano").replace("grid-template-columns:170px", "grid-template-columns:250px"),
 punto("Non ci avevo pensato", "Non sappiamo quando. Sappiamo dove.",
       "Ogni Comune italiano ha una zona sismica, dalla 1 (la più pericolosa) alla 4. Conoscere la tua è la previsione più utile che puoi fare.",
       "Fonti: Dipartimento della Protezione Civile, Io non rischio."),
 check("Cosa fare oggi", [
   "Scopri la zona sismica del tuo Comune",
   "Individua i punti sicuri di casa: muri portanti, architravi",
   "Fissa al muro mobili alti e oggetti pesanti",
   "Tieni pronti torcia, radio, acqua e documenti",
 ], occ="La prevenzione al posto della previsione"),
 finale("Il terremoto non si prevede. Ci si prepara.", "Mandalo a chi crede alle «previsioni»"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
