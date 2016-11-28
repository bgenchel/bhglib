"""
Compress an input file using a huffman coding
"""
import sys
from HCTree import HCTree, EXPECTED_NUM_ARGS, MAX_BYTE_VALUE
from BitOutputStream import BitOutputStream


def printUsage():
    print "Usage: python compress.py {{input file name}} {{output file name}}"
    return


def main(argc, argv):
    # check argc, make sure function is getting the expected number of inputs
    if argc != EXPECTED_NUM_ARGS:
        printUsage()
        return False

    # define input and output filestreams
    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')

    # make sure we can actually read from input file
    if infile.read(1) == "":
        raise IOError("Input file is empty.")
    else:
        infile.seek(0)

    # instantiate list of ints to hold frequency of each byte in the file
    symbol_counts = [0]*MAX_BYTE_VALUE

    # read the input file one byte at a time, keeping track of each byte's
    # frequency in the symbol_counts list.
    byte = infile.read(1)
    while byte:
        symbol_counts[ord(byte)] += 1
        byte = infile.read(1)

    # instantiate and build huffman tree from symbol counts
    code_tree = HCTree()
    code_tree.build(symbol_counts)

    # now that tree is built, prepare to encode file by moving cursor to
    # the beginning.
    infile.seek(0)

    # before reading in and encoding the input file, we write a header of
    # the symbol counts to the output file in order to allow the uncompressor
    # to reconstruct the huffman tree for decoding. Because python isn't great
    # with data types and normalized sizes, this is done with a readable format
    for i in xrange(len(symbol_counts)):
        outfile.write(str(symbol_counts[i]) + '.')

    # Instantiate BitOutputStream to write the compressed output to the outfile
    # bit by bit.
    outstream = BitOutputStream(outfile)
    byte = infile.read(1)
    while byte:
        code_tree.encode(byte, outstream)
        byte = infile.read(1)

    # manually flush the outstream buffer in the event that
    # the encoding does not contain an integral number of bytes.
    # in this case, the remaining bits are filled with zero, and they are not
    # read in the uncompression
    outstream.flush()

    infile.close()
    outfile.close()
    del code_tree
    return True


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

