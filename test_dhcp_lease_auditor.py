import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import audit

from datetime import date
NOW = date(2026, 11, 4)
def row(h, ip, exp):
    return {"host": h, "ip": ip, "expiry": exp}

class TestDHCP(unittest.TestCase):
    def test_expired(self):
        self.assertEqual(audit([row("H1", "10.0.0.5", "2026-11-01")], NOW)[0][3], "EXPIRED")
    def test_expiring_soon(self):
        self.assertEqual(audit([row("H1", "10.0.0.5", "2026-11-08")], NOW)[0][3], "EXPIRING SOON")
    def test_ok(self):
        self.assertEqual(audit([row("H1", "10.0.0.5", "2026-12-01")], NOW)[0][3], "OK")
    def test_soonest_first(self):
        r = audit([row("B", "10.0.0.6", "2026-12-01"), row("A", "10.0.0.5", "2026-11-02")], NOW)
        self.assertEqual(r[0][0], "A")
