# Prints M1 OHLC (from BID price) for a few minutes straight from the tick CSV.
import sys, os
from datetime import datetime
PATH = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\RBTG V2\Documents\Data For Trading\Tick_Data\XAUUSD_dukascopy_TICK_UTC.csv"
START = "2023.02.03 13:28:00"   # first minute to print
MINUTES = 5

def ts(line):
    return datetime.strptime(line[:23], "%Y.%m.%d %H:%M:%S.%f")

def first_line_at_or_after(f, size, target):
    lo, hi = 0, size
    while hi - lo > 4096:
        mid = (lo + hi) // 2
        f.seek(mid); f.readline()
        l = f.readline()
        if not l: hi = mid; continue
        try: t = ts(l.decode())
        except Exception: hi = mid; continue
        if t < target: lo = mid
        else: hi = mid
    f.seek(lo); f.readline()
    return f.tell()

t0 = datetime.strptime(START, "%Y.%m.%d %H:%M:%S")
size = os.path.getsize(PATH)
bars = {}
with open(PATH, "rb") as f:
    f.seek(first_line_at_or_after(f, size, t0))
    for raw in f:
        line = raw.decode().strip()
        t = ts(line)
        m = t.replace(second=0, microsecond=0)
        if (m - t0).total_seconds() >= MINUTES * 60: break
        if m < t0: continue
        bid = float(line.split(",")[1])
        b = bars.setdefault(m, [bid, bid, bid, bid])
        b[1] = max(b[1], bid); b[2] = min(b[2], bid); b[3] = bid
print("Minute (UTC)          Open      High      Low       Close   (BID)")
for m, (o, h, l, c) in sorted(bars.items()):
    print(f"{m:%Y.%m.%d %H:%M}  {o:9.3f} {h:9.3f} {l:9.3f} {c:9.3f}")