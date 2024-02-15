class Seq:

    def __init__(self, sequence = None):
        self.sequence = sequence
        if self.check_base() == "ERROR!!":
            print("INVALID SEQUENCE!")
        elif self.sequence == "NULL":
            print("Null sequence created")
        else:
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.sequence

    def check_base(self):
        bases = ["A", "C", "G", "T"]
        if self.sequence == "" or self.sequence is None:
            self.sequence = "NULL"
            return self.sequence
        for i in self.sequence:
            if i not in bases:
                self.sequence = "ERROR!!"
        return self.sequence
    def len(self):
        if self.sequence == "NULL" or self.sequence == "ERROR!!":
            return 0
        return len(self.sequence)

    def count(self):
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for base in self.sequence:
            if base in bases:
                bases[base] += 1
        return bases

    def reverse(self):
        new_seq = ""
        if self.sequence == "NULL" or self.sequence == "ERROR!!":
            return self.sequence
        for c in range(len(self.sequence)):
            new_seq = self.sequence[c] + new_seq
        return new_seq

    def complement(self):
        complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement = ""
        for base in self.sequence:
            complement += complement_bases.get(base, base)
        return complement

seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")

print("Sequence 1:", "(Length:", seq1.len(), ")", seq1,)
print("Bases: ", seq1.count())
print("Rev:", seq1.reverse())
print("Comp:", seq1.complement())
print("Sequence 2: ", "(Length:", seq2.len(), ")", seq2)
print("Bases:", seq2.count())
print("Rev:", seq2.reverse())
print("Comp:", seq2.complement())
print("Sequence 3: ", "(Length:", seq3.len(), ")", seq3)
print("Bases:", seq3.count())
print("Rev:", seq3.reverse())
print("Comp:", seq3.complement())