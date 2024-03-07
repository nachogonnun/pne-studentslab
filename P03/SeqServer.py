import socket
from Seq1 import *
from pathlib import Path
class ServerSeq:
    def __init__(self):
        PORT = 8080
        IP = "192.168.0.20"

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

        elif msg.startswith("COMP"):
            return self.complement_response(msg)

        elif msg.startswith("COMP"):
            return self.complement_response(msg)

        elif msg.startswith("REV"):
            return self.reverve_response(msg)

        elif msg.startswith("GENE"):
            return self.gen_response(msg)
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

        response = ""
        sequence = Seq(msg.replace("INFO", "").strip())
        total_bases = sequence.len()
        print("INFO")
        print("Sequence:", sequence)
        print("Total length:", total_bases)
        for base, number in sequence.count().items():
            percentaje = number / total_bases * 100
            print(f"{base}: {number} ({percentaje}%)")
            response += f"{base}: {number} ({percentaje})\n"
        return response

    def complement_response(self, msg):
        sequence = Seq(msg.replace("COMP", "").strip())
        print("COMP")
        print(sequence.complement())
        return sequence.complement()

    def reverve_response(self, msg):
        sequence = Seq(msg.replace("REV", "").strip())
        print("REV")
        print(sequence.reverse())
        return sequence.reverse()

    def gen_response(self, msg):
        gene_name = msg.replace("GENE", "").strip()
        sequence = ""
        FILENAME = f"../S04/sequences/{gene_name}.txt"
        file_contents = Path(FILENAME).read_text()
        s = Seq()
        s.read_fasta(file_contents)
        print("GENE")
        print(str(s))
        return str(s)

server = ServerSeq()
print(server)