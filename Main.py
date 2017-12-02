__author__ = 'AKHIL'

from PyQt4 import QtGui
import sys
from PyQt4.QtGui import *
import OpenOPC
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
import os
import connections
import Main_UI
from Create_Group import Create_Group1
import sqlite3
import re
import time

opc = OpenOPC.client()

class About_window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(About_window, self).__init__(parent)
        self.setWindowTitle("OPC Client-About")
        self.setGeometry(500,200,600,500)
        self.label = QtGui.QLabel(self)
        label_font = QtGui.QFont("Times", 13, QtGui.QFont.StyleNormal)
        self.label.setFont(label_font)
        self.label.move(10,30)
        self.label.setText("About ")

        self.label3 = QtGui.QLabel(self)
        self.label4 = QtGui.QLabel(self)
        self.label5 = QtGui.QLabel(self)
        label3_font = QtGui.QFont("Times", 10, QtGui.QFont.StyleItalic)
        self.label3.setFont(label3_font)
        self.label4.setFont(label3_font)
        self.label5.setFont(label3_font)
        self.label3.setText("      This is a is a free OPC Client Test Utility, which is pressed with usefulness for testing and investigating ")
        self.label4.setText("OPC servers and OPC associations. This is built with instinctive UI and easy work process.")
        self.label5.setText("There might be some bugs or errors , please inform us for improving the Client application.")
        self.label3.move(10,55)
        self.label4.move(10,71)
        self.label5.move(10,90)
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap("images\pic.png"))
        pic.move(75,400)
        pic.show()
        self.label2 = QtGui.QLabel(self)
        self.label2.setText('<a href="https://automationforum.in/">Visit Us/</a>')
        self.label2.move(255,385)
        self.label2.setOpenExternalLinks(True)
        self.label2.show()


class MainWindow(QtGui.QMainWindow, Main_UI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("OPC Client")
        self.treeWidget.setHeaderHidden(True)
        self.pushButton.clicked.connect(self.refresh)
        global connected_server
        connected_server = ""
        global group , tags ,TableTags
        TableTags = []
        group= []
        tags = []
        global item , item1 , item2, item5
        item = QtGui.QTableWidgetItem()
        item1 = QtGui.QTableWidgetItem()
        item5 = QtGui.QTableWidgetItem()
        item2 =QtGui.QTableWidgetItem()

        server= opc.servers()
        item = QtGui.QTreeWidgetItem(["Servers"])
        if not item:
            try:
                self.throws()
                return 0
            finally:
                print "Error"
        else:
            for x in server:
                item1 = QtGui.QTreeWidgetItem(item,[x])
            self.treeWidget.addTopLevelItem(item)

        #Button events and Menu events
        self.connect(self.treeWidget,QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem *,int)"),self.function)
        self.pushButton_2.clicked.connect(self.delete_group)
        self.pushButton_3.clicked.connect(self.disconnect)
        self.pushButton_4.clicked.connect(self.delete_tag)
        self.actionAbout_2.triggered.connect(self.about)
        self.actionExit_2.triggered.connect(self.exit)

    def throws(self):
        QMessageBox.about(self, "Error", "No OPC Server Found In this system !! Closing")
        time.sleep(10)
        self.close()

    def exit(self):
        opc.remove(opc.groups())
        opc.close()
        del TableTags[:]
        del group[:]
        del tags[:]
        del TableTags[:]
        connections.disconnect()
        self.close()

    def about(self):
        self.dialogTextBrowser = About_window(self)
        self.dialogTextBrowser.exec_()

    def disconnect(self):
        opc.remove(opc.groups())
        opc.close()
        del group[:]
        del tags[:]
        del TableTags[:]
        self.treeWidget.clear()
        self.label_3.setText("None")
        self.label_4.setText("Offline")
        self.label_.setText("0")
        #opc.close()

    def delete_group(self):
        clicked = self.treeWidget.currentItem()
        column = self.treeWidget.currentColumn()
        if clicked== None :
            QMessageBox.about(self, "Error", "Select a Group !!")
        else:
            item = clicked.text(column)
            if item in group:
                result = QMessageBox.question(self, 'Message', "Do you want to delete the group?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    item =str(item)
                    connected_server = connections.server()
                    connections.delete_G(connected_server,item)
                    root = self.treeWidget.invisibleRootItem()
                    for item in self.treeWidget.selectedItems():
                        (item.parent() or root).removeChild(item)
                    indx = 0
                    if item in group:
                        indx = group.index(item)
                        group.remove(item)
                    connected_server = connections.server()
                    data = connections.read_from_db(connected_server)              #Read groups and tags from DB
                    del group[:]
                    for x in data:
                        group.append(x[0])
                    self.label_7.setText(str(len(group)))                           #update group number
                    QMessageBox.question(self, 'Message', "Deleting the Tag from Table?")
                    for x in tags[indx]:
                        if x in TableTags:                                           #delete tag from table when group is deleted
                            indx_table = TableTags.index(x)
                            del TableTags[indx_table]
                            self.tableWidget.removeRow(indx_table)
                    del tags[indx]                                                  #delete the tags of the group from array

                else:
                    QMessageBox.about(self, "Error", "Select a Group !!")
            else:
                    QMessageBox.about(self, "Error", "Select a Group !!")

    def delete_tag(self):
        selected_row= self.tableWidget.currentRow()
        if selected_row >=0:
            del TableTags[selected_row]
            self.tableWidget.removeRow(selected_row)
        else:
            QMessageBox.about(self, "Error", "Select a Tag in table !!")

    def function(self, clicked, column):
        selected_text = clicked.text(column)
        index = self.treeWidget.currentIndex()
        row = index.row()
        indexes = self.treeWidget.selectedIndexes()
        server= opc.servers()
        if selected_text in server:
            connected_server = selected_text
            self.insert_into_tree(selected_text,row)
        if selected_text == "Add New Group":
            self._new_window = Create_Group1()                                        # Calling the other module (Create Group)
            self._new_window.show()
        if selected_text in group:
            print "Group"
        if any(selected_text in sublist for sublist in tags):
            tag = str(selected_text)
            TableTags.append(tag)
            QtCore.QTimer.singleShot(10000, lambda: self.insert_into_table())
        return 0

    def insert_into_tree(self,selected_text,row):
        del group[:]
        del tags[:]
        connections.serve = selected_text                                            # Saving the Current servername
        self.treeWidget.clear()
        server= opc.servers()
        item = QtGui.QTreeWidgetItem(["Servers"])
        self.treeWidget.addTopLevelItem(item)
        for x in server:
           item1 = QtGui.QTreeWidgetItem(item,[x])
           if x == selected_text:
                self.label_3.setText(selected_text)
                self.label_4.setText("Online")
                item5 = QtGui.QTreeWidgetItem(item1,["Add New Group"])
                self.treeWidget.insertTopLevelItem(row,item1)
                opc.connect(selected_text)
                connections.connect()
                connected_server = connections.server()
                data = connections.read_from_db(connected_server)                   #Passing server name to conn DB
                y = 0
                for x in data:
                    group.append(x[0])
                    temp1 = str(x[1])
                    temp2 = x[1]
                    temp2 = str(temp2)
                    temp2= temp2.replace("'","")
                    temp2= temp2.replace("[","")
                    temp2= temp2.replace("]","")
                    temp2 =''.join(temp2)
                    temp1= re.split("; |, |' ",temp2)
                    tags.append(temp1)
                i=0
                for x in group:
                    item2 = QtGui.QTreeWidgetItem(item1,[x])
                    tags_list = tags[i]
                    for x in tags_list:
                        item3 = QtGui.QTreeWidgetItem(item2,[x])
                    i = i + 1
                self.label_7.setText(str(len(group)))
        self.treeWidget.expandToDepth(row)
        return 0

    def insert_into_table(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        for tag in TableTags:
            tag =str(tag)
            value = opc.read(tag)
            if len(value)== 3:
                rowcount = self.tableWidget.rowCount()
                rcount = rowcount+1
                x = str(rcount)
                self.tableWidget.setRowCount(rcount)
                self.tableWidget.setItem(rcount-1,0, QTableWidgetItem(tag))
                self.tableWidget.setItem(rcount-1,1, QTableWidgetItem(str(value[0])))
                self.tableWidget.setItem(rcount-1,2, QTableWidgetItem("None"))
                self.tableWidget.setItem(rcount-1,3, QTableWidgetItem(str(value[1])))
                self.tableWidget.setItem(rcount-1,4, QTableWidgetItem(str(value[2])))
                rowcount=0
            if len(value)== 4:
                rowcount = self.tableWidget.rowCount()
                rcount = rowcount+1
                x = str(rcount)
                self.tableWidget.setRowCount(rcount)
                self.tableWidget.setItem(rcount-1,0, QTableWidgetItem(tag))
                self.tableWidget.setItem(rcount-1,1, QTableWidgetItem(str(value[0])))
                self.tableWidget.setItem(rcount-1,2, QTableWidgetItem(str(value[1])))
                self.tableWidget.setItem(rcount-1,3, QTableWidgetItem(str(value[2])))
                self.tableWidget.setItem(rcount-1,4, QTableWidgetItem(str(value[3])))
                self.label.setText(value)
                rowcount=0
        QtCore.QTimer.singleShot(10000, lambda: self.insert_into_table())

    def refresh(self):
        del group[:]
        del tags[:]
        self.treeWidget.clear()
        serv = connections.serve
        server= opc.servers()
        item = QtGui.QTreeWidgetItem(["Servers"])
        self.treeWidget.addTopLevelItem(item)
        for x in server:
           item1 = QtGui.QTreeWidgetItem(item,[x])
           if x == serv:
                row = server.index(serv)
                self.label_3.setText(serv)
                self.label_4.setText("Online")
                item5 = QtGui.QTreeWidgetItem(item1,["Add New Group"])
                self.treeWidget.insertTopLevelItem(row,item1)
                opc.connect(serv)
                connections.connect()
                connected_server = connections.server()
                data = connections.read_from_db(connected_server)
                y = 0
                for x in data:
                    group.append(x[0])
                    temp = str(x[1])
                    temp3 = x[1]
                    temp3 = str(temp3)
                    temp3= temp3.replace("'","")
                    temp3= temp3.replace("[","")
                    temp3= temp3.replace("]","")
                    temp3 =''.join(temp3)
                    temp= re.split("; |, |' ",temp3)
                    tags.append(temp)
                i=0
                for x in group:
                    item2 = QtGui.QTreeWidgetItem(item1,[x])
                    list = tags[i]
                    for x in list:
                        item3 = QtGui.QTreeWidgetItem(item2,[x])
                    i=i+1
                self.label_7.setText(str(len(group)))
        self.treeWidget.expandToDepth(row)

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
