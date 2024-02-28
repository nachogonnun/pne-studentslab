from Client0 import *
from Seq1 import *
from pathlib import Path

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
print()

IP = "212.128.255.64"
PORT = 8081
genes = ["U5", "ADA", "FRAT1"]

c = Client(IP, PORT)
print(c)

for gene in genes:
    FILENAME = "../S04/sequences/" + str(gene) + ".txt"
    file_contents = Path(FILENAME).read_text()
    s = Seq()
    sequence = s.read_fasta(file_contents)
    print(f"Sending {gene} GENE to the server...")
    print(f"From client: {sequence}")
    print("To server:", c.talk("Hi"))


