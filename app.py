'''
Created on Apr 12, 2015

@author: greenpaper
'''
from PyQt4 import QtGui
from guipart.mywindow import Mainwindow
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myui = Mainwindow()
    
    myui.show()
    sys.exit(app.exec_())