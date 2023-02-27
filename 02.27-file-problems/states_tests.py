import states
import unittest
import os


class TestStates(unittest.TestCase):
    def test01_parse_row(self):
        regions = {}
        row = "California,West,39538223"
        states.parse_row(row, regions)
        self.assertEqual(regions, {"West": [39538223, 1]})

    def test02_parse_row(self):
        regions = {"West": [39538223, 1]}
        row = "New York,Northeast,20201249"
        states.parse_row(row, regions)
        self.assertEqual(regions, {"West": [39538223, 1], "Northeast": [20201249, 1]})

    def test03_parse_row(self):
        regions = {"West": [39538223, 1], "Northeast": [20201249, 1]}
        row = "Hawaii,West,1455271"
        states.parse_row(row, regions)
        row = "Washington,West,7705281"
        states.parse_row(row, regions)
        self.assertEqual(regions, {"West": [48698775, 3], "Northeast": [20201249, 1]})

    def test04_parse_csv(self):
        # Since files are stored on disk, they persist after a program
        #  terminates -- we need to make sure that this test doesn't
        #  inadvertently use a file left over from a previous test, so we
        #  need to remake the file from scratch.
        with open("example.csv", "w") as csv_file:
            csv_file.write("State,Region,Population\n")
            csv_file.write("California,West,39538223\n")
            csv_file.write("Hawaii,West,1455271\n")
            csv_file.write("New York,Northeast,20201249\n")
            csv_file.write("Washington,West,7705281\n")

        regions = states.parse_csv("example.csv")
        self.assertEqual(regions, {"West": [48698775, 3], "Northeast": [20201249, 1]})

        # We should also remove test files that we no longer need, just so
        #  that we're not cluttering up the file system with useless data.
        os.remove("example.csv")


if __name__ == "__main__":
    unittest.main()
