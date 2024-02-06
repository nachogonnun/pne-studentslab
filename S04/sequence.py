from pathlib import Path
FILENAME = "sequences/ADA.txt"
# -- Open and read the file
file_contents = Path(FILENAME).read_text()
body = file_contents.split("\n")
total = 0
n = ["A", "C", "G, T"]
for i in body[1:]:
    sequence = i
    for nucleotide in sequence:
        if nucleotide in n:
            total += 1
print(" The total number of nucleotides is: ", total)