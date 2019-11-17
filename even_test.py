import unittest

from even import Even

class TestingMyCode(unittest.TestCase):

    def test_odds(self):
        self.assertFalse(Even(1).is_even())
        self.assertFalse(Even(3).is_even())

    def test_evens(self):
        self.assertTrue(Even(0).is_even())
        self.assertTrue(Even(2).is_even())

if __name__ == '__main__':
    unittest.main()
