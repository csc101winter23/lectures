import unittest
import ttt


class TestTicTacToe(unittest.TestCase):
    def test01_check_row(self):
        grid = [["O",  None,  "X"],
                ["O",   "X", None],
                [None, None,  "X"]]

        self.assertFalse(ttt.check_row("O", grid))
        self.assertFalse(ttt.check_row("X", grid))

    def test02_check_row(self):
        grid = [["O",  None, None],
                ["O",  None, None],
                ["X",   "X",  "X"]]

        self.assertFalse(ttt.check_row("O", grid))
        self.assertTrue(ttt.check_row("X", grid))

    def test03_check_column(self):
        grid = [["O",  None,  "X"],
                ["O",   "X", None],
                [None, None,  "X"]]

        self.assertFalse(ttt.check_column("O", grid))
        self.assertFalse(ttt.check_column("X", grid))

    def test04_check_column(self):
        grid = [["X",  None, None],
                ["X",  None, None],
                ["X",   "O",  "O"]]

        self.assertFalse(ttt.check_column("O", grid))
        self.assertTrue(ttt.check_column("X", grid))

    def test05_check_diagonal(self):
        grid = [["O",  None,  "X"],
                ["O",   "X", None],
                [None, None,  "X"]]

        self.assertFalse(ttt.check_diagonal("O", grid))
        self.assertFalse(ttt.check_diagonal("X", grid))

    def test06_check_diagonal(self):
        grid = [[None, None,  "X"],
                [None,  "X", None],
                ["X",   "O",  "O"]]

        self.assertFalse(ttt.check_diagonal("O", grid))
        self.assertTrue(ttt.check_diagonal("X", grid))


if __name__ == "__main__":
    unittest.main()
