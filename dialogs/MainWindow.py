# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kalimati.ui'
#
# Created: Sat Apr 11 13:25:46 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(693, 524)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setColumnCount(5)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.treeWidget.headerItem().setFont(0, font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/progress.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(0, icon)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setMinimumSectionSize(70)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefresh_data = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gears.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh_data.setIcon(icon1)
        self.actionRefresh_data.setObjectName(_fromUtf8("actionRefresh_data"))
        self.actionClose = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sun.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon2)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionUsage = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/not_available.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUsage.setIcon(icon3)
        self.actionUsage.setObjectName(_fromUtf8("actionUsage"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/protection.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionWholsale_price = QtGui.QAction(MainWindow)
        self.actionWholsale_price.setCheckable(True)
        self.actionWholsale_price.setChecked(False)
        self.actionWholsale_price.setObjectName(_fromUtf8("actionWholsale_price"))
        self.actionRetail_price = QtGui.QAction(MainWindow)
        self.actionRetail_price.setCheckable(True)
        self.actionRetail_price.setChecked(True)
        self.actionRetail_price.setObjectName(_fromUtf8("actionRetail_price"))
        self.menuFile.addAction(self.actionRefresh_data)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionUsage)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionWholsale_price)
        self.menuEdit.addAction(self.actionRetail_price)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "commodity     ", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "unit", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "min", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "max", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "average", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "kera", None))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "1 dozen", None))
        self.treeWidget.topLevelItem(0).setText(2, _translate("MainWindow", "30", None))
        self.treeWidget.topLevelItem(0).setText(3, _translate("MainWindow", "35", None))
        self.treeWidget.topLevelItem(0).setText(4, _translate("MainWindow", "32", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "banana", None))
        self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow", "2 dozan", None))
        self.treeWidget.topLevelItem(1).setText(2, _translate("MainWindow", "55", None))
        self.treeWidget.topLevelItem(1).setText(3, _translate("MainWindow", "60", None))
        self.treeWidget.topLevelItem(1).setText(4, _translate("MainWindow", "58", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "edit", None))
        self.actionRefresh_data.setText(_translate("MainWindow", "refresh data", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))
        self.actionUsage.setText(_translate("MainWindow", "usage", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))
        self.actionWholsale_price.setText(_translate("MainWindow", "wholsale price", None))
        self.actionRetail_price.setText(_translate("MainWindow", "retail price", None))

import res



