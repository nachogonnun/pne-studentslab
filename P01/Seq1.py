class Seq:

    def __init__(self, sequence=None):
        self.sequence = sequence
        if self.check_base() == "ERROR!!":
            print("INVALID SEQUENCE!")
            self.sequence = "ERROR"
        elif self.sequence == "NULL":
            print("NULL sequence created")
        else:
            print("New sequence created!")

    def __str__(self):
        return self.sequence

    def len(self):
        if self.sequence == "NULL" or self.sequence == "ERROR":
            return 0
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

    def check_base(self):
        bases = ["A", "C", "G", "T"]
        if self.sequence == "" or self.sequence is None:
            self.sequence = "NULL"
            return self.sequence
        for i in self.sequence:
            if i not in bases:
                return "ERROR!!"
        return self.sequence

    def count_base(self, base):
        return self.sequence.count(base)

    def count(self):
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for base in self.sequence:
            if base in bases:
                bases[base] += 1
        return bases

    def reverse(self):
        new_seq = ""
        if self.sequence == "NULL" or self.sequence == "ERROR":
            return self.sequence
        elif self.sequence == "Invalid sequence":
            return "ERROR"
        for c in range(len(self.sequence)):
            new_seq = self.sequence[c] + new_seq
        return new_seq

    def complement(self):
        complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement = ""
        if self.sequence == "Invalid sequence":
            return "ERROR"
        for base in self.sequence:
            complement += complement_bases.get(base, base)
        return complement

    def read_fasta(self, file_contents):
        body = file_contents.split("\n")
        self.sequence = ""
        for line in body[1:]:
            self.sequence += line.strip()
        return self.sequence

    def seq_count(self, base):
        return self.sequence.count(base)