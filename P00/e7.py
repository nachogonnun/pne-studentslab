from Seq0 import *
from pathlib import Path

filename = "../S04/sequences/" + "U5" + ".txt"
file_contents = Path(filename).read_text()
seq = file_contents.split("\n")
seq = seq[1][:21]
print("Gene U5")
print("Fragment:", seq)
print("Complement fragment:", seq_complement(seq))