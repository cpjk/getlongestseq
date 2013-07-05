from sys import argv, exit


def main():
    infile = open(argv[1]) if len(argv) >= 2 else exit("Usage: getlongestseq.py [FASTA file]")
    length, name = findlongest(infile)
    print "%s: %s" % (length, name)


def findlongest(f):
    """Return the length of the longest sequence and its id line as a tuple"""
    longestlength = 0
    currentseqlength = 0
    oldseqname = None
    newseqname = None
    longestseqname = None

    for line in f.readlines():
        if line[0] == ">":
            oldseqname, newseqname = newseqname, line[1:].rstrip()

            if currentseqlength > longestlength:
                longestlength = currentseqlength
                longestseqname = oldseqname
            currentseqlength = 0
            continue
        else:
            currentseqlength += len(line.rstrip())

    return (longestlength, longestseqname)


if __name__ == "__main__":
    main()
