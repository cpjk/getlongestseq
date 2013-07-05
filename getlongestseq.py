from sys import argv, exit

def main():
    infile = open(argv[1]) if len(argv) >= 2 else exit("Usage: getlongestseq.py [FASTA file]")
    print "%s" % findlongest(infile)


def findlongest(f):
    """Return the length of the longest sequence as a unicode string"""
    longestlength = 0
    currentseqlength = 0

    for line in f.readlines():
        if line[0] == ">":
            if currentseqlength > longestlength:
                longestlength = currentseqlength
            currentseqlength = 0
            continue
        else:
            currentseqlength += len(line.rstrip())

    return longestlength


if __name__ == "__main__":
    main()
