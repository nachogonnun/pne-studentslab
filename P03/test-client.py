
from Client0 import *

print("-------PRACTICE 3 EXERCISE 7--------")

IP = "192.168.0.20"
PORT = 8081

c = Client(IP, PORT)

print(c)

print("* Testing PING...")
c.ping()
print()

print("* Testing GET...")
for i in range(4):
    seq = c.talk(f"GET {str(i)}")
    print(f"GET {i}:", seq)

print("* Testing INFO...")
info = c.talk("INFO ACGTACGT")
print(info)

print("* Testing COMP...")
comp = c.talk("COMP ACGTACGT")
print("COMP:", comp)
print()
print("* Testing REV...")
rev = c.talk("REV ACGTACGT")
print("COMP:", rev)
print()

print("* Testing GENES...")
genes = ["U5", "ADA", "FXN", "FRAT1", "RNU6_269P"]
for gene in genes:
    seq = c.talk(f"GENE {gene}")
    print(f"Gene {gene}: {seq}")

