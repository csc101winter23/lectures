import unittest
import firing_table


class TestFiringTable(unittest.TestCase):
    def test01_time_of_flight(self):
        time = firing_table.time_of_flight(50)
        self.assertAlmostEqual(time, 3.1927543)


if __name__ == "__main__":
    unittest.main()
