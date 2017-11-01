import websocket
import io
import cv2
import numpy as np
from PIL import Image
from time import time, sleep
import logging
from threading import Thread

from KBhit import KBHit
from BrowseCar import BrowseCar

class pyDrivingMatter():
    bc = None
    def __init__(self):
        self.bc = BrowseCar()
        self.bc.start_browser()

    def available_cars(self):
        return self.bc.get_available_car()

    # Destructor
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.bc.stop_browser()

class Car():
    def __init__(self, url_action, url_camera_c = None, url_camera_l = None, url_camera_r = None, url_sensor = None, url_state = None):
        logging.debug("Car class initiated")
        self.url_action = url_action
        self.url_camera_c = url_camera_c
        self.url_camera_l = url_camera_l
        self.url_camera_r = url_camera_r
        self.url_sensor = url_sensor
        self.url_state = url_state

        self.car_message_callback = None
        self.camera_c_callback = None
        self.camera_l_callback = None
        self.camera_r_callback = None
        self.sensor_callback = None

        self.ws_action = None
        self.ws_camera_c = None
        self.ws_camera_l = None
        self.ws_camera_r = None
        self.ws_sensor = None
        self.ws_state = None

        self.frame_c_count = 0
        self.frame_c_start_time = None

        self.connect_ws()

    def test(self):
        print ("test called")

    def _car_state_callback(self, ws, message):
        state = message
        print (state)

    def _state_c_on_open(self, ws):
        ws.send("send_state")
        print ("Websocket state opened, send_state sent")

    def connect_ws(self):
        logging.debug(("="*5) + "Connecting to websocket servers" + ("="*5))
        if self.url_state:
            print ("Connecting url_state")
            self.ws_state = websocket.WebSocketApp(self.url_state,
                              on_message = self._car_state_callback,
                              on_error = self._ws_error,
                              on_close = self._ws_close)
            Thread(target=self.ws_state.run_forever).start()
            self.ws_state.on_open = self._state_c_on_open

        if self.url_action:
            self.ws_action = websocket.WebSocketApp(self.url_action,
                              on_message = self._car_message_callback,
                              on_error = self._ws_error,
                              on_close = self._ws_close)
            Thread(target=self.ws_action.run_forever).start()
            self.ws_action.on_open = self._action_c_on_open

        logging.debug(("="*5) + "Connected to websocket servers" + ("="*5))

    def __sendStep(self, method, step):
        current_time_epoch = int(time())
        """forward 1 1234123213"""
        message = "action {} {} {}".format(method, step, current_time_epoch)
        logging.debug("Sending => {}".format(message))
        self.ws_action.send(message)

    def forward(self, step = 1):
        self.__sendStep("forward", step)

    def forwardRight(self, step = 1):
        self.__sendStep("forwardRight", step)
    
    def forwardLeft(self, step = 1):
        self.__sendStep("forwardLeft", step)
    
    def backward(self, step = 1):
        self.__sendStep("backward", step)
    
    def backwardRight(self, step = 1):
        self.__sendStep("backwardRight", step)

    def backwardLeft(self, step = 1):
        self.__sendStep("backwardLeft", step)

    def stop(self, step = 1):
        self.__sendStep("stop", step)

    def _car_message_callback(self, ws, message):
        """This method will be callback for websocket response of car.
        """
        if self.car_message_callback is not None:
            self.car_message_callback(message)

    def _action_c_on_open(self, ws):
        logging.debug("Action ws connected")

    def _camera_c_callback(self, ws, message):
        """This method will be callback for websocket response of car.
        """
        self.frame_c_count += 1
        frame_rate = self.frame_c_count / (time() - self.frame_c_start_time)

        if self.frame_c_count > 1024:
            self.frame_c_count = frame_rate

        logging.debug("Camera response FPS: " + str(frame_rate))
        if self.camera_c_callback is not None:
            self.camera_c_callback(message)

    def _camera_c_on_open(self, ws):
        self.frame_c_count = 0
        self.frame_c_start_time = time()
        logging.debug("Camera C Connected")

    def start_camera(self):
        logging.debug("Camera C: Sending `read_camera` messages")
        self.ws_camera_c.send("read_camera")

    def _camera_l_callback(self, ws, message):
        """This method will be callback for websocket response of car.
        """
        if self.camera_l_callback is not None:
            self.camera_l_callback(message)

    def _camera_l_on_open(self, ws):

        logging.debug("Camera L Connection, sending `read_camera` messages")
        ws.send("read_camera")

    def _camera_r_callback(self, ws, message):
        """This method will be callback for websocket response of car.
        """
        if self.camera_r_callback is not None:
            self.camera_r_callback(message)

    def _camera_r_on_open(self, ws):

        logging.debug("Camera R Connection, sending `read_camera` messages")
        ws.send("read_camera")

    def _sensor_callback(self, ws, message):
        """This method will be callback for websocket response of car.
        """
        if self.sensor_callback is not None:
            self.sensor_callback(message)

    def _sensor_on_open(self, ws):

        logging.debug("Sensor ws connected")

    def _ws_error(self, ws, error):
        logging.error(error)

    def _ws_close(self, ws):
        logging.debug("### closed ###")

    def set_car_message_callback(self, callback):
        self.car_message_callback = callback

    def set_camera_c_callback(self, callback):
        self.camera_c_callback = callback

    def set_camera_l_callback(self, callback):
        self.camera_l_callback = callback

    def set_camera_r_callback(self, callback):
        self.camera_r_callback = callback

    def set_sensor_callback(self, callback):
        self.sensor_callback = callbac