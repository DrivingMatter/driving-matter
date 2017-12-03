import sys
import base64
from PySide import QtCore, QtGui
sys.modules['PyQt5.QtGui'] = QtGui
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

class MyWindowClass(QtGui.QMainWindow):

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
        
        self.window_width = self.ui.ImgWidgetleft.frameSize().width()

        self.window_height = self.ui.ImgWidgetleft.frameSize().height()
        self.ImgWidgetleft = OwnImageWidget(self.ui.ImgWidgetleft)
        self.ImgWidgetright = OwnImageWidget(self.ui.ImgWidgetright)
        self.ImgWidgetcenter = OwnImageWidget(self.ui.ImgWidgetcenter)    
        
    def stop_clicked(self):
        car.stop() 

    def backward_clicked(self):
        car.backward() 

    def right_clicked(self):
        car.forwardRight()             

    def left_clicked(self):
        car.forwardLeft() 

    def forward_clicked(self):
        car.forward() 
    
    def start_clicked(self):
        global running
        running = True
        self.ui.startButton.setEnabled(False)
        self.ui.startButton.setText('  Starting...  ')  


car_link = "ws://{}:{}".format("192.168.43.60", "8000")

action_link = "{}/action".format(car_link)
state_link = "{}/state".format(car_link)

logging.debug("Action Link: " + action_link)
logging.debug("State Link: " + state_link)

car = Car(action_link, url_state=state_link)

rps_counter = RPSCounter()

def handle_state(data, ws):
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

app = QtGui.QApplication(sys.argv)
w = MyWindowClass(None)
w.setWindowTitle('Driving Matter')
w.show()
car.set_state_callback(handle_state)

# def key_controls():
#     try:
#         kb = KBHit()
#         while True:
#             if kb.kbhit():
#                 c = kb.carkey()
#                 if c == 0:   # Up
#                     car.forward()            
#                 elif c == 1: # Right
#                     car.forwardRight() 
#                 elif c == 2: # Down
#                     car.backward()              
#                 elif c == 3: # Left
#                     car.forwardLeft()              
#                 elif c == 4: # Space
#                     car.stop()              
#     finally:
#         kb.set_normal_term()    
#         cv2.destroyAllWindows()

# capture_thread = threading.Thread(target=key_controls)
# capture_thread.start()
# key_controls()






app.exec_()

