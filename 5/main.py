import sys
from typing import Set

def perform_reaction(polymer: str) -> str:
    new_polymer = ""
    old_polymer = polymer

    while 1:
        new_polymer = ""
        i = 0
        while i < len(old_polymer):
            if i == (len(old_polymer) - 1):
                new_polymer += old_polymer[i]
                break

            if not is_reaction_between_units(old_polymer[i], old_polymer[i + 1]):
                new_polymer += old_polymer[i]
                i += 1
            else:
                i += 2

        if old_polymer == new_polymer:
            return new_polymer
        else:
            old_polymer = new_polymer

    return new_polymer


def is_reaction_between_units(first_unit: str, second_unit: str) -> bool:
    if first_unit.lower() != second_unit.lower():
        return False

    if (first_unit.islower() and not second_unit.islower()) or (not first_unit.islower() and second_unit.islower()):
        return True

    return False


def calculate_improved_polymer_length(polymer: str) -> int:
    units = get_units_from_polymer(polymer)

    units_results = {}

    print(len(units))

    for unit in units:
        print(unit)
        test_polymer = polymer.replace(unit.lower(), "").replace(unit.upper(), "")
        units_results[unit.lower()] = len(perform_reaction(test_polymer))

    best_unit = min(units_results, key=units_results.get)

    return units_results[best_unit]


def get_units_from_polymer(polymer: str) -> Set[str]:
    result = set()

    for unit in polymer:
        result.add(unit.lower())

    return result

def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    content = read_file(sys.argv[1])
    print("reacted polymer length: ", len(perform_reaction(content[0])))
    print("improved polymer length: ", calculate_improved_polymer_length(content[0]))