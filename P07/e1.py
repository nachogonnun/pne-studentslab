import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")


conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()
data = response.read().decode("utf-8")

print(f"Response recived!: {response.status} {response.reason}")

try:
    ping = json.loads(data)
    if ping["ping"] == 1:
        print("PING OK THE SERVER IS RUNNING!")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

