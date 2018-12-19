# -*- coding: utf-8 -*-
"""servo_controller docstrings.

サーボモータ操作用のモジュールです

Author: Yuki SEKIYA
Date: 2018/12/18

Example:
    使用例
        $ python -m `from servo_controller import `

Todo:
    PINをよしなに変更してください。

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""
import RPi.GPIO as GPIO
import time

# GPIOのピン番号
PIN=18

def lock():
    """ロック

    引き出しをロックします
    """
    # GPIO番号でピンを指定する設定にセット
    GPIO.setmode(GPIO.BCM)
    # GPIOの入出力設定 18番をOUTにする
    GPIO.setup(PIN,GPIO.OUT)
    # PWMの設定
    servo=GPIO.PWM(PIN,60)

    # PWMの開始
    servo.start(12.5)
    # ロック
    servo.ChangeDutyCycle(6)
    # sleep(調整用)
    time.sleep(1)
    # 終了
    servo.stop()
    GPIO.cleanup()

def unlock():
    """ロック解除

    引き出しのロックを解除します
    """
    # GPIO番号でピンを指定する設定にセット
    GPIO.setmode(GPIO.BCM)
    # GPIOの入出力設定 18番をOUTにする
    GPIO.setup(PIN,GPIO.OUT)
    # PWMの設定
    servo=GPIO.PWM(PIN,60)

    # PWMの開始
    servo.start(12.5)
    # ロック
    servo.ChangeDutyCycle(12.5)
    # sleep(調整用)
    time.sleep(1)
    # 終了
    servo.stop()
    GPIO.cleanup()
