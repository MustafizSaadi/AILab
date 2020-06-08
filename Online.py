import Searching_BFS
import Searching_DLS
import Searching_IDS
import Searching_UCS
import Searching_ASTAR
import Searching_GBFS
import numpy as np

n = int(input("Enter the value of n:\n"))
initArray = np.zeros((n,n))

print("Enter -1 for blank cell\n")
for i in range(n):
        for j in range(n):
            initArray[i][j] = input("Enter value for cell"+str(i+1)+str(j+1)+(":"))

print("Enter 1 for BFS\n")
print("Enter 2 for UCS\n")
print("Enter 3 for DLS\n")
print("Enter 4 for IDS\n")
print("Enter 5 for GBFS\n")
print("Enter 6 for ASTAR\n")

option = int(input())
if option == 1:
    Searching_BFS.main(n,initArray)
elif option == 2:
    Searching_UCS.main(n,initArray)
elif option == 3:
    Searching_DLS.main(n,initArray)
elif option == 4:
    Searching_IDS.main(n,initArray)
elif option == 5:
    Searching_GBFS.main(n,initArray)
elif option == 6:
    Searching_ASTAR.main(n,initArray)
