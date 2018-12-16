import sys
from typing import List
from command import Command
from opcode import OpcodeTest

def read_file(filename: str) -> List[str]:
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.rstrip() for x in content]
    result = [list(x) for x in content]
    return content


def calculate_matching_commands_count(before: str, opcode: str, after: str) -> int:
    commands = Command.get_commands()
    opcode_test = OpcodeTest(before, opcode, after)
    matching_commands = 0

    for command in commands:
        if opcode_test.match_command(command):
            matching_commands += 1

    return matching_commands


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input>")
        exit()

    file_content = read_file(sys.argv[1])
    file_content = list(filter(lambda l: len(l) > 0, file_content))
    result = 0

    for i in range(0, len(file_content)//3):
        before = file_content[i * 3]
        opcode = file_content[i * 3 + 1]
        after = file_content[i * 3 + 2]
        if calculate_matching_commands_count(before, opcode, after) >= 3:
            result += 1

        if calculate_matching_commands_count(before, opcode, after) == 1:
            print(opcode)

        if calculate_matching_commands_count(before, opcode, after) == 2:
            print(opcode + " match 2")

    print(result)



