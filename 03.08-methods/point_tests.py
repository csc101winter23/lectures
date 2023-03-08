import unittest
import point


class TestPoint(unittest.TestCase):
    def test01_init(self):
        pt = point.Point(3, 4)
        self.assertEqual(pt.x, 3)
        self.assertEqual(pt.y, 4)

    def test02_eq(self):
        pt = point.Point(3, 4)
        self.assertEqual(pt, point.Point(3, 4))
        self.assertNotEqual(pt, point.Point(4, 3))
        self.assertNotEqual(pt, "Point(3, 4)")

    def test03_repr(self):
        pt = point.Point(3, 4)
        self.assertEqual(str(pt), "Point(3, 4)")

    def test04_add(self):
        pt1 = point.Point(5, 4)
        pt2 = point.Point(3, 4)
        pt3 = pt1 + pt2

        self.assertEqual(pt3.x, 8)
        self.assertEqual(pt3.y, 8)

        with self.assertRaises(TypeError):
            pt3 = pt1 + 5

    def test05_translate(self):
        pt = point.Point(3, 4)

        # Methods are accessed using ".", just like attributes:
        pt.translate(1, 2)
        self.assertEqual(pt.x, 4)
        self.assertEqual(pt.y, 6)

        # Ordinary functions will have to be passed the object in question:
        point.translate(pt, 1, 2)
        self.assertEqual(pt.x, 5)
        self.assertEqual(pt.y, 8)

if __name__ == "__main__":
    unittest.main()
