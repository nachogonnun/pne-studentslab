from Seq1 import *

from pathlib import Path
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for gene in genes:
    filename = "../S04/sequences/" + gene + ".txt"
    file_contents = Path(filename).read_text()
    seq = Seq(file_contents.replace("\n", ""))
    seq.read_fasta(file_contents)
    max_base = max(bases, key=lambda base: seq.seq_count(base))
    count = seq.seq_count(max_base)
    print("Gene {} most common nucleotide is {} ({})".format(gene, max_base, count))