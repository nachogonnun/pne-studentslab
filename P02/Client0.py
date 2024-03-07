class Client:
    def __init__(self, ip=None, port=None):
        self.port = int(port)
        self.ip = str(ip)
    def __str__(self):
        return f"Connection to SERVER at {self.ip} , PORT: {self.port}"

    def ping(self):
        print("OK!!")

    def talk(self, msg):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(str(msg)))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response

