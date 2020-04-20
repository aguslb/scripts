import RPi.GPIO as GPIO
import time

gpiOutput = 11
gpiLEDWork = 13
gpiLedIdle = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpiOutput, GPIO.OUT)
GPIO.setup(gpiLEDWork, GPIO.OUT)
GPIO.setup(gpiLedIdle, GPIO.OUT)
GPIO.cleanup()
