import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.94" # this IP address is local, so only requests from the same machine are possible

number_con = 0
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    number_con += 1
    (rs, address) = ls.accept()
    print(f"CONNECTION {number_con}: {address}")

    msg = rs.recv(2048).decode("utf-8")
    print("Message from the client:", msg)

    mes2 = f"ECHO: {msg}"
    rs.send(mes2.encode())

    rs.close()
    # -- Close the socket
ls.close()