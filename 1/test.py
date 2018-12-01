import unittest
from main import get_duplicated_frequency

class MyTestCase(unittest.TestCase):

    def test_get_duplicated_frequency_returns_valid_value(self):
        self.assertEqual(get_duplicated_frequency([+1, -1]), 0)
        self.assertEqual(get_duplicated_frequency([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(get_duplicated_frequency([-6, +3, +8, +5, -6]), 5)
        self.assertEqual(get_duplicated_frequency([+7, +7, -2, -7, -4]), 14)

if __name__ == '__main__':
    unittest.main()
