# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 550)
        MainWindow.setMinimumSize(QtCore.QSize(700, 550))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(63, 63, 63);\n"
"    color: rgb(63, 63, 63);\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"background-color:#3d3d3d;\n"
"color:#fff;\n"
"  selection-background-color: #da532c;\n"
"border:solid;\n"
"border-width:3px;\n"
"border-color:#da532c;\n"
"}\n"
"QHeaderView::section{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 158, 217, 255), stop:1 rgba(36, 158, 217, 255));\n"
"border:none;\n"
"border-top-style:solid;\n"
"border-width:1px;\n"
"border-top-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 158, 217, 255), stop:1 rgba(36, 158, 217, 255));\n"
"color:#fff;\n"
"\n"
"}\n"
"QHeaderView{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 158, 217, 255), stop:1 rgba(36, 158, 217, 255));\n"
"\n"
"border:none;\n"
"border-top-style:solid;\n"
"border-width:1px;\n"
"border-top-color:#149ED9;\n"
"color:#fff;\n"
"    font: 75 12pt \"Calibri\";\n"
"}\n"
"\n"
"QTableCornerButton::section{\n"
"border:none;\n"
"background-color:#149ED9;\n"
"}\n"
"\n"
"QListWidget{\n"
"background-color:#3d3d3d;\n"
"color:#fff;\n"
"}\n"
"\n"
"QMenu{\n"
"background-color:#3d3d3d;\n"
"}\n"
"QStatusBar{\n"
"background-color:#7e3878;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-style:solid;\n"
"\n"
"background-color:#3d3d3d;\n"
"color:#fff;\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"color:#ccc;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));\n"
"    border-color:#2d89ef;\n"
"border-width:2px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(29, 29, 29, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab{\n"
"background-color:#3d3d3d;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:0;\n"
"}\n"
"\n"
"QProgressBar{\n"
"border-radius:0;\n"
"text-align:center;\n"
"color:#fff;\n"
"background-color:transparent;\n"
"border: 2px solid #e3a21a;\n"
"border-radius:7px;\n"
"    font: 75 12pt \"Open Sans\";\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color:#2d89ef;\n"
"width:20px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color: rgb(63, 63, 63);\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.startButton = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(150, 0))
        self.startButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.startButton.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"selection-background-color: rgb(223, 223, 223);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(374, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(232, 232, 232);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(217, 217, 217) !important;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.img_left = QtWidgets.QLabel(self.widget_2)
        self.img_left.setObjectName("img_left")
        self.gridLayout_3.addWidget(self.img_left, 1, 5, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_11 = QtWidgets.QFrame(self.widget_2)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_3.addWidget(self.line_11, 1, 4, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.widget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 0, 3, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.widget_2)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_3.addWidget(self.line_10, 1, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 2, 1, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.widget_2)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_3.addWidget(self.line_8, 1, 0, 1, 1)
        self.img_right = QtWidgets.QLabel(self.widget_2)
        self.img_right.setObjectName("img_right")
        self.gridLayout_3.addWidget(self.img_right, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_9 = QtWidgets.QFrame(self.widget_2)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 1, 6, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 2, 3, 1, 1)
        self.img_center = QtWidgets.QLabel(self.widget_2)
        self.img_center.setObjectName("img_center")
        self.gridLayout_3.addWidget(self.img_center, 1, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_7 = QtWidgets.QFrame(self.widget_2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_3.addWidget(self.line_7, 0, 5, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 2, 5, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(217, 217, 217) !important;")
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setHorizontalSpacing(4)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.backBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setMinimumSize(QtCore.QSize(70, 0))
        self.backBtn.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.backBtn.setObjectName("backBtn")
        self.gridLayout_6.addWidget(self.backBtn, 2, 1, 1, 1)
        self.forwardBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forwardBtn.sizePolicy().hasHeightForWidth())
        self.forwardBtn.setSizePolicy(sizePolicy)
        self.forwardBtn.setMinimumSize(QtCore.QSize(70, 0))
        self.forwardBtn.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.forwardBtn.setFont(font)
        self.forwardBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.forwardBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.forwardBtn.setAutoDefault(False)
        self.forwardBtn.setObjectName("forwardBtn")
        self.gridLayout_6.addWidget(self.forwardBtn, 0, 1, 1, 1)
        self.stopBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setMinimumSize(QtCore.QSize(70, 0))
        self.stopBtn.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stopBtn.setFont(font)
        self.stopBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.stopBtn.setObjectName("stopBtn")
        self.gridLayout_6.addWidget(self.stopBtn, 1, 1, 1, 1)
        self.leftBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy)
        self.leftBtn.setMinimumSize(QtCore.QSize(70, 0))
        self.leftBtn.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leftBtn.setFont(font)
        self.leftBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.leftBtn.setObjectName("leftBtn")
        self.gridLayout_6.addWidget(self.leftBtn, 1, 0, 1, 1)
        self.rightBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightBtn.sizePolicy().hasHeightForWidth())
        self.rightBtn.setSizePolicy(sizePolicy)
        self.rightBtn.setMinimumSize(QtCore.QSize(70, 0))
        self.rightBtn.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rightBtn.setFont(font)
        self.rightBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.rightBtn.setObjectName("rightBtn")
        self.gridLayout_6.addWidget(self.rightBtn, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.logdata = QtWidgets.QPlainTextEdit(self.widget)
        self.logdata.setReadOnly(True)
        self.logdata.setPlainText("")
        self.logdata.setObjectName("logdata")
        self.verticalLayout.addWidget(self.logdata)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 5, 0, 1, 1)
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setStyleSheet("background-color: rgb(217, 217, 217) !important;")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.gridWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sensor_right = QtWidgets.QLabel(self.gridWidget)
        self.sensor_right.setObjectName("sensor_right")
        self.horizontalLayout_2.addWidget(self.sensor_right, 0, QtCore.Qt.AlignHCenter)
        self.sensor_center = QtWidgets.QLabel(self.gridWidget)
        self.sensor_center.setObjectName("sensor_center")
        self.horizontalLayout_2.addWidget(self.sensor_center, 0, QtCore.Qt.AlignHCenter)
        self.sensor_left = QtWidgets.QLabel(self.gridWidget)
        self.sensor_left.setObjectName("sensor_left")
        self.horizontalLayout_2.addWidget(self.sensor_left, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.gridWidget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_Writer = QtWidgets.QAction(MainWindow)
        self.actionOpen_Writer.setObjectName("actionOpen_Writer")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_Writer)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "    Start Preview    "))
        self.label.setText(_translate("MainWindow", "Driving Matter"))
        self.img_left.setText(_translate("MainWindow", "TextLabel"))
        self.img_right.setText(_translate("MainWindow", "TextLabel"))
        self.img_center.setText(_translate("MainWindow", "TextLabel"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.forwardBtn.setText(_translate("MainWindow", "Forward"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.leftBtn.setText(_translate("MainWindow", "Left"))
        self.rightBtn.setText(_translate("MainWindow", "Right"))
        self.label_2.setText(_translate("MainWindow", "Log"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Ultrasonic Sensors Values</span></p></body></html>"))
        self.sensor_right.setText(_translate("MainWindow", "None"))
        self.sensor_center.setText(_translate("MainWindow", "None"))
        self.sensor_left.setText(_translate("MainWindow", "None"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_Writer.setText(_translate("MainWindow", "Open Writer"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

