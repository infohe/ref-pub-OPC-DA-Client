__author__ = 'AKHIL'

import sys
import re
import sqlite3
global serve
serve =''
conn = sqlite3.connect('opc_client.db')
c = conn.cursor()

def server():
    return serve

def connect():
    c.execute("CREATE TABLE IF NOT EXISTS table1(server TEXT, groupn TEXT, tags BLOB, update1 INT)")
    conn.commit()

def create_new(serve,group,tags,upda):
    group = str(group)
    tags = str(tags)
    ser = str(serve)
    upda = int(upda)
    c.execute("INSERT INTO table1 (server, groupn, tags, update1) VALUES (?, ?, ?, ?)",(ser , group , tags , upda))
    conn.commit()

def delete_G(servern,group):
    serv = str(servern)
    group = str(group)
    conn.execute("DELETE FROM table1 where server = ? AND groupn = ?;",(serv , group))
    conn.commit()
    print "deleted"

def read_from_db(serv):
    serv = str(serv)
    c.execute("SELECT groupn, tags, update1 FROM table1 where server = ?",(serv,))
    data = c.fetchall()
    return data

def disconnect():
    c.close()
    conn.close()