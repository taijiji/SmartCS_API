import json,requests

url = 'http://192.168.0.2:10080/api/v1/ttymanage'

with open('cisco-ios.json') as json_file:
	json_data = json.load(json_file)

res = requests.post(
		url,
		auth = ('api', 'api'),
		data = json.dumps(json_data),
		timeout = (3.0, 300.0)	#connectT.O.=3s, readT.O.=300
)

if res.status_code == 200:
    print('connection ok')
    data = res.json()
    print(json.dumps(data, indent=2))

else:
    print('connection error')