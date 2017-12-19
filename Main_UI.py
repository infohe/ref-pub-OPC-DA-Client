# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_homeF.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(847, 450)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("QMenuBar {\n"
"background-color: #eff1f4;\n"
"}\n"
"QTreeWidget{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"QTableWidget{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(9, 9, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.server_name = QtGui.QLabel(self.centralwidget)
        self.server_name.setGeometry(QtCore.QRect(95, 315, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.server_name.setFont(font)
        self.server_name.setObjectName(_fromUtf8("server_name"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 315, 49, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.button_dissconnect = QtGui.QPushButton(self.centralwidget)
        self.button_dissconnect.setGeometry(QtCore.QRect(10, 380, 87, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_dissconnect.setFont(font)
        self.button_dissconnect.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 8px;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 75px;\n"
"max-width: 75px;\n"
"min-height: 18px;\n"
"max-height: 18px;"))
        self.button_dissconnect.setObjectName(_fromUtf8("button_dissconnect"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(9, 30, 281, 281))
        self.treeWidget.setStyleSheet(_fromUtf8("QTreeView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"     border: 1px solid #d9d9d9;\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
"    border: 1px solid #bfcde4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    border: 1px solid #567dbc;\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(images/vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(images/branch-more.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(images/branch-end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image: url(images/branch-closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"        border-image: none;\n"
"        image: url(images/branch-open.png);\n"
"}\n"
""))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.server_groups = QtGui.QLabel(self.centralwidget)
        self.server_groups.setGeometry(QtCore.QRect(95, 357, 31, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        self.server_groups.setFont(font)
        self.server_groups.setObjectName(_fromUtf8("server_groups"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(9, 357, 48, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.server_status = QtGui.QLabel(self.centralwidget)
        self.server_status.setGeometry(QtCore.QRect(95, 336, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.server_status.setFont(font)
        self.server_status.setObjectName(_fromUtf8("server_status"))
        self.button_deletegroup = QtGui.QPushButton(self.centralwidget)
        self.button_deletegroup.setGeometry(QtCore.QRect(100, 380, 87, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_deletegroup.setFont(font)
        self.button_deletegroup.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 8px;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 75px;\n"
"max-width: 75px;\n"
"min-height: 18px;\n"
"max-height: 18px;"))
        self.button_deletegroup.setObjectName(_fromUtf8("button_deletegroup"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(9, 336, 49, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(300, 30, 541, 341))
        self.tableWidget.setStyleSheet(_fromUtf8(" selection-background-color: (x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #ffd592, stop: 1 white);"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.button_deleteTag = QtGui.QPushButton(self.centralwidget)
        self.button_deleteTag.setGeometry(QtCore.QRect(730, 380, 112, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_deleteTag.setFont(font)
        self.button_deleteTag.setStyleSheet(_fromUtf8("\n"
"border: 2px solid gray;\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 8px;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 100px;\n"
"max-width: 100px;\n"
"min-height: 18px;\n"
"max-height: 18px;\n"
""))
        self.button_deleteTag.setObjectName(_fromUtf8("button_deleteTag"))
        self.button_editgroup = QtGui.QPushButton(self.centralwidget)
        self.button_editgroup.setGeometry(QtCore.QRect(190, 380, 87, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_editgroup.setFont(font)
        self.button_editgroup.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 8px;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 75px;\n"
"max-width: 75px;\n"
"min-height: 18px;\n"
"max-height: 18px;"))
        self.button_editgroup.setObjectName(_fromUtf8("button_editgroup"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout_2 = QtGui.QAction(MainWindow)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.menuFIle.addAction(self.actionAbout_2)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "Browse", None))
        self.server_name.setText(_translate("MainWindow", "None", None))
        self.label.setText(_translate("MainWindow", "Server   ::", None))
        self.button_dissconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.server_groups.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "Groups ::", None))
        self.server_status.setText(_translate("MainWindow", "offline", None))
        self.button_deletegroup.setText(_translate("MainWindow", "Delete Group", None))
        self.label_2.setText(_translate("MainWindow", "Status   ::", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Error", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quality", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TimeStamp", None))
        self.button_deleteTag.setText(_translate("MainWindow", "Delete Tag", None))
        self.button_editgroup.setText(_translate("MainWindow", "Add /Edit Group", None))
        self.menuFIle.setTitle(_translate("MainWindow", "File", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout_2.setText(_translate("MainWindow", "About", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

