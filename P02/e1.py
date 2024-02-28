from Client0 import *

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
print()

IP = "212.128.255.94"
PORT = 8080

c = Client(IP, PORT)
c.ping()