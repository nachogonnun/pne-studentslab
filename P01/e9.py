from Seq1 import *

from pathlib import Path

FILENAME = "../S04/sequences/U5.txt"
file_contents = Path(FILENAME).read_text()
s = Seq()
s.read_fasta(file_contents)
print("Sequence 1:", "(Length:", s.len(), ")", s,)
print("Bases: ", s.count())
print("Rev:", s.reverse())
print("Comp:", s.complement())

