import unittest
import firing_table


class TestFiringTable(unittest.TestCase):
    def test01_time_of_flight(self):
        time = firing_table.time_of_flight(50)
        self.assertAlmostEqual(time, 3.1927543)

    def test02_time_of_flight(self):
        time = firing_table.time_of_flight(0)
        self.assertAlmostEqual(time, 0.0000000)

    def test03_range_of_shot(self):
        shot = firing_table.range_of_shot(3.19, 55)
        self.assertAlmostEqual(shot, 175.4500000)

    def test04_range_of_shot(self):
        shot = firing_table.range_of_shot(0, 0)
        self.assertAlmostEqual(shot, 0.0000000)

    def test05_is_hit(self):
        hit = firing_table.is_hit(175.45, 160, 25)
        self.assertTrue(hit)

    def test06_is_hit(self):
        hit = firing_table.is_hit(0.0, 160, 25)
        self.assertFalse(hit)


if __name__ == "__main__":
    unittest.main()
