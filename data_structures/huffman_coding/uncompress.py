"""
uncompress a file that was huffman coded
"""
import sys
from HCTree import HCTree, EXPECTED_NUM_ARGS, MAX_BYTE_VALUE
from BitInputStream import BitInputStream


def printUsage():
    pass


def main(argc, argv):
    # check to see that the proper number of args have been handed in
    if argc != EXPECTED_NUM_ARGS:
        printUsage()
        return False

    # define input and output file pointers
    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')

    # check for feasibility of reading input file
    if not infile.read(1):
        raise IOError("Input file failed to open or failed to read, could be empty.")
    else:
        infile.seek(0)

    # Instantiate list of ints to hold byte freqs
    symbol_counts = [0]*MAX_BYTE_VALUE

    # Read the header of the input file in order to populate the symbol counts.
    num_symbols = 0
    for i in xrange(len(symbol_counts)):
        buff = []
        byte = infile.read(1)
        while byte != ".":
            buff.append(byte)
            byte = infile.read(1)
        symbol_counts[i] = int("".join(buff))
        num_symbols += symbol_counts[i]

    # instantiate a new HCTree to hold our huffman construction specified
    # by the header of the input file
    code_tree = HCTree()
    code_tree.build(symbol_counts)

    # Instantiate a bitinputstream object with our infile in order to
    # read from the compressed file one bit at a time. The num_symbols var
    # keeps the loop from reading in the extra bits possibly appended
    # at the end of the file in order to write an integral number of bytes
    instream = BitInputStream(infile)
    while num_symbols > 0:
        output = code_tree.decode(instream)
        if output is not None:
            outfile.write(output)
        else:
            break
        num_symbols -= 1

    # close files
    infile.close()
    outfile.close()
    del code_tree
    return True

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
