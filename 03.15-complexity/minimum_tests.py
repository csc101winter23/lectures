import random
import unittest
import minimum_v1
import minimum_v2


class TestMinElement(unittest.TestCase):
    def test01_small(self):
        lst = [random.randint(-100, 100) for i in range(100)]

        element = minimum_v1.min_element(lst)
        # element = minimum_v2.min_element(lst)

        for i in range(len(lst)):
            self.assertTrue(element <= lst[i])


if __name__ == "__main__":
    unittest.main()
