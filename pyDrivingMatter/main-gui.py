import sys
from os import path
assert(sys.version_info.major == 3)
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import sys
import base64
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
#sys.modules['PyQt5.QtGui'] = QtGui
from classes.GUI import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import logging
import cv2
import io
from PIL import Image
import numpy as np
import pickle

from classes.pyDrivingMatter import pyDrivingMatter
from classes.Car import Car
from classes.KBhit import KBHit
from classes.Misc import RPSCounter
w=None
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
capture_thread = None
#pydm = pyDrivingMatter()
#car_data, car_link = pydm.get_car()

class OwnImageWidget(QWidget):
    def __init__(self, parent=None):
        super(OwnImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        sz = image.size()
        self.setMinimumSize(sz)
        self.update()

class MyWindowClass(QMainWindow):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.forwardBtn.clicked.connect(self.forward_clicked)
        self.ui.backBtn.clicked.connect(self.backward_clicked)
        self.ui.leftBtn.clicked.connect(self.left_clicked)
        self.ui.rightBtn.clicked.connect(self.right_clicked)
        self.ui.stopBtn.clicked.connect(self.stop_clicked)

        self.ui.startButton.clicked.connect(self.start_clicked)

        #self.window_width = self.ui.ImgWidgetleft.frameSize().width()
        #self.window_height = self.ui.ImgWidgetleft.frameSize().height()
        #print (self.window_height)
        #print (self.window_width)

        self.img_left = self.ui.img_left
        self.img_right = self.ui.img_right
        self.img_center = self.ui.img_center    

        self.add_log("DrivingMatter GUI Started.")
        self.load_car() 
        self.show_image()

    def add_log(self, message):
        from datetime import datetime
        message = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " + message 
        self.ui.logdata.appendPlainText(message)

        #scroll log textedit to bottom
        self.ui.logdata.verticalScrollBar().setValue(self.ui.logdata.verticalScrollBar().maximum());

    def load_car(self):
        car_link = "ws://{}:{}".format("192.168.43.60", "8000")
        action_link = "{}/action".format(car_link)
        state_link = "{}/state".format(car_link)
        
        logging.debug("Action Link: " + action_link)
        logging.debug("State Link: " + state_link)

        self.car = Car(action_link, url_state=state_link)
        self.rps_counter = RPSCounter()

        self.car.set_state_callback(self.handle_state)

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
        self.ui.startButton.setText('  Starting...  ')  

    def show_image(self):
        
        
        qim = QtGui.QImage("images/no-image.png") # PNG only
        qim = qim.scaled(200,200, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.ui.img_left.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.ui.img_right.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.ui.img_center.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.ui.img_left.adjustSize()

        self.add_log("Showing default images.")

        #image_profile = image_profile.scaled(250,250, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
        #label_Image.setPixmap(QtGui.QPixmap.fromImage(image_profile)) 
   
        #from scipy import misc
        #img = misc.imread('sample.jpg')

        #img_height, img_width, img_colors = img.shape
        #scale_w = float(self.window_width) / float(img_width)
        #scale_h = float(self.window_height) / float(img_height)
        #scale = 1 #0 if (min([scale_w, scale_h]) == 0) else 1
        #img = cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #height, width, bpc = img.shape
        #bpl = bpc * width
        #image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)

        #self.img_left.setImage(image)

    def handle_state(self, data, ws):
        global rps_counter


        current_datavector = pickle.loads(data,encoding='bytes')
        #pc_rps = rps_counter.get()

        #logger.debug("PC RPS: " + str(pc_rps) + "\n\nCar RPS: " + str(car_rps) + "\n\nTotal: " + str(total_requests))

        sensors = current_datavector['sensors']
        logger.debug(sensors)
        camera_names = [key for key in current_datavector if key.startswith('camera')]
        for name in camera_names:
            frame = current_datavector[name]
            if frame != None:
                img = Image.open(io.BytesIO(frame))
                current_datavector[name] = img
                cv2.imshow(name, np.asarray(img))
                cv2.waitKey(1) # CV2 Devil - Don't dare to remove

                ###### This May Not Work ################
                if w!=None:
                    w.ui.startButton.setText('Camera is live')
                    img_height, img_width, img_colors = img.shape
                    scale_w = float(w.window_width) / float(img_width)
                    scale_h = float(w.window_height) / float(img_height)
                    scale = min([scale_w, scale_h])

                    if scale == 0:
                        scale = 1
                
                    img = cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    height, width, bpc = img.shape
                    bpl = bpc * width
                    image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
                    camera_widget=ImgWidget+name
                    w.camera_widget.setImage(image)
                ########### ##############################    
            else:
                logger.debug("None frame received. Camera: " + name)

app = QApplication(sys.argv)
w = MyWindowClass(None)
w.setWindowTitle('Driving Matter')
w.show()
app.exec_()