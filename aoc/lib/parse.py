import collections.abc
import itertools
import logging


logger = logging.getLogger(__name__)


def flatten(item):
    if isinstance(item, collections.abc.Iterable) and not isinstance(item, str):
        item = list(item)
        if len(item) == 1:
            return item[0]
    return item


def parse_blocks(string):
    result = [
        flatten(v)
        for k, v in itertools.groupby(string.splitlines(), lambda x: x.strip() != "")
        if k
    ]
    return flatten(result)
