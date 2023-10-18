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
            data = f.read()
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


class Answer(Case):
    def __init__(self, path):
        self.path = path

    @cached_property
    def data(self):
        with open(self.path) as f:
            data = f.read()
        data = aoc.lib.parse.parse_blocks(data)
        return data

    @cached_property
    def answers(self):
        path = self.path.parent / "answers"
        answers = []
        if path.is_file():
            with open(path) as f:
                answers = f.read().splitlines()
        return answers

    def answer(self, idx):
        if idx <= len(self.answers):
            return self.answers[idx - 1]

    @property
    def name(self):
        return self.path.name


class AOCPuzzle(pytest.Module):
    def collect(self):
        self.cases = [Case(path) for path in self.path.parent.glob("cases/*.txt")]
        data = self.path.parent / "input"
        if data.is_file():
            self.cases.append(Answer(data))
        for path in self.path.parent.glob("*.py"):
            if path.name == "test.py":
                yield pytest.Module.from_parent(self, path=path)
            if path.name.startswith("solution"):
                yield AOCModule.from_parent(self, path=path)

    @property
    def year(self):
        return getattr(self.obj, "__year__", "__year__")

    @property
    def day(self):
        return getattr(self.obj, "__day__", "__day__")

    @property
    def title(self):
        return getattr(self.obj, "__title__", "__title__")


class AOCModule(pytest.Module):
    @staticmethod
    def issolution(item):
        return (
            isinstance(item, type)
            and issubclass(item, SolutionBase)
            and item != SolutionBase
        )

    def collect(self):
        for name, obj in self.obj.__dict__.items():
            if AOCModule.issolution(obj):
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

    @property
    def puzzle(self):
        this = self.parent
        while this:
            if isinstance(this, AOCPuzzle):
                return this
            else:
                this = getattr(this, "parent", None)

    def runtest(self):
        result = self.function(self.data)
        if str(result) != str(self.answer):
            raise AOCException(self, result)

    def repr_failure(self, excinfo):
        if isinstance(excinfo.value, AOCException):
            return f"Expected {self.answer!r}, got {excinfo.value.args[1]!r}"
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return (
            "filename",
            None,
            f"{self.puzzle.year} Day {self.puzzle.day}: {self.puzzle.title}",
        )

    def _traceback_filter(self, excinfo):
        if hasattr(self, "_obj") and not self.config.getoption("fulltrace", False):
            from _pytest._code import Code
            from _pytest._code.code import Traceback, filter_traceback
            from _pytest.compat import get_real_func

            fun = get_real_func(self.obj)
            # get_real_func not unwrap partial functions
            while getattr(fun, "__wrapped__", None):
                fun = getattr(fun, "__wrapped__")
            code = Code.from_function(fun)
            path, firstlineno = code.path, code.firstlineno
            traceback = excinfo.traceback
            ntraceback = traceback.cut(path=path, firstlineno=firstlineno)
            if ntraceback == traceback:
                ntraceback = ntraceback.cut(path=path)
                if ntraceback == traceback:
                    ntraceback = ntraceback.filter(filter_traceback)
                    if not ntraceback:
                        ntraceback = traceback
            ntraceback = ntraceback.filter(excinfo)

            # issue364: mark all but first and last frames to
            # only show a single-line message for each frame.
            if self.config.getoption("tbstyle", "auto") == "auto":
                if len(ntraceback) > 2:
                    ntraceback = Traceback(
                        entry
                        if i == 0 or i == len(ntraceback) - 1
                        else entry.with_repr_style("short")
                        for i, entry in enumerate(ntraceback)
                    )
            ntraceback = Traceback(entry for i, entry in enumerate(ntraceback))

            return ntraceback
        return excinfo.traceback


class AOCException(Exception):
    """Custom exception for result diffrence."""
