import termcolor
class Seq:

    def __init__(self, sequence):
        self.sequence = sequence
        print("New sequence created!!")
    def print_seqs(seq_list, color):
        data = []
        for i in seq_list:
            index = seq_list.index(i)
            length = len(i.sequence)
            seq = i.sequence
            data.append((index, length, seq))
        for i, x, l in data:
            termcolor.cprint(f"Sequence {i}: (Length: {x}) {l}", color)
    def generate_seqs(pattern, number):
        seq = []
        for i in range(1, int(number) + 1):
            seq.append(Seq(pattern * i))

        return seq



seq_list1 = Seq.generate_seqs("A", 3)
seq_list2 = Seq.generate_seqs("AC", 5)

print("List 1:")
Seq.print_seqs(seq_list1, "blue")


print()
print("List 2:")
Seq.print_seqs(seq_list2, "green")
