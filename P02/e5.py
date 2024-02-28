from Client0 import *
from Seq1 import *
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
print()

IP = "212.128.255.64"
PORT = 8081

c = Client(IP, PORT)
print(c)

FILENAME = "../S04/sequences/FRAT1.txt"
file_contents = Path(FILENAME).read_text()
s = Seq()
sequence = s.read_fasta(file_contents)
print("GENE FRAT1:", sequence)
for i in sequence:
     s_1 =
