class Seq:
    """A class for representing sequences"""

    def __init__(self, sequence):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.sequence = sequence
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.sequence

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.sequence)

    def print_seqs(seq_list):
        data = []
        for i in seq_list:
            index = seq_list.index(i)
            length = len(i.sequence)
            seq = i.sequence
            data.append((index, length, seq))
        for i, x, l in data:
            print(f"Sequence {i}: (Length: {x}) {l}")