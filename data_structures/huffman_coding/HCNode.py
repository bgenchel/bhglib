

class HCNode:
    count = -1
    symbol = ""
    child0 = None
    child1 = None
    parent = None

    def __init__(self, count, symbol):
        self.count = count
        self.symbol = symbol
        return

    def __str__(self):
        return "[" + self.count + "," + self.symbol + "]"

    def __lt__(self, other):
        assert isinstance(other, self.__class__)
        """
        returns True if the frequency of the node is greater
        than the node being compared to. else, False.

        For breaking ties, return a comparison of symbol values
        """
        if self.count != other.count:
            return self.count > other.count
        else:
            return self.symbol < other.symbol

