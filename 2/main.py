# Advent of Code day 2
from typing import List
import sys


def contains_exactly_count_of_any_letter(word: str, count: int = 2) -> bool :
    temp_dict = {}

    for letter in word:
        if letter in temp_dict.keys():
            temp_dict[letter] += 1
        else:
            temp_dict[letter] = 1

    for val in temp_dict.values():
        if val == count:
            return True

    return False


def calculate_checksum(codes: List[str]) -> int :
    two_letter_codes_count = 0
    three_letter_codes_count = 0

    for code in codes:
        if contains_exactly_count_of_any_letter(code, 2):
            two_letter_codes_count += 1

        if contains_exactly_count_of_any_letter(code, 3):
            three_letter_codes_count += 1

    return two_letter_codes_count * three_letter_codes_count


def read_file(filename: str) -> List[str]:
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


def get_different_letters_count(first_word: str, second_word: str) -> int:
    different_letters_count = 0

    for i in range(0, len(first_word)):
        if first_word[i] != second_word[i]:
            different_letters_count += 1

    return different_letters_count


def get_common_part_of_words(first_word: str, second_word: str) -> str:
    common_part = ""

    for i in range(0, len(first_word)):
        if first_word[i] == second_word[i]:
            common_part += first_word[i]

    return common_part


def get_common_id(codes: List[str]) -> str:

    for i in range(0, len(codes)):
        for j in range(i + 1, len(codes)):
            if get_different_letters_count(codes[i], codes[j]) == 1:
                return get_common_part_of_words(codes[i], codes[j])

    return ""

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    codes = read_file(sys.argv[1])
    print(calculate_checksum(codes))
    print(get_common_id(codes))
