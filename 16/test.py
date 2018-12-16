import unittest
from main import calculate_matching_commands_count


class MyTestCase(unittest.TestCase):
    def test_calculate_matching_commands_count(self):
        before = "Before: [3, 2, 1, 1]"
        opcode = "9 2 1 2"
        after = "After:  [3, 2, 2, 1]"
        self.assertEqual(calculate_matching_commands_count(before, opcode, after), 3)

if __name__ == '__main__':
    unittest.main()
