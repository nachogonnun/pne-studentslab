import http.client
import json
from e2 import GENES
from Seq1 import *


def info_seq(seq):
    response = ""
    bases = seq.count()
    max_base = max(bases, key=bases.get)
    print("Total length:", seq.len())

    for base, number in bases.items():
        percentage = round((number / seq.len() * 100), 1)
        print(f"{base}: {number} ({percentage}%)")
        response += f"{base}: {number} ({percentage} %)\n"

    print("Most frequent base: " + max_base)
    return response


for gene, id_gene in GENES.items():
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/" + id_gene + "?content-type=application/json"
    URL = SERVER + ENDPOINT
    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT)
    response = conn.getresponse()
    data = response.read().decode("utf-8")

    print(f"Response received!: {response.status} {response.reason}")
    print()

    try:
        info = json.loads(data)
        sequence = info["seq"]
        s = Seq(sequence)
        print(f"Gene: {gene}")
        print(f"Description: {info["desc"]}")
        info_seq(s)
        print()

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
