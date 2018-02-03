import sys
from os import path
assert(sys.version_info.major == 3)
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import sys
import base64
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, QLineEdit
#sys.modules['PyQt5.QtGui'] = QtGui
from GUI import Ui_MainWindow
from GUIWriter import Writer

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import logging
import cv2
import io
from PIL import Image
import numpy as np
import pickle

import logging
import numpy as np
import pickle
from time import time

from classes.pyDrivingMatter import pyDrivingMatter
from classes.Car import Car
from classes.KBhit import KBHit
from classes.Misc import RPSCounter
import base64
import json
import socket

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MyWindowClass(QMainWindow):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.car = None
        self.rps_counter = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.forwardBtn.clicked.connect(self.forward_clicked)
        self.ui.backBtn.clicked.connect(self.backward_clicked)
        self.ui.leftBtn.clicked.connect(self.left_clicked)
        self.ui.rightBtn.clicked.connect(self.right_clicked)
        self.ui.stopBtn.clicked.connect(self.stop_clicked)
        self.ui.startButton.clicked.connect(self.start_clicked)

        self.ui.actionOpen_Writer.triggered.connect(self.open_writer)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionAbout.triggered.connect(self.about)

        self.img_left = self.ui.img_left
        self.img_right = self.ui.img_right
        self.img_center = self.ui.img_center    

        self.camera_label = {
            'camera_l': self.img_left,
            'camera_c': self.img_center,
            'camera_r': self.img_right
        }

        self.sensor_label = {
            'left': self.ui.sensor_left,
            'center': self.ui.sensor_center,
            'right': self.ui.sensor_right
        }

        self.add_log("DrivingMatter GUI Started.")
        self.show_image()

    def open_writer(self):
        self.add_log("OpenWriter called")
        self.writer = Writer(self.car)
        self.writer.setWindowTitle('Driving Matter - Writer')
        self.writer.show()

    def exit(self):
        self.add_log("Exit called")
        
    def about(self):
        self.add_log("About called")

    def add_log(self, message):
        from datetime import datetime
        message = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " + message 
        self.ui.logdata.appendPlainText(message)

        #scroll log textedit to bottom
        self.ui.logdata.verticalScrollBar().setValue(self.ui.logdata.verticalScrollBar().maximum());

    def load_car(self):
        ip, okPressed = QInputDialog.getText(self, "Car IP Address","Enter IP Address", QLineEdit.Normal, "192.168.137.2")
        if okPressed:
            try:
                socket.inet_aton(ip) # throw exception in invalid ip
                
                car_link = "ws://{}:{}".format(ip, "8000")

                action_link = "{}/action".format(car_link)
                state_link = "{}/state".format(car_link)

                self.add_log("Action Link: " + action_link)
                self.add_log("State Link: " + state_link)

                self.car = Car(action_link, url_state=state_link)
                self.rps_counter = RPSCounter()
                self.car.set_state_callback(self._handle_dataset_response)

                self.ui.startButton.setText('Started')
            except socket.error:
                pass # leave the condition
        else:
            self.ui.startButton.setText('Start')    
            self.ui.startButton.setEnabled(False)
        
    def stop_clicked(self):
        self.car.stop() 

    def backward_clicked(self):
        self.add_log("Car::backward()")
        self.car.backward() 

    def right_clicked(self):
        self.add_log("Car::right()")
        self.car.forwardRight()             

    def left_clicked(self):
        self.add_log("Car::left()")
        self.car.forwardLeft() 

    def forward_clicked(self):
        self.add_log("Car::forward()")
        self.car.forward() 
    
    def start_clicked(self):
        global running
        running = True
        self.ui.startButton.setEnabled(False)
        self.ui.startButton.setText('Starting...')  
        self.load_car() 

    def show_image(self):
        qim = QtGui.QImage("../images/no-image.png") # PNG only
        qim = qim.scaled(200,200, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.ui.img_left.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.ui.img_right.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.ui.img_center.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.ui.img_left.adjustSize()

        self.add_log("Showing default images.")

    def _handle_dataset_response(self, data, ws):
        current_datavector = json.loads(data)
        
        pc_rps = self.rps_counter.get()

        #logger.debug("PC RPS: " + str(pc_rps) + "\n\nCar RPS: " + str(car_rps) + "\n\nTotal: " + str(total_requests))
        sensors = current_datavector['sensors']
        
        for key, value in sensors.items():
            self.sensor_label[key].setText(str(value))

            if value:
                self.sensor_label[key].setStyleSheet('color: red')
            else:
                self.sensor_label[key].setStyleSheet('color: green')


        camera_names = [key for key in current_datavector if key.startswith('camera')]
        for name in camera_names:
            frame_data = current_datavector[name] # [type, array, shape]

            frame = base64.decodestring(frame_data[1].encode("utf-8"))
            frame = np.frombuffer(frame, frame_data[0]) # https://stackoverflow.com/questions/30698004/how-can-i-serialize-a-numpy-array-while-preserving-matrix-dimensions    
            frame = frame.reshape(frame_data[2])

            qim = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888) # https://gist.github.com/smex/5287589
            qim = qim.scaled(200,200, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            
            self.camera_label[name].setPixmap(QtGui.QPixmap.fromImage(qim))
            self.camera_label[name].adjustSize()

            self.add_log("Received dataset. RPS: " + str(int(pc_rps)))

app = QApplication(sys.argv)
w = MyWindowClass(None)
w.setWindowTitle('Driving Matter')
w.show()
app.exec_()