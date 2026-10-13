"""Scarica l'ultimo Bollettino di criticità DPC e salva rischio/allerte.json (zona -> livelli oggi/domani).
Fonte: github.com/pcm-dpc/DPC-Bollettini-Criticita-Idrogeologica-Idraulica (CC-BY 4.0)."""
import json, os, re, sys, urllib.request

REPO = "pcm-dpc/DPC-Bollettini-Criticita-Idrogeologica-Idraulica"
RAW = f"https://raw.githubusercontent.com/{REPO}/master/"
API = f"https://api.github.com/repos/{REPO}"
OUT = os.path.join(os.path.dirname(__file__), "..", "rischio", "allerte.json")

def get(url, api=False):
    req = urllib.request.Request(url, headers={"User-Agent": "safe-and-sound"})
    tok = os.environ.get("GITHUB_TOKEN")
    if api and tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def ultimo_bollettino():
    commits = get(f"{API}/commits?path=files&per_page=5", api=True)
    for c in commits:
        det = get(f"{API}/commits/{c['sha']}", api=True)
        for f in det.get("files", []):
            m = re.match(r"files/(\d{8}_\d{4})\.json$", f["filename"])
            if m:
                return m.group(1)
    raise SystemExit("Bollettino non trovato")

def livello(testo):
    t = (testo or "").upper()
    if "ROSSA" in t: return 3
    if "ARANCIONE" in t: return 2
    if "GIALLA" in t: return 1
    return 0

def zone_da_topojson(url):
    d = get(url)
    out = {}
    for obj in d["objects"].values():
        for g in obj.get("geometries", []):
            p = g.get("properties", {})
            nome = p.get("Nome zona")
            if not nome: continue
            out[nome] = {
                "l": livello(p.get("Rappresentata nella mappa")),
                "idraulico": livello(p.get("Per rischio idraulico")),
                "idrogeologico": livello(p.get("Per rischio idrogeologico")),
                "temporali": livello(p.get("Per rischio temporali")),
            }
    return out

def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else ultimo_bollettino()
    b = get(f"{RAW}files/{nome}.json")
    res = {
        "bollettino": b.get("name"),
        "emesso": b.get("date"),
        "id": nome,
        "oggi": zone_da_topojson(b["today"]["topo_json"]),
        "domani": zone_da_topojson(b["tomorrow"]["topo_json"]),
        "fonte": "Dipartimento della Protezione Civile, Bollettino di criticità nazionale (CC-BY 4.0)",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, separators=(",", ":"))
    print(res["bollettino"], len(res["oggi"]), "zone")

if __name__ == "__main__":
    main()
