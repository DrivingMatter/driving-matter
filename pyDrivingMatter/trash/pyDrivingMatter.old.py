#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect
import io
import cv2
import numpy as np
from PIL import Image
from time import time, sleep

from KBhit import KBHit
from BrowseCar import BrowseCar

class pyDrivingMatter():
    def __init__(self):
        self.bc = BrowseCar()
        self.bc.start_browser()

    def available_cars(self):
        return self.bc.get_available_car()

    # Destructor
    def __enter__(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback)
        bc.stop_browser()

class Car():
    def __init__(self, url_action, url_camera_c = None, url_camera_l = None, url_camera_r = None, url_sensor = None):
        self.url_action = url_action
        self.url_camera_c = url_camera_c
        self.url_camera_l = url_camera_l
        self.url_camera_r = url_camera_r
        self.url_sensor = url_sensor

        self.car_message_callback = None
        self.camera_c_callback = None
        self.camera_l_callback = None
        self.camera_r_callback = None
        self.sensor_callback = None

        self.start()

    def start(self):
        self.ws_action = None
        self.ws_camera_c = None
        self.ws_camera_l = None
        self.ws_camera_r = None
        self.ws_sensor = None

        if self.url_action:
            self.ws_action = yield websocket_connect(self.url_action, on_message_callback=self._car_message_callback)
        
        if self.url_camera_c:
            self.ws_camera_c = yield websocket_connect(self.url_camera_c, on_message_callback=self._camera_c_callback)
        
        if self.url_camera_l:
            self.ws_camera_l = yield websocket_connect(self.url_camera_l, on_message_callback=self._camera_l_callback)

        if self.url_camera_r:
            self.ws_camera_r = yield websocket_connect(self.url_camera_r, on_message_callback=self._camera_r_callback)        

        if self.url_sensor:
            self.ws_sensor = yield websocket_connect(self.url_sensor, on_message_callback=self._sensor_callback)        

    def __sendStep(self, method, step)
        current_time_epoch = int(time())
        self.ws_action.write_message("{} {} {}".format(method, step, current_time_epoch))

    def forward(self, step = 1)
        self.__sendStep("forward", step)

    def forwardRight(self, step = 1)
        self.__sendStep("forwardRight", step)
    
    def forwardLeft(self, step = 1)
        self.__sendStep("forwardLeft", step)
    
    def backward(self, step = 1)
        self.__sendStep("backward", step)
    
    def backwardRight(self, step = 1)
        self.__sendStep("backwardRight", step)

    def backwardLeft(self, step = 1)
        self.__sendStep("backwardLeft", step)

    def stop(self, step = 1)
        self.__sendStep("stop", step)

    def _car_message_callback(self, message):
        """This method will be callback for websocket response of car.
        """
        if self.car_message_callback is not None:
            self.car_message_callback(message)

    def _camera_c_callback(self, message):
        """This method will be callback for websocket response of car.
        """
        if self.camera_c_callback is not None:
            self.camera_c_callback(message)

    def _camera_l_callback(self, message):
        """This method will be callback for websocket response of car.
        """
        if self.camera_l_callback is not None:
            self.camera_l_callback(message)

    def _camera_r_callback(self, message):
        """This method will be callback for websocket response of car.
        """
        if self.camera_r_callback is not None:
            self.camera_r_callback(message)

    def _sensor_callback(self, message):
        """This method will be callback for websocket response of car.
        """
        if self.sensor_callback is not None:
            self.sensor_callback(message)

    def set_car_message_callback(self, callback):
        self.car_message_callback = callback

    def set_camera_c_callback(self, callback):
        self.camera_c_callback = callback

    def set_camera_l_callback(self, callback):
        self.camera_l_callback = callback

    def set_camera_r_callback(self, callback):
        self.camera_r_callback = callback

    def set_sensor_callback(self, callback)
        self.sensor_callback = callback

"""
class CameraOne(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
        #PeriodicCallback(self.keep_alive, 20000, io_loop=self.ioloop).start()
        self.ioloop.start()

    @gen.coroutine
    def connect(self):
        print "trying to connect"
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception, e:
            print "connection error"
        else:
            print "connected"
            self.ws.write_message("read_camera")
            self.run()

    @gen.coroutine
    def run(self):
        stream = io.BytesIO()
        import time
        start = time.time()
        i = 0
        elapse = 1 
        while True:
            
            data = yield self.ws.read_message()
            
            if data is None:
                print "connection closed"
                self.ws = None
                break

            stream.write(data)
            stream.seek(0)
            img = np.asarray(Image.open(stream))
            cv2.imshow("Frame", img)
            stream.seek(0)
            key = cv2.waitKey(1) & 0xFF

            i += 1
            elapse = (time.time() - start)
            if elapse > 300000:
                break;

        cv2.destroyWindow("Frame")
        print (i)
        print (elapse)
        print (str(i/elapse) + " fps")

    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message("keep alive")


class Action(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
        #PeriodicCallback(self.keep_alive, 20000, io_loop=self.ioloop).start()
        self.ioloop.start()

    @gen.coroutine
    def connect(self):
        print "trying to connect"
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception, e:
            print "connection error"
        else:
            print "connected"
            self.run()

    @gen.coroutine
    def run(self):
        kb = KBHit()
        sent = time()
        tmp = -1
        while True:
            #sleep(0.1)
            if kb.kbhit():
                sent = time()
                c = kb.carkey()
                
                if c == 0: # Up
                    print ("forward")
                    self.ws.write_message("forward")              
                elif c == 1: # Right
                    print ("forwardRight")
                    self.ws.write_message("forwardRight")              
                elif c == 2: # Down
                    print ("backward")
                    self.ws.write_message("backward")              
                elif c == 3: # Left
                    print ("forwardLeft")
                    self.ws.write_message("forwardLeft")              
                elif c == 4: # Space
                    print ("stop")
                    self.ws.write_message("stop")              
                tmp = c

            # if no signal for 1 second then stop the car and car not already stoped
            elapse = time() - sent
            if tmp != 4 and elapse > 0.1:
                print (elapse)
                self.ws.write_message("stop")                  
                tmp = 4;

        kb.set_normal_term()    
        # if the `q` key was pressed, break from the loop
        #if key == ord("q"):
        #data = yield self.ws.read_message()
        
        #if data is None:
        #    print "connection closed"
        #    self.ws = None
        #    break

    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message("keep alive")



if __name__ == "__main__":

    camera = CameraOne("ws://192.168.43.183:8000/CameraOne", 5)
    print ("here")
    action = Action("ws://192.168.43.183:8000/Action", 5)
    print ("After Action")
    #camera = CameraOne("ws://192.168.1.11:8000/Sensor", 5)
    
    #camera = Client("ws://192.168.137.2:8000/CameraOne", 5)
"""