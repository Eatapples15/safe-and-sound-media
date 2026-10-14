#!/usr/bin/env bash
# Prepara l'ambiente per generare grafiche e Reel di Safe & Sound:
# font del brand (da github.com/google/fonts) e verifica di Playwright e ffmpeg.
set -e
mkdir -p ~/.fonts
B=https://raw.githubusercontent.com/google/fonts/main/ofl
for f in "unbounded/Unbounded%5Bwght%5D.ttf" "instrumentsans/InstrumentSans%5Bwdth,wght%5D.ttf" "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"; do
  n=$(basename "$f")
  [ -f ~/.fonts/"$n" ] || curl -sSfL "$B/$f" -o ~/.fonts/"$n"
done
fc-cache -f >/dev/null 2>&1 || true
command -v ffmpeg >/dev/null || echo "ATTENZIONE: ffmpeg non installato"
node -e "require('playwright')" 2>/dev/null || npm i -g playwright >/dev/null 2>&1 || echo "ATTENZIONE: playwright non disponibile"
echo "Ambiente pronto."
