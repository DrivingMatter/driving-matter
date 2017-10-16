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
        """
        data = yield self.ws.read_message()
        
        if data is None:
            print "connection closed"
            self.ws = None
            break

        """

    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message("keep alive")



if __name__ == "__main__":

    #camera = CameraOne("ws://192.168.43.183:8000/CameraOne", 5)
    action = Action("ws://192.168.43.183:8000/Action", 5)
    print ("After Action")
    #camera = CameraOne("ws://192.168.1.11:8000/Sensor", 5)
    
    #camera = Client("ws://192.168.137.2:8000/CameraOne", 5)