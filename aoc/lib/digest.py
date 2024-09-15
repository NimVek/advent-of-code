import collections
import concurrent.futures
import itertools
import typing

import logging


__log__ = logging.getLogger(__name__)


class Digest(typing.NamedTuple):
    idx: int
    digest: str


def sequential(digest, prefix, validator, start=0, end=None):
    dgst = digest(prefix.encode()).copy
    indices = itertools.count(start) if end is None else range(start, end)
    for idx in indices:
        tmp = dgst()
        tmp.update(str(idx).encode())
        result = tmp.hexdigest()
        if validator(result):
            yield Digest(idx, result)


def _sequential(digest, prefix, validator, start, end):
    return tuple(sequential(digest, prefix, validator, start, end))


def parallel(digest, prefix, validator, start=0, end=None, step=50000):
    indices = (
        itertools.count(start=start, step=step)
        if end is None
        else itertools.chain(range(start, end, step), [end])
    )
    chunks = itertools.pairwise(indices)
    with concurrent.futures.ProcessPoolExecutor() as pool:
        futures = collections.deque(
            pool.submit(_sequential, digest, prefix, validator, *next(chunks))
            for _ in range(pool._max_workers)
        )
        while True:
            yield from futures.popleft().result()
            futures.append(
                pool.submit(_sequential, digest, prefix, validator, *next(chunks))
            )
