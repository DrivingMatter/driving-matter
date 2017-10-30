from pyDrivingMatter import pyDrivingMatter, Car
from Dataset import Dataset
from KBhit import KBHit
import sys
# import os
import time
# import datetime
from time import sleep
import logging
import cv2
import io
from PIL import Image
import numpy as np

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

car_data = cars[0]

car_link = "ws://{}:{}".format(car_data['address'], car_data['port'])
action_link = "{}/action".format(car_link)
camera_c_link = "{}/camera_c".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("Camera C Link: " + camera_c_link)

car = Car(action_link, camera_c_link)

def handle_camera_c(data):
    stream = io.BytesIO()
    stream.write(data)
    stream.seek(0)
    img = Image.open(stream)
    img = np.asarray(img)
    dataset=Dataset('dataset/'+time.strftime("%d-%m-%Y"),'dataset.csv')
    dataset.save_data(img)
    # cv2.imshow("camera_c", img)
    stream.seek(0)
    key = cv2.waitKey(1) & 0xFF

car.set_camera_c_callback(handle_camera_c)

try:
    kb = KBHit()
    while True:
        if kb.kbhit():
            c = kb.carkey()

            if c == 0: # Up
                car.forward()            
            elif c == 1: # Right
                car.forwardRight() 
            elif c == 2: # Down
                car.backward()              
            elif c == 3: # Left
                car.forwardLeft()              
            elif c == 4: # Space
                car.stop()              
finally:
    kb.set_normal_term()    
    cv2.destroyWindow("camera_c")