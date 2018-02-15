import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget ,QErrorMessage)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from math import sqrt
import time

step_size = 5.0

class Writer(QWidget):
    distance_from_center = 0
    def __init__(self, car):
        super().__init__()
        
        self.car = car
        print (self.car)
        if car is None:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Car not connected.')
            #self.hide()

        self.points = []
        self.start = False

        self.setGeometry(200, 200, 1000, 500)
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.pos = None

        self.setMouseTracking(True)
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.points = []
            self.paintEvent(None)
            self.start = False
        elif event.button() == QtCore.Qt.LeftButton:
            self.start = True

    def mouseMoveEvent(self, event):
        if self.start:
            distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)
            self.label.setText('Coordinates: ( %d : %d )' % (event.x(), event.y()) + "Distance from center: " + str(distance_from_center))       
            self.pos = event.pos()
            self.update()

    def get_action(self, x1, y1, x2, y2, steps):
        if x1 == x2:
            x3 = 0
        elif x1 > x2:
            x3 = -1
        elif x1 < x2:
            x3 = 1

        if y1 == y2:
            y3 = 0
        elif y1 > y2:
            y3 = -1
        elif y1 < y2:
            y3 = 1
            
        directions = {
            '[-1, -1]':'forwardLeft',
            '[-1, 0]' :'left',
            '[-1, 1]' :'backwardLeft',
            '[0, 1]'  :'backward',
            '[1, 1]'  :'backwardRight',
            '[1, 0]'  :'right',
            '[1, -1]' :'forwardRight',
            '[0, -1]' :'forward',
        }

        key = str([x3, y3])
        direction = directions[key]
        
        actions = {
            'backwardRight' : 'backwardRight backward',
            'right'         : 'forwardRight forwardRight forward',
            'forwardRight'  : 'forwardRight forward',
            'forward'       : 'forwardRight',
            'forwardLeft'   : 'forwardLeft forward',
            'left'          : 'forwardLeft forwardLeft forward',
            'backwardLeft'  : 'backwardLeft backward',
            'backward'      : 'backward',
        }

        return actions[direction].split(" "), int(steps/step_size), direction

    def take_action(self, actions, steps, delay=0.3):        
        for action in actions:
            print (action)
            self.car.take_action(action)
            time.sleep(delay)

        for step in range(steps-1):
            print (actions[-1])
            self.car.take_action(actions[-1])
            time.sleep(delay)

    def paintEvent(self, event):
        if not self.start:
            return 

        if self.pos:
            q = QPainter(self)

            new_point = (self.pos.x(), self.pos.y())            
            self.points.append(new_point)

            x, y = self.points[0]
            if len(self.points) == 1:
                q.drawPoint(x, y)
            else:
                old_point = self.points[-2]

                x2, y2 = new_point
                x1, y1 = old_point
                steps = int(sqrt(((x2-x1)**2) + ((y2-y1)**2)))
                for (new_x, new_y) in self.points:
                    q.drawLine(x, y, new_x, new_y)
                    x, y = new_x, new_y

                if steps < step_size:
                    self.points = self.points[:-1]
                else:
                    actions, steps, direction = self.get_action(x1, y1, x2, y2, steps)
                    print ("Mouse Direction: " + direction)
                    self.take_action(actions, steps, delay=0)