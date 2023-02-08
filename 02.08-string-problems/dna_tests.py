import unittest
import dna


class TestDNA(unittest.TestCase):
    def test01_check_string(self):
        valid = dna.check_string("GTA")
        self.assertTrue(valid)

    def test02_check_string(self):
        valid = dna.check_string("FAT")
        self.assertFalse(valid)

    def test03_check_string(self):
        valid = dna.check_string("")
        self.assertFalse(valid)

    def test04_check_strands(self):
        pair = dna.check_strands("GTA", "CAT")
        self.assertIsNone(pair)

    def test05_check_strands(self):
        pair = dna.check_strands("GTA", "GTA")
        self.assertEqual(pair, ("G", "G"))

    def test06_check_bases(self):
        result = dna.check_bases("G", "C")
        self.assertTrue(result)

    def test07_check_bases(self):
        result = dna.check_bases("G", "G")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
