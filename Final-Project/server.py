import http.server
import http.client
import json
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import *

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


def get_connection(endpoint):
    SERVER = "rest.ensembl.org"
    PARAMS = "content-type=application/json"
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", endpoint + PARAMS)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    return data

def get_gene_info(gene):
    gene_id_info = get_connection("/lookup/symbol/human/" + gene + "?")
    gene_id_info_2 = json.loads(gene_id_info)
    gene_id = gene_id_info_2["id"]
    region = gene_id_info_2["seq_region_name"]
    start = gene_id_info_2["start"]
    end = gene_id_info_2["end"]
    gene_seq_info = get_connection("/sequence/id/" + gene_id + "?")
    gene_seq_info_2 = json.loads(gene_seq_info)
    sequence = gene_seq_info_2["seq"]
    return gene_id, sequence, region, start, end

def info_seq(seq):
    response = ""
    response += f"Total length:{seq.len()}<br>"
    for base, number in seq.count().items():
        percentage = round(number / seq.len() * 100, 2)
        print(f"{base}: {number} ({percentage}%)")
        response += f"{base}: {number} ({percentage} %)<br>"
    return response


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
                data = get_connection("/info/species?")

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
                data_1 = get_connection("/info/species?")
                info_1 = json.loads(data_1)
                data_2 = get_connection("/info/assembly/" + url_name + "?")

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
                data_1 = get_connection("/info/species?")
                info_1 = json.loads(data_1)
                data_2 = get_connection("/info/assembly/" + url_name + "?")
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
            gene = arguments["gene"][0]
            gene_id, sequence, region, start, end = get_gene_info(gene)
            contents = read_html_file("html/geneSeq.html").render(
                context={"seq": sequence, "gene": gene})
        elif path == "/geneInfo":
            gene = arguments["gene"][0]
            gene_id, sequence, region, start, end = get_gene_info(gene)
            contents = read_html_file("html/geneInfo.html").render(
                context={"seq": sequence, "start": start, "end": end, "id": gene_id, "gene": gene, "loc": region,
                         "len": len(sequence)})
        elif path == "/geneCalc":
            gene = arguments["gene"][0]
            gene_id, sequence, region, start, end = get_gene_info(gene)
            seq = Seq(sequence)
            contents = read_html_file("html/geneCalc.html").render(
                context={"seq": info_seq(seq), "gene": gene})
        elif path == "/geneList":
            gene_list = []
            chromosome = arguments["chromo"][0]
            startpoint = arguments["start"][0]
            endpoint = arguments["end"][0]
            genes_data = get_connection(
                "/overlap/region/human/" + chromosome + ":" + startpoint + "-" + endpoint + "?feature=gene&")
            gene_info = json.loads(genes_data)
            for genes in gene_info:
                gene_list.append(genes["external_name"])
            contents = read_html_file("html/geneList.html").render(
                context={"list": gene_list, "start": startpoint, "end": endpoint})
        # <----------------------| MEDIUM LEVEL |---------------------->
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
