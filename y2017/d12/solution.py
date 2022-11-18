from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        result = {
            int(k): list(map(int, v.split(", ")))
            for k, v in [line.split(" <-> ") for line in data]
        }
        __log__.error(result)
        return result

    @staticmethod
    def partition(graph, start):
        seen = set()
        queue = [start]
        while queue:
            node = queue.pop()
            if node not in seen:
                seen.add(node)
                queue.extend(graph[node])
        return seen

    @staticmethod
    def part_01(data):
        return len(Solution.partition(data, 0))

    @staticmethod
    def part_02(data):
        partitions = []
        nodes = set(data.keys())
        while nodes:
            start = tuple(nodes)[0]
            partition = Solution.partition(data, start)
            partitions.append(partition)
            nodes -= partition
        __log__.debug(partitions)
        return len(partitions)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
