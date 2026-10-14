#!/usr/bin/env python3
"""Controlla una didascalia di Safe & Sound prima della pubblicazione.

Uso:  python3 controlla_didascalia.py didascalia.txt
      echo "testo" | python3 controlla_didascalia.py -

Controlli: anteprima dei primi 125 caratteri (quelli visibili prima di «altro»),
lunghezza, hashtag, fonte citata, parole da evitare, nome dell'autore, numeri da verificare.
Lavora solo sul testo, offline.
"""
import re
import sys

ANTEPRIMA = 125
MAX_HASHTAG = 5
ESCA = ["tagga", "commenta sì", "commenta si", "doppio tap", "metti like", "lascia un like", "scrivi sì", "scrivi si"]
VIETATE = {
    # allarmismo e acchiappa-click
    "shock": "allarmismo", "incredibile": "acchiappa-click", "non crederai": "acchiappa-click",
    "nessuno ti dice": "acchiappa-click", "terrificante": "allarmismo", "apocalisse": "allarmismo",
    "catastrofe imminente": "allarmismo", "panico": "allarmismo", "devi assolutamente": "tono imperativo",
    # parole vuote tipiche dei testi generati
    "fondamentale": "parola vuota", "cruciale": "parola vuota", "imprescindibile": "parola vuota",
    "a 360 gradi": "parola vuota", "in un mondo in cui": "formula fatta", "è importante sottolineare": "formula fatta",
    "in conclusione": "formula fatta", "approfondiamo": "formula fatta", "viaggio": "metafora abusata",
    "tuffiamoci": "formula fatta", "game changer": "anglicismo inutile", "svolta epocale": "enfasi",
}
NOMI_VIETATI = ["mangiamele", "antonio m", "dott. antonio", "dott antonio"]
FONTI = ["fonte", "protezione civile", "dpc", "ingv", "d.lgs", "inail", "erc", "linee guida", "io non rischio", "it-alert.it"]
TEMI_CON_FONTE = ["allerta", "terremot", "scoss", "d.lgs", "legge", "norma", "rcp", "compressioni", "it-alert", "bollettino"]


def controlla(testo):
    t = testo.strip()
    basso = t.lower()
    esiti = []

    prima = t.split("\n")[0]
    anteprima = t[:ANTEPRIMA].replace("\n", " ")
    esiti.append(("info", f"Anteprima nel feed ({ANTEPRIMA} caratteri):\n    «{anteprima}…»"))
    if len(prima) > ANTEPRIMA:
        esiti.append(("attenzione", "La prima frase supera l'anteprima: l'aggancio deve stare nei primi 125 caratteri."))
    if not re.search(r"[?!.:]", t[:ANTEPRIMA]):
        esiti.append(("attenzione", "Nessuna frase completa nell'anteprima: chiudi l'aggancio prima di «altro»."))

    n = len(t)
    if n > 2200:
        esiti.append(("errore", f"{n} caratteri: Instagram ne accetta al massimo 2.200."))
    elif n > 1300:
        esiti.append(("attenzione", f"{n} caratteri: lunga per un post, valuta di spostare dettagli nel carosello."))

    tag = re.findall(r"#\w+", t)
    if not tag:
        esiti.append(("attenzione", "Nessun hashtag: aggiungi almeno #SafeAndSound."))
    elif "#safeandsound" not in [x.lower() for x in tag]:
        esiti.append(("attenzione", "Manca #SafeAndSound."))
    if len(tag) > MAX_HASHTAG:
        esiti.append(("attenzione", f"{len(tag)} hashtag: ne bastano 3–{MAX_HASHTAG}, mirati."))

    for x in ESCA:
        if x in basso:
            esiti.append(("errore", f"«{x}»: esca per l'engagement, Instagram la penalizza. Usa un invito a mandare o salvare."))

    for nome in NOMI_VIETATI:
        if nome in basso:
            esiti.append(("errore", "Compare il nome dell'autore: in Safe & Sound si firma solo «Formazione e Sicurezza»."))
            break

    for parola, motivo in VIETATE.items():
        if parola in basso:
            esiti.append(("attenzione", f"«{parola}»: {motivo}."))

    if any(x in basso for x in TEMI_CON_FONTE) and not any(f in basso for f in FONTI):
        esiti.append(("errore", "Tema tecnico o di attualità senza fonte: cita la fonte ufficiale."))

    numeri = re.findall(r"\b\d+(?:[.,]\d+)?\s?(?:%|per cento|cm|km|metri|minuti|bpm|regioni|morti|vittime|feriti)\b", basso)
    if numeri:
        esiti.append(("info", "Numeri da verificare con la fonte: " + ", ".join(sorted(set(numeri)))))

    inviti = ["?", "commenti", "salva", "condividi", "manda", "link in bio", "scorri", "segui"]
    if not any(x in basso for x in inviti):
        esiti.append(("attenzione", "Nessun invito all'azione (manda a qualcuno, salva, una domanda)."))

    return esiti


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    testo = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    esiti = controlla(testo)
    errori = 0
    for livello, msg in esiti:
        segno = {"errore": "✗", "attenzione": "!", "info": "·"}[livello]
        errori += livello == "errore"
        print(f"{segno} {msg}")
    print("\nPronta." if errori == 0 else f"\n{errori} errore/i da correggere.")
    sys.exit(1 if errori else 0)


if __name__ == "__main__":
    main()
