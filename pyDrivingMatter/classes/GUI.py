# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 467)
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color: rgb(63, 63, 63);\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.startButton = QtGui.QPushButton(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.startButton.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"selection-background-color: rgb(223, 223, 223);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(374, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget_3)
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
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(217, 217, 217) !important;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_8 = QtGui.QFrame(self.widget_2)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_3.addWidget(self.line_8, 1, 0, 1, 1)
        self.line_9 = QtGui.QFrame(self.widget_2)
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 1, 6, 1, 1)
        self.line_7 = QtGui.QFrame(self.widget_2)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_3.addWidget(self.line_7, 0, 5, 1, 1)
        self.line_6 = QtGui.QFrame(self.widget_2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 0, 3, 1, 1)
        self.line_5 = QtGui.QFrame(self.widget_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 0, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self.widget_2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 2, 5, 1, 1)
        self.line_10 = QtGui.QFrame(self.widget_2)
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_3.addWidget(self.line_10, 1, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.widget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 2, 3, 1, 1)
        self.line_3 = QtGui.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 2, 1, 1, 1)
        self.ImgWidgetright = QtGui.QWidget(self.widget_2)
        self.ImgWidgetright.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ImgWidgetright.setObjectName("ImgWidgetright")
        self.gridLayout_3.addWidget(self.ImgWidgetright, 1, 5, 1, 1)
        self.ImgWidgetleft = QtGui.QWidget(self.widget_2)
        self.ImgWidgetleft.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.ImgWidgetleft.setObjectName("ImgWidgetleft")
        self.gridLayout_3.addWidget(self.ImgWidgetleft, 1, 1, 1, 1)
        self.ImgWidgetcenter = QtGui.QWidget(self.widget_2)
        self.ImgWidgetcenter.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.ImgWidgetcenter.setObjectName("ImgWidgetcenter")
        self.gridLayout_3.addWidget(self.ImgWidgetcenter, 1, 3, 1, 1)
        self.line_11 = QtGui.QFrame(self.widget_2)
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_3.addWidget(self.line_11, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(217, 217, 217) !important;")
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtGui.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtGui.QTabWidget(self.widget)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setHorizontalSpacing(4)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.backBtn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setMaximumSize(QtCore.QSize(50, 30))
        self.backBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.backBtn.setObjectName("backBtn")
        self.gridLayout_6.addWidget(self.backBtn, 2, 1, 1, 1)
        self.forwardBtn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forwardBtn.sizePolicy().hasHeightForWidth())
        self.forwardBtn.setSizePolicy(sizePolicy)
        self.forwardBtn.setMaximumSize(QtCore.QSize(50, 30))
        self.forwardBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.forwardBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.forwardBtn.setAutoDefault(False)
        self.forwardBtn.setObjectName("forwardBtn")
        self.gridLayout_6.addWidget(self.forwardBtn, 0, 1, 1, 1)
        self.stopBtn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setMaximumSize(QtCore.QSize(50, 30))
        self.stopBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.stopBtn.setObjectName("stopBtn")
        self.gridLayout_6.addWidget(self.stopBtn, 1, 1, 1, 1)
        self.leftBtn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy)
        self.leftBtn.setMaximumSize(QtCore.QSize(50, 30))
        self.leftBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.leftBtn.setObjectName("leftBtn")
        self.gridLayout_6.addWidget(self.leftBtn, 1, 0, 1, 1)
        self.rightBtn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightBtn.sizePolicy().hasHeightForWidth())
        self.rightBtn.setSizePolicy(sizePolicy)
        self.rightBtn.setMaximumSize(QtCore.QSize(50, 30))
        self.rightBtn.setStyleSheet("background-color: rgb(175, 175, 175);\n"
"color: rgb(47, 47, 47);\n"
"selection-background-color: rgb(199, 199, 199);")
        self.rightBtn.setObjectName("rightBtn")
        self.gridLayout_6.addWidget(self.rightBtn, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 1, 1, 1)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.widget, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "    Start Preview    "))
        self.label.setText(_translate("MainWindow", "Driving Matter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Server"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Console"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.forwardBtn.setText(_translate("MainWindow", "Forward"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.leftBtn.setText(_translate("MainWindow", "Left"))
        self.rightBtn.setText(_translate("MainWindow", "Right"))

