from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, BeaconEvent,
)

# DB操作用モジュール
from db_controller import search_last_user, update_login_time, update_snack, search_snack, add_user, search_user
# サーボモーター操作用モジュール
from servo_controller import lock, unlock

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# LINEボットからのリクエストをハンドリング
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# テキストメッセージが来た場合の処理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # ユーザー名を取得
    profile = line_bot_api.get_profile(event.source.user_id)

    # メッセージ内容のハンドリング
    if(event.message.text == "ロック"):
        lock()
    elif(event.message.text == "解除"):
        unlock()
    else:
        # レスポンスを返す
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(profile.display_name) + "さんこんにちは"))

# ビーコンメッセージが来た場合の処理
@handler.add(BeaconEvent)
def handle_beacon(event):
    # デバイス名
    device_name = "名無し"
    # ラスパイのhwid
    if(event.beacon.hwid == '01202d8c16'):
        device_name = "ラズパイ"

    # 新規ユーザーか確認する
    if(search_user(event.source.user_id)):
        pass
    else:
        # 新規ユーザーの場合、追加する
        add_user(event.source.user_id)
    # ログイン履歴をつける
    update_login_time(event.source.user_id)

    # ユーザー名を取得
    profile = line_bot_api.get_profile(event.source.user_id)
    # レスポンスを返す
    line_bot_api.reply_message(
        event.reply_token,[
            TextSendMessage(text='{} さんようこそ。{}にログインしました'.format(profile.display_name, device_name)),
        ]
    )

@app.route('/lock/')
def hello1():
    lock()
    return "locked"

@app.route('/unlock/')
def hello2():
    unlock()
    return "unlocked"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)
