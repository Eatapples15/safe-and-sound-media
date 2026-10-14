#!/usr/bin/env python3
"""Settimana sismica: scarica dal servizio FDSN dell'INGV i terremoti della settimana
precedente (lunedì–domenica) in Italia e zone limitrofe e prepara dati e didascalia
per il Reel del lunedì. Uscite: strumenti/sismica/dati.js e sismica/AAAA-MM-GG/didascalia.txt
"""
import datetime as dt, json, os, sys, urllib.request, urllib.parse

MESI = ["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"]
CANZONI = ["Il mondo · Jimmy Fontana", "Che sarà · Ricchi e Poveri", "Terra promessa · Eros Ramazzotti", "Gli anni · 883"]

oggi = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today()
lun = oggi - dt.timedelta(days=oggi.weekday() + 7)   # lunedì della settimana precedente
dom = lun + dt.timedelta(days=6)
q = {"starttime": f"{lun}T00:00:00", "endtime": f"{dom}T23:59:59", "minlat": 35.5, "maxlat": 47.3,
     "minlon": 6, "maxlon": 19, "format": "text", "limit": 20000}
url = "https://webservices.ingv.it/fdsnws/event/1/query?" + urllib.parse.urlencode(q)
righe = urllib.request.urlopen(url, timeout=60).read().decode("utf-8").strip().splitlines()
ev = []
for r in righe:
    if r.startswith("#") or not r.strip():
        continue
    c = r.split("|")
    try:
        ev.append({"t": c[1][:19], "lat": float(c[2]), "lon": float(c[3]), "z": float(c[4]), "m": float(c[10]), "luogo": c[12].replace(" [Mare]", " (in mare)").replace("[Mare]", "(in mare)").strip()})
    except (ValueError, IndexError):
        continue
ev.sort(key=lambda e: e["t"])
if not ev:
    sys.exit("Nessun evento scaricato")
top = max(ev, key=lambda e: e["m"])
sotto = sum(1 for e in ev if e["m"] < 2.5)
pct = round(100 * sotto / len(ev))
m3 = sum(1 for e in ev if e["m"] >= 3)
def gm(d): return f"{d.day} {MESI[d.month-1]}"
def il(d): return ("l'" if d.day in (1, 8, 11) else "il ") + gm(d)
periodo = f"{lun.day}–{gm(dom)}" if lun.month == dom.month else f"{gm(lun)} – {gm(dom)}"
td = dt.date.fromisoformat(top["t"][:10])
canzone = CANZONI[lun.isocalendar()[1] % len(CANZONI)]
mag = lambda x: f"{x:.1f}".replace(".", ",")
dati = {"periodo": periodo, "n": len(ev), "pct_sotto": pct, "m3": m3,
        "top": {"m": mag(top["m"]), "luogo": top["luogo"], "giorno": gm(td), "z": round(top["z"])},
        "canzone": canzone, "ev": [[round(e["lat"], 3), round(e["lon"], 3), round(e["m"], 1)] for e in ev]}
open("strumenti/sismica/dati.js", "w").write("window.DATI=" + json.dumps(dati, ensure_ascii=False) + ";")
out = f"sismica/{oggi}"
os.makedirs(out, exist_ok=True)
json.dump(dati, open(f"{out}/dati.json", "w"), ensure_ascii=False)
cap = f"""{len(ev)} terremoti in 7 giorni in Italia e zone vicine. Ne hai sentito qualcuno? Probabilmente no.

Settimana sismica {periodo}: il {pct}% ha avuto magnitudo sotto 2,5, in genere troppo debole per essere avvertito. Il più forte: magnitudo {mag(top['m'])}, {top['luogo']}, {il(td)}, a {round(top['z'])} km di profondità.

L'Italia trema ogni giorno: per questo conviene sapere cosa fare prima, durante e dopo. Salvalo e cerca la zona sismica del tuo Comune (link in bio).

🎧 {canzone}
Fonte: INGV, Istituto Nazionale di Geofisica e Vulcanologia (dati preliminari).
Segui @safe_and_sound_it: la sicurezza a tempo di musica.

#SafeAndSound #SettimanaSismica #Terremoto #INGV"""
open(f"{out}/didascalia.txt", "w").write(cap)
print(json.dumps({k: v for k, v in dati.items() if k != "ev"}, ensure_ascii=False))
