import json,requests

url = 'http://192.168.0.2:10080/api/v1/system/version'
res = requests.get(url, auth=('api', 'api'))

if res.status_code == 200:
    print('connection ok')
    data = res.json()
    print(json.dumps(data, indent=2))

else:
    print('connection error')