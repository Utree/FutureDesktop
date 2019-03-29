from flask import Flask, request, abort

# DB操作用モジュール
from db_controller import search_last_user, update_login_time, update_snack, search_snack, add_user, search_user
# サーボモーター操作用モジュール
from servo_controller import lock, unlock

from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
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
