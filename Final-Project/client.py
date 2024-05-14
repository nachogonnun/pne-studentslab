import http.client
import json

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

url_s = "/listSpecies?json=1"
url_s2 = "/listSpecies?limit=1&json=1"
url_k = "/karyotype?species=Shrew+mouse&json=1"
url_c = "/chromosomeLength?species=mouse&chromo=18&json=1"
url_seq = "/geneSeq?gene=FRAT1&json=1"
url_info = "/geneInfo?gene=FRAT1&json=1"
url_calc = "/geneCalc?gene=FRAT1&json=1"
url_list = "/geneList?chromo=9&start=22125500&end=22136000&json=1"

conn.request("GET", url_list)

response = conn.getresponse()

print(f"Response received!: {response.status} {response.reason}\n")

server_information = response.read().decode("utf-8")

json_object = json.loads(server_information)
print("Data received from IGNACIO'S server:")
print()
print(json.dumps(json_object, indent=4))
