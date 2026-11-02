# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from ChildcareTime import add_entry, read_entries

class ChildcareTests(unittest.TestCase):
    def test_add_and_backup(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "work.xml"
            path.write_text("<root/>")
            add_entry(path, "Sam", "2026-11-02", "2.5", "Test note")
            self.assertEqual(read_entries(path)[0]["hours"], "2.5")
            self.assertEqual(len(list(Path(folder).glob("*.bak"))), 1)
    def test_invalid_input_no_change(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "work.xml"
            path.write_text("<root/>")
            for person, day, hours in (("Unknown", "2026-11-02", "2"), ("Sam", "bad", "2"), ("Sam", "2026-11-02", "-1")):
                with self.assertRaises(ValueError):
                    add_entry(path, person, day, hours, "")
            self.assertEqual(path.read_text(), "<root/>")

if __name__ == "__main__":
    unittest.main()
