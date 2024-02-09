from Seq0 import *
from pathlib import Path

genes = ["U5", "ADA", "FRAT1", "FXN"]
for gene in genes:
    filename = "../S04/sequences/" + gene + ".txt"
    file_contents = Path(filename).read_text()
    seq = file_contents.replace("\n", "")
    count = seq_count(seq)
    print("- Gene", gene, ":", count)








