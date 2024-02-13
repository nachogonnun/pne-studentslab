class Seq:
    def __init__(self, sequence):
        self.sequence = sequence
    def print_seqs(seq_list):
        data = []
        for i in seq_list:
            index = seq_list.index(i)
            length = len(i.sequence)
            seq = i.sequence
            info = data.append((index, length, seq))
        return data

seqs = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
data = Seq.print_seqs(seqs)
for i, x, z in data:
    print(f"Sequence {i}: (Length: {x}) {z}")


