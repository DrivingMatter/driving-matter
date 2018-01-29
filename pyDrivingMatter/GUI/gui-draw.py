import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class MouseTracker(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.points = []
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)
        self.label.setText('Coordinates: ( %d : %d )' % (event.x(), event.y()) + "Distance from center: " + str(distance_from_center))       
        self.pos = event.pos()
        self.update()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)

            new_point = (self.pos.x(), self.pos.y())
            
            if new_point not in self.points:
                self.points.append(new_point)

            x, y = self.points[0]
            if len(self.points) == 1:
                q.drawPoint(x, y)
            else:
                for (new_x, new_y) in self.points:
                    q.drawLine(x, y, new_x, new_y)
                    x, y = new_x, new_y


app = QApplication(sys.argv)
ex = MouseTracker()
sys.exit(app.exec_())
