import unittest


def foo():
    raise ValueError


def bar():
    return None


class TestExceptions(unittest.TestCase):
    def test01_value_error(self):
        # Now that functions raise exceptions, there may be unit tests where
        #  an error is actually the expected behavior:
        with self.assertRaises(ValueError):
            foo()
        # ...the test passes if and only if the expected exception occurs.

    def test02_index_error(self):
        # If a different exception is raised, the test fails:
        with self.assertRaises(IndexError):
            foo()

    def test03_no_error(self):
        # If no exception is raised, the test also fails:
        with self.assertRaises(Exception):
            bar()


if __name__ == "__main__":
    unittest.main()
