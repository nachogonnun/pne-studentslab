from pathlib import Path

FILENAME = "sequences/U5.txt"

file_contents = Path(FILENAME).read_text()

body = file_contents.split("\n")
print("The body of the U5 gene is:")
for i in body[1:21]:
    print(i)