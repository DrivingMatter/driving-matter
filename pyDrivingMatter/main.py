import sys
import time
from time import sleep
import logging
import cv2
import io
from PIL import Image
import numpy as np

logging.basicConfig(level=logging.DEBUG)

from classes.pyDrivingMatter import pyDrivingMatter
from classes.Car import Car
from classes.Dataset import Dataset
from classes.KBhit import KBHit


cars = None
"""
with pyDrivingMatter() as pydm:
    while True:
        cars = pydm.available_cars()
        if len(cars) == 0:
            logging.debug("Waiting for cars on network")
        else: 
            break
        sleep(1)

car_data = cars[0]

if len(sys.argv) == 2 and sys.argv[1] == "find_my_car":
    logging.debug ("="*80)
    logging.debug (car_data)
    logging.debug ("="*80)
    sys.exit()

car_link = "ws://{}:{}".format(car_data['address'], car_data['port'])
action_link = "{}/action".format(car_link)
#camera_c_link = "{}/camera_c".format(car_link)
state_link = "{}/state".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("State Link: " + state_link)
#logging.debug("Camera C Link: " + camera_c_link)
"""
car_link = "ws://192.168.8.105:8000"
action_link = "ws://192.168.8.105:8000/action"
state_link = "ws://192.168.8.105:8000/state"
car = Car(action_link, url_state=state_link)

def bytes2int(xbytes):
    return int.from_bytes(xbytes, 'big')

def handle_state(data, ws):
    #print (data)
    stream = io.BytesIO()
    stream.write(data)
    stream.seek(0)
    sensor_count = bytes2int(stream.read(4))
    for _ in range(sensor_count):
        name = stream.read(16).decode()
        value = bytes2int(stream.read(4))
        print ("Sensor: {} value: {} ".format(name, value))

    camera_count = bytes2int(stream.read(4))
    for _ in range(camera_count):
        name = stream.read(16).decode()
        frame_size = bytes2int(stream.read(4))
        frame = stream.read()
        print ("Camera: {} Size: {} ".format(name, frame_size))

        #img_stream = io.BytesIO()
        #img_stream.write(frame)
        #img_stream.seek(0)
        img = Image.open(io.BytesIO(frame))
        img = np.asarray(img)
        cv2.imshow(name, img)

    #img = Image.open(stream)
    #img = np.asarray(img)
    # dataset=Dataset('dataset/'+time.strftime("%d-%m-%Y"),'dataset.csv')
    # dataset.save_data(img)
    #cv2.imshow("camera_c", img)
    #stream.seek(0)
    #key = cv2.waitKey(1) & 0xFF

car.set_state_callback(handle_state)

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