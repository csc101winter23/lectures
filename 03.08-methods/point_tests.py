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


if __name__ == "__main__":
    unittest.main()
