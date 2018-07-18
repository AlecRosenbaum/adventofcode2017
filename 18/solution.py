"""
Day 18 challenge
"""
import re
from collections import defaultdict

import attr


class Interrupt(Exception):
    pass


@attr.s
class Memory:
    registers = attr.ib(default=attr.Factory(lambda: defaultdict(int)))
    instructions = attr.ib(default=attr.Factory(tuple))
    instruction_idx = attr.ib(default=0)
    last_frequency_played = attr.ib(default=None)

    def process_instructions(self):
        while self.instruction_idx < len(self.instructions):
            print(self.instruction_idx, self.instructions[self.instruction_idx])
            self.instructions[self.instruction_idx].apply_to(self)
            self.instruction_idx += 1

    def get_val(self, val):
        """Returns val if it's a number, or memory[val] otherwise"""
        try:
            return int(val)
        except ValueError:
            return int(self.registers[val])


@attr.s
class Instruction:
    REGEX = None

    a = attr.ib()
    b = attr.ib(default=None)

    def apply_to(self, memory):
        raise NotImplementedError()

    @classmethod
    def get_regex(cls):
        if not hasattr(cls, "_REGEX"):
            cls._REGEX = re.compile(cls.REGEX)

        return cls._REGEX

@attr.s
class SndInstruction(Instruction):
    """
    snd X plays a sound with a frequency equal to the value of X.
    """
    REGEX = r"snd (?P<a>-?\w+)"

    def apply_to(self, memory):
        print("playing", self.a, "->", memory.get_val(self.a))
        memory.last_frequency_played = memory.get_val(self.a)


@attr.s
class SetInstruction(Instruction):
    """
    set X Y sets register X to the value of Y.
    """
    REGEX = r"set (?P<a>\w) (?P<b>-?\w+)"

    def apply_to(self, memory):
        memory.registers[self.a] = memory.get_val(self.b)

@attr.s
class AddInstruction(Instruction):
    """
    add X Y increases register X by the value of Y.
    """
    REGEX = r"add (?P<a>\w) (?P<b>-?\w+)"

    def apply_to(self, memory):
        memory.registers[self.a] += memory.get_val(self.b)

@attr.s
class MulInstruction(Instruction):
    """
    mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
    """
    REGEX = r"mul (?P<a>\w) (?P<b>-?\w+)"

    def apply_to(self, memory):
        memory.registers[self.a] *= memory.get_val(self.b)

@attr.s
class ModInstruction(Instruction):
    """
    mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
    """
    REGEX = r"mod (?P<a>\w) (?P<b>-?\w+)"

    def apply_to(self, memory):
        memory.registers[self.a] = memory.registers[self.a] % memory.get_val(self.b)

@attr.s
class RcvInstruction(Instruction):
    """
    rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
    """
    REGEX = r"rcv (?P<a>-?\w+)"

    def apply_to(self, memory):
        if memory.get_val(self.a):
            raise Interrupt(memory.last_frequency_played)

@attr.s
class RealRcvInstruction(Instruction):
    """
    rcv X recieves a value and stores it in X
    """
    REGEX = r"rcv (?P<a>\w)"

    def apply_to(self, memory):
        # TODO

@attr.s
class JgzInstruction(Instruction):
    """
    jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
    """
    REGEX = r"jgz (?P<a>(\w|\d+)) (?P<b>-?\w+)"

    def apply_to(self, memory):
        if memory.get_val(self.a):
            memory.instruction_idx += memory.get_val(self.b) - 1



def solution_part_one(arg):
    possible_ops = (
        SndInstruction,
        SetInstruction,
        AddInstruction,
        MulInstruction,
        ModInstruction,
        RcvInstruction,
        JgzInstruction,
    )

    instructions = []
    for op in arg.strip().split("\n"):
        found = False
        for i in possible_ops:
            match = i.get_regex().match(op)
            if match:
                instructions.append(i(**match.groupdict()))
                found = True
                break
        if not found:
            raise ValueError(f"'{op}' not found")

    state = Memory(
        instructions=tuple(instructions)
    )
    try:
        state.process_instructions()
    except Interrupt as e:
        return int(str(e))


def solution_part_two(arg):
    pass


if __name__ == "__main__":
    problem_input = """
set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 680
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
    """
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
