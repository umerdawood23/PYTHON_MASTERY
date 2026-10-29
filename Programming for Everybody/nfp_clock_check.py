"""
Phase 0, step 1: find out which clock a tick CSV uses.  Standard library only.

Usage (Windows Command Prompt):
    python nfp_clock_check.py
    python nfp_clock_check.py "C:\\path\\to\\ticks.csv"

It jumps straight to the dates it needs (binary search on the file), so it
finishes in seconds to a few minutes even on a very large file. Nothing is
modified. Paste the printed report back into the chat.
"""
import os
import sys
from datetime import datetime, timedelta

DEFAULT = r"C:\Users\RBTG V2\Documents\Data For Trading\Tick_Data\XAUUSD_dukascopy_TICK_UTC.csv"
PATH = sys.argv[1] if len(sys.argv) > 1 else DEFAULT

# US jobs-report days in 2023 (released 08:30 New York time) and the UTC time that implies.
# US daylight saving ran 12 Mar to 5 Nov 2023, so 3 Nov is still summer time.
NFP = [("2023-01-06", "13:30"), ("2023-02-03", "13:30"), ("2023-03-10", "13:30"),
       ("2023-04-07", "12:30"), ("2023-05-05", "12:30"), ("2023-06-02", "12:30"),
       ("2023-07-07", "12:30"), ("2023-08-04", "12:30"), ("2023-09-01", "12:30"),
       ("2023-10-06", "12:30"), ("2023-11-03", "12:30"), ("2023-12-08", "13:30")]
# Ordinary Tuesdays used to find the daily market break
GAP_DAYS = [("2023-01-17", "winter"), ("2023-07-18", "summer")]


def parse_ts(tok):
    """Timestamp text or epoch number -> naive datetime, taken as written."""
    tok = tok.strip().strip('"').strip()
    if not tok:
        raise ValueError("empty")
    try:
        v = float(tok)
    except ValueError:
        v = None
    if v is not None:
        if v > 1e17:
            v /= 1e9
        elif v > 1e14:
            v /= 1e6
        elif v > 1e11:
            v /= 1e3
        return datetime(1970, 1, 1) + timedelta(seconds=v)
    t = tok.replace("T", " ").replace("Z", "").replace(" UTC", "").replace(" GMT", "")
    if len(t) > 11 and "+" in t[11:]:
        t = t[:11 + t[11:].index("+")]
    if len(t) >= 10 and t[4] in ".-/" and t[7] in ".-/":
        t = t[:4] + "-" + t[5:7] + "-" + t[8:]
    base, _, frac = t.strip().partition(".")
    dt = datetime.strptime(base.strip(), "%Y-%m-%d %H:%M:%S")
    if frac:
        dt = dt.replace(microsecond=int((frac + "000000")[:6]))
    return dt


def dec(b):
    return b.decode("utf-8", "replace").rstrip("\r\n")


# ---------------------------------------------------------------- peek
size = os.path.getsize(PATH)
with open(PATH, "rb") as f:
    first_lines = [dec(f.readline()) for _ in range(4)]
    f.seek(max(0, size - 4000))
    tail_lines = [dec(x) for x in f.read().splitlines()[-2:]]

line1 = first_lines[0]
delim = max([",", ";", "\t"], key=lambda d: line1.count(d))
header = False
try:
    parse_ts(line1.split(delim)[0])
except Exception:
    header = True
names = [n.strip().strip('"').lower() for n in line1.split(delim)] if header else []
sample = first_lines[1] if header else first_lines[0]
sample_parts = sample.split(delim)

if header:
    price_idx = [i for i, n in enumerate(names)
                 if ("bid" in n or "ask" in n or n in ("price", "last", "mid", "close"))
                 and "vol" not in n and "size" not in n]
else:
    price_idx = []
    for i in (1, 2):
        try:
            float(sample_parts[i])
            price_idx.append(i)
        except (ValueError, IndexError):
            pass
if not price_idx:
    price_idx = [1]

with open(PATH, "rb") as f:
    if header:
        f.readline()
    data_start = f.tell()

print("=" * 70)
print("FILE   :", PATH)
print("SIZE   : %.2f GB" % (size / 1e9))
print("HEADER :", line1 if header else "(none)")
print("FIRST  :", first_lines[1] if header else first_lines[0])
print("LAST   :", tail_lines[-1])
print("DELIM  : %r   price columns used: %s" % (delim, price_idx))
try:
    t_first = parse_ts(sample_parts[0])
    t_last = parse_ts(tail_lines[-1].split(delim)[0])
    print("RANGE  : %s  ->  %s   (as written in the file)" % (t_first, t_last))
    if t_first > t_last:
        print("WARNING: file looks sorted newest-first; this script needs oldest-first.")
except Exception as e:
    print("Could not parse first/last timestamp:", e)
    sys.exit(1)


# ---------------------------------------------------------------- random access
def line_ts(f, offset):
    f.seek(offset)
    if offset > data_start:
        f.readline()                      # drop the partial line
    while True:
        raw = f.readline()
        if not raw:
            return None
        try:
            return parse_ts(dec(raw).split(delim)[0])
        except Exception:
            continue


def find_offset(f, target):
    lo, hi = data_start, size
    while hi - lo > 8192:
        mid = (lo + hi) // 2
        ts = line_ts(f, mid)
        if ts is None or ts >= target:
            hi = mid
        else:
            lo = mid
    return lo


def read_window(f, start, end):
    """List of (timestamp, price) for start <= ts < end."""
    lo = find_offset(f, start)
    f.seek(lo)
    if lo > data_start:
        f.readline()
    out = []
    for raw in f:
        parts = dec(raw).split(delim)
        try:
            ts = parse_ts(parts[0])
        except Exception:
            continue
        if ts < start:
            continue
        if ts >= end:
            break
        try:
            px = [float(parts[i]) for i in price_idx if i < len(parts)]
        except ValueError:
            continue
        if px:
            out.append((ts, sum(px) / len(px)))
    return out


def day(s):
    return datetime.strptime(s, "%Y-%m-%d")


# ---------------------------------------------------------------- test 1: jobs-report spike
print("=" * 70)
print("TEST 1  Biggest one-minute move between 09:00 and 18:00 on jobs-report days")
print("        (expected UTC time shown; 'shift' = observed minus expected)")
print("-" * 70)
shifts = []
observed = []
with open(PATH, "rb") as f:
    for d, exp in NFP:
        rows = read_window(f, day(d) + timedelta(hours=9), day(d) + timedelta(hours=18))
        if not rows:
            print("%s  no ticks found in window" % d)
            continue
        mins = {}
        for ts, px in rows:
            k = ts.replace(second=0, microsecond=0)
            if k in mins:
                if px > mins[k][0]:
                    mins[k][0] = px
                if px < mins[k][1]:
                    mins[k][1] = px
            else:
                mins[k] = [px, px]
        ranked = sorted(mins.items(), key=lambda kv: kv[1][0] - kv[1][1], reverse=True)
        best = ranked[0][0]
        eh, em = map(int, exp.split(":"))
        shift = (best.hour * 60 + best.minute) - (eh * 60 + em)
        shifts.append(shift)
        observed.append(best.strftime("%H:%M"))
        top3 = ", ".join("%s (%.2f)" % (k.strftime("%H:%M"), v[0] - v[1]) for k, v in ranked[:3])
        print("%s  expected %s UTC | biggest %s | shift %+d min | top3: %s"
              % (d, exp, best.strftime("%H:%M"), shift, top3))

if shifts:
    shifts_sorted = sorted(shifts)
    med = shifts_sorted[len(shifts_sorted) // 2]
    near = sum(1 for s in shifts if abs(s - med) <= 5)
    print("-" * 70)
    print("Median shift: %+d min; %d of %d dates agree with it within 5 min." % (med, near, len(shifts)))
    if abs(med) <= 5 and near >= len(shifts) * 0.7:
        print("=> The file clock matches UTC (including the winter/summer change).")
    elif len(set(observed)) == 1:
        print("=> The spike sits at the SAME clock time (%s) in winter and summer: this is a"
              % observed[0])
        print("   broker-style clock tied to New York time (e.g. GMT+2 winter / GMT+3 summer),")
        print("   not UTC. Send me this whole report.")
    else:
        print("=> The file clock does NOT match UTC. Send me this whole report.")

# ---------------------------------------------------------------- test 2: daily market break
print("=" * 70)
print("TEST 2  Longest quiet gap in the ticks, Tuesday 18:00 to Wednesday 03:00")
print("        (gold's daily break follows New York time, so in a UTC file it")
print("         moves by one hour between winter and summer)")
print("-" * 70)
with open(PATH, "rb") as f:
    for d, season in GAP_DAYS:
        rows = read_window(f, day(d) + timedelta(hours=18), day(d) + timedelta(hours=27))
        if len(rows) < 2:
            print("%s (%s): not enough ticks" % (d, season))
            continue
        gap, g0, g1 = timedelta(0), None, None
        for (t0, _), (t1, _) in zip(rows, rows[1:]):
            if t1 - t0 > gap:
                gap, g0, g1 = t1 - t0, t0, t1
        print("%s (%s): longest gap %s -> %s  (%.0f min)"
              % (d, season, g0.strftime("%d %H:%M:%S"), g1.strftime("%d %H:%M:%S"), gap.total_seconds() / 60))
print("=" * 70)
print("Done. Copy everything above and paste it into the chat.")