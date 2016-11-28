"""
Python implementation of a Huffman Coding Tree. Since python isn't as good
as C++ at dealing with types and sizes, the compression header is written
in plane text instead of a more compressed format. Successfully tested on
War and Peace
"""
from HCNode import HCNode
from PriorityQueue import PriorityQueue

MAX_BYTE_VALUE = 256
ASCII_OFFSET = 48
EXPECTED_NUM_ARGS = 3


class HCNodePtrComp(object):
    pass


class HCTree(object):
    root = None
    leaves = None

    def __init__(self):
        self.leaves = [None]*256

    def build(self, freqs):
        pq = PriorityQueue()
        for i in xrange(MAX_BYTE_VALUE):
            if freqs[i] != 0:
                new_node = HCNode(freqs[i], chr(i))
                pq.push(new_node, new_node.count)
                self.leaves[i] = new_node

        while len(pq) > 1:
            node1 = pq.pop()
            node0 = pq.pop()
            new_node = HCNode(node0.count + node1.count, node1.symbol)
            node0.parent = new_node
            node1.parent = new_node
            new_node.child0 = node0
            new_node.child1 = node1
            pq.push(new_node, new_node.count)

        self.root = pq.pop()
        return

    def encode(self, symbol, outstream):
        node = self.leaves[ord(symbol)]
        self.getBit(node, outstream)
        return

    def getBit(self, node, outstream):
        """
        recursively traverse up the tree until at parent, then
        print values of the leaf in correct order
        """
        if node.parent is not None:
            self.getBit(node.parent, outstream)
            if node == node.parent.child1:
                outstream.writeBit(1)
            else:
                outstream.writeBit(0)

        if self.root.child0 is None and self.root.child1 is None:
            outstream.writeBit(0)

    def decode(self, instream):
        curr = self.root
        while not instream.eof():
            b = instream.readBit()
            if b == 0 and curr.child0 is not None:
                curr = curr.child0
            elif b == 1 and curr.child1 is not None:
                curr = curr.child1

            if curr.child0 is None and curr.child1 is None:
                # print "symbol = {}, type = {}".format(curr.symbol, type(curr.symbol))
                return curr.symbol
        return


