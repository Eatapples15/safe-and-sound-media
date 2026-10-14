# Strumenti della redazione

- `prepara_ambiente.sh` — scarica i font del brand e controlla Playwright e ffmpeg.
- `controlla_didascalia.py` — controllo della didascalia: anteprima a 125 caratteri, hashtag (3–5), esche per l'engagement, fonte, parole da evitare, nome dell'autore.
- `caroselli/` — generatore dei caroselli 1080×1350.
  - `fissi.py` contiene i blocchi riutilizzabili: `cover`, `lista`, `check`, `chiusura` e la pagina `P`.
  - `esempio_nuovo_post.py` è il modello per un post nuovo: copialo, cambia `POST`, esegui `python3 <file>.py`, poi `node shotn.js <cartella>`.
  - `render.py` + `episodi.json` sono le prime tre Tracce.
- `reel/` — Reel a testo animato 1080×1920.
  - `modello-reel.html` contiene le scene `s1`…`s5`, la funzione `draw(t)` e le funzioni di uscita `win`/`inn`.
  - Per generare: `node cap.js modello-reel.html <secondi> <cartella-fotogrammi>`, poi `ffmpeg -framerate 30 -i <cartella>/%04d.jpg -c:v libx264 -pix_fmt yuv420p -crf 19 -movflags +faststart <uscita>.mp4`.

I file pubblicati vanno in `tracce/` o `fissi/` e si usano da `https://raw.githubusercontent.com/Eatapples15/safe-and-sound-media/main/...`.
