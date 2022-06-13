# SmartCS_API
コンソールサーバー SmartCS の API を利用したデモプログラムです。

# 動画デモ
https://youtu.be/qWMwl6M3-_8?t=2674

# サンプルプログラム

SmartCSのコンソールポート接続情報を調べるPythonプログラム

```
python check_tty_port.py
```

SmartCS経由でコンソール接続されているCisco Catalyst2960へshow versionコマンドを送信するPythonプログラム

```
python ttymanage_show_version.py
```

SmartCS経由でコンソール接続されているCisco Catalyst2960のIPアドレスを追加するPythonプログラム

```
python ttymanage_set_ip.py
```

# API サンプル
## /system/version
<GET>
curl -u api:api -X GET http://192.168.0.2:10080/api/v1/system/version | jq

python system-version.py 


## /users
現在、ログイン中のユーザ ( = 作業者一覧 ) を表示

GET

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/users | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/users/showint | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/users/login | jq```



POST

```curl -u api:api -X POST -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/users --data @./users-post.json``` 

PUT

```curl -u api:api -X PUT -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/users/abcdefghijklmn51 --data @./users-put.json```


DELETE

```curl -u api:api -X DELETE http://192.168.0.2:10080/api/v1/users/abcdefghijklmn51```


## /serial

GET

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/serial/tty | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/serial/tty/1 | jq```

PUT

```curl -u api:api -X PUT -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/serial/tty/10 --data @./tty-put.json```

POST

```curl -u api:api -X POST -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/serial/hangup/tty/10 -d "" ```


## /ttymanage

POST

```curl -u api:api -X POST -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/ttymanage -d @./cisco-ios.json | jq```

```python ttymanage.py```

```python ttymanage-extfile.py```


## /log/history

GET

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/command | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/command?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/command?lines=10 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/console | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/console?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/console?lines=5 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/ttysend/tty/1 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/ttysend/tty/1?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/ttysend/tty/?lines=20 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi?lines=3 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/webapi | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi?lines=3 | jq```


## /log/serial

GET

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/tty/1 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/tty/1?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/tty/1?lines=500 | jq```

```curl -u api:api -o serial-tty02.log -X GET http://192.168.0.2:10080/api/v1/log/serial/files/tty/1```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/search/tty/1?string=Version | jq```

```curl -u api:api -X GET "http://192.168.0.2:10080/api/v1/log/serial/search/tty/1?string=version&lines" | jq```

```curl -u api:api -X GET "http://192.168.0.2:10080/api/v1/log/serial/search/tty/1?string=version&lines=1" | jq```

```curl -u api:api -X GET "http://192.168.0.2:10080/api/v1/log/serial/search/tty/2?string=version&lines=3" | jq```
