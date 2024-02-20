from Seq1 import *

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")

print("Sequence 1:", "(Length:", seq1.len(), ")", seq1,)
print("A:", seq1.count_base("A"), "C:", seq1.count_base("C"), "G:", seq1.count_base("G"), "T:", seq1.count_base("T"))
print("Sequence 2: ", "(Length:", seq2.len(), ")", seq2)
print("A:", seq2.count_base("A"), "C:", seq2.count_base("C"), "G:", seq2.count_base("G"), "T:", seq2.count_base("T"))
print("Sequence 3: ", "(Length:", seq3.len(), ")", seq3)
print("A:", seq3.count_base("A"), "C:", seq3.count_base("C"), "G:", seq3.count_base("G"), "T:", seq3.count_base("T"))