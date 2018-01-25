import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def right(x):
    print "right"
    GPIO.output(18, GPIO.HIGH)
    sleep(x)
    GPIO.output(18, GPIO.LOW)

def left(x):
    print "left"
    GPIO.output(16, GPIO.HIGH)
    sleep(x)
    GPIO.output(16, GPIO.LOW)


def forward(x):
    print "forward"
    GPIO.output(13, GPIO.HIGH)
    sleep(x)
    GPIO.output(13, GPIO.LOW)

def reverse(x):
    print "reverse"
    GPIO.output(15, GPIO.HIGH)
    sleep(x)
    GPIO.output(15, GPIO.LOW)

try:
        right(3);
        sleep(0.5);
        left(3);
        
        forward(3)
        sleep(0.5)
        reverse(3)
except:  
       print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit
