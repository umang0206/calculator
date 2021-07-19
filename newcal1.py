# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newcalci.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt


class Ui_Calculator(object):
    def __init__(self):
        self.s1=''
        self.s2=''
        self.s3=''
        self.s4=''
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(110, 114, 331, 51))
        self.T1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T1.setObjectName("T1")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(110, 230, 61, 25))
        self.B1.setObjectName("B1")
        self.B1.clicked.connect(self.B1change)
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(200, 230, 61, 25))
        self.B2.setObjectName("B2")
        self.B2.clicked.connect(self.B2change)
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(290, 230, 61, 25))
        self.B3.setObjectName("B3")
        self.B3.clicked.connect(self.B3change)
        self.B13 = QtWidgets.QPushButton(self.centralwidget)
        self.B13.setGeometry(QtCore.QRect(380, 230, 61, 25))
        self.B13.setObjectName("B13")
        self.B13.clicked.connect(self.B13change)
        self.B4 = QtWidgets.QPushButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(110, 280, 61, 25))
        self.B4.setObjectName("B4")
        self.B4.clicked.connect(self.B4change)
        self.B5 = QtWidgets.QPushButton(self.centralwidget)
        self.B5.setGeometry(QtCore.QRect(200, 280, 61, 25))
        self.B5.setObjectName("B5")
        self.B5.clicked.connect(self.B5change)
        self.B6 = QtWidgets.QPushButton(self.centralwidget)
        self.B6.setGeometry(QtCore.QRect(290, 280, 61, 25))
        self.B6.setObjectName("B6")
        self.B6.clicked.connect(self.B6change)
        self.B14 = QtWidgets.QPushButton(self.centralwidget)
        self.B14.setGeometry(QtCore.QRect(380, 280, 61, 25))
        self.B14.setObjectName("B14")
        self.B14.clicked.connect(self.B14change)
        self.B7 = QtWidgets.QPushButton(self.centralwidget)
        self.B7.setGeometry(QtCore.QRect(110, 330, 61, 25))
        self.B7.setObjectName("B7")
        self.B7.clicked.connect(self.B7change)
        self.B8 = QtWidgets.QPushButton(self.centralwidget)
        self.B8.setGeometry(QtCore.QRect(200, 330, 61, 25))
        self.B8.setObjectName("B8")
        self.B8.clicked.connect(self.B8change)
        self.B9 = QtWidgets.QPushButton(self.centralwidget)
        self.B9.setGeometry(QtCore.QRect(290, 330, 61, 25))
        self.B9.setObjectName("B9")
        self.B9.clicked.connect(self.B9change)
        self.B15 = QtWidgets.QPushButton(self.centralwidget)
        self.B15.setGeometry(QtCore.QRect(380, 330, 61, 25))
        self.B15.setObjectName("B15")
        self.B15.clicked.connect(self.B15change)
        self.B10 = QtWidgets.QPushButton(self.centralwidget)
        self.B10.setGeometry(QtCore.QRect(110, 380, 61, 25))
        self.B10.setObjectName("B10")
        self.B10.clicked.connect(self.B10change)
        self.B11 = QtWidgets.QPushButton(self.centralwidget)
        self.B11.setGeometry(QtCore.QRect(380, 480, 61, 25))
        self.B11.setObjectName("B11")
        self.B11.clicked.connect(self.B11change)
        self.B17 = QtWidgets.QPushButton(self.centralwidget)
        self.B17.setGeometry(QtCore.QRect(380, 430, 61, 25))
        self.B17.setObjectName("B17")
        self.B17.clicked.connect(self.B17change)
        self.B16 = QtWidgets.QPushButton(self.centralwidget)
        self.B16.setGeometry(QtCore.QRect(380, 380, 61, 25))
        self.B16.setObjectName("B16")
        self.B16.clicked.connect(self.B16change)
        self.B12 = QtWidgets.QPushButton(self.centralwidget)
        self.B12.setGeometry(QtCore.QRect(290, 380, 61, 25))
        self.B12.setObjectName("B12")
        self.B12.clicked.connect(self.B12change)
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(110, 180, 331, 25))
        self.T2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T2.setObjectName("T2")
        self.fact = QtWidgets.QPushButton(self.centralwidget)
        self.fact.setGeometry(QtCore.QRect(200, 380, 61, 25))
        self.fact.setObjectName("fact")
        self.fact.clicked.connect(self.facto)
        self.Bopen = QtWidgets.QPushButton(self.centralwidget)
        self.Bopen.setGeometry(QtCore.QRect(110, 430, 61, 25))
        self.Bopen.setObjectName("Bopen")
        self.Bclose = QtWidgets.QPushButton(self.centralwidget)
        self.Bclose.setGeometry(QtCore.QRect(200, 430, 61, 25))
        self.Bclose.setObjectName("Bclose")
        self.binary = QtWidgets.QPushButton(self.centralwidget)
        self.binary.setGeometry(QtCore.QRect(110, 480, 61, 25))
        self.binary.setObjectName("binary")
        self.binary.clicked.connect(self.binchange)
        self.octal = QtWidgets.QPushButton(self.centralwidget)
        self.octal.setGeometry(QtCore.QRect(200, 480, 61, 25))
        self.octal.setObjectName("octal")
        self.octal.clicked.connect(self.octalchange)
        self.hexa = QtWidgets.QPushButton(self.centralwidget)
        self.hexa.setGeometry(QtCore.QRect(290, 480, 61, 25))
        self.hexa.setObjectName("hexa")
        self.hexa.clicked.connect(self.hexachange)
        self.squarerooot = QtWidgets.QPushButton(self.centralwidget)
        self.squarerooot.setGeometry(QtCore.QRect(290, 430, 61, 25))
        self.squarerooot.setObjectName("squarerooot")
        self.squarerooot.clicked.connect(self.squareroootchange)
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.T1.setText(_translate("Calculator", "0"))
        self.B1.setText(_translate("Calculator", "1"))
        self.B2.setText(_translate("Calculator", "2"))
        self.B3.setText(_translate("Calculator", "3"))
        self.B13.setText(_translate("Calculator", "+"))
        self.B4.setText(_translate("Calculator", "4"))
        self.B5.setText(_translate("Calculator", "5"))
        self.B6.setText(_translate("Calculator", "6"))
        self.B14.setText(_translate("Calculator", "-"))
        self.B7.setText(_translate("Calculator", "7"))
        self.B8.setText(_translate("Calculator", "8"))
        self.B9.setText(_translate("Calculator", "9"))
        self.B15.setText(_translate("Calculator", "x"))
        self.B10.setText(_translate("Calculator", "0"))
        self.B11.setText(_translate("Calculator", "Clear"))
        self.B17.setText(_translate("Calculator", "="))
        self.B16.setText(_translate("Calculator", "/"))
        self.B12.setText(_translate("Calculator", "."))
        self.T2.setText(_translate("Calculator", "0"))
        self.fact.setText(_translate("Calculator", "!"))
        self.Bopen.setText(_translate("Calculator", "("))
        self.Bclose.setText(_translate("Calculator", ")"))
        self.binary.setText(_translate("Calculator", "Bin"))
        self.octal.setText(_translate("Calculator", "Octal"))
        self.hexa.setText(_translate("Calculator", "Hexa"))
        self.squarerooot.setText(_translate("Calculator", "Sqrt"))
    def B1change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B1.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B2change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B2.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B3change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B3.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B4change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B4.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B5change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B5.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B6change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B6.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B7change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B7.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B8change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B8.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B9change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B9.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B10change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B10.text())
        c3 = c1+c2
        self.T1.setText(str(c3))
    def B11change(self):
        self.T1.setText("")
        self.T2.setText("")
        self.T1.setText("0")
    def B12change(self):
        c1 = str(self.T1.text())
        if '.' not in c1:
            c2 = str(self.B12.text())
            c3 = c1+c2
            self.T1.setText(str(c3))
    
    def B13change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B13.text())
        c3 = c1+c2
        self.s2 = c2
        self.T1.setText(str(c3))
    def B14change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B14.text())
        c3 = c1+c2
        self.s2 = c2
        self.T1.setText(str(c3))
    def B15change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B15.text())
        c3 = c1+c2
        self.s2 = c2
        self.T1.setText(str(c3))
    def B16change(self):
        c1 = str(self.T1.text())
        c2 = str(self.B16.text())
        c3 = c1+c2
        self.s2 = c2
        self.T1.setText(str(c3))
    def squareroootchange(self):
        c1 = str(self.T1.text())
        c2 = float(c1)
        c3 = sqrt(c2)
        self.T2.setText(str(c3))
    def facto(self):
        f = 1
        c1 = str(self.T1.text())
        c2 = str(self.fact.text())
        c3 = c1+c2
        self.s2 = c2
        self.T1.setText(str(c3))
        if c1.isdigit():
            for i in range(1,int(c1)+1):
                f = f * i
            self.T2.setText(str(f))
        else:
            self.T2.setText("Error!")
    def binchange(self):
        r1 = ''
        r2 = ''
        c = 0
        c1 = str(self.T1.text())
        for i in c1:
            if i == '.':
                break
            r1 = r1 + i
            c += 1
        if r1.isdigit():
            a = int(r1)
            count=1
            b = 0
            while a>0:
                remi = a%2
                b = b +remi*count
                a = a // 2
                count *= 10
            self.T2.setText(str(b))
    def octalchange(self):
        r1 = ''
        r2 = ''
        c = 0
        c1 = str(self.T1.text())
        for i in c1:
            if i == '.':
                break
            r1 = r1 + i
            c += 1
        if r1.isdigit():
            a = int(r1)
            count=1
            b = 0
            while a>0:
                remi = a%8
                b = b +remi*count
                a = a // 8
                count *= 10
            self.T2.setText(str(b))
    def hexachange(self):
        r1 = ''
        r2 = ''
        c = 0
        c1 = str(self.T1.text())
        h={'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
        for i in c1:
            if i == '.':
                break
            r1 = r1 + i
            c += 1
        if r1.isdigit():
            a = int(r1)
            b = ''; s =''
            while a>0:
                remi = str(a%16)
                if remi in h:
                    b = b+ h[remi]
                else:
                    b= b+remi
                a = a//16
            for i in range(len(b)-1,-1,-1):
                s = s +b[i]
            self.T2.setText(str(s))
                
                           
        
        
        
    def B17change(self):
        c1 = str(self.T1.text())
        r1 =''
        r2 =''
        r3= '.'
        c = 0;a =0;b = 0;
        for i in c1:
            if (i=="+") or (i =="-") or (i == "x") or (i == "/") or ( i == "!"):
                break
            r1 = r1 + i
            c+=1
        r2 = c1[c+1:]
        # this is for arthematic
        if r3 not in r1 :
            a = int(r1)  
        else:
            a = float(r1)
        if r3 not in r2 :
            b = int(r2)  
        else:
            b = float(r2)
           
        if i=="+":
            d = a+b
            self.T2.setText(str(d) )
        elif i=="-":
            d = a-b
            self.T2.setText(str(d) )
        elif i=="x":
            d = a*b
            self.T2.setText(str(d) )
        elif i=="/":
            d = a/b
            self.T2.setText(str(d) )
        else:
            self.T2.setText("Error")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
