# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalGui.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from open_file import App
import pyqtgraph as pg
from pyqtgraph.ptime import time
import numpy as np
from Get_arduino_data import Live
import atexit


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(968, 648)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logos/Hamdard-University-Karachi-Address-Campus-Fee-Structure-Courses.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_widget = QtWidgets.QWidget(self.centralwidget)
        self.Main_widget.setGeometry(QtCore.QRect(-1, 0, 971, 651))
        self.Main_widget.setAutoFillBackground(False)
        self.Main_widget.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.Main_widget.setObjectName("Main_widget")
        self.thi_mainwidget = QtWidgets.QWidget(self.Main_widget)
        self.thi_mainwidget.setGeometry(QtCore.QRect(10, 0, 951, 631))
        self.thi_mainwidget.setAutoFillBackground(False)
        self.thi_mainwidget.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.thi_mainwidget.setObjectName("thi_mainwidget")
        self.thi_top_graphic_2 = QtWidgets.QGraphicsView(self.thi_mainwidget)
        self.thi_top_graphic_2.setGeometry(QtCore.QRect(10, 10, 931, 61))
        self.thi_top_graphic_2.setStyleSheet("background-color: rgb(6, 6, 159);")
        self.thi_top_graphic_2.setObjectName("thi_top_graphic_2")
        self.thi_main_graphicsView_2 = QtWidgets.QGraphicsView(self.thi_mainwidget)
        self.thi_main_graphicsView_2.setGeometry(QtCore.QRect(10, 70, 931, 591))
        self.thi_main_graphicsView_2.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.thi_main_graphicsView_2.setObjectName("thi_main_graphicsView_2")
        self.thi_topbarwidget_2 = QtWidgets.QWidget(self.thi_mainwidget)
        self.thi_topbarwidget_2.setGeometry(QtCore.QRect(20, 20, 911, 41))
        self.thi_topbarwidget_2.setStyleSheet("background-color: rgb(7, 2, 50);")
        self.thi_topbarwidget_2.setObjectName("thi_topbarwidget_2")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.thi_topbarwidget_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(60, 0, 346, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.thi_horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.thi_horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.thi_horizontalLayout_6.setObjectName("thi_horizontalLayout_6")
        self.thi_back_Button_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.thi_back_Button_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("logos/back-button.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thi_back_Button_2.setIcon(icon1)
        self.thi_back_Button_2.setObjectName("thi_back_Button_2")
        self.thi_horizontalLayout_6.addWidget(self.thi_back_Button_2)
        self.thi_startstream_button_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.thi_startstream_button_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("logos/Custom-Icon-Design-Flatastic-9-Start.ico"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.thi_startstream_button_2.setIcon(icon2)
        self.thi_startstream_button_2.setObjectName("thi_startstream_button_2")
        self.thi_horizontalLayout_6.addWidget(self.thi_startstream_button_2)
        self.thi_stopstream_button_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.thi_stopstream_button_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("logos/Icons-Land-Play-Stop-Pause-Stop-Pressed.ico"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.thi_stopstream_button_2.setIcon(icon3)
        self.thi_stopstream_button_2.setObjectName("thi_stopstream_button_2")
        self.thi_horizontalLayout_6.addWidget(self.thi_stopstream_button_2)
        self.thi_openfile_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.thi_openfile_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("logos/PaperClip3_Black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thi_openfile_button.setIcon(icon4)
        self.thi_openfile_button.setObjectName("thi_openfile_button")

        self.thi_horizontalLayout_6.addWidget(self.thi_openfile_button)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.thi_topbarwidget_2)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(440, 0, 160, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.thi_horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.thi_horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.thi_horizontalLayout_8.setObjectName("thi_horizontalLayout_8")
        self.thi_HUlogo_label = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.thi_HUlogo_label.setStyleSheet("image: url(logos/logo.png);")
        self.thi_HUlogo_label.setText("")
        self.thi_HUlogo_label.setObjectName("thi_HUlogo_label")
        self.thi_horizontalLayout_8.addWidget(self.thi_HUlogo_label)
        self.thi_pdaq_label = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.thi_pdaq_label.setAutoFillBackground(False)
        self.thi_pdaq_label.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
                                          "color: rgb(255, 255, 255);")
        self.thi_pdaq_label.setObjectName("thi_pdaq_label")
        self.thi_horizontalLayout_8.addWidget(self.thi_pdaq_label)
        self.thi_openfile_button.clicked.connect(self.open_file_dialogue)
        '''
                         *****   PlayBack work Starts from here    *****
        '''

        pg.setConfigOption('background', 'w')
        self.thi_graph_widget = pg.GraphicsLayoutWidget(
            self.thi_mainwidget)  # QtWidgets.QWidget(self.thi_mainwidget) # Put graph here
        self.a = ''
        self.thi_graph_widget.resize(741, 481)
        self.ch = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.curve = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.y = ['r', 'b', 'g', 'r', 'c', 'm', 'b', 'k']

        self.channels = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []]]
        self.i = 0
        self.WINDOW_SIZE = 1
        self.MAX_DATA_SIZE = 1000
        self.add_graphs(self.thi_graph_widget, 0)
        self.stream = False
        self.timer = QtCore.QTimer()
        self.live = False

        '''
                        *****   PlayBack work Ends Here     ******
        '''

        self.thi_graph_widget.setGeometry(QtCore.QRect(140, 120, 741, 481))
        self.thi_graph_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.thi_graph_widget.setObjectName("thi_graph_widget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.thi_mainwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 120, 49, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.thi_channel_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.thi_channel_verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.thi_channel_verticalLayout.setSpacing(30)
        self.thi_channel_verticalLayout.setObjectName("thi_channel_verticalLayout")
        self.fps_2 = QtWidgets.QLabel(self.thi_mainwidget)
        self.fps_2.setGeometry(QtCore.QRect(460, 90, 111, 20))
        self.fps_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fps_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fps_2.setObjectName("fps_2")
        self.thi_ch1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch1.setObjectName("thi_ch1")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch1)
        self.thi_ch2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch2.setObjectName("thi_ch2")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch2)
        self.thi_ch3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch3.setObjectName("thi_ch3")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch3)
        self.thi_ch4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch4.setObjectName("thi_ch4")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch4)
        self.thi_ch5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch5.setObjectName("thi_ch5")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch5)
        self.thi_ch6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch6.setObjectName("thi_ch6")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch6)
        self.thi_ch7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch7.setObjectName("thi_ch7")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch7)
        self.thi_ch8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.thi_ch8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.thi_ch8.setObjectName("thi_ch8")
        self.thi_channel_verticalLayout.addWidget(self.thi_ch8)
        self.sec_mainwidget = QtWidgets.QWidget(self.Main_widget)
        self.sec_mainwidget.setGeometry(QtCore.QRect(20, 0, 931, 631))
        self.sec_mainwidget.setAutoFillBackground(False)
        self.sec_mainwidget.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.sec_mainwidget.setObjectName("sec_mainwidget")
        self.sec_top_graphic = QtWidgets.QGraphicsView(self.sec_mainwidget)
        self.sec_top_graphic.setGeometry(QtCore.QRect(0, 10, 931, 61))
        self.sec_top_graphic.setStyleSheet("background-color: rgb(6, 6, 159);")
        self.sec_top_graphic.setObjectName("sec_top_graphic")
        self.sec_main_graphicsView = QtWidgets.QGraphicsView(self.sec_mainwidget)
        self.sec_main_graphicsView.setGeometry(QtCore.QRect(0, 70, 931, 591))
        self.sec_main_graphicsView.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.sec_main_graphicsView.setObjectName("sec_main_graphicsView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.sec_mainwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 120, 49, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.sec_channel_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.sec_channel_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sec_channel_verticalLayout.setObjectName("sec_channel_verticalLayout")
        self.sec_ch1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch1.setObjectName("sec_ch1")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch1)
        self.sec_ch2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch2.setObjectName("sec_ch2")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch2)
        self.sec_ch3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch3.setObjectName("sec_ch3")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch3)
        self.sec_ch4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch4.setObjectName("sec_ch4")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch4)
        self.sec_ch5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch5.setObjectName("sec_ch5")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch5)
        self.sec_ch6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch6.setObjectName("sec_ch6")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch6)
        self.sec_ch7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch7.setObjectName("sec_ch7")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch7)
        self.sec_ch8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sec_ch8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 87 10pt \"Segoe UI Black\";")
        self.sec_ch8.setObjectName("sec_ch8")
        self.sec_channel_verticalLayout.addWidget(self.sec_ch8)
        self.sec_topbarwidget = QtWidgets.QWidget(self.sec_mainwidget)
        self.sec_topbarwidget.setGeometry(QtCore.QRect(10, 20, 911, 41))
        self.sec_topbarwidget.setStyleSheet("background-color: rgb(7, 2, 50);")
        self.sec_topbarwidget.setObjectName("sec_topbarwidget")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.sec_topbarwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(60, 0, 346, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.sec_horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.sec_horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sec_horizontalLayout_5.setObjectName("sec_horizontalLayout_5")
        self.sec_back_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.sec_back_Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sec_back_Button.setIcon(icon1)
        self.sec_back_Button.setObjectName("sec_back_Button")
        self.sec_horizontalLayout_5.addWidget(self.sec_back_Button)
        self.sec_startstream_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.sec_startstream_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sec_startstream_button.setIcon(icon2)
        self.sec_startstream_button.setObjectName("sec_startstream_button")
        self.sec_horizontalLayout_5.addWidget(self.sec_startstream_button)
        self.sec_stopstream_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.sec_stopstream_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sec_stopstream_button.setIcon(icon3)
        self.sec_stopstream_button.setObjectName("sec_stopstream_button")
        self.sec_horizontalLayout_5.addWidget(self.sec_stopstream_button)
        self.sec_notchfilter_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.sec_notchfilter_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sec_notchfilter_button.setObjectName("sec_notchfilter_button")
        self.sec_horizontalLayout_5.addWidget(self.sec_notchfilter_button)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.sec_topbarwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(440, 0, 160, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.sec_horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.sec_horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sec_horizontalLayout_7.setObjectName("sec_horizontalLayout_7")
        self.sec_HUlogo_label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.sec_HUlogo_label.setStyleSheet("image: url(logos/logo.png);")
        self.sec_HUlogo_label.setText("")
        self.sec_HUlogo_label.setObjectName("sec_HUlogo_label")
        self.sec_horizontalLayout_7.addWidget(self.sec_HUlogo_label)
        self.sec_pdaq_label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.sec_pdaq_label.setAutoFillBackground(False)
        self.sec_pdaq_label.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
                                          "color: rgb(255, 255, 255);")
        self.sec_pdaq_label.setObjectName("sec_pdaq_label")
        self.sec_horizontalLayout_7.addWidget(self.sec_pdaq_label)

        self.sec_graph_widget = pg.GraphicsLayoutWidget(self.sec_mainwidget)

        self.sec_graph_widget.setGeometry(QtCore.QRect(130, 120, 731, 481))
        self.sec_graph_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sec_graph_widget.setObjectName("sec_graph_widget")
        self.add_graphs(self.sec_graph_widget, 1)
        self.fps = QtWidgets.QLabel(self.sec_mainwidget)
        self.fps.setGeometry(QtCore.QRect(450, 90, 111, 20))
        self.fps.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fps.setAlignment(QtCore.Qt.AlignCenter)
        self.fps.setObjectName("fps")

        self.fir_mainwidget = QtWidgets.QWidget(self.Main_widget)
        self.fir_mainwidget.setGeometry(QtCore.QRect(10, -20, 951, 641))
        self.fir_mainwidget.setAutoFillBackground(False)
        self.fir_mainwidget.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.fir_mainwidget.setObjectName("fir_mainwidget")
        self.fir_top_graphic = QtWidgets.QGraphicsView(self.fir_mainwidget)
        self.fir_top_graphic.setGeometry(QtCore.QRect(10, 30, 931, 61))
        self.fir_top_graphic.setStyleSheet("background-color: rgb(6, 6, 159);")
        self.fir_top_graphic.setObjectName("fir_top_graphic")
        self.fir_topbarwidget = QtWidgets.QWidget(self.fir_mainwidget)
        self.fir_topbarwidget.setGeometry(QtCore.QRect(20, 40, 911, 41))
        self.fir_topbarwidget.setStyleSheet("background-color: rgb(7, 2, 50);")
        self.fir_topbarwidget.setObjectName("fir_topbarwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.fir_topbarwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 0, 235, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.fir_horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.fir_horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fir_horizontalLayout_2.setObjectName("fir_horizontalLayout_2")

        self.Live_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Live_Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Live_Button.setIconSize(QtCore.QSize(16, 16))
        self.Live_Button.setObjectName("Live_Button")

        self.fir_horizontalLayout_2.addWidget(self.Live_Button)
        self.playback_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.playback_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.playback_button.setIconSize(QtCore.QSize(15, 16))
        self.playback_button.setObjectName("playback_button")
        self.fir_horizontalLayout_2.addWidget(self.playback_button)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.fir_topbarwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(440, 0, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.fir_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.fir_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fir_horizontalLayout.setObjectName("fir_horizontalLayout")
        self.fir_HUlogo_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fir_HUlogo_label.setStyleSheet("image: url(logos/logo.png);")
        self.fir_HUlogo_label.setText("")
        self.fir_HUlogo_label.setObjectName("fir_HUlogo_label")
        self.fir_horizontalLayout.addWidget(self.fir_HUlogo_label)
        self.fir_pdaq_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fir_pdaq_label.setAutoFillBackground(False)
        self.fir_pdaq_label.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
                                          "color: rgb(255, 255, 255);")
        self.fir_pdaq_label.setObjectName("fir_pdaq_label")
        self.fir_horizontalLayout.addWidget(self.fir_pdaq_label)
        self.fir_main_graphicsView = QtWidgets.QGraphicsView(self.fir_mainwidget)
        self.fir_main_graphicsView.setGeometry(QtCore.QRect(10, 90, 931, 591))
        self.fir_main_graphicsView.setAccessibleName("")
        self.fir_main_graphicsView.setAccessibleDescription("")
        self.fir_main_graphicsView.setStyleSheet("background-color: rgb(2, 3, 56);")
        self.fir_main_graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.fir_main_graphicsView.setObjectName("fir_main_graphicsView")
        self.fir_PDAQ_label = QtWidgets.QLabel(self.fir_mainwidget)
        self.fir_PDAQ_label.setGeometry(QtCore.QRect(260, 440, 481, 41))
        self.fir_PDAQ_label.setStyleSheet("font: 81 16pt \"Rockwell Extra Bold\";\n"
                                          "color: rgb(255, 255, 255);")
        self.fir_PDAQ_label.setObjectName("fir_PDAQ_label")
        self.fir_bottom_widget = QtWidgets.QWidget(self.fir_mainwidget)
        self.fir_bottom_widget.setGeometry(QtCore.QRect(90, 580, 811, 51))
        self.fir_bottom_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fir_bottom_widget.setObjectName("fir_bottom_widget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.fir_bottom_widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(280, 0, 403, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.fir_horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.fir_horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fir_horizontalLayout_3.setObjectName("fir_horizontalLayout_3")
        self.muddasir_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.muddasir_label.setStyleSheet("font: 81 8pt \"Rockwell Extra Bold\";")
        self.muddasir_label.setObjectName("muddasir_label")
        self.fir_horizontalLayout_3.addWidget(self.muddasir_label)
        self.khizar_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.khizar_label.setStyleSheet("font: 81 8pt \"Rockwell Extra Bold\";")
        self.khizar_label.setObjectName("khizar_label")
        self.fir_horizontalLayout_3.addWidget(self.khizar_label)
        self.mirza_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.mirza_label.setStyleSheet("font: 81 8pt \"Rockwell Extra Bold\";")
        self.mirza_label.setObjectName("mirza_label")
        self.fir_horizontalLayout_3.addWidget(self.mirza_label)
        self.zubair_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.zubair_label.setStyleSheet("font: 81 8pt \"Rockwell Extra Bold\";")
        self.zubair_label.setObjectName("zubair_label")
        self.fir_horizontalLayout_3.addWidget(self.zubair_label)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.fir_bottom_widget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(100, 10, 160, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.fir_horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.fir_horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.fir_horizontalLayout_4.setObjectName("fir_horizontalLayout_4")
        self.team_member_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.team_member_label.setStyleSheet("font: 81 11pt \"Rockwell Extra Bold\";")
        self.team_member_label.setObjectName("team_member_label")
        self.fir_horizontalLayout_4.addWidget(self.team_member_label)
        self.fir_huimage_label = QtWidgets.QLabel(self.fir_mainwidget)
        self.fir_huimage_label.setGeometry(QtCore.QRect(360, 210, 241, 201))
        self.fir_huimage_label.setStyleSheet("image: url(logos/logo.png);")
        self.fir_huimage_label.setText("")
        self.fir_huimage_label.setObjectName("fir_huimage_label")
        self.fir_label_supervisor = QtWidgets.QLabel(self.fir_mainwidget)
        self.fir_label_supervisor.setGeometry(QtCore.QRect(310, 500, 391, 51))
        self.fir_label_supervisor.setStyleSheet("font: 81 12pt \"Rockwell Extra Bold\";\n"
                                                "color: rgb(255, 255, 255);")
        self.fir_label_supervisor.setObjectName("fir_label_supervisor")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.playback_button.clicked.connect(self.sec_mainwidget.hide)
        self.playback_button.clicked.connect(self.fir_mainwidget.hide)
        self.playback_button.clicked.connect(self.set_mode_p)
        self.sec_back_Button.clicked.connect(self.live_back)
        self.sec_startstream_button.clicked.connect(self.timera)
        self.sec_stopstream_button.clicked.connect(self.timer.stop)
        # self.Live_Button.clicked.connect(self.fir_mainwidget.hide)
        self.Live_Button.clicked.connect(self.set_mode_l)
        self.thi_back_Button_2.clicked.connect(self.fir_mainwidget.show)
        self.thi_back_Button_2.clicked.connect(self.sec_mainwidget.show)
        self.thi_startstream_button_2.clicked.connect(self.star_stream)
        self.thi_stopstream_button_2.clicked.connect(self.stop_stream)


        self.fp = 0

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        '''
                    *****   PlayBack work continue from here     ******
        '''

    def live_back(self):
        self.fir_mainwidget.show()
        self.live = False
        self.liv.close_serial()
        self.stop_stream()

    def set_mode_p(self):
        self.m = 0

    def set_mode_l(self):

        try:
            self.liv = Live(False)
            self.liv.initialize()
            self.liv.run(self.error_msg)
            atexit.register(self.liv.close_serial)
            self.fir_mainwidget.hide()
            self.m = 1
            self.live = True
        except:
            self.error_msg("Error", "Couldn't find arduino")

    def error_msg(self, title, msg):
        QMessageBox.about(self, title, msg)

    def add_graphs(self, glayout, md):
        if md == 1: yaxis = False
        else: yaxis = True
        for x in range(8):
            self.ch[x][md] = glayout.addPlot()
            self.ch[x][md].showGrid(False, False)
            self.ch[x][md].setYRange(-5, 5)
            self.ch[x][md].setXRange(0, 4)
            self.ch[x][md].enableAutoRange(x=False, y=yaxis)
            self.curve[x][md] = self.ch[x][md].plot(pen=self.y[x])
            glayout.nextRow()
            if x < 7:
                self.ch[x][md].hideAxis('bottom')
            if x < 8:
                self.ch[x][md].hideAxis('left')

    def open_file_dialogue(self):
        self.open_files = App(self.get_file_path)
        # self.open_files.abc()
        # self.fil= self.open_file_dialogue.file

    def update_graph(self):

        if self.live:
            try:
                temp = self.liv.decode_frame_analog()
            except OSError:
                print("Error")
                self.stop_stream()
                # self.live_back()

        for j in range(8):
            if self.live:
                r = temp[j] * (5 / 1023)
            else:
                r = self.datacollect[self.i, j + 1] * 10 ** (-2)

            self.channels[j][self.m].append(r)
            t = np.arange(start=0, stop=0.004 * len(self.channels[j][self.m]), step=0.004)
            self.curve[j][self.m].setData(x=t[0:len(self.channels[j][self.m])], y=self.channels[j][self.m])
            if len(self.channels[j][self.m]) > self.MAX_DATA_SIZE:
                self.channels[j][self.m] = self.channels[j][self.m][self.WINDOW_SIZE:]
        if self.m == 0:
            self.i += 1
            if self.i == len(self.datacollect):
                self.stop_stream()
                print("end")

        self.counter += 1

        ctime = time() - self.start_time

        if self.fp == 0:
            self.fp = self.counter / ctime
        if ctime > self.x:
            self.fp = self.counter / ctime
            #print(self.counter , ctime)
            self.counter = 0
            self.start_time = time()

        if self.live:
            self.fps.setText('%0.2f fps' % self.fp)
        else:
            self.fps_2.setText('%0.2f fps' % self.fp)
        '''
                        *****   PlayBack work Ends Here     ******
        '''

    def get_file_path(self, path):
        self.a = path  # '/root/Desktop/--Codes--/Final Gui/testdata.txt'
        if '.txt' in self.a:
            try:
                self.datacollect = np.loadtxt(fname=self.a, delimiter=',', skiprows=1,usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
            except IndexError:
                QMessageBox.about(self, "Format Error", "File format not suported")
                self.a = ''

        print(self.a)

    def plot_file(self):
        if '.txt' in self.a:
            # self.datacollect = np.loadtxt(fname=self.a, delimiter=',', skiprows=1, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
            self.timera()
        # print(self.datacollect)

    def timera(self):
        if self.timer.isActive(): self.timer.stop();
        self.start_time = time()
        self.x = 0.5  # displays the frame rate every 1 second
        self.counter = 0
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(1)
        # while(self.stream == True):
        # self.update()

    def star_stream(self):
        if not self.timer.isActive():
            self.stream = True
            self.plot_file()
            print('start')

    '''    def stp(self):
        self.stream = False
        self.timer.stop()'''

    def stop_stream(self):
        self.stream = False
        if self.live:
            self.liv.command(b's')
        if self.timer.isActive():
            self.timer.stop()
            self.timer.timeout.disconnect(self.update_graph)
            self.i = 0
            print('stop')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HU P-DAQ"))
        MainWindow.setAccessibleName(_translate("MainWindow", "as"))
        self.thi_back_Button_2.setText(_translate("MainWindow", "Back"))
        self.thi_startstream_button_2.setText(_translate("MainWindow", "Start Stream"))
        self.thi_stopstream_button_2.setText(_translate("MainWindow", "Stop Stream"))
        self.thi_openfile_button.setText(_translate("MainWindow", "Open File"))
        self.thi_pdaq_label.setText(_translate("MainWindow", " HU P-DAQ"))
        self.thi_ch1.setText(_translate("MainWindow", "   CH 1"))
        self.thi_ch2.setText(_translate("MainWindow", "   CH 2"))
        self.thi_ch3.setText(_translate("MainWindow", "   CH 3"))
        self.thi_ch4.setText(_translate("MainWindow", "   CH 4"))
        self.thi_ch5.setText(_translate("MainWindow", "   CH 5"))
        self.thi_ch6.setText(_translate("MainWindow", "   CH 6"))
        self.thi_ch7.setText(_translate("MainWindow", "   CH 7"))
        self.thi_ch8.setText(_translate("MainWindow", "   CH 8"))
        self.sec_ch1.setText(_translate("MainWindow", "   CH 1"))
        self.sec_ch2.setText(_translate("MainWindow", "   CH 2"))
        self.sec_ch3.setText(_translate("MainWindow", "   CH 3"))
        self.sec_ch4.setText(_translate("MainWindow", "   CH 4"))
        self.sec_ch5.setText(_translate("MainWindow", "   CH 5"))
        self.sec_ch6.setText(_translate("MainWindow", "   CH 6"))
        self.sec_ch7.setText(_translate("MainWindow", "   CH 7"))
        self.sec_ch8.setText(_translate("MainWindow", "   CH 8"))
        self.sec_back_Button.setText(_translate("MainWindow", "Back"))
        self.sec_startstream_button.setText(_translate("MainWindow", "Start Stream"))
        self.sec_stopstream_button.setText(_translate("MainWindow", "Stop Stream"))
        self.sec_notchfilter_button.setText(_translate("MainWindow", "Notch Filter"))
        self.sec_pdaq_label.setText(_translate("MainWindow", " HU P-DAQ"))
        """
                            First Page Start
        """

        self.Live_Button.setText(_translate("MainWindow", "Live Data"))
        self.playback_button.setText(_translate("MainWindow", "PlayBack Data"))
        self.fir_pdaq_label.setText(_translate("MainWindow", " HU P-DAQ"))
        self.fir_PDAQ_label.setText(_translate("MainWindow", "Python based Physiological Data Acquisition System"))
        self.muddasir_label.setText(_translate("MainWindow", "Muddasir Noor |"))
        self.khizar_label.setText(_translate("MainWindow", "Khizar Ali |"))
        self.mirza_label.setText(_translate("MainWindow", "Mirza Ubaidullah |"))
        self.zubair_label.setText(_translate("MainWindow", "Zubair Jamil"))
        self.team_member_label.setText(_translate("MainWindow", "Team Members:"))
        self.fir_label_supervisor.setText(_translate("MainWindow", "Project Supervisor: Engr. Azhar Dilshad"))
        """
                            First Page End
        """


# import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
