import RPi.GPIO as GPIO
import time

#def printSleep (howLong) :
#  arrow = '-->'
#  once = False
#  while howLong > 0 :
#    if once == False and howLong <= 10 :
#      arrow = '--->'
#      once = True
#    time.sleep(1)
#    howLong -= 1
#    print (arrow + str(howLong), end='\r')
#Default Settings
initPosition = 12
finalPosition = 9
slShort = 1
slLong = 100
gpiOutput = 11
gpiLEDOut = 13
workingTimes = 0
#Setting GPIO and servo config
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpiOutput, GPIO.OUT)
p = GPIO.PWM(gpiOutput, 50)
p.start(initPosition)
#Setting GPIO led
GPIO.setup(gpiLEDOut, GPIO.OUT)
#Runtine
try:
    while True:
        p.ChangeDutyCycle(initPosition)
        GPIO.output(gpiLEDOut,True)
        time.sleep(slLong)
        p.ChangeDutyCycle(finalPosition)
        GPIO.output(gpiLEDOut,False)
        time.sleep(slShort)
        workingTimes += 1
        print (str(workingTimes) + '<-- times runned :)', end='\r')
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

