# -*- coding: utf-8 -*-
"""db_controller docstrings.

DB操作用のモジュールです

Author: Yuki SEKIYA
Date: 2018/12/18

Example:
    使用例
        $ python -m `from db_controller import `

Todo:
    DB_PATHをよしなに変更してください。

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""
import sqlite3


# データベースファイルのパス
DB_PATH = 'drawer.sqlite3'


def search_user(user_id: str) -> bool:
    """ユーザー検索

    ユーザーIDをuserテーブルから探す

    Args:
        user_id (str): LINEから送られてくるuser_id

    Raises:
        sqlite3.Error occurred:

    Returns:
        bool: 該当者がいた場合はTrue、いない場合はFalse。
    """

    # データベース接続
    connection = sqlite3.connect(DB_PATH)
    # カーソル生成
    cursor = connection.cursor()

    # 結果
    result = None

    try:
        # 検索
        cursor.execute('SELECT * FROM user WHERE line_id=?', (user_id,))
    except sqlite3.Error as e:
        # 例外処理
        print('sqlite3.Error occurred:', e.args[0])

    # 結果を保存
    result = cursor.fetchone()[0]

    # 保存
    connection.commit()
    # 接続を閉じる
    connection.close()

    if result != None:
        return True
    else:
        return False


def add_user(user_id: str) -> None:
    """ユーザー追加

    ユーザーIDをuserテーブルに追加する

    Args:
        user_id (str): LINEから送られてくるuser_id

    Raises:
        sqlite3.Error occurred:

    Returns:
        None
    """

    # データベース接続
    connection = sqlite3.connect(DB_PATH)
    # カーソル生成
    cursor = connection.cursor()

    try:
        # 追加
        cursor.execute("INSERT INTO user(line_id) VALUES('%s')" % (user_id))
    except sqlite3.Error as e:
        # 例外処理
        print('sqlite3.Error occurred:', e.args[0])

    # 保存
    connection.commit()
    # 接続を閉じる
    connection.close()


def search_snack(user_id: str) -> int:
    """おかしの取得

    ユーザーIDに紐付けられているおかしの情報を取得
    0: チロルチョコ, 1: ハイチュー

    Args:
        user_id (str): LINEから送られてくるuser_id

    Raises:
        sqlite3.Error occurred:

    Returns:
        snack (int): 設定したおかし 0: チロルチョコ, 1: ハイチュー
    """

    # データベース接続
    connection = sqlite3.connect(DB_PATH)
    # カーソル生成
    cursor = connection.cursor()

    # 結果
    result = 0

    try:
        # 検索
        cursor.execute('SELECT snack FROM user WHERE line_id=?', (user_id,))
    except sqlite3.Error as e:
        # 例外処理
        print('sqlite3.Error occurred:', e.args[0])

    # 結果を保存
    result = int(cursor.fetchone()[0])

    # 保存
    connection.commit()
    # 接続を閉じる
    connection.close()

    return result


def update_snack(user_id: str, snack: int) -> None:
    """おかしの更新

    ユーザーIDに紐付けられているおかしの情報を更新
    0: チロルチョコ, 1: ハイチュー

    Args:
        user_id (str): LINEから送られてくるuser_id
        snack (int): おかし 0: チロルチョコ, 1: ハイチュー

    Raises:
        sqlite3.Error occurred:

    Returns:
        None
    """

    # データベース接続
    connection = sqlite3.connect(DB_PATH)
    # カーソル生成
    cursor = connection.cursor()

    try:
        # 更新
        cursor.execute('UPDATE user SET snack=? WHERE line_id=?', (snack, user_id))
    except sqlite3.Error as e:
        # 例外処理
        print('sqlite3.Error occurred:', e.args[0])

    # 保存
    connection.commit()
    # 接続を閉じる
    connection.close()


def update_login_time(user_id: str) -> None:
    """ログイン履歴をつける

    ログイン履歴をつける

    Args:
        user_id (str): LINEから送られてくるuser_id

    Raises:
        sqlite3.Error occurred:

    Returns:
        None
    """

    # データベース接続
    connection = sqlite3.connect(DB_PATH)
    # カーソル生成
    cursor = connection.cursor()

    try:
        # 追加
        cursor.execute("INSERT INTO login_log(line_id) VALUES('%s')" % (user_id))
    except sqlite3.Error as e:
        # 例外処理
        print('sqlite3.Error occurred:', e.args[0])

    # 保存
    connection.commit()
    # 接続を閉じる
    connection.close()


def search_last_user() -> str:
    """最終ログインユーザーを検索

    最後に引き出しにアクセスしたユーザーを検索する

    Args:

    Raises:
        sqlite3.Error occurred:

    Returns:
        user_id (str): LINEから送られてくるuser_id
    """

    # データベース接続
    connection = sqlite3.connect(DB_PATH)
    # カーソル生成
    cursor = connection.cursor()

    # 結果
    result = ""

    try:
        # 検索
        cursor.execute('SELECT line_id FROM login_log ORDER BY time DESC LIMIT 1')
    except sqlite3.Error as e:
        # 例外処理
        print('sqlite3.Error occurred:', e.args[0])

    # 結果を保存
    result = cursor.fetchone()[0]

    # 保存
    connection.commit()
    # 接続を閉じる
    connection.close()

    return result
