import os
exec(open('fissi.py').read().split('POST={')[0])
exec(open('non_ci_avevo_pensato.py').read().split('L = ')[0].split("exec(open('fissi.py')")[1].split('\n',1)[1])

POST = {
"accadde-san-giuliano-scuola": ("Accadde oggi · 31.10", [
 gancio("Accadde oggi · 31 ottobre 2002", [("Trema mentre", W), ("tuo figlio è", W), ("a scuola.", W), ("Sai cosa fanno?", V)], "La cura · Franco Battiato"),
 punto("Non ci avevo pensato", "Il piano di emergenza della scuola non è un segreto.",
       "Ogni scuola deve averne uno e fare le prove di evacuazione durante l'anno. Puoi chiedere di conoscerlo: dove vengono portati i bambini, chi li accompagna, come vengono avvisate le famiglie.",
       "Fonte: D.Lgs. 81/08 · DM 26 agosto 1992, prevenzione incendi nell'edilizia scolastica."),
 punto("31 ottobre 2002, ore 11:32", "San Giuliano di Puglia, Molise. Magnitudo 5.8.",
       "Crollò la scuola «Francesco Jovine»: morirono 27 bambini e una maestra. Da quel giorno è partita la nuova classificazione sismica di tutta Italia: nessun Comune è più considerato «non sismico».",
       "Fonte: Dipartimento della Protezione Civile · OPCM 3274/2003."),
 check("Cosa chiedere alla scuola", ["Dov'è l'area di raccolta dei bambini dopo l'evacuazione", "Quando si fanno le prove, e com'è andata l'ultima", "Come vengono avvisate le famiglie in emergenza", "Se l'edificio ha avuto la verifica sismica"], occ="Al prossimo colloquio"),
 finale("E a casa insegnalo ai bambini: durante la scossa, sotto il banco.", "Mandalo a un genitore"),
]),
}
for slug, (label, pp) in POST.items():
    d = f"fissi/{slug}"; os.makedirs(d, exist_ok=True); n = len(pp)
    for i, c in enumerate(pp, 1):
        open(f"{d}/{i}.html", "w").write(P(label, i, n, c, BG5 if i == n else ""))
print("ok")
