'''
Created on Apr 12, 2015

@author: greenpaper
'''
from dialogs.MainWindow import  Ui_MainWindow
from PyQt4 import QtGui, QtCore
from utils.tarkari import ParsetThread

class Mainwindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignals()
        self.threadedparser = ParsetThread()
        
    
    def connectSignals(self):
        self.ui.actionUsage.triggered.connect(self.update_commodity)
        self.ui.actionRefresh_data.triggered.connect(self.oops)
    
    def update_commodity(self):
        self.ui.treeWidget.topLevelItem(0).setText(0,"just practice")
    
    def oops(self,data):
        self.threadedparser.start()
        self.threadedparser.dataready.connect(self.display_data)
        
        
#         self.ui.treeWidget.topLevelItem(0).setText(0,data[0])
#         self.ui.treeWidget.topLevelItem(0).setText(2,data[2])
#         self.ui.treeWidget.topLevelItem(0).setText(3,data[3])
#
    def display_data(self,data):
        print(data)
        for i in range(len(data)):
            self.ui.treeWidget.topLevelItem(0).setText(i,data[i])
    
