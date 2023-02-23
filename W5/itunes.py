import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit("Mention the artist while running file")

request = requests.get(f"https://itunes.apple.com/search?entity=song&limit=10&term= {sys.argv[1]}")

json = request.json()

for result in json["results"]:
    print(result["trackName"])
