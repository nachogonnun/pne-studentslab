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

    def read_fasta(self, file_contents):
        body = file_contents.split("\n")
        self.sequence = ""
        for line in body[1:]:
            self.sequence += line.strip()
        return self.sequence
    def seq_count(self, base):
        return self.sequence.count(base)

from pathlib import Path
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for gene in genes:
    filename = "../S04/sequences/" + gene + ".txt"
    file_contents = Path(filename).read_text()
    seq = Seq(file_contents.replace("\n", ""))
    seq.read_fasta(file_contents)
    max_base = max(bases, key= lambda base: seq.seq_count(base))
    count = seq.seq_count(max_base)
    print("Gene {} most common nucleotide is {} ({})".format(gene, max_base, count))