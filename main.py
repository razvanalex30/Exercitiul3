import requests
import pprint
# import json
r = requests.get("https://official-joke-api.appspot.com/random_joke")
print(r.status_code)
# pprint.pprint(r.text)
pprint.pprint(r.json())

