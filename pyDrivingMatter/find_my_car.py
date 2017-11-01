from pyDrivingMatter import pyDrivingMatter, Car
import sys
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)

cars = None
with pyDrivingMatter() as pydm:
    while True:
        cars = pydm.available_cars()
        if len(cars) == 0:
            logging.debug("Waiting for cars on network")
        else: 
            break
        sleep(1)

print (cars)