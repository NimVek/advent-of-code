import operator

from collections.abc import Iterable

import logging


__log__ = logging.getLogger(__name__)


class Interval(tuple):
    def __new__(cls, infimum, supremum=None, step=1):
        if isinstance(infimum, Interval):
            return infimum
        if isinstance(infimum, Iterable):
            infimum, *_, supremum = infimum
        result = tuple.__new__(cls, (infimum, supremum or infimum))
        result.step = step
        return result

    @property
    def infimum(self):
        return self[0]

    @property
    def supremum(self):
        return self[-1]

    def __contains__(self, other):
        if isinstance(other, int):
            return self.infimum <= other <= self.supremum
        if isinstance(other, Interval):
            return other <= self
        return NotImplemented

    def __iter__(self):
        yield from range(self.infimum, self.supremum + self.step)

    def __len__(self):
        return self.supremum - self.infimum + self.step

    def __and__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        infimum, supremum = max(self.infimum, other.infimum), min(
            self.supremum, other.supremum
        )
        if infimum <= supremum:
            return Interval(infimum, supremum)

    intersection = __and__

    def isdisjoint(self, other):
        return not self.__and__(other)

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return self.infimum == other.infimum and self.supremum == other.supremum

    def __le__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return self.infimum >= other.infimum and self.supremum <= other.supremum

    issubset = __le__

    def __lt__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return self.__le__(other) and self.__ne__(other)

    def __ge__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return self.infimum <= other.infimum and self.supremum >= other.supremum

    issuperset = __ge__

    def __gt__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return self.__ge__(other) and self.__ne__(other)


class IntervalSet:
    def _simplify(self, components):
        components = sorted(components, key=operator.attrgetter("infimum"))
        result = []
        for component in components:
            if not result or component.infimum > result[-1].supremum + 1:
                result.append(component)
            elif component.supremum > result[-1].supremum:
                result[-1] = Interval((result[-1].infimum, component.supremum))
        return result

    def __init__(self, *elements):
        self.elements = self._simplify(Interval(e) for e in elements)

    def __repr__(self):
        return (
            type(self).__name__
            + "("
            + ", ".join(f"[{e.infimum}, {e.supremum}]" for e in self.elements)
            + ")"
        )

    def __contains__(self, other):
        if isinstance(other, (int, Interval)):
            return any(other in element for element in self.elements)
        if isinstance(other, IntervalSet):
            return all(any(o in s for s in self.elements) for o in other.elements)
        return NotImplemented

    def __iter__(self):
        for element in self.elements:
            yield from element

    def __len__(self):
        return sum(len(element) for element in self.elements)

    def __or__(self, other):
        return IntervalSet(*self.elements, *other.elements)

    def __and__(self, other):
        result = []
        for a in self.elements:
            for b in other.elements:
                infimum, supremum = max(a.infimum, b.infimum), min(
                    a.supremum, b.supremum
                )
                if infimum <= supremum:
                    result.append(Interval((infimum, supremum)))
        return IntervalSet(*result)

    def __sub__(self, other):
        result = []
        for a in self.elements:
            for b in other.elements:
                if a.infimum < b.infimum <= a.supremum:
                    result.append(Interval((a.infimum, b.infimum - 1)))
                if a.infimum <= b.supremum < a.supremum:
                    result.append(Interval((b.supremum + 1, a.supremum)))
        return IntervalSet(*result)
