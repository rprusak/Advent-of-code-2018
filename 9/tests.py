import unittest
from main import calculate_winner_score


class MyTestCase(unittest.TestCase):
    def test_calculate_winner_score(self):
        self.assertEqual(calculate_winner_score(9, 25), 32)
        self.assertEqual(calculate_winner_score(1, 48), 95)
        self.assertEqual(calculate_winner_score(9, 48), 63)
        self.assertEqual(calculate_winner_score(10, 1618), 8317)


if __name__ == '__main__':
    unittest.main()
