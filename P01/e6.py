from Seq1 import *

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")

print("Sequence 1:", "(Length:", seq1.len(), ")", seq1,)
print("Bases: ", seq1.count())
print("Sequence 2: ", "(Length:", seq2.len(), ")", seq2)
print("Bases:", seq2.count())
print("Sequence 3: ", "(Length:", seq3.len(), ")", seq3)
print("Bases:", seq3.count())