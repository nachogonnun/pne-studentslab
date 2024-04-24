import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552?content-type=application/json"
URL = SERVER + ENDPOINT

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")


conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT)
response = conn.getresponse()
data = response.read().decode("utf-8")

print(f"Response received!: {response.status} {response.reason}")

try:
    info = json.loads(data)
    print("Gene: MIR633")
    print("Description:", info["desc"])
    print("Sequence:", info["seq"])
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()