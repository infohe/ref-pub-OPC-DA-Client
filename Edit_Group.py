__author__ = 'AKHIL'
import numpy as np
import sys
from PyQt4.QtGui import *
import OpenOPC
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel
from PyQt4.QtCore import pyqtSlot
import os
import re
import edit_create_groupUI
import connections
import sqlite3
opc = OpenOPC.client()


class Edit_Group1(QtGui.QMainWindow, edit_create_groupUI.Ui_MainWindow):
    global Tarray, Main_Tags, Sub_Tags, tag_list, group_list, update_rate, Tags_db
    Main_Tags = []
    Sub_Tags = []
    Tarray = []
    group_list = []
    tag_list = []
    update_rate = []
    Tags_db = []
    global connected_server
    connected_server = ''

    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.parent = parent;
        self.setupUi(self)
        self.setWindowTitle("OPC Test Client- Create Group")
        connected_server = connections.server()
        opc.connect(connected_server)
        self.comboData = ['None']
        self.comboBox.addItem(" Select")
        self.treeWidget.setHeaderHidden(True)
        self.comboBox_2.comboData = ("--- Select a Group ---")
        self.comboBox_2.addItem("--- Select a Group ---")
        s_ind = 0
        tag_list = opc.list('*', recursive=True)
        for x in tag_list:
            str_list = x.split('.')
            tag = str_list[0]
            if tag not in Main_Tags:
                ind = tag_list. index(x)
                array = tag_list[s_ind:ind]
                if not array:
                    print "do nothing"
                else:
                    Sub_Tags.append([array])
                Main_Tags.append(tag)
                s_ind = ind
        for y in Main_Tags:
            self.comboBox.addItem(y)

        connected_server = connections.server()
        data = connections.read_from_db(connected_server)                   #Passing server name to conn DB
        for con1 in data:
            update_rate.append(con1[2])
            self.comboBox_2.addItem(con1[0])
            group_list.append(con1[0])
            temp2 = con1[1]
            temp2 = str(temp2)
            temp2 = temp2.replace("'", "")
            temp2 = temp2.replace("[", "")
            temp2 = temp2.replace("]", "")
            temp2 = ''.join(temp2)
            temp1 = re.split("; |, |' ", temp2)
            Tags_db.append(temp1)

        edit = self.lineEdit_searchTag
        completer = QCompleter()
        edit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.get_data(model, tag_list)

        line_g = self.lineEdit_GroupName
        regex = QtCore.QRegExp("[a-z-A-Z-0-9-@-#-$_]+")
        validator = QtGui.QRegExpValidator(regex)
        line_g.setValidator(validator)

        line_update = self.lineEdit_UpdateRate
        regex2 = QtCore.QRegExp("[0-9]+")
        validator2 = QtGui.QRegExpValidator(regex2)
        line_update.setValidator(validator2)

        self.comboBox.activated[str].connect(self.onActivate)
        self.comboBox_2.activated[str].connect(self.load_data)
        self.button_cancel.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.button_createGroup.clicked.connect(self.load_tree)
        self.button_searchTag.clicked.connect(self.search)
        self.button_deleteTag.clicked.connect(self.delete_Tag)
        self.pushButton.clicked.connect(self.refresh_screen)
        self.connect(self.treeWidget, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem *,int)"), self.check_condition)

    def refresh_screen(self):
        self.comboBox.comboData = ("--= Select a Group ---")
        self.lineEdit_UpdateRate.clear()
        self.lineEdit_GroupName.clear()
        self.lineEdit_GroupName.setReadOnly(False)
        self.listWidget.clear()

    def load_data(self, text):
        if text == "--- Select a Group ---":
            self.refresh_screen()
        else:
            self.listWidget.clear()
            del Tarray[:]
            indx = group_list.index(text)
            self.lineEdit_GroupName.setReadOnly(True)
            self.lineEdit_GroupName.setText(group_list[indx])
            self.lineEdit_UpdateRate.setText(str(update_rate[indx]))
            for item in Tags_db[indx]:
                self.listWidget.addItem(item)
                Tarray.append(item)

    def get_data(self, model, tag_list):
        model.setStringList(tag_list)

    def search(self, tag_list):
        input_tag = self.lineEdit_searchTag.text()
        check_list = opc.list('*', recursive=True)
        if input_tag in check_list:
            result = QMessageBox.question(None, 'Message', "The tag has been Found !! \n Do you want to insert it ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.Add_to_tree(str(input_tag))
        else:
            QMessageBox.Warning(None, 'Error', ' Enter a valid Tag!!', QMessageBox.Ok, QMessageBox.Ok)

    def load_tree(self):
        group = self.lineEdit_GroupName.text()
        rate = self.lineEdit_UpdateRate.text()
        group = str(group)
        if not group or not Tarray:
            QMessageBox.Warning(None, 'Error', ' Check the Group name / Tags !!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            if group not in group_list:
                if not rate:
                    QMessageBox.information(None, 'Message', ' Update rate is seconds !!', QMessageBox.Ok, QMessageBox.Ok)
                    rate = "5"
                    self.create_group(group, rate)
                else:
                    try:
                        val = int(rate)
                        if type(val) == int:
                            self.create_group(group, rate)
                    except ValueError:
                        QMessageBox.Warning(None, 'Error', ' Enter the a Integer for Update Rate!!', QMessageBox.Ok, QMessageBox.Ok)

            else:
                result = QMessageBox.question(None, 'Message', "The group Name Exist!! \n Do you want to change it ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if result == QMessageBox.Yes:
                    if not rate:
                        QMessageBox.information(None, 'Message', ' Update rate is seconds !!', QMessageBox.Ok, QMessageBox.Ok)
                        rate = "5"
                        connected_server = connections.server()
                        group = str(group)
                        connections.edit_group(connected_server, Tarray, group, rate)
                        del Tarray[:]
                        self.parent.refresh();
                        self.close()
                    else:
                        try:
                            val = int(rate)
                            if type(val) == int:
                                connected_server = connections.server()
                                group = str(group)
                                connections.edit_group(connected_server, Tarray, group, rate)
                                del Tarray[:]
                                self.parent.refresh();
                                self.close()
                        except ValueError:
                            QMessageBox.Warning(None, 'Error', ' Enter the a Integer for Update Rate !!', QMessageBox.Ok, QMessageBox.Ok)
        return 0

    def create_group(self, group, rate):
            tags = str(Tarray)
            connected_server = connections.server()
            connected_server = str(connected_server)
            QMessageBox.about(None, "Success", "Group has been created ")
            connections.create_new(connected_server, group, tags, rate)
            del Tarray[:]
            self.parent.refresh();
            self.close()

    def onActivate(self, text):
        self.comboBox.clear()                                 # delete all items from comboBox
        self.comboData = [text]
        self.comboBox.addItems(self.comboData)
        self.treeWidget.setHeaderHidden(True)

        for y in Main_Tags:
            self.comboBox.addItem(y)
        self.comboBox.activated[str].connect(self.onActivate)
        self.treeWidget.clear()
        indx = Main_Tags.index(text)
        item = QtGui.QTreeWidgetItem(["Tags"])
        list = Sub_Tags[indx]
        temp = np.array(list)
        list = temp.ravel()
        for x in list:
            item2 = QtGui.QTreeWidgetItem(item, [x])
        self.treeWidget.addTopLevelItem(item)

    def Add_to_tree(self, tag):
        list_item = self.listWidget.findItems(tag, QtCore.Qt.MatchExactly)
        if len(list_item) >= 1:
            QMessageBox.about(None, "Error", "Tag Already exist!!")
        else:
            self.listWidget.addItem(tag)
            Tarray.append(tag)

    def check_condition(self, clicked, column):
        add = clicked.text(column)
        add = str(add)
        if add == "Tags":
            QMessageBox.about(None, "Error", "Select Tag !")
        else:
            list_item = self.listWidget.findItems(add, QtCore.Qt.MatchExactly)    # Check if any tag with same name exist
            if len(list_item) >= 1:
                QMessageBox.about(None, "Error", "Tag Already exist!!")
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
    form = Edit_Group1()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
