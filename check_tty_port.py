import json,requests


url = 'http://192.168.0.2:10080/api/v1/serial/tty'

res = requests.get(url, auth=('api', 'api'))

data = res.json()
print(json.dumps(data, indent=2))