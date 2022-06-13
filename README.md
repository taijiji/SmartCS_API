# SmartCS_API
コンソールサーバー SmartCS の API を利用したデモプログラムです。

# 動画デモ	
[![show int API が存在しないレガシー機器をネットワーク自動化する裏ワザ](http://img.youtube.com/vi/qWMwl6M3-_8/hqdefault.jpg)](https://youtu.be/qWMwl6M3-_8?t=2674)


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

# APIリソース

<html>
<body>
<table>
  <tr>
    <td style="text-align:left;">Category</td>
    <td style="text-align:left;">URL</td>
    <td style="text-align:left;">Method</td>
    <td style="text-align:left;">概要</td>
  </tr>
  <tr>
    <td style="text-align:left;">SYSTEM</td>
    <td style="text-align:left;">/system/version</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">システム情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;" rowspan="6">USERS</td>
    <td style="text-align:left;" rowspan="2">/users</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">ユーザ情報（一覧）の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;">POST</td>
    <td style="text-align:left;">ユーザ作成</td>
  </tr>
  <tr>
    <td style="text-align:left;" rowspan="3">/users/{username}</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">ユーザ情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;">PUT</td>
    <td style="text-align:left;">ユーザ情報の編集</td>
  </tr>
  <tr>
    <td style="text-align:left;">DELETE</td>
    <td style="text-align:left;">ユーザ削除</td>
  </tr>
  <tr>
    <td style="text-align:left;">/users/login</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">ログインユーザ情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;" rowspan="4">SERIAL</td>
    <td style="text-align:left;">/serial/tty</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">シリアル情報(一覧)の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;" rowspan="2">/serial/tty/{ttylist}</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">シリアル情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;">PUT</td>
    <td style="text-align:left;">シリアル情報の編集</td>
  </tr>
  <tr>
    <td style="text-align:left;">/serial/hangup/tty/{ttylist}</td>
    <td style="text-align:left;">POST</td>
    <td style="text-align:left;">シリアルのhangup</td>
  </tr>
  <tr>
    <td style="text-align:left;">TTYMANAGE</td>
    <td style="text-align:left;">/ttymanage</td>
    <td style="text-align:left;">POST</td>
    <td style="text-align:left;">TTYマネージ機能を使ってシリアルポートに<br>文字列の送受信スクリプトを実行</td>
  </tr>
  <tr>
    <td style="text-align:left;" rowspan="4">LOG/HISTORY</td>
    <td style="text-align:left;">/log/history/console</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">SmartCSのコンソールログ情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;">/log/history/command</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">SmartCSのコマンドログ情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;">/log/history/ttysend</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">SmartCSのttysendログ情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;">/log/history/webapi</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">SmartCSのwebapiログ情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;" rowspan="3">LOG/SERIAL</td>
    <td style="text-align:left;">/log/serial/tty/{ttyno} </td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">SmartCSのttyログ情報の取得</td>
  </tr>
  <tr>
    <td style="text-align:left;">/log/serial/files/tty/{ttyno}</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">SmartCSのttyログ情報の取得（DL）</td>
  </tr>
  <tr>
    <td style="text-align:left;">/log/serial/search/tty/{ttyno}</td>
    <td style="text-align:left;">GET</td>
    <td style="text-align:left;">SmartCSのttyログ情報を検索</td>
  </tr>
</table>
</body>
</html>


# 実行例

## /system/version

### GET （システム情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/system/version | jq```
#### python
```python system-version.py```


## /users

### GET　（ユーザ情報一覧の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/users | jq```

### POST　（ユーザ作成）
```curl -u api:api -X POST -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/users --data @./users-post.json``` 

## /users/{username}
### GET　（ユーザ情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/users/showint | jq```

### PUT　（ユーザ情報の編集）
#### curl
```curl -u api:api -X PUT -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/users/abcdefghijklmn51 --data @./users-put.json```

### DELETE　（ユーザ削除）
#### curl
```curl -u api:api -X DELETE http://192.168.0.2:10080/api/v1/users/abcdefghijklmn51```

## /users/login
### GET　（現在、ログイン中のユーザ ( = 作業者一覧 ) を表示）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/users/login | jq```


## /serial
### GET　（シリアル情報一覧の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/serial/tty | jq```

## /serial/tty/{ttylist}
### GET　（シリアル情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/serial/tty/1 | jq```

### PUT　（シリアル情報の編集）
#### curl
```curl -u api:api -X PUT -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/serial/tty/10 --data @./tty-put.json```

### POST　（シリアルのhangup）
#### curl
```curl -u api:api -X POST -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/serial/hangup/tty/10 -d "" ```

## /ttymanage
### POST　（シリアルポートに文字列の送受信スクリプトを実行）
#### curl
```curl -u api:api -X POST -H "Content-Type: application/json" http://192.168.0.2:10080/api/v1/ttymanage -d @./cisco-ios.json | jq```
#### python(1)
```python ttymanage.py```
#### python(2)
```python ttymanage-extfile.py```


## /log/history/console
### GET　（SmartCSのコンソールログ情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/console | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/console?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/console?lines=5 | jq```

## /log/history/command
### GET　（SmartCSのコマンドログ情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/command | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/command?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/command?lines=10 | jq```

## /log/history/ttysend
### GET　（SmartCSのttysendログ情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/ttysend/tty/1 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/ttysend/tty/1?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/ttysend/tty/?lines=20 | jq```

## /log/history/webapi
### GET　（SmartCSのwebapiログ情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/history/webapi?lines=3 | jq```


## /log/serial/tty/{ttyno}
### GET　（SmartCSのttyログ情報の取得）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/tty/1 | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/tty/1?lines=all | jq```

```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/tty/1?lines=500 | jq```

## /log/serial/files/tty/{ttyno}
### GET　（SmartCSのttyログ情報の取得（DL））
#### curl
```curl -u api:api -o serial-tty02.log -X GET http://192.168.0.2:10080/api/v1/log/serial/files/tty/1```

## /log/serial/search/tty/{ttyno}
### GET　（SmartCSのttyログ情報を検索）
#### curl
```curl -u api:api -X GET http://192.168.0.2:10080/api/v1/log/serial/search/tty/1?string=Version | jq```

```curl -u api:api -X GET "http://192.168.0.2:10080/api/v1/log/serial/search/tty/1?string=version&lines" | jq```

```curl -u api:api -X GET "http://192.168.0.2:10080/api/v1/log/serial/search/tty/1?string=version&lines=1" | jq```

```curl -u api:api -X GET "http://192.168.0.2:10080/api/v1/log/serial/search/tty/2?string=version&lines=3" | jq```
