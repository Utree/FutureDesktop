# 未来のデスクトップ -ラズパイ-

## TODO
1. server.pyを編集
> 20行目にアクセストークン、21行目にチャンネルシークレットを設定。
> https://developers.line.biz/ja/
>
> 詳しくは[LINE BOT SDK](https://github.com/line/line-bot-sdk-python)を参照

2. DBを設定
```
$ sqlite3 drawer.sqlite3
$ CREATE TABLE login_log(id integer primary key, line_id text, time TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')));
$ CREATE TABLE user(id integer primary key, line_id text UNIQUE, snack int DEFAULT 0);
```
3. サーボモータを設定
> 詳しくは[Qiita](https://qiita.com/DRM/items/52e2837236e5b87c2bdd)を確認

!["画像"](https://camo.qiitausercontent.com/e894487becb1672fb34e7523f9231e38bd7f4ae7/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3234363434372f36643530623662622d396337652d353738622d343630302d6233383663313636303931642e706e67)
4. 実行
```
$ sudo python3 ./server.py
```
5. ngrokを実行
> [ngrok](https://ngrok.com/)のサイトからダウンロードして、ポートを公開
```
$ ngrok http 8080
```
6. lineボットにURLをセット
