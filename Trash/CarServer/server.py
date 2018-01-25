import argparse
import base64
import hashlib
import os
import time
import threading
import webbrowser
#try:
#    import cStringIO as io
#except ImportError:
import io

import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback
from time import sleep
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


camera = "";
resolution = 'medium';
cameraOneState = True;

def forward(action):
    print ("Forward");
    pass

def reverse(action):
    print ("Reverse");
    pass

def right():
    print ("Right");
    pass

def left():
    print ("Left");
    pass

def straight():
    print ("Straight");
    pass

def speed(value):
    print ("Speed");
    pass

class ActionAndSensor(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True
    
    def on_message(self, message):

        try:
            pass
            #self.write_message("Yahoo");
        except tornado.websocket.WebSocketClosedError:
            self.camera_loop.stop()

        if message == 'MoveForward':
            forward(True);
        elif message == 'StopForward':
            forward(False)
        elif message == 'MoveBackward':
            reverse(True);
        elif message == 'StopBackward':
            reverse(False);
        elif message == 'Right':
            right();
        elif message == 'Left':
            left();
        elif message == 'Straight':
            straight();
        elif message == 'SetResolutionLow':
            stopCamera();
            startCamera('low');
        elif message == 'SetResolutionMedium':
            stopCamera();
            startCamera('medium');
        elif message == 'SetResolutionHigh':
            stopCamera();
            startCamera('high');
        elif message == 'StopCamera':
            stopCamera();
        #elif message == 'speed':
        #    try:
        #        data = self.request.arguments['d'];
        #        speed(data);
        #    except KeyError:
        #        pass

        else:
            print("Unsupported function: " + message)


class CameraOne(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True
    
    def on_message(self, message):
        global cameraOneState

        cameraOneState = False

        if message in ["high", "medium", "low"]:
            stopCamera();        
            startCamera(message);
            print message + " resolution set"    
        elif message == "close":
            stopCamera();        
            print "close_camera"    
        elif message == "start":
            startCamera();
            sleep(1);
            cameraOneState = True
            print("read_camera");
            self.camera_loop = PeriodicCallback(self.loop, 10)
            self.camera_loop.start()
        else:
            print("Unsupported function: " + message)

    def loop(self):
        global camera
        sio = io.BytesIO()

        if cameraOneState == False:
            self.camera_loop.stop();
            return;

        if args.use_usb:
            _, frame = camera.read()
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img.save(sio, "JPEG")
        else:
            camera.capture(sio, "jpeg", use_video_port=True)
        try:
            #.tobytes("raw", "RGBA")
            #self.write_message(sio.getvalue())
            self.write_message(sio.getvalue(), True)
        except tornado.websocket.WebSocketClosedError:
            self.camera_loop.stop()


parser = argparse.ArgumentParser(description="Starts a webserver that "
                                 "connects to a webcam.")
parser.add_argument("--port", type=int, default=8000, help="The "
                    "port on which to serve the website.")
parser.add_argument("--use-usb", action="store_true", help="Use a USB "
                    "webcam instead of the standard Pi camera.")
args = parser.parse_args()

if args.use_usb:
    import cv2
    from PIL import Image
else:
    import picamera

def setResolution(resolution):
    global camera
    resolutions = {"high": (1280, 720), "medium": (640, 480), "low": (320, 240)}
    if resolution in resolutions:
        if args.use_usb:
            w, h = resolutions[resolution]
            camera.set(3, w)
            camera.set(4, h)
        else:
            camera.resolution = resolutions[resolution]
    else:
        raise Exception("%s not in resolution options." % resolution)


def stopCamera():
    global cameraOneState, camera
    if args.use_usb:
        camera.release()
        cv2.destroyAllWindows()
    else:
        camera.stop();
    
    cameraOneState = False;
    pass

def startCamera(resolution = 'low'):
    global cameraOneState, camera
    cameraOneState = True;
    if args.use_usb:
        camera = cv2.VideoCapture(0)
    else:
        camera = picamera.PiCamera()
        camera.start_preview()

    setResolution(resolution);

handlers = [
#                (r"/", IndexHandler), 
                (r"/CameraOne", CameraOne),
                (r"/ActionAndSensor", ActionAndSensor)
#                (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': ROOT}),
            ]

application = tornado.web.Application(handlers)
application.listen(args.port)

#webbrowser.open("http://localhost:%d/" % args.port, new=2)

try:
    tornado.ioloop.IOLoop.instance().start()
except KeyboardInterrupt:
    stopCamera();
    print "Exiting";