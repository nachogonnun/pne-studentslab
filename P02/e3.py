from Client0 import *

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
print()

IP = "212.128.255.94"
PORT = 8081

c = Client(IP, PORT)
print(c)
print("Sending a message to the server...")
response = c.talk("HI!!!")
print(f"Response: {response}")
