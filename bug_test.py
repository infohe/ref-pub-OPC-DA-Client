import numpy as np
def check(parent, list):
    if not list:
        print list
    else:
        for y in list:
            str = parent + '.' + y
            print str
            list2 = opc.list(str)
            #check(y,list2)

import OpenOPC
import time
opc = OpenOPC.client()
server = opc.servers()
print server
serv = 'Matrikon.OPC.Simulation'
#serv = 'Kepware.KEPServerEX.V6'
print opc.connect(serv)
print "Connected to :: " + serv
global g_list
g_list = []
list = opc.list()
var =0
while var == 1 :
    if not list:
        if ~(np.all(g_list == list)).any():
            var=1
            g_list.append(list)
    else:
        for temp in list:
            temp2 = temp
            print temp
            list=opc.list(temp)

print "Out while loop :"
print g_list

'''

for parent in list:
    list2 = opc.list(parent)
    if not list2:
        if ~(np.all(g_list == list)).any():
            print "Already exist"
        else:
            print list
            #g_list = np.append(g_list, list).reshape(-1, 3)
    else:
        check(parent,list2)

def check(list):
    for x in list:
        list1 = opc.list(x)
        if not list1:
            print list
        else:
            for y in list1:
                str = x + '.' + y
                #print str
                list2 = opc.list(str)
                print list2


'''

#print opc.list('Configured Aliases')
#print opc.list('Simulation Items')
#print opc.list('Bucket Brigade')



opc.close()