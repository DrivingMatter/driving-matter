import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import logging
from time import sleep
import pickle
from skimage import color
from scipy import misc
import logging
import cv2
import io
from PIL import Image
import numpy as np
import pickle
from time import time, sleep
from classes.pyDrivingMatter import pyDrivingMatter
from classes.Car import Car
from classes.KBhit import KBHit
from classes.Misc import RPSCounter
import base64
import cStringIO
import json

#from keras.models import model_from_json

ACTIONS = ('forward', 'forwardLeft', 'forwardRight', 'backward', 'backwardRight', 'backwardLeft', 'stop')

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#pydm = pyDrivingMatter()
#car_data, car_link = pydm.get_car()

"""
logging.debug("Loading model")

json_file = open('models/model003.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("models/model003.h5")

loaded_model.compile(loss='categorical_crossentropy',
                  optimizer='adadelta',
                  metrics=['accuracy'])

logging.debug("Model loaded")
"""

car_link = "ws://{}:{}".format("192.168.137.2", "8000")

action_link = "{}/action".format(car_link)
state_link = "{}/state".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("State Link: " + state_link)

car = Car(action_link, url_state=state_link)

rps_counter = RPSCounter()

logger.debug("ACTIONS = " + str(ACTIONS))

def handle_state(data, ws):
    global rps_counter, loaded_model, car

    print (len(data))

    current_datavector = json.loads(data)
    
    pc_rps = rps_counter.get()

    logger.debug("PC RPS: " + str(pc_rps))
    
    sensors = current_datavector['sensors']
    
    collisions = sensors

    #frame = cStringIO.StringIO(base64.decodestring(current_datavector['camera_c'].encode("utf-8")))
    #frame = np.asarray(Image.open(frame))
    #frame = np.roll(frame, 1, axis=-1) # BGR to RGB

    # Reading NumPy 
    for name in ['camera_c', 'camera_l', 'camera_r']:
        frame_data = current_datavector[name]
        frame = base64.decodestring(frame_data[1].encode("utf-8"))
        frame = np.frombuffer(frame, frame_data[0]) # https://stackoverflow.com/questions/30698004/how-can-i-serialize-a-numpy-array-while-preserving-matrix-dimensions    
        frame = frame.reshape(frame_data[2])
    
        #frame = color.rgb2gray(frame)

        cv2.imshow(name, frame)
        cv2.waitKey(1)

    """
    #print ("Showing"  + str(time()))
    frame = misc.imresize(frame, 10)
    #print ("Resized"  + str(time()))
    frame = frame.astype('float32')
    #print ("done type " + str(time()))
    frame /= 255
    #print ("done dvision "  + str(time()))
    frame = frame.reshape(1, 1, frame.shape[0], frame.shape[1])
    #print ("preprocessing done"  + str(time()))


    print (frame.shape)
    #loaded_model.summary()
    #action = loaded_model._make_predict_function(frame)
    
    json_file = open('models/model003.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    model = model_from_json(loaded_model_json)
    model.load_weights("models/model003.h5")

    model.compile(loss='categorical_crossentropy',
                      optimizer='adadelta',
                      metrics=['accuracy'])

    action = model.predict(frame) # we get a integer

    action = np.argmax(action, axis=1)[0]
    action = ACTIONS[action]    # convert integer to function name eg forward, forwardLeft...

    logger.debug("Predicted Action: " + action + " " + str(time()))
    
    #logger.debug("Collisions: " + collisions)        
    can_take_action = True    
    
    for name in collisions:
        if collisions[name] == True and COLLISIONS[action] == name:
            can_take_action = False
            logger.debug("Collision detected" + " " + str(time()))
            break

    logger.debug("can_take_action: " + str(can_take_action) + " " + str(time()))        

    #if can_take_action:
    logger.debug("Taking action " + str(time()))
    car.take_action(action)
    sleep(car.timeframe) # Wait for action to complete            
    car.stop()
    logger.debug("Car Stopped " + str(time()))
    # sleep(1) # Wait for action to complete
    print ("="*80)
    """

car.set_state_callback(handle_state)
