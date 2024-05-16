import http.client
import json

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

URLS = [
    "/listSpecies?json=1",
    "/listSpecies?limit=10&json=1",
    "/karyotype?species=Shrew+mouse&json=1",
    "/chromosomeLength?species=mouse&chromo=18&json=1",
    "/geneSeq?gene=FRAT1&json=1",
    "/geneInfo?gene=FRAT1&json=1",
    "/geneCalc?gene=FRAT1&json=1",
    "/geneList?chromo=9&start=22125500&end=22136000&json=1"
]

for url in URLS:

    conn.request("GET", url)

    response = conn.getresponse()

    print(f"Response received!: {response.status} {response.reason}\n")

    server_information = response.read().decode("utf-8")

    json_object = json.loads(server_information)
    print("Data received from IGNACIO'S server:")
    print()
    print(json.dumps(json_object, indent=4))
