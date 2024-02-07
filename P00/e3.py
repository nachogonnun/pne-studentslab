from Seq0 import *

genes = ["U5", "ADA", "FRAT1", "FXN"]
for gene in genes:

    filename = "../S04/sequences/" + gene + ".txt"
    with open(filename, "r") as f:
        next(f)
        seq = f.read().strip()
        length = seq_len(seq)
        print("Gene {}, length = {}".format(gene, length))
