import unittest
from main import perform_reaction
from main import is_reaction_between_units
from main import calculate_improved_polymer_length

class MyTestCase(unittest.TestCase):

    def test_perform_reaction(self):
        new_polymer = perform_reaction("dabAcCaCBAcCcaDA")
        self.assertEqual(new_polymer, "dabCBAcaDA")

    def test_is_reaction_between_units(self):
        self.assertEqual(is_reaction_between_units("a", "A"), True)
        self.assertEqual(is_reaction_between_units("A", "a"), True)
        self.assertEqual(is_reaction_between_units("a", "a"), False)
        self.assertEqual(is_reaction_between_units("b", "a"), False)
        self.assertEqual(is_reaction_between_units("B", "a"), False)
        self.assertEqual(is_reaction_between_units("B", "A"), False)
        self.assertEqual(is_reaction_between_units("b", "A"), False)

    def test_improve_polymer(self):
        self.assertEqual(calculate_improved_polymer_length("dabAcCaCBAcCcaDA"), 4)

if __name__ == '__main__':
    unittest.main()