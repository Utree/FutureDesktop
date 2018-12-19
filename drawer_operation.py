import RPi.GPIO as GPIO
import time

class DrawerOperator:
    def __init__(self):
        self.gpio_manip = 4
        
    def setup(self):
        GPIO.setup(self.gp_manip, GPIO.OUT)
        self.servo = GPIO.PRM(self.gpio_manip)

    def lock(self):
        self.servo.start(0)
        self.servo.ChangeDutyCycle(2.5)
        time.sleep(1)
        self.servo.stop()

    def unlock(self):
        self.servo.start(0)
        self.servo.ChangeDutyCycle(7.25)
        time.sleep(1)
        self.servo.stop()

    def cleanUpGPIO(self):
        GPIO.cleanup()
