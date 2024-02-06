from pathlib import Path

FILENAME = "sequences/U5.txt"
# -- Open and read the file
file_contents = Path(FILENAME).read_text()

body = file_contents.split("\n")
print("The body of the U5 gene is:")
for i in body[1:]:
    print(i)