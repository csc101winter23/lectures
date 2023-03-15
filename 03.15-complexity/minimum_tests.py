import random
import unittest
import minimum_v1
import minimum_v2


class TestMinElement(unittest.TestCase):
    def test01_small(self):
        # This test is so small that the running time doesn't really tell us
        #  anything -- it's so small that *any* function will probably finish
        #  almost instantaneously:
        lst = [random.randint(-100, 100) for i in range(100)]

        # minimum_v1 finished practically instantaneously:
        element = minimum_v1.min_element(lst)
        # minimum_v2 also finished practically instantaneously:
        element = minimum_v2.min_element(lst)

        for i in range(len(lst)):
            self.assertTrue(element <= lst[i])

    def test02_large(self):
        lst = [random.randint(-1000000, 1000000) for i in range(1000000)]

        # minimum_v1 finished in about:
        #  1000 element, 0.002s
        #  10000 elements, 0.016s
        #  100000 elements, 0.125s
        #  1000000 elements, 1.308s
        element = minimum_v1.min_element(lst)
        # minimum_v2 finished in about:
        #  1000 element, 0.002s
        #  10000 elements, 0.013s
        #  100000 elements, 0.125s
        #  1000000 elements, 1.254s
        element = minimum_v2.min_element(lst)

        for i in range(len(lst)):
            self.assertTrue(element <= lst[i])

    def test03_best(self):
        # The best case scenario is that the minimum element is the first
        #  element we try:
        lst = list(range(10000))

        # minimum_v1 finished in about:
        #  10000 element, 0.001s
        element = minimum_v1.min_element(lst)
        # minimum_v2 finished in about:
        #  10000 element, 0.001s
        element = minimum_v2.min_element(lst)

    def test04_worse(self):
        # The worst case scenario is that the minimum element is the last
        #  element we try:
        lst = list(range(25000, -1, -1))

        # minimum_v1 finished in about:
        #  10000 element, 1.437s
        #  25000 element, 8.915s
        element = minimum_v1.min_element(lst)
        # minimum_v2 finished in about:
        #  10000 element, 0.001s
        #  25000 element, 0.003s
        element = minimum_v2.min_element(lst)


if __name__ == "__main__":
    unittest.main()
