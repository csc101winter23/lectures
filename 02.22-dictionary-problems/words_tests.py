import unittest
import words


class TestWords(unittest.TestCase):
    def test01_sanitize_token(self):
        word = words.sanitize_token("Well,")
        self.assertEqual(word, "well")

    def test02_sanitize_string(self):
        string = words.sanitize_string("Well, Prince, so")
        self.assertEqual(string, ["well", "prince", "so"])

    def test03_count_words(self):
        dct = words.count_words(["well", "prince", "so", "well"])
        self.assertEqual(dct, {"well": 2, "prince": 1, "so": 1})


if __name__ == "__main__":
    unittest.main()
