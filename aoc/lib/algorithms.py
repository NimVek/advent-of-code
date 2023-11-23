from collections.abc import Mapping, Set
from typing import Any

import logging


__log__ = logging.getLogger(__name__)


def possibilities_to_dict(possibilities: Mapping[Any, Set[Any]]) -> Mapping[Any, Any]:
    result = {}
    while possibilities:
        result.update(
            {
                item: next(iter(possibility))
                for item, possibility in possibilities.items()
                if len(possibility) == 1
            }
        )
        possibilities = {
            item: possibility - frozenset(result.values())
            for item, possibility in possibilities.items()
            if len(possibility) > 1
        }
    return result
