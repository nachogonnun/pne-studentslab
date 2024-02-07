
def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    first_line = file_contents.find("\n")
    sequence = file_contents[first_line:]
    print("The first 20 bases are:", sequence[0:21])

def seq_len(seq):
    n = ["A", "C", "G", "T"]
    total = 0
    for i in seq:
        if i in n:
            total += 1
    return total

def seq_count_base(seq, base):
    return seq.count(base)






