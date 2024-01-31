with open('dna.txt', "r") as file:
    sequence = ""
    for line in file:
        sequence += line
    sequence_first = sequence.find("\n")
    sequence = sequence[sequence_first:]
    sequence = sequence.replace("\n", "")

letters = {"A": 0, "C": 0, "G": 0, "T": 0}
for i in sequence:
    if i == "A":
        letters["A"] += 1
    elif i == "C":
        letters["C"] += 1
    elif i == "G":
        letters["G"] += 1
    elif i == "T":
        letters["T"] += 1

print("The user sequence:",sequence)
print("Total length:", len(sequence))
for letter, number in letters.items():
    print("{}: {}".format(letter, number))



