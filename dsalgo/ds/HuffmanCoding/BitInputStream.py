
class BitInputStream(object):
    buff = 0  # one byte buffer of bits
    nbits = 0  # how many inputs have been read from buff
    inpt = None  # input "stream" to use

    def __init__(self, fp):
        self.inpt = fp
        self.fill()
        return

    def fill(self):
        self.buff = ord(self.inpt.read(1))
        self.nbits = 0
        return

    def readBit(self):
        if self.nbits == 8:
            self.fill()
        rbit = self.bitVal(self.buff, self.nbits)
        self.nbits += 1
        return rbit

    def bitVal(self, char, n):
        return (char >> n) & 1

    def eof(self):
        pos = self.inpt.tell()
        read = self.inpt.read(1)
        self.inpt.seek(pos)
        return read == ""
