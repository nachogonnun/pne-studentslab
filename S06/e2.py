class Seq:
    """A class for representing sequences"""

    def __init__(self, sequence):
        self.sequence = sequence


    def print_seqs(seq_list):
        data = []
        for i in seq_list:
            index = seq_list.index(i)
            length = len(i.sequence)
            seq = i.sequence
            data.append((index, length, seq))
        return data

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
info = Seq.print_seqs(seq_list)
for i, l, s in info:
    print(f"Sequence {i}: (Length: {l}) {s}")