__author__ = 'AKHIL'

import sys
from PyQt4.QtGui import *
import OpenOPC
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
import os
import Create_Group_UI
import connections
import sqlite3
opc = OpenOPC.client()

class Create_Group1(QtGui.QMainWindow, Create_Group_UI.Ui_MainWindow):
    global Tarray
    Tarray = []
    global connected_server
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.parent = parent;
        self.setupUi(self)
        self.setWindowTitle("OPC Client- Create Group")
        connected_server = connections.server()
        opc.connect(connected_server)
        self.comboData = ['None']
        self.comboBox.addItem(" select")
        self.treeWidget.setHeaderHidden(True)
        if connected_server == 'Matrikon.OPC.Simulation.1':
            comboData = opc.list('Simulation Items')
            for y in comboData:
                self.comboBox.addItem(y)
        else:
            comboData = opc.list()
            for y in comboData:
                self.comboBox.addItem(y)

        self.comboBox.activated[str].connect(self.onActivate)
        self.button_cancel.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.button_createGroup.clicked.connect(self.load_tree)
        self.button_searchTag.clicked.connect(self.search)
        self.button_deleteTag.clicked.connect(self.delete_Tag)
        self.connect(self.treeWidget, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem *,int)"), self.function)

    def search(self):
        input_tag = self.lineEdit_searchTag.text()
        tag_array = []
        if connected_server == 'Matrikon.OPC.Simulation.1':
            data = opc.list('Simulation Items')
            for y in data:
                data = str(y)
                search = 'Simulation Items.' + data
                data = opc.list(search)
                tag_array.append(data)
        else:
            data = opc.list()
            for y in data:
                data = str(y)
                data = opc.list(data)
                tag_array.append(data)
        if any(input_tag in sublist for sublist in tag_array):
            result = QMessageBox.question(self, 'Message', "The tag has been Found !! \n Do you want to insert it ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.Add_to_tree(input_tag)
            else:
                print "No"
        else:
            QMessageBox.about(self, "Sucess", "Enter a valid Tag")

    def load_tree(self):
        group = self.lineEdit_GroupName.text()
        rate = self.lineEdit_UpdateRate.text()
        group = str(group)
        if not group:
            QMessageBox.about(self, "Error", "Enter the Group name!!")
        else:
             if not rate:
                QMessageBox.about(self, "Error", " Update rate is 5 seconds!!")
                rate = "5"
             self.create_group(group, rate)

        return 0

    def create_group(self, group, rate):
            tags = str(Tarray)
            connected_server = connections.server()
            connected_server = str(connected_server)
            QMessageBox.about(self, "Sucess", "Group has been created ")
            connections.create_new(connected_server, group, tags, rate)
            del Tarray[:]
            self.parent.refresh();
            self.close()

    def onActivate(self, text):
        connected_server = connections.server()
        self.comboBox.clear()                                 # delete all items from comboBox
        self.comboData = [text]
        self.comboBox.addItems(self.comboData)
        self.treeWidget.setHeaderHidden(True)
        if connected_server == 'Matrikon.OPC.Simulation.1':
            comboData = opc.list('Simulation Items')
            for y in comboData:
                self.comboBox.addItem(y)
            self.comboBox.activated[str].connect(self.onActivate)
            self.treeWidget.clear()
            strt = "Simulation Items." + text
            tag = str(strt)
            list = opc.list(tag)
            item = QtGui.QTreeWidgetItem(["Tags"])
            for x in list:
               item2 = QtGui.QTreeWidgetItem(item, [x])
            self.treeWidget.addTopLevelItem(item)
        else:
            comboData = opc.list()
            for y in comboData:
                self.comboBox.addItem(y)
            self.comboBox.activated[str].connect(self.onActivate)
            self.treeWidget.clear()
            strt = text
            tag = str(strt)
            list = opc.list(tag)
            item = QtGui.QTreeWidgetItem(["Tags"])
            for x in list:
               item2 = QtGui.QTreeWidgetItem(item, [x])
            self.treeWidget.addTopLevelItem(item)

    def Add_to_tree(self, tag):
        list_item = self.listWidgetName.findItems(tag, QtCore.Qt.MatchExactly)
        if len(list_item) >= 1:
            QMessageBox.about(self, "Error", "Tag Already exist!!")
        else:
            self.listWidget.addItem(tag)
            Tarray.append(tag)

    def function(self, clicked, column):
        add = clicked.text(column)
        add = str(add)
        if add == "Tags":
            QMessageBox.about(self, "Error", "Select Tag !")
        else:
            list_item = self.listWidget.findItems(add, QtCore.Qt.MatchExactly)    # Check if any tag with same name exist
            if len(list_item) >= 1:
                QMessageBox.about(self, "Error", "Tag Already exist!!")
            else:
                self.listWidget.addItem(add)
                Tarray.append(add)

    def delete_Tag(self):
        item = self.listWidget.currentItem().text()
        if item in Tarray:
            Tarray.remove(item)
        listItems = self.listWidget.selectedItems()
        if not listItems:
            return 0
        for item in listItems:
            self.listWidget.takeItem(self.listWidget.row(item))
        self.listWidget.update()
def main():
    app = QtGui.QApplication(sys.argv)
    form = Create_Group1()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
