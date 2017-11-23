import sys
import time
from time import sleep
import logging
import cv2
import io
from PIL import Image
import numpy as np
import pickle
from time import time
from threading import Thread
from Queue import Queue

logging.basicConfig(level=logging.DEBUG)

from classes.pyDrivingMatter import pyDrivingMatter
from classes.Car import Car
from classes.Dataset import Dataset
from classes.KBhit import KBHit

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
#car_link = "ws://{}:{}".format("192.168.0.120", "8000")
car_link = "ws://{}:{}".format("192.168.8.109", "8000")

action_link = "{}/action".format(car_link)
state_link = "{}/state".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("State Link: " + state_link)

car = Car(action_link, url_state=state_link)

start_time = time()
total_requests = 1
dataset = Dataset()
previous_datavector = None
timer = [0, 0]
timer_index = 0
dataset_time = None
dataset_queue = Queue()


def handle_state(data, ws):
    global total_requests, start_time, dataset, previous_datavector, timer_index, timer, dataset_time, dataset_queue
    current_datavector = pickle.loads(data)

    # Request Per Second Checker
    total_requests += 1
    timer[timer_index] += 1
    elapsed = time() - start_time

    if elapsed > 1:
        start_time = time()
        timer_index = 1
        timer[0] = (timer[0] + timer[1]) / 2  
        timer[1] = 0

    print ("RPS: " + str(timer[0]) + "\n\nTotal: " + str(total_requests))

    sensors = current_datavector['sensors']

    print (sensors)

    camera_names = [key for key in current_datavector if key.startswith('camera')]
    for name in camera_names:
        frame = current_datavector[name]
        if frame != None:
            img = Image.open(io.BytesIO(frame))
            current_datavector[name] = img
            cv2.imshow(name, np.asarray(img))
            cv2.waitKey(1) # CV2 Devil - Don't dare to remove
        else:
            logging.debug("None frame received. Camera: " + name)

    if (previous_datavector is not None) and (previous_datavector['car_action_id'] != current_datavector['car_action_id']):
        datavector = {}
        
        dataset_delay = int((time() - dataset_time) * 1000)

        # Misc Info
        datavector['timestamp'] = time()
        datavector['dataset_delay'] = dataset_delay

        # Previous State
        for sensor_name in previous_datavector['sensors']:
            name = "previous_sensor_{}".format(sensor_name)
            datavector[name] = previous_datavector['sensors'][sensor_name]

        datavector['previous_state'] = previous_datavector['car_state']

        for camera_name in camera_names:
            name = "previous_camera_{}".format(camera_name) # Camera names
            datavector[name] = previous_datavector[camera_name]

        # Current State
        for sensor_name in current_datavector['sensors']:
            name = "current_sensor_{}".format(sensor_name)
            datavector[name] = current_datavector['sensors'][sensor_name]

        datavector['current_state'] = current_datavector['car_state']

        for camera_name in camera_names:
            name = "current_{}".format(camera_name) # Camera names
            datavector[name] = current_datavector[camera_name]
        
        #dataset_queue.put(datavector)
        dataset.save_data(datavector)

        dataset_time = time()
    
    previous_datavector = current_datavector

car.set_state_callback(handle_state)

try:
    kb = KBHit()
    while True:
        if kb.kbhit():
            c = kb.carkey()
            if c == 0:   # Up
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
    cv2.destroyAllWindows()
