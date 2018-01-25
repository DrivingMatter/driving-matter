import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Tyre:
    forwardPin = None
    backwardPin = None

    def __init__(self, forwardPin, backwardPin):
        GPIO.setup(forwardPin, GPIO.OUT)
        GPIO.setup(backwardPin, GPIO.OUT)

        self.forwardPin = forwardPin
        self.backwardPin = backwardPin

    def forward(self):
        GPIO.output(self.forwardPin, GPIO.HIGH)

    def backward(self):
        GPIO.output(self.backwardPin, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.forwardPin, GPIO.LOW)
        GPIO.output(self.backwardPin, GPIO.LOW)

    def test(self):
        from time import sleep

        self.forward()
        sleep(1)
        self.stop()

        self.backward()
        sleep(1)
        self.stop()

class Car4W:
    frontRight = None
    frontLeft = None
    backRight = None
    backLeft = None
    
    def __init__(self,frontRight,frontLeft,backRight,backLeft):
        self.frontRight = frontRight
        self.frontLeft = frontLeft
        self.backRight = backRight
        self.backLeft = backLeft

    def forward(self):
        self.frontLeft.forward()
        self.frontRight.forward()
        self.backLeft.forward()
        self.backRight.forward()

    def backward(self):
        self.frontLeft.backward()
        self.frontRight.backward()
        self.backLeft.backward()
        self.backRight.backward()

    def stop(self):
        self.frontLeft.stop()
        self.frontRight.stop()
        self.backLeft.stop()
        self.backRight.stop()

    def forwardRight(self):
        self.frontLeft.forward()
        self.backLeft.forward()

        self.frontRight.stop()
        self.backRight.stop()

    def forwardLeft(self):
        self.frontRight.forward()
        self.backRight.forward()

        self.frontLeft.stop()
        self.backLeft.stop()

    def backwardRight(self):
        self.frontLeft.backward()
        self.backLeft.backward()

        self.frontRight.stop()
        self.backRight.stop()

    def backwardLeft(self):
        self.frontRight.backward()
        self.backRight.backward()

        self.frontLeft.stop()
        self.backLeft.stop()

    def test(self):
        from time import sleep
        
        self.forward()
        sleep(0.5)
        self.stop()

        sleep(3)

        self.backward()
        sleep(0.5)
        self.stop()

        sleep(3)
        
        self.forwardRight()
        sleep(0.5)
        self.stop()

        sleep(3)

        self.forwardLeft()
        sleep(0.5)
        self.stop()

        sleep(3)

        self.backwardLeft()
        sleep(0.5)
        self.stop()

        sleep(3)

        self.backwardRight()
        sleep(0.5)
        self.stop()

frontRight = Tyre(24, 25)
frontLeft = Tyre(11, 9)
backLeft = Tyre(15, 14)
backRight = Tyre(23, 18)

"""
frontLeft.test()
frontRight.test()
backLeft.test()
backRight.test()
"""

car = Car4W(frontRight, frontLeft, backRight, backLeft)

car.test()
    
GPIO.cleanup() # this ensures a clean exit
