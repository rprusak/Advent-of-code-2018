import unittest
from main import contains_exactly_count_of_any_letter
from main import calculate_checksum
from main import get_different_letters_count
from main import get_common_part_of_words
from main import get_common_id

class MyTestCase(unittest.TestCase):

    def test_contains_exactly_two_of_any_letter(self):
        self.assertFalse(contains_exactly_count_of_any_letter("abcdef", 2))
        self.assertTrue(contains_exactly_count_of_any_letter("bababc", 2))
        self.assertTrue(contains_exactly_count_of_any_letter("abbcde", 2))
        self.assertFalse(contains_exactly_count_of_any_letter("abcccd", 2))
        self.assertTrue(contains_exactly_count_of_any_letter("aabcdd", 2))
        self.assertTrue(contains_exactly_count_of_any_letter("abcdee", 2))
        self.assertFalse(contains_exactly_count_of_any_letter("ababab", 2))

    def test_contains_exactly_three_of_any_letter(self):
        self.assertFalse(contains_exactly_count_of_any_letter("abcdef", 3))
        self.assertTrue(contains_exactly_count_of_any_letter("bababc", 3))
        self.assertFalse(contains_exactly_count_of_any_letter("abbcde", 3))
        self.assertTrue(contains_exactly_count_of_any_letter("abcccd", 3))
        self.assertFalse(contains_exactly_count_of_any_letter("aabcdd", 3))
        self.assertFalse(contains_exactly_count_of_any_letter("abcdee", 3))
        self.assertTrue(contains_exactly_count_of_any_letter("ababab", 3))

    def test_calculate_checksum(self):
        self.assertEqual(calculate_checksum(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]), 12)

    def test_get_different_letters_count(self):
        self.assertEqual(get_different_letters_count("abcde", "axcye"), 2)
        self.assertEqual(get_different_letters_count("fghij", "fguij"), 1)

    def test_get_common_part_of_words(self):
        self.assertEqual(get_common_part_of_words("fghij", "fguij"), "fgij")

    def test_get_common_id(self):
        self.assertEqual(get_common_id(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]), "fgij")


if __name__ == '__main__':
    unittest.main()

