import logging
import cv2
import io
from PIL import Image
import numpy as np
import pickle
from time import time

from classes.pyDrivingMatter import pyDrivingMatter
from classes.Car import Car
from classes.KBhit import KBHit
from classes.Misc import RPSCounter
import base64
import cStringIO

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#pydm = pyDrivingMatter()
#car_data, car_link = pydm.get_car()

car_link = "ws://{}:{}".format("192.168.12.103", "8000")

action_link = "{}/action".format(car_link)
state_link = "{}/state".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("State Link: " + state_link)

car = Car(action_link, url_state=state_link)

rps_counter = RPSCounter()

import json

def handle_state(data, ws):
    global rps_counter
    current_datavector = json.loads(data)
    
    pc_rps = rps_counter.get()

    logger.debug("PC RPS: " + str(pc_rps))
    sensors = current_datavector['sensors']
    
    # logger.debug(sensors)
    # logger.debug(time())

    camera_names = [key for key in current_datavector if key.startswith('camera')]
    for name in camera_names:
        frame_data = current_datavector[name] # [type, array, shape]
        
        frame = cStringIO.StringIO(base64.decodestring(frame_data.encode("utf-8")))
        frame = np.asarray(Image.open(frame))
        frame = np.roll(frame, 1, axis=-1) # BGR to RGB


        # Reading NumPy 
        # frame = base64.decodestring(frame_data[1].encode("utf-8"))
        # frame = np.frombuffer(frame, frame_data[0]) # https://stackoverflow.com/questions/30698004/how-can-i-serialize-a-numpy-array-while-preserving-matrix-dimensions    
        # frame = frame.reshape(frame_data[2])

        cv2.imshow(name, frame)
        cv2.waitKey(1) # CV2 Devil - Don't dare to remove

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
