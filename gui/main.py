import sys
import io
import base64
from PySide import QtCore, QtGui
sys.modules['PyQt4.QtGui'] = QtGui
from mainui import Ui_MainWindow
from ws4py.client.threadedclient import WebSocketClient
from PIL import Image
from PIL.ImageQt import ImageQt
import signal
import copy
signal.signal(signal.SIGINT, signal.SIG_DFL)


class CameraOneClient(WebSocketClient):
    def opened(self):
        pass

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, m):
        #print "Message arrived";
        if m.is_binary:
            mySW.setImage(m.data);


class ControlMainWindow(QtGui.QMainWindow):
    up_camera_signal = QtCore.Signal(io.BytesIO)

    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.up_camera_signal.connect(self.updateImage)

    def updateImage(self, data):
        image = Image.open(data)
        raw_data = str(image.convert("RGBA").tobytes("raw", "RGBA"));
        qim = QtGui.QImage(raw_data, image.size[0], image.size[1], QtGui.QImage.Format_ARGB32)
        self.ui.cameraOneLabel.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.ui.cameraOneLabel.adjustSize()
      
    def setImage(self, data):
        data = io.BytesIO(data) 
        
        self.up_camera_signal.emit(data)

if __name__ == "__main__":

    try:
        ws = CameraOneClient('ws://localhost:8000/CameraOne')
        ws.connect()
        ws.send("start")
        #ws.send("medium")
        #ws.run_forever()        


        app = QtGui.QApplication(sys.argv)
        mySW = ControlMainWindow()
        mySW.show()
        sys.exit(app.exec_())

    except KeyboardInterrupt:
        pass
        #ws.send("close_camera")
        #ws.close()

    

