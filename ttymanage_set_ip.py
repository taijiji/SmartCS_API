import json,requests

url = 'http://192.168.0.2:10080/api/v1/ttymanage'
json_data = {
	"tty": 1,
	"nl": "cr",
	"cmd_timeout": 30,
	"recvchar": [
			"Switch>",
			"Switch#",
			"Switch(config)#",
			"Switch(config-vlan)#",
			"Switch(config-if)#",
			"Press RETURN to get started."
	],
	"recvchar_regex": [
			"[Uu]sername:",
			"[Pp]assword:",
			"(^|\\r|\\n|!)[a-zA-Z0-9_().-]*(>|#) "
	],
	"sendchar": [
			"__NL__",
			"enable",
			"terminal length 0",
			"configure terminal",
			" vlan 100,200",
			" interface GigabitEthernet0/1",
			"  switchport access vlan 100",
 			"  switchport mode access",
			"  exit",
			" interface Vlan100",
 			"  ip address 192.168.1.254 255.255.255.0",
			"  no ip route-cache",
 			"  exit",
			" exit",
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