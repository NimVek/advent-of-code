import abc

import logging


__log__ = logging.getLogger(__name__)


class SolutionBase(abc.ABC):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    @abc.abstractmethod
    def part_01(data):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def part_02(data):
        raise NotImplementedError

    @classmethod
    def solve(cls, part, data):
        data = cls.prepare(data)
        return getattr(cls, f"part_{part:02d}")(data)
