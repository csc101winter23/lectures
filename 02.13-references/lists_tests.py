import unittest
import lists


class TestLists(unittest.TestCase):
    def test01_max_element(self):
        lst = [2, -1, 9, 8, 5, -3, 0, 8]
        element = lists.max_element(lst)
        self.assertEqual(element, 9)

    def test02_max_element(self):
        lst = [-1, -1, -1, -1, -1, -1, -1, -1]
        element = lists.max_element(lst)
        self.assertEqual(element, -1)

    def test03_max_element(self):
        lst = [0]
        element = lists.max_element(lst)
        self.assertEqual(element, 2)


if __name__ == "__main__":
    unittest.main()
