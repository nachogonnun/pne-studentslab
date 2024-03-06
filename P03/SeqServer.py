import socket

class ServerSeq:

    def ping(self):
        print("Ping command!")
        return "OK!"

    def return_response(self, msg):
        if msg == "PING":
            print("PING")
            return self.ping()
        else:
            return "Unknown command"

    def __init__(self):
        PORT = 8081
        IP = "127.0.0.1"

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_socket.bind((IP, PORT))
            server_socket.listen()
            print("Seq Server configured!")
            while True:
                print("Waiting for clients...")
                (client_socket, address) = server_socket.accept()

                msg = client_socket.recv(2048).decode("utf-8")

                response = self.return_response(str(msg))
                send_bytes = str.encode(response)
                client_socket.send(send_bytes)
                client_socket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            server_socket.close()


server = ServerSeq()
print(server)

