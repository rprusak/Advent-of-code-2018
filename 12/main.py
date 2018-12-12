import sys
import re
from typing import List, Tuple


initial_state_patter = re.compile("initial state: (.+)")
rule_pattern = re.compile("(.{5})\s+=>\s(.{1})")


def read_file(filename: str) -> List[str]:
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


def parse_file_content(content: List[str]) -> Tuple[str, List[Tuple[str, str]]]:
    state = None
    rules = []

    match = initial_state_patter.match(content[0])
    if match:
        state = match[1]
    else:
        raise RuntimeError("Could not parse initial state")

    for line in content[2:]:
        match = rule_pattern.match(line)
        if match:
            rules.append((match[1], match[2]))

    return state, rules


def get_next_value(sub_state: str, rules: List[Tuple[str, str]]):
    for rule in rules:
        if sub_state == rule[0]:
            return rule[1]

    return "."


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    generations_count = 500
    file_content = read_file(sys.argv[1])
    state, rules = parse_file_content(file_content)

    state = "...................." + state
    print(0, state)

    for i in range(1, generations_count):
        next_state = ""
        state += "...."

        for j in range(2, len(state) - 2):
            next_state += get_next_value(state[j - 2: j + 3], rules)

        state = ".." + next_state
        state = re.sub('\.+$', '', state)

        print(i, state)

    result = 0

    for i in range(0, len(state)):
        if state[i] == "#":
            result += (i - 20)

    print(result)