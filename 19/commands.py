from typing import List, Dict


class Command:
    def execute(self, opcode: List[int], registers: List[int]) -> List[int]:
        if len(opcode) != 3:
            raise RuntimeError("Invalid opcode arguments count: " + str(opcode))

        if len(registers) != 6:
            raise RuntimeError("Invalid registers count: " + str(registers))

        return self.__run(opcode, registers)

    def __run(self, opcode: List[int], registers: List[int]) -> List[int]:
        raise NotImplementedError("Method __run_command is not implemented")

    @staticmethod
    def get_command_dict() -> Dict[str, 'Command']:
        d = {
            "addr": AddRegister(),
            "addi": AddImmediate(),
            "mulr": MultiplyRegister(),
            "muli": MultiplyImmediate(),
            "banr": BitwiseANDRegister(),
            "bani": BitwiseANDImmediate(),
            "borr": BitwiseORRegister(),
            "bori": BitwiseORImmediate(),
            "setr": SetRegister(),
            "seti": SetImmediate(),
            "gtir": GreaterThanImmediateRegister(),
            "gtri": GreaterThanRegisterImmediate(),
            "gtrr": GreaterThanRegisterRegister(),
            "eqir": EqualImmediateRegister(),
            "eqri": EqualRegisterImmediate(),
            "eqrr": EqualRegisterRegister()
        }

        return d


class AddRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] + registers[register_b]

        return registers


class AddImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        value_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] + value_b

        return registers


class MultiplyRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] * registers[register_b]

        return registers


class MultiplyImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        value_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] * value_b

        return registers


class BitwiseANDRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] & registers[register_b]

        return registers


class BitwiseANDImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        value_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] & value_b

        return registers


class BitwiseORRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] | registers[register_b]

        return registers


class BitwiseORImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        value_b = opcode[1]
        register_c = opcode[2]

        registers[register_c] = registers[register_a] | value_b

        return registers


class SetRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        register_c = opcode[2]

        registers[register_c] = registers[register_a]

        return registers


class SetImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        value_a = opcode[0]
        register_c = opcode[2]

        registers[register_c] = value_a

        return registers


class GreaterThanImmediateRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        value_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        if value_a > registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class GreaterThanRegisterImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        value_b = opcode[1]
        register_c = opcode[2]

        if registers[register_a] > value_b:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class GreaterThanRegisterRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        if registers[register_a] > registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class EqualImmediateRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        value_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        if value_a == registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class EqualRegisterImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        value_b = opcode[1]
        register_c = opcode[2]

        if value_b == registers[register_a]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class EqualRegisterRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[0]
        register_b = opcode[1]
        register_c = opcode[2]

        if registers[register_a] == registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers
