from SeqServer import *
from Client0 import *

print("-------PRACTICE 3 EXERCISE 7--------")

IP = "192.168.0.20"
PORT = 8080

c = Client(IP, PORT)

print("* Testing PING...")
c.ping()
print()

print("* Testing GET...")
c.talk("GET 0")


