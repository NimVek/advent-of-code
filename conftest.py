import pathlib
import re

from functools import cached_property

import pytest

import aoc.lib.parse

from aoc.lib.solution import SolutionBase

import logging


__log__ = logging.getLogger(__name__)


def pytest_collect_file(file_path, parent):
    if re.search(r"/y[0-9]{4,}/d(0[1-9]|1[0-9]|2[0-5])/__init__\.py", str(file_path)):
        return AOCPuzzle.from_parent(parent, path=file_path)


class Case:
    def __init__(self, path):
        self.path = path

    @cached_property
    def data(self):
        with open(self.path) as f:
            data = f.read().strip()
        data = aoc.lib.parse.parse_blocks(data)
        return data

    @property
    def filename(self):
        return self.path.name

    def answer(self, idx):
        return self.filename.split(".")[idx] or None

    @property
    def name(self):
        return self.answer(0)


class AOCPuzzle(pytest.Module):
    def collect(self):
        self.cases = [Case(path) for path in self.path.parent.glob("cases/*.txt")]
        for path in self.path.parent.glob("*.py"):
            if path.name == "test.py":
                yield pytest.Module.from_parent(self, path=path)
            if path.name.startswith("solution"):
                yield AOCModule.from_parent(self, path=path)


class AOCModule(pytest.Module):
    def issolution(self, item):
        return (
            isinstance(item, type)
            and issubclass(item, SolutionBase)
            and item != SolutionBase
        )

    def collect(self):
        for name, obj in self.obj.__dict__.items():
            if self.issolution(obj):
                yield AOCSolution.from_parent(self, name=name, obj=obj)


class AOCSolution(pytest.Class):
    @property
    def cases(self):
        this = self.parent
        while this:
            if hasattr(this, "cases"):
                return this.cases
            else:
                this = getattr(this, "parent", None)

    def collect(self):
        for case in self.cases:
            data = self.obj.prepare(case.data)
            for name in self.obj.__dict__:
                if re.match(r"part_[0-9]+$", name):
                    idx = int(name.split("_")[1])
                    answer = case.answer(idx)
                    if answer:
                        yield AOCPart.from_parent(
                            self,
                            name=f"{name}[{case.name}] -> {answer}",
                            originalname=name,
                            data=data,
                            answer=answer,
                        )


class AOCPart(pytest.Function):
    def __init__(self, *, data, answer, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.answer = answer

    def runtest(self):
        assert str(self.function(self.data)) == str(self.answer)
