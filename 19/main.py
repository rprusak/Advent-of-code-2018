import sys
import re
from typing import List, Tuple
from commands import Command

def read_file(filename: str) -> List[str]:
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.rstrip() for x in content]
    result = [list(x) for x in content]
    return content


def get_instruction_pointer(program_header: str) -> int:
    header_pattern = re.compile("^#ip (\d)$")
    match = header_pattern.match(program_header)

    if match:
        return int(match[1])
    else:
        raise RuntimeError("Could not parse program header: " + program_header)


opcode_pattern = re.compile("^(\w+)\s+(\d+)\s+(\d+)\s+(\d+)$")


def get_command_opcodes(file_input: List[str]) -> List[Tuple[str, int, int, int]]:
    opcodes = []

    for line in file_input:
        match = opcode_pattern.match(line)
        if match:
            opcodes.append((match[1], int(match[2]), int(match[3]), int(match[4])))
        else:
            raise RuntimeError("Could not parse line: " + line)

    return opcodes


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    file_content = read_file(sys.argv[1])

    instruction_pointer = get_instruction_pointer(file_content[0])
    opcodes = get_command_opcodes(file_content[1:])
    registers = [0, 0, 0, 0, 0, 0]

    commands = Command.get_command_dict()

    while not registers[instruction_pointer] >= len(opcodes):
        instruction_index = registers[instruction_pointer]
        opcode = opcodes[instruction_index]
        commands[opcode[0]].execute(opcode[1:], registers)
        registers[instruction_pointer] += 1

    print(registers)
