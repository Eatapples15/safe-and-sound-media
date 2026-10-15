"""Genera le storie «Accadde oggi» (1080×1920) da dati.json.
Uso: python3 strumenti/accadde-oggi/genera.py [id ...]   (dalla radice del repo)
Uscita: fissi/accadde-oggi/<id>.html e .png"""
import json, os, subprocess, sys
QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(os.path.dirname(QUI))
OUT = os.path.join(RADICE, "fissi", "accadde-oggi")
os.makedirs(OUT, exist_ok=True)
modello = open(os.path.join(QUI, "modello-storia.html"), encoding="utf-8").read()
voci = json.load(open(os.path.join(QUI, "dati.json"), encoding="utf-8"))
scelti = set(sys.argv[1:])
fatti = []
for v in voci:
    if scelti and v["id"] not in scelti:
        continue
    html = modello
    for k in ("data", "titolo", "sotto", "sezione", "fonte"):
        html = html.replace("{{%s}}" % k, v[k])
    html = html.replace("{{punti}}", "".join(f"<li><span>{p}</span></li>" for p in v["punti"]))
    open(os.path.join(OUT, v["id"] + ".html"), "w", encoding="utf-8").write(html)
    fatti.append(v["id"])
js = os.path.join(QUI, "shot.js")
subprocess.run(["node", js, OUT, *fatti], check=True, env={**os.environ, "NODE_PATH": os.environ.get("NODE_PATH", "/opt/npm-tools/node_modules")})
print("\n".join(f"fissi/accadde-oggi/{i}.png" for i in fatti))
