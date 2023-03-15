import unittest
import random
import sort


class TestSelectionSort(unittest.TestCase):
    def test01_small(self):
        lst = [2, -1, 9, 8, 5, -3, 0, 8]
        sorted_lst = sort.selection_sort(lst)
        self.assertEqual(sorted_lst, [-3, -1, 0, 2, 5, 8, 8, 9])

    def test02_large(self):
        lst = [random.randint(-10000, 10000) for i in range(10000)]
        sorted_lst = sort.selection_sort(lst)

        for i in range(len(sorted_lst) - 1):
            self.assertTrue(sorted_lst[i] <= sorted_lst[i + 1])


if __name__ == "__main__":
    unittest.main()
