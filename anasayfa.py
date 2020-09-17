# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ornek8 import *
from ornek7 import *
from ornek6 import *
from ornek5 import *
from ornek4 import *

class Ui_MainWindow(object):
    def ornek8bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow8()
        self.ui.setup8(self.window)
        self.window.show()
    def ornek7bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow7()
        self.ui.setup7(self.window)
        self.window.show()
    def ornek6bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow6()
        self.ui.setup6(self.window)
        self.window.show()
    def ornek5bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow5()
        self.ui.setup5(self.window)
        self.window.show()
    def ornek4bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow4()
        self.ui.setup4(self.window)
        self.window.show()
    def nsayisi(self):
        content=self.comboBox.currentText()
        if content=="8":
            self.ornek8bas()
        if content=="7":
            self.ornek7bas()
        if content=="6":
            self.ornek6bas()
        if content=="5":
            self.ornek5bas()
        if content=="4":
            self.ornek4bas()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oyun_buton = QtWidgets.QPushButton(self.centralwidget)
        self.oyun_buton.setGeometry(QtCore.QRect(50, 14, 231, 331))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.oyun_buton.setFont(font)
        self.oyun_buton.setObjectName("oyun_buton")
        self.ornek_buton = QtWidgets.QPushButton(self.centralwidget)
        self.ornek_buton.setGeometry(QtCore.QRect(308, 14, 241, 331))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.ornek_buton.setFont(font)
        self.ornek_buton.setObjectName("ornek_buton")
        self.ornek_buton.clicked.connect(self.nsayisi)
        	#self.ornek8bas && 
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 360, 101, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 360, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8 Vezir "))
        self.oyun_buton.setText(_translate("MainWindow", "Oyun"))
        self.ornek_buton.setText(_translate("MainWindow", "Örnek"))
        self.label.setText(_translate("MainWindow", "N Sayısı:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "4"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "7"))
        self.comboBox.setItemText(4, _translate("MainWindow", "8"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
