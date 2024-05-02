import http.server
import http.client
import json
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


def get_connection(endpoint):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", endpoint + PARAMS)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    return data


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/":
            contents = Path("html/main.html").read_text()
        # <----------------------| BASIC LEVEL |---------------------->
        elif path == "/listSpecies":
            if "limit" not in arguments:
                contents = Path("html/error.html").read_text()
            else:
                data = get_connection("/info/species")

                try:
                    limit = arguments["limit"][0]
                    info_1 = json.loads(data)
                    total = len(info_1["species"])
                    if int(limit) <= total:
                        species = []
                        for i in range(int(limit)):
                            species.append(info_1["species"][i]["common_name"])
                        contents = read_html_file("html/listspecies.html").render(
                            context={"species": species, "len": total, "limit": limit})
                    else:
                        contents = Path("html/error.html").read_text()
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
        elif path == "/karyotype":
            if "species" not in arguments:
                contents = Path("html/error.html").read_text()
            else:
                name_specie = arguments["species"][0]
                url_name = name_specie.replace(" ", "%20")
                data_1 = get_connection("/info/species")
                info_1 = json.loads(data_1)
                data_2 = get_connection("/info/assembly/" + url_name)

                try:
                    species_names = []
                    for specie in info_1["species"]:
                        species_names.append(specie["common_name"])
                    if name_specie in species_names:
                        info_2 = json.loads(data_2)
                        karyotype = info_2["karyotype"]
                        contents = read_html_file("html/karyotype.html").render(
                            context={"k": karyotype, "name": name_specie})
                    else:
                        contents = Path("html/error.html").read_text()
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
        elif path == "/chromosomeLength":
            if "species" not in arguments or "chromo" not in arguments:
                contents = Path("html/error.html").read_text()
            else:
                name_specie2 = arguments["species"][0]
                chromosome = arguments["chromo"][0]
                url_name = name_specie2.replace(" ", "%20")
                data_1 = get_connection("/info/species")
                info_1 = json.loads(data_1)
                data_2 = get_connection("/info/assembly/" + url_name)
                try:
                    species_names2 = []
                    for specie in info_1["species"]:
                        species_names2.append(specie["common_name"])
                        if name_specie2 in species_names2:
                            info_3 = json.loads(data_2)
                            for c in info_3["top_level_region"]:
                                if c["coord_system"] == "chromosome" and chromosome == c["name"]:
                                    contents = read_html_file("html/chromosomelength.html").render(
                                        context={"len": c["length"]})
                        else:
                            contents = Path("html/error.html").read_text()
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
        # <----------------------| BASIC LEVEL |---------------------->
        # <----------------------| MEDIUM LEVEL |---------------------->
        elif path == "/geneSeq":

            print()
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


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
