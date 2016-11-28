"""
Iterator for a BST, helps with navigating in order
"""
from BSTNode import BSTNode


class BSTIterator(object):
    curr = None

    def __init__(self, node):
        if node is None:
            return

        assert isinstance(node, BSTNode)
        self.curr = node
        return

    def __iter__(self):
        return self

    def next(self):
        """
        increment the iterator by 1
        """
        if self.curr is None:
            raise StopIteration

        nxt = self.curr.successor()
        if nxt is None:
            raise StopIteration
        else:
            return nxt

    def __eq__(self, other):
        """
        test for equality to another iterator
        """
        return self.curr == other.curr

    def __ne__(self, other):
        """
        test for inequality
        """
        return self.curr != other.curr

