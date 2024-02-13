class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")
    def __str__(self):
        return self.strbases

    def check_base(self):
        bases = ["A", "C", "G", "T"]
        for i in self.strbases:
            if i not in bases:
                return "ERROR!!"
        return "New sequence created!!"



s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
