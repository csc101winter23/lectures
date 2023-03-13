import unittest
import minimum_v1


class TestMinElement(unittest.TestCase):
    def test01_v1(self):
        lst = [2, -1, 9, 8, 5, -3, 0, 8]
        element = minimum_v1.min_element(lst)
        self.assertEqual(element, -3)


if __name__ == "__main__":
    unittest.main()
