import numpy as np
import OpenOPC
import time
opc = OpenOPC.client()
server = opc.servers()
print server
serv = 'Matrikon.OPC.Simulation'
#serv = 'Kepware.KEPServerEX.V6'
print opc.connect(serv)
print "Connected to :: " + serv
node_list = []
list = opc.list()
for node in list:
    list1= opc.list(node)
    if not list1:
        print "Empty"
    else:
        if not node_list:
            node_list.append(list)
        else:
            if ~(np.all(node_list == list,node_list)).any():
                print "exist"

            else:
                print "not"


print node_list
opc.close()