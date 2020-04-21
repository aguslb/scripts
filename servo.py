import RPi.GPIO as GPIO
import time

def showSleep (howLong, led ) :
    howLong = howLong * 4
    while howLong > 0 :
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.125)
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.125)
        howLong -= 1
def finalize (workingTimes, p, initPosition) :
    p.ChangeDutyCycle(initPosition)
    p.stop()
    GPIO.cleanup()

#Default Settings
initPosition = 12
finalPosition = 9
slShort = 1
slLong = 99
gpiOutput = 11
gpiLedGreen = 13
gpiLedRed = 15
workingTimes = 300
#Setting GPIO and servo config
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpiOutput, GPIO.OUT)
p = GPIO.PWM(gpiOutput, 50)
p.start(initPosition)
#Setting GPIO led
GPIO.setup(gpiLedGreen, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(gpiLedRed, GPIO.OUT, initial=GPIO.LOW)

#Runtine
try:
    while workingTimes > 0:
        p.ChangeDutyCycle(initPosition)
        showSleep(slLong,gpiLedGreen)
        p.ChangeDutyCycle(finalPosition)
        showSleep(slShort,gpiLedRed)
        workingTimes -= 1
except (KeyboardInterrupt, OSError):
    finalize(workingTimes,p,initPosition)
finalize(workingTimes,p,initPosition)
