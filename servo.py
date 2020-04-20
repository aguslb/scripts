import RPi.GPIO as GPIO
import time

def showSleep (howLong, led ) :
    totalTime = howLong/2
    while totalTime > 0 :
        GPIO.output(led,False)
        time.sleep(2)
        GPIO.output(led,True)
        totalTime -= 1
def finalize (workingTimes, p) :
    print (str(workingTimes) + '<-- times runned :)', end='\r')
    p.stop()
    GPIO.cleanup()

#Default Settings
initPosition = 12
finalPosition = 9
slShort = 1
slLong = 100
gpiOutput = 11
gpiLEDWork = 13
gpiLedIdle = 15
workingTimes = 0
#Setting GPIO and servo config
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpiOutput, GPIO.OUT)
p = GPIO.PWM(gpiOutput, 50)
p.start(initPosition)
#Setting GPIO led
GPIO.setup(gpiLEDWork, GPIO.OUT)
GPIO.setup(gpiLedIdle, GPIO.OUT)

#Runtine
try:
    while workingTimes < 600:
        p.ChangeDutyCycle(initPosition)
        showSleep(slLong,gpiLEDWork)
        p.ChangeDutyCycle(finalPosition)
        showSleep(slShort,gpiLedIdle)
        workingTimes += 1
except (KeyboardInterrupt, OSError):
    finalize(workingTimes,p)
finalize(workingTimes,p)