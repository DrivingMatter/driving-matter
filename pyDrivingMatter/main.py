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

import pickle
from time import time

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

if len(sys.argv) == 2 and sys.argv[1] == "find_my_car":
    logging.debug ("="*80)
    logging.debug (car_data)
    logging.debug ("="*80)
    sys.exit()

car_link = "ws://{}:{}".format(car_data['address'], car_data['port'])
action_link = "{}/action".format(car_link)
state_link = "{}/state".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("State Link: " + state_link)

car = Car(action_link, url_state=state_link)

start_time = int(time())
total_requests = 1
dataset = Dataset()

def handle_state(data, ws):
    global total_requests, start_time, dataset

    #total_requests += 1

    #elapsed = int(time()) - start_time

    #request_per_sec = total_requests / elapsed

    #print ("RPS: " + str(request_per_sec))

    print (int(time()))

    data = pickle.loads(data)
    sensors = data['sensors']

    datavector = sensors    

    camera_names = [key for key in data if key.startswith('camera')]
    for name in camera_names:
        img = Image.open(io.BytesIO(data[name]))
        datavector[name] = img

        cv2.imshow(name, np.asarray(img))
        cv2.waitKey(1) # CV2 Devil - Don't dare to remove

    dataset.save_data(datavector)

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
    #cv2.destroyWindow("camera_c")