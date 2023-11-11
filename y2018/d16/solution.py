import collections

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)

import json

from y2018.lib.device import Device, OpCode


@dataclass
class Sample:
    before: tuple[int, int, int, int]
    instruction: tuple[int, int, int, int]
    after: tuple[int, int, int, int]


@dataclass
class Input:
    samples: tuple[Sample, ...]
    program: tuple[tuple[int, int, int, int], ...]


@dataclass
class SampleTest:
    code: int
    opportunities: set[type[OpCode]]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        *samples, program = data
        samples = tuple(
            Sample(
                before=tuple(json.loads(s[0][8:])),
                instruction=tuple(map(int, s[1].split())),
                after=tuple(json.loads(s[2][8:])),
            )
            for s in samples
        )
        return Input(
            samples=samples,
            program=tuple(
                tuple(map(int, instruction.split())) for instruction in program
            ),
        )

    @staticmethod
    def test_samples(samples):
        return (
            SampleTest(
                code=sample.instruction[0],
                opportunities={
                    opcode
                    for opcode in tuple(Device.opcodes)
                    if tuple(opcode(*(sample.instruction[1:]))(sample.before))
                    == sample.after
                },
            )
            for sample in samples
        )

    @staticmethod
    def part_01(data):
        return sum(
            1
            for sample in Solution.test_samples(data.samples)
            if len(sample.opportunities) >= 3
        )

    @staticmethod
    def part_02(data):
        investigate = collections.defaultdict(lambda: set(Device.opcodes))
        for sample in Solution.test_samples(data.samples):
            investigate[sample.code] &= sample.opportunities
        translate = {}
        while investigate:
            translate.update(
                {
                    code: opcodes.pop()
                    for code, opcodes in investigate.items()
                    if len(opcodes) == 1
                }
            )
            investigate = {
                code: opcodes - set(translate.values())
                for code, opcodes in investigate.items()
                if len(opcodes) > 1
            }

        program = tuple(
            translate[instruction[0]](*(instruction[1:]))
            for instruction in data.program
        )

        device = Device(program=program)
        device.run()
        return device.register[0]


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
