import Searching_BFS
import Searching_DLS
import Searching_IDS
import Searching_UCS
import Searching_ASTAR
import Searching_GBFS
import numpy as np
from io import StringIO
import os
import matplotlib.pyplot as plt

def giveY(f):
        y = np.zeros(20)
        for i in range(1,21):
                input = f.readline()
                y[i-1] = float(input)
        return y

os.remove("astar_node.txt")
os.remove("astar_path.txt")
os.remove("astar_time.txt")
os.remove("bfs_node.txt")
os.remove("bfs_path.txt")
os.remove("bfs_time.txt")
os.remove("dls_node.txt")
os.remove("dls_path.txt")
os.remove("dls_time.txt")
os.remove("gbfs_node.txt")
os.remove("gbfs_path.txt")
os.remove("gbfs_time.txt")
os.remove("ids_node.txt")
os.remove("ids_path.txt")
os.remove("ids_time.txt")
os.remove("ucs_node.txt")
os.remove("ucs_path.txt")
os.remove("ucs_time.txt")
os.remove("bfs_output.txt")
os.remove("ucs_output.txt")
os.remove("dls_output.txt")
os.remove("ids_output.txt")
os.remove("gbfs_output.txt")
os.remove("astar_output.txt")

temp = open("input.txt","r")
allData = np.loadtxt(temp)
len = allData.shape[0]
input = np.zeros((3,3))
for i in range(0,len-2,3):
        input[0] = allData[i]
        input[1] = allData[i+1]
        input[2] = allData[i+2]
        Searching_BFS.main(3,input)
        Searching_UCS.main(3,input)
        Searching_DLS.main(3,input)
        Searching_IDS.main(3,input)
        Searching_GBFS.main(3,input)
        Searching_ASTAR.main(3,input)

plt.subplot(3, 1, 1)

x = np.linspace(1,20,20) 
# y = np.zeros(21)
f = open("bfs_time.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "BFS")

f = open("ucs_time.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "UCS")

f = open("dls_time.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y,label = "DLS")

f = open("ids_time.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "IDS")

f = open("gbfs_time.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "GBFS")

f = open("astar_time.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "ASTAR")

plt.legend()
plt.title("Clock Time")

plt.subplot(3, 1, 2)

f = open("bfs_node.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "BFS")

f = open("ucs_node.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "UCS")

f = open("dls_node.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "DLS")

f = open("ids_node.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "IDS")

f = open("gbfs_node.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "GBFS")

f = open("astar_node.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "ASTAR")

plt.legend()
plt.title("Number of Nodes")

plt.subplot(3, 1, 3)

f = open("bfs_path.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "BFS")

f = open("ucs_path.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "UCS")

f = open("dls_path.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "DLS")

f = open("ids_path.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "IDS")

f = open("gbfs_path.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "GBFS")

f = open("astar_path.txt","r")
y = giveY(f)
f.close()

plt.plot(x,y, label = "ASTAR")

plt.legend()
plt.title("Path Cost")

plt.tight_layout() 
plt.show()

