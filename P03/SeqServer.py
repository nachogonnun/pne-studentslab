import socket
from Seq1 import *
class ServerSeq:

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

    def return_response(self, msg):
        if msg.startswith("PING"):
            return self.ping_response()

        elif msg.startswith("GET"):
            return self.get_response(msg)

        elif msg.startswith("INFO"):
            return self.info_response(msg)

        else:
            return "Unknown command"
    def ping_response(self):
        print("Ping command!")
        return "OK!\n"

    def get_response(self, msg):
        sequences = ["ACGTACGT", "ACCTTCCA", "TGGCAACG", "ACGGTGCT"]
        for i in msg:
            if i.isdigit():
                if 0 <= int(i) <= 3:
                    n = sequences[int(i)]
                    print("GET")
                    print(n)
                    return n + "\n"
            else:
                return "Invalid command!"
    def info_response(self, msg):
        base = ["A", "C", "G", "T"]
        sequence = Seq(msg.replace("INFO", "").strip())
        print("INFO")
        print("Sequence:", sequence)
        print("Total length:", sequence.len())
        info = sequence.count()
        print(info)
        return info


server = ServerSeq()
print(server)