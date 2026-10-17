import json, re

FIX = {"tab": "tape", "tap": "tape", "side": "site", "risah": "risau", "undui": "on the way",
       "outway": "on the way", "sexy": "seksi", "terliu": "terliur", "kelisah": "gelisah", "gelisah": "gelisah", "risau": "gelisah", "beri": "beli", "bag": "beg", "conduit": "on the way", "single": "singgah", "seksi": "seksi", "menja": "", "rebu": "jerebu"}
DROP = {"oh", "dikibayah", "diki-diki", "bukankah", "eh", "hmm", "ah"}


def clean(tok, prev):
    core = re.sub(r"[^\w\-']", "", tok).lower()
    if core in DROP:
        return None
    if core == "hari" and prev == "selamat":
        return "pagi"
    if core in FIX:
        return FIX[core] or None
    return re.sub(r"[.,!?]+$", "", tok)


def load_words(path):
    raw = json.load(open(path))
    out, prev = [], ""
    for w in raw:
        t = clean(w["text"], prev)
        prev = re.sub(r"[^\w]", "", w["text"]).lower()
        if t:
            out.append([t, w["start"], w["end"]])
    return out


def load_segs(path):
    return json.load(open(path))


def tag_span(segs, tag):
    s = [x for x in segs["segments"] if x["tag"] == tag]
    return s[0]["out_in"], s[-1]["out_out"]


def jump_cuts(segs, offset_of=None):
    """Times (in A-roll time) where consecutive cuts come from the same piece."""
    out = []
    ss = segs["segments"]
    for a, b in zip(ss, ss[1:]):
        out.append((b["out_in"], a["piece"] == b["piece"]))
    return out


def find(words, token, after=0.0, before=1e9):
    for w in words:
        if after <= w[1] < before and w[0].lower().strip(".,?!") == token.lower():
            return w[1]
    raise KeyError(f"{token} after {after}")
