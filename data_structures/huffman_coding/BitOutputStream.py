"""
Class used for writing to a file bit by bit
"""


class BitOutputStream(object):
    buff = 0
    nbits = 0
    outpt = None

    def __init__(self, fp):
        self.outpt = fp
        return

    def flush(self):
        """
        clears the buffer
        """
        self.outpt.write(chr(self.buff))
        self.outpt.flush()
        self.buff = self.nbits = 0
        return

    def writeBit(self, i):
        """
        write the LSB of the argument to the bit buffer,
        increment bit buffer index. Flush buffer firrst, if it is full.
        """
        if self.nbits == 8:
            self.flush()
        self.buff = self.buff | ((i & 1) << self.nbits)
        self.nbits += 1
        return
