import sys

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        sys.exit("Usage: getlongestseq.py [FASTA file]")
    ids, seqlen = longest_seq_and_length(filename)
    print "Longest sequence(s): ", ids 
    print "Length:", seqlen
        
def longest_seq_and_length(filename):
    """Returns a tuple containing a list of the longest sequence(s) in the file,
    and the length of the sequence(s) in the form (list, integer)"""
    longest_len = 0
    current_len = 0
    longest_ids = []
    current_id = None
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif line[0] == ">":
                if current_len > longest_len:
                    longest_ids, longest_len = [current_id], current_len
                elif current_len == longest_len:
                    longest_ids.append(current_id)
                current_id, current_len = line[1:], 0
            else:
                current_len += len(line)               
        if current_len > longest_len: # for last sequence
            longest_ids, longest_len = [current_id], current_len
        elif current_len == longest_len:
            longest_ids.append(current_id)
    return (longest_ids, longest_len) 
                             
if __name__ == "__main__":
    main()