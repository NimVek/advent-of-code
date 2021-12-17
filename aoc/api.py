import logging
import re

import bs4
import html2markdown
import requests


logger = logging.getLogger(__name__)

import pprint


class API:

    BASE_URL = "https://adventofcode.com"

    def __init__(self, cookie):
        self.cookie = cookie

    def _request(self, method, suffix, data=None):
        url = f"{self.BASE_URL}/{suffix}"
        response = requests.request(
            method, url, data=data, cookies={"session": self.cookie}
        )
        if response.ok:
            return response.text

    def input(self, year, day):
        return self._request("GET", f"{year}/day/{day}/input")

    def mission(self, year, day):
        result = []
        html = self._request("GET", f"{year}/day/{day}")
        if html:
            soup = bs4.BeautifulSoup(html, "html.parser")
            for article in soup.find_all("article"):
                result.append(html2markdown.convert(article.renderContents()))
        return "\n\n".join(result)

    def answer(self, year, day, level, answer):
        result = []
        html = self._request(
            "POST", f"{year}/day/{day}/answer", {"level": level, "answer": answer}
        )
        pprint.pprint(html)

    def stars(self):
        result = {}
        html = self._request("GET", "events")
        if html:
            soup = bs4.BeautifulSoup(html, "html.parser")
            p = re.compile(r"\[(?P<year>\d+)\]\s+((?P<stars>\d+)\*)?")
            for event in soup.find_all("div", {"class": "eventlist-event"}):
                m = p.search(event.text)
                if m:
                    result[int(m.group("year"))] = int(m.group("stars") or 0)
        return result
