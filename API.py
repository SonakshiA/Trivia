import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")
text = json.dumps(response.json(), sort_keys=True)
dict= json.loads(text)