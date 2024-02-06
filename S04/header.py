from pathlib import Path
FILENAME = "sequences/RNU6_269P.txt"
# -- Open and read the file
file_contents = Path(FILENAME).read_text()

header = file_contents.split("\n")
print("The first line of the sequence of that genes is: ")
print(header[0])