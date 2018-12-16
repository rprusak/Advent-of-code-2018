from typing import List, Dict


class Command:
    def execute(self, opcode: List[int], registers: List[int]) -> List[int]:
        if len(opcode) != 4:
            raise RuntimeError("Invalid opcode arguments count: " + str(opcode))

        if len(registers) != 4:
            raise RuntimeError("Invalid registers count: " + str(registers))

        return self.__run(opcode, registers)

    def __run(self, opcode: List[int], registers: List[int]) -> List[int]:
        raise NotImplementedError("Method __run_command is not implemented")

    @staticmethod
    def get_commands() -> List['Command']:
        commands = []

        commands.append(AddRegister())
        commands.append(AddImmediate())
        commands.append(MultiplyRegister())
        commands.append(MultiplyImmediate())
        commands.append(BitwiseANDRegister())
        commands.append(BitwiseANDImmediate())
        commands.append(BitwiseORRegister())
        commands.append(BitwiseORImmediate())
        commands.append(SetRegister())
        commands.append(SetImmediate())
        commands.append(GreaterThanRegisterImmediate())
        commands.append(GreaterThanImmediateRegister())
        commands.append(GreaterThanRegisterRegister())
        commands.append(EqualImmediateRegister())
        commands.append(EqualRegisterImmediate())
        commands.append(EqualRegisterRegister())

        return commands

    @staticmethod
    def get_command_dict() -> Dict[int, 'Command']:
        d = {
            0: GreaterThanImmediateRegister(),
            1: SetRegister(),
            2: BitwiseORImmediate(),
            3: GreaterThanRegisterRegister(),
            4: GreaterThanRegisterImmediate(),
            5: EqualImmediateRegister(),
            6: SetImmediate(),
            7: EqualRegisterImmediate(),
            8: EqualRegisterRegister(),
            9: BitwiseORRegister(),
            10: AddRegister(),
            11: MultiplyRegister(),
            12: BitwiseANDImmediate(),
            13: MultiplyImmediate(),
            14: BitwiseANDRegister(),
            15: AddImmediate()
        }

        return d


class AddRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] + registers[register_b]

        return registers


class AddImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        value_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] + value_b

        return registers


class MultiplyRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] * registers[register_b]

        return registers


class MultiplyImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        value_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] * value_b

        return registers


class BitwiseANDRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] & registers[register_b]

        return registers


class BitwiseANDImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        value_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] & value_b

        return registers


class BitwiseORRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] | registers[register_b]

        return registers


class BitwiseORImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        value_b = opcode[2]
        register_c = opcode[3]

        registers[register_c] = registers[register_a] | value_b

        return registers


class SetRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        register_c = opcode[3]

        registers[register_c] = registers[register_a]

        return registers


class SetImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        value_a = opcode[1]
        register_c = opcode[3]

        registers[register_c] = value_a

        return registers


class GreaterThanImmediateRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        value_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        if value_a > registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class GreaterThanRegisterImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        value_b = opcode[2]
        register_c = opcode[3]

        if registers[register_a] > value_b:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class GreaterThanRegisterRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        if registers[register_a] > registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class EqualImmediateRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        value_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        if value_a == registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class EqualRegisterImmediate(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        value_b = opcode[2]
        register_c = opcode[3]

        if value_b == registers[register_a]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers


class EqualRegisterRegister(Command):
    def _Command__run(self, opcode: List[int], registers: List[int]) -> List[int]:
        register_a = opcode[1]
        register_b = opcode[2]
        register_c = opcode[3]

        if registers[register_a] == registers[register_b]:
            registers[register_c] = 1
        else:
            registers[register_c] = 0

        return registers
