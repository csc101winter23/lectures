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
        self.assertEqual(element, 0)

    def test04_scale_list(self):
        lst = [2, -1, 9, 8, 5, -3, 0, 8]
        
        # Note that this passes to "scale_list" a reference to the same list
        #  defined above -- the function will modify that list, and those
        #  modifications will be reflected in "lst".
        lists.scale_list(lst, 2)

        # There is no need to assign the result of "scale_list" to a new
        #  variable; we can simply check the new contents of the existing
        #  variable.
        self.assertEqual(lst, [4, -2, 18, 16, 10, -6, 0, 16])

    def test05_scale_copy(self):
        lst = [2, -1, 9, 8, 5, -3, 0, 8]

        # Note that "scale_copy" will create and return a new list -- it will
        #  not modify "lst", and if we want to see the new list, we need to
        #  assign it to a variable:.
        lst2 = lists.scale_copy(lst, 2)
        self.assertEqual(lst2, [4, -2, 18, 16, 10, -6, 0, 16])

if __name__ == "__main__":
    unittest.main()
