# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_group.ui'
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
        MainWindow.resize(731, 525)
        MainWindow.setStyleSheet(_fromUtf8("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid darkgray;\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 80px;\n"
"max-width: 80px;\n"
"min-height: 18px;\n"
"max-height: 18px;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 331, 441))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.treeWidget = QtGui.QTreeWidget(self.groupBox)
        self.treeWidget.setGeometry(QtCore.QRect(30, 130, 281, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 90, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.button_searchTag = QtGui.QPushButton(self.groupBox)
        self.button_searchTag.setGeometry(QtCore.QRect(220, 30, 92, 26))
        self.button_searchTag.setObjectName(_fromUtf8("button_searchTag"))
        self.lineEdit_searchTag = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_searchTag.setGeometry(QtCore.QRect(30, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.lineEdit_searchTag.setFont(font)
        self.lineEdit_searchTag.setObjectName(_fromUtf8("lineEdit_searchTag"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 10, 371, 431))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 171, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_GroupName = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_GroupName.setGeometry(QtCore.QRect(140, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.lineEdit_GroupName.setFont(font)
        self.lineEdit_GroupName.setObjectName(_fromUtf8("lineEdit_GroupName"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_UpdateRate = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_UpdateRate.setGeometry(QtCore.QRect(140, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.lineEdit_UpdateRate.setFont(font)
        self.lineEdit_UpdateRate.setObjectName(_fromUtf8("lineEdit_UpdateRate"))
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 130, 321, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(110, 110, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.button_deleteTag = QtGui.QPushButton(self.groupBox_2)
        self.button_deleteTag.setGeometry(QtCore.QRect(230, 400, 92, 26))
        self.button_deleteTag.setObjectName(_fromUtf8("button_deleteTag"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(330, 30, 32, 33))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-image: url(refresh.png) 3 10 3 10;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 20px;\n"
"max-width: 20px;\n"
"min-height: 25px;\n"
"max-height: 25px;\n"
"}"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.button_cancel = QtGui.QPushButton(self.centralwidget)
        self.button_cancel.setGeometry(QtCore.QRect(580, 450, 92, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_cancel.setFont(font)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.button_createGroup = QtGui.QPushButton(self.centralwidget)
        self.button_createGroup.setGeometry(QtCore.QRect(480, 450, 92, 26))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.button_createGroup.setFont(font)
        self.button_createGroup.setObjectName(_fromUtf8("button_createGroup"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Tags", None))
        self.label_2.setText(_translate("MainWindow", "Select the tags", None))
        self.button_searchTag.setText(_translate("MainWindow", "Search", None))
        self.label_4.setText(_translate("MainWindow", "Search Tags", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Group Details", None))
        self.label.setText(_translate("MainWindow", "Group Name", None))
        self.label_3.setText(_translate("MainWindow", "Update Time (in sec)", None))
        self.label_5.setText(_translate("MainWindow", "Tags in the group", None))
        self.button_deleteTag.setText(_translate("MainWindow", "Delete Tag", None))
        self.button_cancel.setText(_translate("MainWindow", "Cancel", None))
        self.button_createGroup.setText(_translate("MainWindow", "Add / Edit Group", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

