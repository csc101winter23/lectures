import random
import unittest
import minimum_v1
import minimum_v2


class TestMinElement(unittest.TestCase):
    def test01_v1(self):
        # Passing a single unit test tells us almost nothing -- a function
        #  could pass this test by *always* returning -3.
        lst = [2, -1, 9, 8, 5, -3, 0, 8]
        element = minimum_v1.min_element(lst)
        self.assertEqual(element, -3)

    def test02_v1(self):
        # Passing both of these tests gives us a little more confidence, but
        #  they still don't have 100% coverage...
        lst = [2, -1, 9, 8, 5, 0, 8]
        element = minimum_v1.min_element(lst)
        self.assertEqual(element, -1)

    def test03_v1(self):
        # ...without 100% coverage, we know nothing about whether or not the
        #  uncovered lines are actually correct -- they have never been tested.
        lst = []
        element = minimum_v1.min_element(lst)
        self.assertIsNone(element)

    def test04_v1(self):
        # Note that unit tests and code coverage are only as good as our
        #  ability to identify all possible cases -- coverage can only tell us
        #  if we tested every line we wrote; it cannot tell us if we needed to
        #  write more lines.
        # "Fuzz testing" is the practice of randomly generating inputs, hoping
        #  that we randomly stumble upon additional cases:
        lst = [random.randint(-100, 100) for i in range(100)]
        element = minimum_v1.min_element(lst)

        # Since the input is randomly generated, we don't know what the
        #  correct output ought to be. We have to actively check to see if the
        #  returned value is actually correct.
        # To be correct, the returned value must be less than or equal to all
        #  values in the list:
        for i in range(len(lst)):
            self.assertTrue(element <= lst[i])

    # When comparing two functions that both claim to solve the same problem,
    #  the first question we must ask is whether or not they are both correct.
    #  If one of them is incorrect, it is useless; we will use the other.

    def test05_v2(self):
        lst = [2, -1, 9, 8, 5, -3, 0, 8]
        element = minimum_v2.min_element(lst)
        self.assertEqual(element, -3)

    def test06_v2(self):
        lst = [2, -1, 9, 8, 5, 0, 8]
        element = minimum_v2.min_element(lst)
        self.assertEqual(element, -1)

    def test07_v2(self):
        lst = []
        element = minimum_v2.min_element(lst)
        self.assertIsNone(element)

    def test08_v2(self):
        lst = [random.randint(-100, 100) for i in range(100)]
        element = minimum_v2.min_element(lst)

        for i in range(len(lst)):
            self.assertTrue(element <= lst[i])

if __name__ == "__main__":
    unittest.main()
