import re
from command import Command

before_regex = re.compile("Before:\s+\[(\d+),\s+(\d+),\s+(\d+), (\d+)]")
after_regex = re.compile("After:\s+\[(\d+),\s+(\d+),\s+(\d+), (\d+)]")


class OpcodeTest:
    def __init__(self, before: str, opcode: str, after: str) -> None:
        match = before_regex.match(before)
        if match:
            self.register_0_before = int(match[1])
            self.register_1_before = int(match[2])
            self.register_2_before = int(match[3])
            self.register_3_before = int(match[4])
        else:
            raise RuntimeError("Could not parse before line: " + before)

        self.opcode = [int(x) for x in opcode.split(" ")]
        if len(self.opcode) != 4:
            raise RuntimeError("Invalid opcode size: " + str(opcode))

        match = after_regex.match(after)
        if match:
            self.register_0_after = int(match[1])
            self.register_1_after = int(match[2])
            self.register_2_after = int(match[3])
            self.register_3_after = int(match[4])
        else:
            raise RuntimeError("Could not parse after line: " + after)

    def match_command(self, command: 'Command') -> bool:
        registers = [self.register_0_before, self.register_1_before, self.register_2_before, self.register_3_before]
        r0, r1, r2, r3 = command.execute(self.opcode, registers)

        return self.register_0_after == r0 and self.register_1_after == r1 and self.register_2_after == r2 \
               and self.register_3_after == r3
