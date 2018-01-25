import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView
 

app = QApplication(sys.argv)
view = QDeclarativeView()

url = QUrl('CarInterface.qml')

view.setSource(url)
view.show()

sys.exit(app.exec_())