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

# with pyDrivingMatter() as pydm:
#     while True:
#         cars = pydm.available_cars()
#         if len(cars) == 0:
#             logging.debug("Waiting for cars on network")
#         else: 
#             break
#         sleep(1)

# car_data = cars[0]

# if len(sys.argv) == 2 and sys.argv[1] == "find_my_car":
#     logging.debug ("="*80)
#     logging.debug (car_data)
#     logging.debug ("="*80)
#     sys.exit()

#car_link = "ws://{}:{}".format(car_data['address'], car_data['port'])
#car_link = "ws://{}:{}".format("192.168.137.2", "8000")
car_link = "ws://{}:{}".format("192.168.0.120", "8000")

action_link = "{}/action".format(car_link)
state_link = "{}/state".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("State Link: " + state_link)

car = Car(action_link, url_state=state_link)

start_time = int(time())
total_requests = 1
dataset = Dataset()
previous_datavector = None

def handle_state(data, ws):
    global total_requests, start_time, dataset, previous_datavector
    current_datavector = pickle.loads(data)
    
    total_requests += 1
    
    print ("Total requests: " + str(total_requests) + "\t\t" + str(int(time())))

    # request_per_sec = 0
    # elapsed = int(time()) - start_time

    # if elapsed == 0:
    #     request_per_sec = total_requests / elapsed
    
    # if elapsed > 5:
    #     total_requests = request_per_sec
    #     start_time = int(time())        

    # print ("RPS: " + str(request_per_sec))

    sensors = current_datavector['sensors']
    
    #print (sensors)

    camera_names = [key for key in current_datavector if key.startswith('camera')]
    for name in camera_names:
        frame = current_datavector[name]
        if frame != None:
            img = Image.open(io.BytesIO(frame))
            
            cv2.imshow(name, np.asarray(img))
            cv2.waitKey(1) # CV2 Devil - Don't dare to remove
        else:
            logging.debug("None frame received. Camera: " + name)

    #dataset.save_data(datavector)

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
    cv2.destroyAllWindow()
