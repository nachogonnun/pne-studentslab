import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import *

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

def info_seq(seq):
    bases = "ACGT"
    response = ""
    response += f"Total length:{seq.len()}<br>"
    for base, number in seq.count().items():
        percentage = number / seq.len() * 100
        print(f"{base}: {number} ({percentage}%)")
        response += f"{base}: {number} ({percentage} %)<br>"
    return response



  # provide a dictionary to build the form


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        sequences = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
        genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
        if path == "/":
            contents = Path("html/index.html").read_text()
        elif path == "/ping":
            contents = Path("html/ping.html").read_text()

        elif path == "/get":
            contents = ""
            option = arguments.get("n")[0]
            for i in range(0, 5):
                if option == str(i):
                    contents = read_html_file("html/get.html").render(context={"todisplay": sequences[i], "option": option})

        elif path == "/gene":
            contents = ""
            final_sequence = ""
            gene = arguments.get("name")[0]
            for i in range(0, 5):
                if gene == genes[i]:
                    filename = "../S04/sequences/" + gene + ".txt"
                    sequence = Path(filename).read_text()
                    sequence = sequence.split("\n")[1:]
                    for line in sequence:
                        final_sequence += line
                    contents = read_html_file("html/gene.html").render(context={"todisplay": final_sequence[1:], "GENE": gene})

        elif path == "/operations":
            seq = Seq(arguments["sequence"][0])
            calculation = arguments["operation"][0]
            if calculation == "Rev":
                msg = seq.reverse()
                contents = read_html_file("html/operation.html").render(context={"todisplay": seq, "todisplay2": calculation, "todisplay3": msg})
            elif calculation == "Comp":
                msg = seq.complement()
                contents = read_html_file("html/operation.html").render(context={"todisplay": seq, "todisplay2": calculation, "todisplay3": msg})
            elif calculation == "Info":
                msg = info_seq(seq)
                contents = read_html_file("html/operation.html").render(context={"todisplay": seq, "todisplay2": calculation, "todisplay3": msg})
        else:
            contents = Path("html/error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()