# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import dijkstra

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 418)
        #MainWindow.setAttribute(QtCore.Qt.WA_StyledBackground)
        MainWindow.setStyleSheet('''''')
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 0, 311, 26))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(10, 20, 381, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.P_A = QtWidgets.QPushButton(self.centralWidget)
        self.P_A.setGeometry(QtCore.QRect(10, 40, 81, 101))
        self.P_A.setObjectName("P_A")
        self.P_B = QtWidgets.QPushButton(self.centralWidget)
        self.P_B.setGeometry(QtCore.QRect(130, 40, 71, 91))
        self.P_B.setObjectName("P_B")
        self.P_E = QtWidgets.QPushButton(self.centralWidget)
        self.P_E.setGeometry(QtCore.QRect(300, 40, 80, 91))
        self.P_E.setObjectName("P_E")
        self.P_J = QtWidgets.QPushButton(self.centralWidget)
        self.P_J.setGeometry(QtCore.QRect(250, 290, 121, 61))
        self.P_J.setObjectName("P_J")
        self.P_C = QtWidgets.QPushButton(self.centralWidget)
        self.P_C.setGeometry(QtCore.QRect(10, 170, 141, 81))
        self.P_C.setObjectName("P_C")
        self.P_D = QtWidgets.QPushButton(self.centralWidget)
        self.P_D.setGeometry(QtCore.QRect(220, 40, 51, 51))
        self.P_D.setObjectName("P_D")
        self.CS2 = QtWidgets.QPushButton(self.centralWidget)
        self.CS2.setGeometry(QtCore.QRect(250, 100, 31, 26))
        self.CS2.setObjectName("CS2")
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        self.line_6.setGeometry(QtCore.QRect(160, 140, 66, 20))
        self.line_6.setStyleSheet("Line{\n"
"    background: rgb(85, 87, 83);\n"
"}")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        self.line_7.setGeometry(QtCore.QRect(49, 140, 16, 13))
        self.line_7.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(5)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        self.line_8.setGeometry(QtCore.QRect(150, 130, 16, 23))
        self.line_8.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(5)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.line_10 = QtWidgets.QFrame(self.centralWidget)
        self.line_10.setGeometry(QtCore.QRect(230, 100, 20, 20))
        self.line_10.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(5)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralWidget)
        self.line_11.setGeometry(QtCore.QRect(320, 130, 16, 23))
        self.line_11.setStyleSheet('''Line{\n
    color: rgb(85, 87, 83);\n
}''')
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(5)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralWidget)
        self.line_12.setGeometry(QtCore.QRect(331, 140, 61, 20))
        self.line_12.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(5)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.P_H = QtWidgets.QPushButton(self.centralWidget)
        self.P_H.setGeometry(QtCore.QRect(10, 290, 51, 71))
        self.P_H.setObjectName("P_H")
        self.P_G = QtWidgets.QPushButton(self.centralWidget)
        self.P_G.setGeometry(QtCore.QRect(170, 170, 51, 71))
        self.P_G.setObjectName("P_G")
        self.P_I = QtWidgets.QPushButton(self.centralWidget)
        self.P_I.setGeometry(QtCore.QRect(120, 290, 111, 81))
        self.P_I.setObjectName("P_I")
        self.CS4 = QtWidgets.QPushButton(self.centralWidget)
        self.CS4.setGeometry(QtCore.QRect(330, 230, 31, 26))
        self.CS4.setObjectName("CS4")
        self.P_F = QtWidgets.QPushButton(self.centralWidget)
        self.P_F.setGeometry(QtCore.QRect(240, 170, 141, 61))
        self.P_F.setObjectName("P_F")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(36, 255, 30, 20))
        self.line_2.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setGeometry(QtCore.QRect(70, 255, 26, 20))
        self.line_5.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_13 = QtWidgets.QFrame(self.centralWidget)
        self.line_13.setGeometry(QtCore.QRect(230, 257, 65, 16))
        self.line_13.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(5)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralWidget)
        self.line_14.setGeometry(QtCore.QRect(148, 153, 20, 51))
        self.line_14.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(5)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralWidget)
        self.line_15.setGeometry(QtCore.QRect(5, 140, 50, 20))
        self.line_15.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_15.setLineWidth(5)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralWidget)
        self.line_16.setGeometry(QtCore.QRect(60, 250, 16, 18))
        self.line_16.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_16.setLineWidth(5)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralWidget)
        self.line_17.setGeometry(QtCore.QRect(161, 255, 65, 20))
        self.line_17.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_17.setLineWidth(5)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setObjectName("line_17")
        self.CS3 = QtWidgets.QPushButton(self.centralWidget)
        self.CS3.setGeometry(QtCore.QRect(70, 290, 31, 26))
        self.CS3.setObjectName("CS3")
        self.line_18 = QtWidgets.QFrame(self.centralWidget)
        self.line_18.setGeometry(QtCore.QRect(220, 152, 16, 116))
        self.line_18.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_18.setLineWidth(5)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralWidget)
        self.line_19.setGeometry(QtCore.QRect(150, 263, 16, 28))
        self.line_19.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(5)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralWidget)
        self.line_20.setGeometry(QtCore.QRect(30, 268, 16, 23))
        self.line_20.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_20.setLineWidth(5)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.centralWidget)
        self.line_21.setGeometry(QtCore.QRect(60, 300, 11, 12))
        self.line_21.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_21.setLineWidth(5)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.centralWidget)
        self.line_22.setGeometry(QtCore.QRect(90, 263, 16, 28))
        self.line_22.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_22.setLineWidth(5)
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.centralWidget)
        self.line_23.setGeometry(QtCore.QRect(101, 257, 55, 16))
        self.line_23.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_23.setLineWidth(5)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setObjectName("line_23")
        self.line_25 = QtWidgets.QFrame(self.centralWidget)
        self.line_25.setGeometry(QtCore.QRect(289, 230, 16, 33))
        self.line_25.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_25.setLineWidth(5)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.centralWidget)
        self.line_26.setGeometry(QtCore.QRect(289, 268, 16, 22))
        self.line_26.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_26.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_26.setLineWidth(5)
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.centralWidget)
        self.line_27.setGeometry(QtCore.QRect(295, 255, 52, 20))
        self.line_27.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_27.setLineWidth(5)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.centralWidget)
        self.line_28.setGeometry(QtCore.QRect(340, 256, 16, 12))
        self.line_28.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_28.setLineWidth(5)
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setObjectName("line_28")
        self.line_9 = QtWidgets.QFrame(self.centralWidget)
        self.line_9.setGeometry(QtCore.QRect(218, 113, 20, 36))
        self.line_9.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(5)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_24 = QtWidgets.QFrame(self.centralWidget)
        self.line_24.setGeometry(QtCore.QRect(156, 196, 14, 20))
        self.line_24.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_24.setLineWidth(5)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setObjectName("line_24")
        self.line_29 = QtWidgets.QFrame(self.centralWidget)
        self.line_29.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.line_29.setGeometry(QtCore.QRect(150, 209, 16, 54))
        self.line_29.setStyleSheet("Line{\n"
"    color: rgb(114, 159, 207);\n"
"}")
        self.line_29.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_29.setLineWidth(5)
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(self.centralWidget)
        self.line_30.setGeometry(QtCore.QRect(5, 257, 31, 16))
        self.line_30.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_30.setLineWidth(5)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(self.centralWidget)
        self.line_31.setGeometry(QtCore.QRect(351, 257, 41, 16))
        self.line_31.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_31.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_31.setLineWidth(5)
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setObjectName("line_31")
        self.CS1 = QtWidgets.QPushButton(self.centralWidget)
        self.CS1.setEnabled(True)
        self.CS1.setGeometry(QtCore.QRect(90, 110, 31, 26))
        self.CS1.setObjectName("CS1")
        self.line_32 = QtWidgets.QFrame(self.centralWidget)
        self.line_32.setGeometry(QtCore.QRect(95, 136, 16, 17))
        self.line_32.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_32.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_32.setLineWidth(5)
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setObjectName("line_32")
        self.line_33 = QtWidgets.QFrame(self.centralWidget)
        self.line_33.setGeometry(QtCore.QRect(105, 142, 51, 16))
        self.line_33.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_33.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_33.setLineWidth(5)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setObjectName("line_33")
        self.Reset = QtWidgets.QPushButton(self.centralWidget)
        self.Reset.setGeometry(QtCore.QRect(330, 3, 61, 21))
        self.Reset.setCheckable(False)
        self.Reset.setFlat(False)
        self.Reset.setObjectName("Reset")
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setWindowModality(QtCore.Qt.NonModal)
        self.line_3.setGeometry(QtCore.QRect(226, 140, 100, 20))
        self.line_3.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(60, 140, 41, 20))
        self.line_4.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_34 = QtWidgets.QFrame(self.centralWidget)
        self.line_34.setGeometry(QtCore.QRect(218, 90, 20, 23))
        self.line_34.setStyleSheet("Line{\n"
"    color: rgb(85, 87, 83);\n"
"}")
        self.line_34.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_34.setLineWidth(5)
        self.line_34.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_34.setObjectName("line_34")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.setText("Select your nearest building")

        self.Reset.clicked.connect(self.reset)

        self.P_A.clicked.connect(lambda: self.path('A'))
        self.P_B.clicked.connect(lambda: self.path('B'))
        self.P_C.clicked.connect(lambda: self.path('C'))
        self.P_D.clicked.connect(lambda: self.path('D'))
        self.P_E.clicked.connect(lambda: self.path('E'))
        self.P_F.clicked.connect(lambda: self.path('F'))
        self.P_G.clicked.connect(lambda: self.path('G'))
        self.P_H.clicked.connect(lambda: self.path('H'))
        self.P_I.clicked.connect(lambda: self.path('I'))
        self.P_J.clicked.connect(lambda: self.path('J'))


    def reset(self):
        lines = (self.line, self.line_2, self.line_3, self.line_4, self.line_5,
                 self.line_6, self.line_7, self.line_8, self.line_9, self.line_10,
                 self.line_11, self.line_12, self.line_13, self.line_14, self.line_15,
                 self.line_16, self.line_17, self.line_18, self.line_19, self.line_20,
                 self.line_21, self.line_22, self.line_23, self.line_24, self.line_25,
                 self.line_26, self.line_27, self.line_28, self.line_29, self.line_30,
                 self.line_31, self.line_32, self.line_33, self.line_34)
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        for i in lines:
            i.setPalette(palette)

        self.lineEdit.setText("Select your nearest building")
        pb = (self.P_A, self.P_B, self.P_C, self.P_D, self.P_E, self.P_F, 
            self.P_G, self.P_H, self.P_I, self.P_J, self.CS1, self.CS2, self.CS3, self.CS4)
        for i in pb:
            i.setEnabled(True)
    def path(self, caller):
        near = dijkstra.main(caller)
        if near == 0:
            self.lineEdit.setText("No Cycles available")
    
        else:
            hs = near[0]
            dist = near[1]
            back = near[2]
            self.pathHl(hs,dist,back)
            pb = (self.P_A, self.P_B, self.P_C, self.P_D, self.P_E, self.P_F, 
            self.P_G, self.P_H, self.P_I, self.P_J, self.CS1, self.CS2, self.CS3, self.CS4)
            for i in range(14):
                if i == ord(caller) - 65 or i == hs - 10:
                    continue
                pb[i].setEnabled(False)



    def pathHl(self,hs,dist,back):
        lines = {'0-10' : (self.line_4,self.line_7), '10-20' : self.line_32,
                '10-11': self.line_33, '1-11': self.line_8, 
                '11-12': self.line_6, '12-13': self.line_9, 
                '3-13': self.line_34, '13-21': self.line_10, 
                '4-12': (self.line_3,self.line_11), '11-14': self.line_14, 
                '6-14': self.line_24, '14-15': self.line_29, 
                '12-18': self.line_18, '8-15': self.line_19,
                '15-16': self.line_23, '16-17': self.line_5,
                '2-17': self.line_16, '7-17': (self.line_2,self.line_17), 
                '16-22': self.line_22, '7-22': self.line_21, 
                '15-18': self.line_17, '18-19': self.line_13, 
                '5-19': self.line_25, '9-19': self.line_26,
                '19-23': (self.line_28,self.line_27)}

        i = back[hs]
        while i != None:
            j = min(i,hs)
            k = max(i,hs)
            ki = str(j)+'-'+str(k)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            if str(type(lines[ki])) == "<class 'tuple'>":
                lines[ki][0].setPalette(palette)
                lines[ki][1].setPalette(palette)
            else:
                lines[ki].setPalette(palette)
            hs = i
            i = back[hs]
        self.lineEdit.setText("Nearest hotspot is "+str(dist)+"m away")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.P_A.setText(_translate("MainWindow", "A"))
        self.P_B.setText(_translate("MainWindow", "B"))
        self.P_E.setText(_translate("MainWindow", "E"))
        self.P_J.setText(_translate("MainWindow", "J"))
        self.P_C.setText(_translate("MainWindow", "C"))
        self.P_D.setText(_translate("MainWindow", "D"))
        self.CS2.setText(_translate("MainWindow", "CS2"))
        self.P_H.setText(_translate("MainWindow", "H"))
        self.P_G.setText(_translate("MainWindow", "G"))
        self.P_I.setText(_translate("MainWindow", "I"))
        self.CS4.setText(_translate("MainWindow", "CS4"))
        self.P_F.setText(_translate("MainWindow", "F"))
        self.CS3.setText(_translate("MainWindow", "CS3"))
        self.CS1.setText(_translate("MainWindow", "CS1"))
        self.Reset.setStatusTip(_translate("MainWindow", "Click this button to select the building nearest to you."))
        self.Reset.setText(_translate("MainWindow", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

