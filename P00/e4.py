from Seq0 import *
from pathlib import Path
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for gene in genes:
    filename = "../S04/sequences/" + gene + ".txt"
    file_contents = Path(filename).read_text()
    seq = file_contents.replace("\n", "")
    print("- Gene", gene, "bases:")
    for base in bases:
        count = seq_count_base(seq, base)
        print("{}: {}".format(base, count))

