import re

import bs4
import html2markdown

from aoc.misc import session

import logging


__log__ = logging.getLogger(__name__)


class API:
    def __init__(self, cookie, cache_dir):
        self.session = session.CachedSession(
            cache_dir=cache_dir, base="https://adventofcode.com"
        )
        self.session.cookies.set("session", cookie, domain="adventofcode.com")

    def _request(self, method, suffix, data=None):
        return self.session.request(method, suffix, data=data)

    def data(self, year, day):
        return self._request("GET", f"{year}/day/{day}/input")

    def mission(self, year, day):
        result = []
        html = self._request("GET", f"{year}/day/{day}")
        if html:
            soup = bs4.BeautifulSoup(html, "html.parser")
            for article in soup.find_all("article"):
                result.append(html2markdown.convert(article.renderContents()))
        return "\n\n".join(result)

    def answers(self, year, day):
        result = []
        html = self._request("GET", f"{year}/day/{day}")
        if html:
            soup = bs4.BeautifulSoup(html, "html.parser")
            for answer in soup.find_all("p"):
                if answer.text.startswith("Your puzzle answer was"):
                    for code in answer.find_all("code"):
                        result.append(code.text)
        return result

    def answer(self, year, day, level, answer):
        html = self._request(
            "POST", f"{year}/day/{day}/answer", {"level": level, "answer": answer}
        )
        __log__.debug(html)
        if html:
            soup = bs4.BeautifulSoup(html, "html.parser")
            for article in soup.find_all("article"):
                result = html2markdown.convert(article.renderContents())
                if result.startswith("That's the right answer!"):
                    self.session.purge(f"{year}/day/{day}")
                    self.session.purge(f"{year}")
                    self.session.purge("events")
                return result

    def stars_of_year(self, year):
        result = {}
        html = self._request("GET", f"{year}")
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
        html = self._request("GET", "events")
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
