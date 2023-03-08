import unittest
import point
import circle


class TestCircle(unittest.TestCase):
    def test01_init(self):
        # To create a Circle, we must first create a Point which we can then
        #  pass to the Circle:
        pt = point.Point(3, 4)
        c = circle.Circle(pt, 1)

        # To access the Point inside a Circle, we can chain together the ".":
        self.assertEqual(c.center.x, 3)
        self.assertEqual(c.center.y, 4)
        self.assertEqual(c.radius, 1)

    def test02_eq(self):
        c1 = circle.Circle(point.Point(3, 4), 1)
        c2 = circle.Circle(point.Point(3, 4), 1)
        c3 = circle.Circle(point.Point(4, 3), 1)

        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)

    def test03_repr(self):
        c1 = circle.Circle(point.Point(3, 4), 1)

        self.assertEqual(str(c1), "Circle(Point(3, 4), 1)")


if __name__ == "__main__":
    unittest.main()
