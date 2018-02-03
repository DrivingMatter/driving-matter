import websocket
import io
import cv2
import numpy as np
from PIL import Image
from time import time, sleep
import logging
from threading import Thread

from .KBhit import KBHit
from .BrowseCar import BrowseCar

class Car():
    def __init__(self, url_action, url_state = None):
        logging.debug("Car class initiated")
        self.url_action = url_action
        self.url_state = url_state

        self.car_message_callback = None
        self.state_callback = None

        self.ws_action = None
        self.ws_state = None

        self.connect_ws()

    def connect_ws(self):
        logging.debug(("="*5) + "Connecting to websocket servers" + ("="*5))

        if self.url_state:
            self.ws_state = websocket.WebSocketApp(self.url_state,
                              on_message = self._state_callback,
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

    def __sendStep(self, method, step):
        current_time_epoch = int(time())
        """forward 1 1234123213"""
        message = "action {} {} {}".format(method, step, current_time_epoch)
        logging.debug("Sending => {}".format(message))
        self.ws_action.send(message)

    def take_action(self, method):
        self.__sendStep(method, 1)

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

    def _state_callback(self, ws, message):
        """This method will be callback for websocket response of car.
        """
        if self.state_callback is not None:
            self.state_callback(message, ws)

    def _state_c_on_open(self, ws):
        #ws.send("send_state")
        ws.send("read_state")
        # ws.send("stop_read_state") # This is also possible, think where to use
        print ("Websocket state opened, send_state sent")

    def _car_message_callback(self, ws, message):
        """This method will be callback for websocket response of car.
        """
        if self.car_message_callback is not None:
            self.car_message_callback(message, ws)

    def _action_c_on_open(self, ws):
        logging.debug("Action ws connected")

    def _ws_error(self, ws, error):
        logging.error(error)

    def _ws_close(self, ws):
        logging.debug("### closed ###")

    def set_car_message_callback(self, callback):
        self.car_message_callback = callback

    def set_state_callback(self, callback):
        self.state_callback = callback