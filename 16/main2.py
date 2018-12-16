import sys
from main import read_file
from command import Command
from opcode import OpcodeTest


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main2.py <input part 2>")
        exit()

    part_two_content = read_file(sys.argv[1])
    commands = Command.get_command_dict()

    registers = [0, 0, 0, 0]

    for line in part_two_content:
        opcode = [int(x) for x in line.split(" ")]
        command_number = opcode[0]

        registers = commands[command_number].execute(opcode, registers)

    print(registers[0])
