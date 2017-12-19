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
import sqlite3
from Edit_Group import Edit_Group1
import re
import time
opc = OpenOPC.client()
class About_window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(About_window, self).__init__(parent)
        self.setWindowTitle("OPC Client-About")
        self.setGeometry(500, 200, 600, 500)
        self.heading = QtGui.QLabel(self)
        label_font = QtGui.QFont("Times", 13, QtGui.QFont.StyleNormal)
        self.heading.setFont(label_font)
        self.heading.move(10, 30)
        self.heading.setText("About ")

        self.line1 = QtGui.QLabel(self)
        self.line2 = QtGui.QLabel(self)
        self.line3 = QtGui.QLabel(self)
        line_font = QtGui.QFont("Times", 10, QtGui.QFont.StyleItalic)
        self.line1.setFont(line_font)
        self.line2.setFont(line_font)
        self.line3.setFont(line_font)
        self.line1.setText("      This is a is a free OPC Client Test Utility, which is pressed with usefulness for testing and investigating ")
        self.line2.setText("OPC servers and OPC associations. This is built with instinctive UI and easy work process.")
        self.line3.setText("There might be some bugs or errors , please inform us for improving the Client application.")
        self.line1.move(10, 55)
        self.line2.move(10, 71)
        self.line3.move(10, 90)
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap("images\pic.png"))
        pic.move(75, 400)
        pic.show()
        self.line_link = QtGui.QLabel(self)
        self.line_link.setText('<a href="https://automationforum.in/">Visit Us/</a>')
        self.line_link.move(255, 385)
        self.line_link.setOpenExternalLinks(True)
        self.line_link.show()

class MainWindow(QtGui.QMainWindow, Main_UI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("OPC Test Client")
        self.treeWidget.setHeaderHidden(True)
        global connected_server, group_index
        connected_server = ""
        group_index = ""
        global group, tags, TableTags, update_rate
        TableTags = []
        group = []
        tags = []
        update_rate = []
        global item, item1, item2, item5
        item = QtGui.QTableWidgetItem()
        item1 = QtGui.QTableWidgetItem()
        item5 = QtGui.QTableWidgetItem()
        item2 = QtGui.QTableWidgetItem()

        header = self.tableWidget.horizontalHeader()
        for i in range(5):
            header.setResizeMode(i, QtGui.QHeaderView.Stretch)
        server = opc.servers()
        item = QtGui.QTreeWidgetItem(["Servers"])
        if not item:
            try:
                self.throws()
                return 0
            finally:
                print "Error"
        else:
            for x in server:
                item1 = QtGui.QTreeWidgetItem(item, [x])
            self.treeWidget.addTopLevelItem(item)

#Button events and Menu events
        self.connect(self.treeWidget, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem *,int)"), self.check_condition)
        self.connect(self.treeWidget, QtCore.SIGNAL("itemClicked(QTreeWidgetItem *,int)"), self.condition_tag)
        self.button_deletegroup.clicked.connect(self.delete_group)
        self.button_dissconnect.clicked.connect(self.disconnect)
        self.button_deleteTag.clicked.connect(self.delete_tag)
        self.button_editgroup.clicked.connect(self.edit_group)
        self.actionAbout_2.triggered.connect(self.about)
        self.actionExit_2.triggered.connect(self.exit)

    def edit_group(self):
        server = connections.server()
        if not server:
            QMessageBox.information(None, 'Error', ' Connect to Server First.', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self._new_window1 = Edit_Group1(self)                                     # Calling the other module (Edit Group)
            self._new_window1.show()

    def throws(self):
        QMessageBox.information(None, 'Error', ' No OPC Server Found In this system !! Closing.', QMessageBox.Ok, QMessageBox.Ok)
        time.sleep(10)
        self.close()

    def exit(self):
        opc.remove(opc.groups())
        opc.close()
        del TableTags[:]
        del group[:]
        del tags[:]
        del update_rate[:]
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
        del update_rate[:]
        self.treeWidget.clear()
        self.server_name.setText("None")
        self.server_status.setText("Offline")
        self.label_.setText("0")
        #opc.close()

    def delete_group(self):
        clicked = self.treeWidget.currentItem()
        column = self.treeWidget.currentColumn()
        if clicked == None:
            QMessageBox.information(None, 'Error', ' Select a Group !!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            item = clicked.text(column)
            if item in group:
                result = QMessageBox.question(self, 'Message', "Do you want to delete the group?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    item = str(item)
                    opc.remove(item)
                    connected_server = connections.server()
                    connections.delete_G(connected_server, item)
                    root = self.treeWidget.invisibleRootItem()
                    for item in self.treeWidget.selectedItems():
                        (item.parent() or root).removeChild(item)
                    indx = 0
                    if item in group:
                        indx = group.index(item)
                        group.remove(item)
                    connected_server = connections.server()
                    data = connections.read_from_db(connected_server)                 #Read groups and tags from DB
                    del group[:]
                    for x in data:
                        group.append(x[0])
                    self.server_groups.setText(str(len(group)))                      #update group number

                    QMessageBox.question(self, 'Message', "Deleting the Tag from Table?")
                    for x in tags[indx]:
                        if x in TableTags:                                           #delete tag from table when group is deleted
                            indx_table = TableTags.index(x)
                            del TableTags[indx_table]
                            self.tableWidget.removeRow(indx_table)
                    del tags[indx]                                                  #delete the tags of the group from array

                else:
                    QMessageBox.information(None, 'Error', ' Select a Group !!', QMessageBox.Ok, QMessageBox.Ok)
            else:
                    QMessageBox.information(None, 'Error', ' Select a Group !!', QMessageBox.Ok, QMessageBox.Ok)

    def delete_tag(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            temp = connections.group()                              #index of the group which tag is
            cell = self.tableWidget.item(selected_row, 0).text()     #tag name from table
            indx = tags[temp].index(cell)                           #index of tag in group[num]
            current_server = connections.server()
            group_name = group[temp]
            new_tags = tags[temp]
            QMessageBox.question(None, 'Message', ' Remove the tag? !!', QMessageBox.Ok, QMessageBox.Ok)
            self.tableWidget.removeRow(selected_row)
            del new_tags[indx]
            connections.delete_tag(current_server,new_tags,group_name)
            del TableTags[selected_row]
            opc.remove(group_name)
            tags_ = tags[temp]
            g_name = group_name
            u_rate = update_rate[temp]
            opc.read(tags_, group=g_name, update=u_rate)
            self.refresh()

        else:
            QMessageBox.about(None, 'Error', ' Select a Tag in table !! !!', QMessageBox.Ok, QMessageBox.Ok)

    def condition_tag(self, clicked, column):
        selected_text = clicked.text(column)
        index = self.treeWidget.currentIndex()
        if selected_text in group:
            del TableTags[:]
            group_index = group.index(selected_text)
            connections.selected_group = group_index                                            # Saving the Current group
            for tag in tags[group_index]:
                TableTags.append(tag)
            self.tableWidget.setRowCount(len(TableTags))
            self.tableWidget.setColumnCount(5)
            QtCore.QTimer.singleShot(2000, lambda: self.insert_into_table())
        return 0

    def check_condition(self, clicked, column):
        selected_text = clicked.text(column)
        index = self.treeWidget.currentIndex()
        row = index.row()
        server = opc.servers()
        if selected_text in server:
            self.insert_into_tree(selected_text, row)
        if selected_text == "Add New Group":
            self._new_window = Edit_Group1(self)                                     # Calling the other module (Create Group)
            self._new_window.show()
        return 0
        if any(selected_text in sublist for sublist in tags):
            print "tag"

    def insert_into_tree(self, selected_text, row):
        del group[:]
        del tags[:]
        del update_rate[:]
        connections.serve = selected_text                                            # Saving the Current server name
        self.treeWidget.clear()
        self.create_tree(selected_text, row)
        return 0

    def create_tree(self, selected_text, row):
        server = opc.servers()
        item = QtGui.QTreeWidgetItem(["Servers"])
        self.treeWidget.addTopLevelItem(item)
        for x in server:
           item1 = QtGui.QTreeWidgetItem(item, [x])
           if x == selected_text:
                self.server_name.setText(selected_text)
                self.server_status.setText("Online")
                item5 = QtGui.QTreeWidgetItem(item1, ["Add New Group"])
                self.treeWidget.insertTopLevelItem(row, item1)
                opc.connect(selected_text)
                connections.connect()
                connected_server = connections.server()
                data = connections.read_from_db(connected_server)                   #Passing server name to conn DB
                for con1 in data:
                    update_rate.append(con1[2])
                    group.append(con1[0])
                    temp1 = str(con1[1])
                    temp2 = con1[1]
                    temp2 = str(temp2)
                    temp2 = temp2.replace("'", "")
                    temp2 = temp2.replace("[", "")
                    temp2 = temp2.replace("]", "")
                    temp2 = ''.join(temp2)
                    temp1 = re.split("; |, |' ", temp2)
                    tags.append(temp1)
                i = 0
                for con2 in group:
                    item2 = QtGui.QTreeWidgetItem(item1, [con2])
                    tags_list = tags[i]
                    tags_ = tags[i]
                    g_name = group[i]
                    u_rate = update_rate[i]
                    opc.read(tags_, group=g_name, update=u_rate)
                    for con3 in tags_list:
                        item3 = QtGui.QTreeWidgetItem(item2, [con3])
                    i += 1
                self.server_groups.setText(str(len(group)))
        self.treeWidget.expandToDepth(row)

    def insert_into_table(self):
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        group_ind = connections.group()
        group_name = group[group_ind]
        data = opc.read(group = group_name)
        for value in data:
            print value
            index_table = TableTags.index(value[0])
            rcount = index_table
            self.tableWidget.setItem(rcount, 0, QTableWidgetItem(value[0]))
            self.tableWidget.setItem(rcount, 1, QTableWidgetItem(str(value[1])))
            if len(value) == 4:
                self.tableWidget.setItem(rcount, 2, QTableWidgetItem("None"))
                self.tableWidget.setItem(rcount, 3, QTableWidgetItem(str(value[2])))
                self.tableWidget.setItem(rcount, 4, QTableWidgetItem(str(value[3])))
            if len(value) == 5:
                self.tableWidget.setItem(rcount, 2, QTableWidgetItem(str(value[2])))
                self.tableWidget.setItem(rcount, 3, QTableWidgetItem(str(value[3])))
                self.tableWidget.setItem(rcount, 4, QTableWidgetItem(str(value[4])))
        QtCore.QTimer.singleShot(5000, lambda: self.insert_into_table())

    def refresh(self):
        del group[:]
        del tags[:]
        del update_rate[:]
        opc.remove(opc.groups())

        self.treeWidget.clear()
        serv = connections.serve
        server = opc.servers()
        row = server.index(serv)
        self.create_tree(serv, row)


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    app.setWindowIcon(QtGui.QIcon('images/icon.jpg'))
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()