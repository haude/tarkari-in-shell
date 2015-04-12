'''
Created on Apr 12, 2015

@author: greenpaper
'''
from dialogs.MainWindow import  Ui_MainWindow
from PyQt4 import QtGui, QtCore
from utils.tarkari import ParserTarkari

class Mainwindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignals()
        self.parsser = ParserTarkari()
    
    def connectSignals(self):
        self.ui.actionUsage.triggered.connect(self.update_commodity)
        self.ui.actionRefresh_data.triggered.connect(self.oops)
    
    def update_commodity(self):
        self.ui.treeWidget.topLevelItem(0).setText(0,"just practice")
    
    def oops(self):
        data = self.parsser.prepare_data()
        print(type(data))
        print(data)
        self.ui.treeWidget.topLevelItem(0).setText(0,data[0])
        self.ui.treeWidget.topLevelItem(0).setText(2,data[2])
        self.ui.treeWidget.topLevelItem(0).setText(3,data[3])
        self.ui.treeWidget.topLevelItem(0).setText(1,data[1])
        self.ui.treeWidget.topLevelItem(0).setText(4,data[4])
    
    
