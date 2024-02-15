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

    def count_base(self, base):
        return self.sequence.count(base)

seq1 = Seq()
seq2 = Seq("TACTA")
seq3 = Seq("Invalid sequence")

print("Sequence 1:", "(Length:", seq1.len(), ")", seq1,)
print("A:", seq1.count_base("A"), "C:", seq1.count_base("C"), "G:", seq1.count_base("G"), "T:", seq1.count_base("T"))
print("Sequence 2: ", "(Length:", seq2.len(), ")", seq2)
print("A:", seq2.count_base("A"), "C:", seq2.count_base("C"), "G:", seq2.count_base("G"), "T:", seq2.count_base("T"))
print("Sequence 3: ", "(Length:", seq3.len(), ")", seq3)
print("A:", seq3.count_base("A"), "C:", seq3.count_base("C"), "G:", seq3.count_base("G"), "T:", seq3.count_base("T"))