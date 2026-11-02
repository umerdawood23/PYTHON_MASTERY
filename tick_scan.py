# Phase 0, step 4: scan the tick CSV for damage. Needs: pip install pandas
import sys, time, heapq
import numpy as np, pandas as pd
PATH = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\RBTG V2\Documents\Data For Trading\Tick_Data\XAUUSD_dukascopy_TICK_UTC.csv"
CHUNK = int(sys.argv[2]) if len(sys.argv)>2 else 5_000_000
FMT = "%Y.%m.%d %H:%M:%S.%f"
yrs = {}      # year -> dict of counters
gaps, jumps = [], []   # jumps: heap of (size, time, from, to)
prev = None; t0 = time.time(); rows = 0
def Y(y):
    return yrs.setdefault(y, dict(n=0, sp_sum=0.0, wide=0, crossed=0, zero=0, back=0, dup=0, sat=0, badp=0, badt=0, med=[]))
for ch in pd.read_csv(PATH, header=None, usecols=[0, 1, 2], names=["ts", "bid", "ask"],
                      dtype={"ts": str}, chunksize=CHUNK):
    ch["t"] = pd.to_datetime(ch["ts"], format=FMT, errors="coerce")
    if prev is not None:
        ch = pd.concat([prev, ch], ignore_index=True); skip = 1
    else: skip = 0
    prev = ch.iloc[[-1]].copy()
    bad = ch["t"].isna()
    ch["t"] = ch["t"].ffill()
    dt = ch["t"].diff().dt.total_seconds()
    sp = ch["ask"] - ch["bid"]
    same = (dt == 0) & (ch["bid"] == ch["bid"].shift()) & (ch["ask"] == ch["ask"].shift())
    jmp = ch["bid"].diff().abs()
    yr = ch["t"].dt.year
    for y, idx in ch.groupby(yr).indices.items():
        idx = idx[idx >= skip]
        if len(idx) == 0: continue
        d = Y(int(y)); s = sp.values[idx]
        d["n"] += len(idx); d["sp_sum"] += float(np.nansum(s)); d["wide"] += int((s > 1.0).sum())
        d["crossed"] += int((s < 0).sum()); d["zero"] += int((s == 0).sum())
        d["back"] += int((dt.values[idx] < 0).sum()); d["dup"] += int(same.values[idx].sum())
        d["sat"] += int((ch["t"].dt.dayofweek.values[idx] == 5).sum())
        d["badp"] += int(((ch["bid"].values[idx] < 100) | (ch["bid"].values[idx] > 10000)).sum())
        d["badt"] += int(bad.values[idx].sum()); d["med"].append(float(np.nanmedian(s)))
    g = ch.index[(dt > 90 * 60) & (dt < 2000 * 60) & (ch.index >= skip)]
    for i in g: gaps.append((dt[i] / 60, str(ch["t"][i - 1]), str(ch["t"][i])))
    for i in jmp.nlargest(10).index:
        if i >= skip: heapq.heappush(jumps, (float(jmp[i]), str(ch["t"][i]), float(ch["bid"][i - 1]), float(ch["bid"][i])))
    jumps = heapq.nlargest(15, jumps); heapq.heapify(jumps)
    rows += len(ch) - skip
    print(f"  ...{rows/1e6:.0f}M ticks, up to {ch['t'].iloc[-1]}, {time.time()-t0:.0f}s", flush=True)
print("\nYEAR  ticks(M)  medSpread  avgSpread  >$1(%)  crossed  zeroSpr  backwards  dupes  Sat  badPrice  badTime")
for y in sorted(yrs):
    d = yrs[y]
    print(f"{y}  {d['n']/1e6:8.2f}  {np.median(d['med']):9.3f}  {d['sp_sum']/d['n']:9.3f}  {100*d['wide']/d['n']:6.2f}  "
          f"{d['crossed']:7d}  {d['zero']:7d}  {d['back']:9d}  {d['dup']:5d}  {d['sat']:3d}  {d['badp']:8d}  {d['badt']:7d}")
gaps.sort(reverse=True)
print(f"\nGAPS over 90 min on a trading week (excluding weekends): {len(gaps)} total; 20 longest:")
for m, a, b in gaps[:20]: print(f"  {m:7.0f} min   {a}  ->  {b}")
print("\nBIGGEST single-tick BID jumps ($):")
for j in sorted(jumps, reverse=True): print(f"  {j[0]:8.2f}   {j[1]}   {j[2]:.3f} -> {j[3]:.3f}")
print(f"\nDone in {time.time()-t0:.0f}s. Paste everything above (without the '...' progress lines if long).")