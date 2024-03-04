from Client0 import *
from Seq1 import *
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
print()

IP = "212.128.255.102"
PORT = 8081

c = Client(IP, PORT)
print(c)

FILENAME = "../S04/sequences/FRAT1.txt"
file_contents = Path(FILENAME).read_text()
s = Seq()
sequence = s.read_fasta(file_contents)
print("GENE FRAT1:", sequence)
segments = []
for i in range(0, len(sequence) + 1):
     segment = sequence[i:i + 10]
     segments.append(segment)
for i in segments[0:5]:
     msg = f"Segment {segments.index(i) + 1}: {i}"
     print(msg)
     print(c.talk(msg))
