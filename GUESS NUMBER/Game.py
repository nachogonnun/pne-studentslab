import socket
import random

class NumberGuesser:
    def __init__(self, secret_number):

        self.secret_number = secret_number
        self.attempts = []
        self.number_attempts = 0

        PORT = 8081
        IP = "127.0.0.1"

        gs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            gs.bind((IP, PORT))
            gs.listen()
            print("STARTING THE GUESSING NUMBER GAME")
            while True:
                print("Waiting the player for its number")
                client_socket, addr = gs.accept()
                client_number = int(client_socket.recv(2048).decode("utf-8"))
                response = self.guess(client_number)
                client_socket.send(response.encode())
                client_socket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            gs.close()

    def guess(self, client_number):

        n = int(client_number)
        flag = True

        if 0 <= n <= 100:
            while flag:
                if n == self.secret_number:
                    flag = False
                    return "THAT IS THE NUMBER CONGRATULATIONS!!!" + "\n"

                elif n != self.secret_number and n < self.secret_number:
                    self.attempts.append(n)
                    self.number_attempts += 1
                    return f" HIGHER ({self.number_attempts}). Attempts: [{', '.join(map(str, self.attempts))}]" + "\n"
                elif n != self.secret_number and n > self.secret_number:
                    self.attempts.append(n)
                    self.number_attempts += 1
                    return f" LOWER ({self.number_attempts}). Attempts: [{', '.join(map(str, self.attempts))}]" + "\n"
        else:
            return "NUMBER OUT OF RANGE!!" + "\n"


secret_number = random.randint(1, 100)
game = NumberGuesser(secret_number)