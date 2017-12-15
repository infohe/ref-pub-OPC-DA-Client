__author__ = 'AKHIL'

import sys
import re
import sqlite3
global serve
serve = ''
global selected_group
selected_group = ''
conn = sqlite3.connect('opc_client.db')
c = conn.cursor()
def group():
    return selected_group
def server():
    return serve
def connect():
    c.execute("CREATE TABLE IF NOT EXISTS table1(server TEXT, groupn TEXT, tags BLOB, update1 INT)")
    conn.commit()
def create_new(serve, group, tags, upda):
    group = str(group)
    tags = str(tags)
    ser = str(serve)
    upda = int(upda)
    c.execute("INSERT INTO table1 (server, groupn, tags, update1) VALUES (?, ?, ?, ?)", (ser, group, tags, upda))
    conn.commit()

def delete_G(servern, group):
    serv = str(servern)
    group = str(group)
    conn.execute("DELETE FROM table1 where server = ? AND groupn = ?;", (serv , group))
    conn.commit()

def read_from_db(serv):
    serv = str(serv)
    c.execute("SELECT groupn, tags, update1 FROM table1 where server = ?", (serv,))
    data = c.fetchall()
    return data

def edit_group(current_server, new_tags, group_name, upda):
    group_name = str(group_name)
    new_tags=str(new_tags)
    current_server= str(current_server)
    upda = int(upda)
    c.execute("UPDATE table1 SET tags = ?, update1 = ? WHERE groupn = ? AND server = ?", [new_tags, upda, group_name, current_server,])
    conn.commit()

def delete_tag(current_server,new_tags,group_name):
    group_name = str(group_name)
    new_tags=str(new_tags)
    current_server= str(current_server)
    c.execute("UPDATE table1 SET tags = ? WHERE groupn = ? AND server = ?", [new_tags, group_name,current_server,])
    conn.commit()

def disconnect():
    c.close()
    conn.close()

