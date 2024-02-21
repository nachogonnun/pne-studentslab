from Seq1 import *

from pathlib import Path
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]


for gene in genes:
    filename = "../S04/sequences/" + gene + ".txt"
    file_contents = Path(filename).read_text()
    seq = Seq(file_contents.replace("\n", ""))
    seq.read_fasta(file_contents)

    max_count = 0
    max_base = None
    for base in bases:
        count = seq.seq_count(base)
        if count > max_count:
            max_base = base
            max_count = count

    print("Gene {} most common nucleotide is {} ({})".format(gene, max_base, max_count))

