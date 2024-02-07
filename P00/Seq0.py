
def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    first_line = file_contents.find("\n")
    sequence = file_contents[first_line:]
    print("The first 20 bases are:", sequence[0:21])

def seq_len(seq):
    print("Gene:", gene, "---->", len(seq))




