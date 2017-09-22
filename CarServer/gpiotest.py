import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)
sleep(3)
GPIO.output(7, GPIO.LOW)

GPIO.cleanup() # this ensures a clean exit
