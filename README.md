# dhcp-lease-auditor

Audit DHCP leases: expired, expiring within 7 days, or OK — soonest expiry first, so no workstation silently loses its address.

## How to run

```sh
python3 main.py leases.csv --now 2026-11-04
```

## Example output

```
PC-07 10.0.0.5: EXPIRING SOON (expires 2026-11-08)
PC-09 10.0.0.9: OK (expires 2026-12-01)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
