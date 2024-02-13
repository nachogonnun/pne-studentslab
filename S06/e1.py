class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        if self.check_base() == "ERROR!!":
            print("ERROR")
        else:
            print("New sequence created!")
    def __str__(self):
        return self.strbases

    def check_base(self):
        bases = ["A", "C", "G", "T"]
        for i in self.strbases:
            if i not in bases:
                return "ERROR!!"
        return self.strbases



s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1.check_base()}")
print(f"Sequence 2: {s2.check_base()}")
