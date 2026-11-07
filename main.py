"""Flag DHCP leases expiring soon or already expired.

Usage: python3 main.py leases.csv [--now 2026-11-04]
CSV columns: host,ip,expiry (ISO date).
EXPIRED before today, EXPIRING SOON within 7 days, otherwise OK.
Soonest expiry first.
"""
import argparse, csv, sys
from datetime import date, timedelta

def audit(rows, now):
    out = []
    for row in rows:
        expiry = date.fromisoformat(row["expiry"].strip())
        if expiry < now:
            verdict = "EXPIRED"
        elif expiry <= now + timedelta(days=7):
            verdict = "EXPIRING SOON"
        else:
            verdict = "OK"
        out.append((row["host"], row["ip"], str(expiry), verdict))
    return sorted(out, key=lambda r: r[2])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--now", default=None)
    args = parser.parse_args(argv)
    now = date.fromisoformat(args.now) if args.now else date.today()
    with open(args.path, newline="", encoding="utf-8") as f:
        for host, ip, expiry, verdict in audit(list(csv.DictReader(f)), now):
            print(f"{host} {ip}: {verdict} (expires {expiry})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
