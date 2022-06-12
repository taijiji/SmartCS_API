import json,requests

url = 'http://192.168.0.2:10080/api/v1/ttymanage'
json_data = {
	"tty": 1,
	"nl": "cr",
	"cmd_timeout": 30,
	"recvchar": [
			"Switch>",
			"Switch#",
			"Press RETURN to get started."
	],
	"recvchar_regex": [
			"[Uu]sername:",
			"[Pp]assword:",
			"(^|\\r|\\n|!)[a-zA-Z0-9_().-]*(>|#) "
	],
	"sendchar": [
			"__NL__",
			"showint",
			"showint",
			"enable",
			"enable",
			"terminal length 0",
			"show version",
			"show license",
			"show env all",
			"show process cpu __WAIT__:60",
			"show process memory __WAIT__:60",
			"show flash",
			"show clock",
			"show running-config",
			"exit"
	]
}

res = requests.post(
		url,
		auth=('api', 'api'),
		data=json.dumps(json_data),
		timeout=(3.0, 300.0)	#connectT.O.=3s, readT.O.=300
)

if res.status_code == 200:
    print('connection ok')
    data = res.json()
    print(json.dumps(data, indent=2))

else:
    print('connection error')