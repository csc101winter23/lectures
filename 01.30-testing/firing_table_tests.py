# The Python standard library includes the "unittest" module for defining
#  unit tests:
import unittest
import firing_table


class TestFiringTable(unittest.TestCase):
    # Each test case must be a function inside the above class, and that
    #  function's name must begin with "test":
    def test01_time_of_flight(self):
        # To call just one of our functions:
        time = firing_table.time_of_flight(50)
        # To test that function's return value:
        self.assertAlmostEqual(time, 3.1927543)
        # Note that floating point numbers are inherently imprecise; by
        #  default, the unittest module will check for equality to the
        #  seventh decimal place.

    # The name doesn't actually matter to the unittest module, but it will be
    #  shown if the test fails; it's good practice to pick a meaningful name:
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


# To run all of the tests in this file:
if __name__ == "__main__":
    unittest.main()
