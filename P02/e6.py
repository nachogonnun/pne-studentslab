from Client0 import *
from Seq1 import *
from pathlib import Path

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
print()

IP = "127.0.0.1"
PORT1 = 8081
PORT2 = 8080

c_even = Client(IP, PORT1)
c_odd = Client(IP, PORT2)

print(c_even)
print(c_odd)

FILENAME = "../S04/sequences/FRAT1.txt"
file_contents = Path(FILENAME).read_text()
s = Seq()
sequence = s.read_fasta(file_contents)
print("GENE FRAT1:", sequence)

segments = []
for i in range(0, len(sequence) + 1):
     segment = sequence[i:i + 10]
     segments.append(segment)
for i in segments[0:10]:
     msg = f"Segment {segments.index(i) + 1}: {i}"
     if segments.index(i) % 2 == 0:
          print(msg)
          print(c_even.talk(msg))
     else:
          print(msg)
          print(c_odd.talk(msg))