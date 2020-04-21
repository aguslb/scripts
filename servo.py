import RPi.GPIO as GPIO
import time
import datetime

def showSleep (howLong, led ) :
    howLong = howLong * 4
    while howLong > 0 :
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.125)
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.125)
        howLong -= 1
def finalize (workingTimes, p, initPosition) :
    print ("Finilize ...")
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
now = datetime.datetime.now()
workingTimes = 300
print ("<---" + now.strftime("%Y-%m-%d %H:%M:%S") + " --->")
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Setup")
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Inital position: " + str(initPosition))
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Final position: " + str(finalPosition))
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Short value to sleep: " + str(slShort))
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Long Value to sleep: " + str(slLong))
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Servo GPIO:  " + str(gpiOutput))
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Green GPIO: " + str(gpiLedGreen))
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Red GPIO: " + str(gpiLedRed))
print (now.strftime("%Y-%m-%d %H:%M:%S") + " Number of times will work: " + str(workingTimes))
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
        print (now.strftime("%Y-%m-%d %H:%M:%S") + " Waiting ... |-)")
        p.ChangeDutyCycle(initPosition)
        showSleep(slLong,gpiLedGreen)
        p.ChangeDutyCycle(finalPosition)
        showSleep(slShort,gpiLedRed)
        workingTimes -= 1
        print (now.strftime("%Y-%m-%d %H:%M:%S")+ " Remainig times: " + str(workingTimes))
except (KeyboardInterrupt, OSError):
    finalize(workingTimes,p,initPosition)
print ("<---" + now.strftime("%Y-%m-%d %H:%M:%S") + " --->")
