import inspect
import re

import bs4
import pyhtml2md

from aoc.misc import color, session

import logging


__log__ = logging.getLogger(__name__)


class Puzzle:
    def __init__(self, session, year: int, day: int):
        self.session = session
        self.year = year
        self.day = day

    @property
    def __soup(self):
        return bs4.BeautifulSoup(
            self.session.request("GET", f"{self.year}/day/{self.day}"),
            features="html.parser",
        )

    @property
    def title(self):
        return self.__soup.h2.text.strip("-").split(":")[1].strip()

    @property
    def input(self):
        return self.session.request("GET", f"{self.year}/day/{self.day}/input")

    @property
    def missions(self):
        return tuple(
            pyhtml2md.convert(article.renderContents())
            for article in self.__soup("article")
        )

    @property
    def answers(self):
        return tuple(
            answer.code.text
            for answer in self.__soup.main("p", recursive=False)
            if answer.text.startswith("Your puzzle answer was")
        )

    def answer(self, level, answer):
        html = self.session.post(
            f"{self.year}/day/{self.day}/answer",
            {"level": level, "answer": answer},
        )
        __log__.debug(html)
        soup = bs4.BeautifulSoup(html, features="html.parser")
        return pyhtml2md.convert(soup.article.renderContents())

    def purge(self):
        self.session.purge(f"{self.year}/day/{self.day}/input")
        self.session.purge(f"{self.year}/day/{self.day}")
        self.session.purge(f"{self.year}")
        self.session.purge("events")


class User:
    def __init__(self, session):
        self.session = session

    def stars_of_year(self, year):
        result = {}
        html = self.session.request("GET", f"{year}")
        if html:
            soup = bs4.BeautifulSoup(html, "html.parser")
            p = re.compile(r"Day (?P<day>\d+)(, (?P<stars>one|two))?")
            for event in soup.find_all("a", {"aria-label": True}):
                m = p.search(event["aria-label"])
                if m:
                    day = int(m.group("day"))
                    stars = m.group("stars") or "zero"
                    stars = {"zero": 0, "one": 1, "two": 2}[stars]
                    result[day] = stars
        return result

    def stars(self, verbose=False):
        result = {}
        html = self.session.request("GET", "events")
        if html:
            soup = bs4.BeautifulSoup(html, "html.parser")
            p = re.compile(r"\[(?P<year>\d+)\]\s+((?P<stars>\d+)\*)?")
            for event in soup.find_all("div", {"class": "eventlist-event"}):
                m = p.search(event.text)
                if m:
                    year = int(m.group("year"))
                    stars = int(m.group("stars") or 0)
                    result[year] = self.stars_of_year(year) if verbose else stars
        return result

    def purge(self):
        for year in range(2015, 2024):
            self.session.purge(f"{year}")
        self.session.purge("events")

    def Puzzle(self, year, day):
        return Puzzle(self.session, year, day)


class API:
    def __init__(self, cookie, cache_dir):
        self.session = session.CachedSession(
            cache_dir=cache_dir, base="https://adventofcode.com"
        )
        self.session.cookies.set("session", cookie, domain="adventofcode.com")

    def _request(self, method, suffix, data=None):
        return self.session.request(method, suffix, data=data)

    def User(self):
        return User(self.session)

    def initialize(self, base, year, day, update=False, force=False):
        update = update or force

        puzzle = self.User().Puzzle(year, day)

        year_path = base / f"y{year}"
        year_path.mkdir(parents=True, exist_ok=True)

        init = year_path / "__init__.py"
        if not init.is_file():
            with open(init, "w") as f:
                pass

        day_path = year_path / f"d{day:02d}"
        day_path.mkdir(parents=True, exist_ok=True)

        init = day_path / "__init__.py"
        if not init.is_file() or update:
            with open(init, "w") as f:
                f.write(
                    f'__year__ = {year}\n__day__ = {day}\n__title__ = "{puzzle.title}"\n'
                )

        solution = day_path / "solution.py"
        if not solution.is_file() or force:
            with open(solution, "w") as f:
                import aoc.template.solution

                f.write(inspect.getsource(aoc.template.solution))

        test = day_path / "test.py"
        if not (test.is_file() or update) or force:
            with open(test, "w") as f:
                import aoc.template.test

                f.write(inspect.getsource(aoc.template.test))

        readme = day_path / "README.md"
        if not readme.is_file() or update:
            with open(readme, "w") as f:
                f.write("\n\n".join(puzzle.missions) + "\n")

        data = day_path / "input"
        if not data.is_file() or update:
            with open(data, "w") as f:
                f.write(puzzle.input)

        answers = day_path / "answers"
        if not answers.is_file() or update:
            content = puzzle.answers
            if content:
                with open(answers, "w") as f:
                    f.write("\n".join(content) + "\n")

    def update_readme(self, base, events=None):
        events = events or self.User().stars()

        readme = base / "README.md"
        with open(readme) as f:
            content = f.read()
        for year, days in events.items():
            stars = days if isinstance(days, int) else sum(days.values())
            colour = color.color_scale(stars, (0, 50)) if stars else color.LIGHTGREY
            content = re.sub(
                rf"\(https:\/\/img\.shields\.io\/badge\/{year}-★_[^)]*\)",
                f"(https://img.shields.io/badge/{year}-★_{stars}-{colour.html})",
                content,
            )
        with open(readme, "w") as f:
            f.write(content)
