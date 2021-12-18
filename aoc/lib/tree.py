import logging

from collections.abc import Sequence


__all__ = ["Node", "BinaryNode"]
logger = logging.getLogger(__name__)


class Node(Sequence):
    def __init__(self, value, parent=None):
        self.parent = parent
        if isinstance(value, Node):
            value = value.value
        if isinstance(value, Sequence):
            self.value = [self.__class__(v, self) for v in value]
        else:
            self.value = value

    @property
    def depth(self):
        if self.parent:
            return self.parent.depth + 1
        return 0

    @property
    def is_internal(self):
        return isinstance(self.value, Sequence)

    @property
    def is_leaf(self):
        return not self.is_internal

    def __len__(self):
        if self.is_internal:
            return sum(map(len, self.value))
        else:
            return 1

    def __getitem__(self, idx):
        logger.error((self, idx))
        if self.is_internal:
            for child in self.value:
                if idx < len(child):
                    return child[idx]
                idx -= len(child)
            raise IndexError("index out of range")
        else:
            return self.value

    def __repr__(self):
        if self.is_internal:
            return "[" + ", ".join(map(repr, self.value)) + "]"
        else:
            return str(self.value)

    @property
    def nested(self):
        if self.is_leaf:
            return self.value
        else:
            return [n.nested for n in self.value]


class BinaryNode(Node):
    @property
    def left(self):
        if self.is_leaf:
            raise NotImplementedError
        return self.value[0]

    @property
    def right(self):
        if self.is_leaf:
            raise NotImplementedError
        return self.value[1]

    def previous_node(self):
        if self.is_internal:
            result = self.left
            while result.is_internal:
                result = result.right
        else:
            now = self
            result = now.parent
            while result and result.left == now:
                now = result
                result = now.parent
        return result

    def next_node(self):
        if self.is_internal:
            result = self.right
            while result.is_internal:
                result = result.left
        else:
            now = self
            result = now.parent
            while result and result.right == now:
                now = result
                result = now.parent
        return result

    def previous_leaf(self):
        result = self.previous_node()
        while result and result.is_internal:
            result = result.previous_node()
        return result

    def next_leaf(self):
        result = self.next_node()
        while result and result.is_internal:
            result = result.next_node()
        return result
