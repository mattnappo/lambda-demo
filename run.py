import requests
import json

url = 'https://31l562n36c.execute-api.us-east-2.amazonaws.com/default/tokgen/generate'

obj = {
    'message': 'hello',
    'time': '11/04/23',
}

res = requests.get(url, data=json.dumps(obj))
print(json.dumps(res.json(), indent=2))

