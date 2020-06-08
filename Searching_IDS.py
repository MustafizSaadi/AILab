import numpy as np
import time
UP = 1
LEFT = 2
BOTTOM = 3
RIGHT = 4
dx = [-1,0,1,0]
dy = [0,-1,0,1]  #up,left,right,bottom
max_node = 0
explored = {}
f = open("IDS_states.txt","a")

class node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost+1

class state:
    def __init__(self, row, col, array): 
        self.row = row
        self.col = col
        self.array = np.copy(array)

def hash(array):
    res = ""
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            res += str(array[i][j])
    #print(res)
    return res


def goal_test(node,n):
    row = node.state.row
    col = node.state.col
    array = node.state.array
    if(row == 0 and col == 0):
        k=1
        for i in range(n):
            for j in range(n):
                if not(i==0 and j==0):
                    if(not(array[i][j] == k)):
                        return False
                    else:
                        k+=1
        return True
    else:
        return False


def child_node(parent, actionRow, actionCol, action):
    array = parent.state.array
    newArray = np.copy(array)
    if (action == UP):
        newArray[actionRow+1][actionCol] = array[actionRow][actionCol]
        newArray[actionRow][actionCol] = -1
    elif(action == LEFT):
        newArray[actionRow][actionCol+1] = array[actionRow][actionCol]
        newArray[actionRow][actionCol] = -1
    elif(action == BOTTOM):
        newArray[actionRow-1][actionCol] = array[actionRow][actionCol]
        newArray[actionRow][actionCol] = -1
    else:
        newArray[actionRow][actionCol-1] = array[actionRow][actionCol]
        newArray[actionRow][actionCol] = -1
    childState = state(actionRow,actionCol,newArray)
    child = node(childState,parent,action,parent.path_cost)
    return child

def print_states(node,initArray,f):
    if(np.array_equal(node.state.array,initArray)):
        return
    else:
        print_states(node.parent,initArray,f)
        if(node.action == UP):
            f.write("UP" + "\n")
            np.savetxt(f,node.state.array.astype(int), fmt = "%d", delimiter = " ")
            f.write("\n")
        elif(node.action == LEFT):
            f.write("LEFT" + "\n")
            np.savetxt(f,node.state.array.astype(int), fmt = "%d", delimiter = " ")
            f.write("\n")
        elif(node.action == BOTTOM):
            f.write("BOTTOM" + "\n")
            np.savetxt(f,node.state.array.astype(int), fmt = "%d", delimiter = " ")
            f.write("\n")
        elif(node.action == RIGHT):
            f.write("RIGHT" + "\n")
            np.savetxt(f,node.state.array.astype(int), fmt = "%d", delimiter = " ")
            f.write("\n")



def dls(node,n,limit):
    #print(limit)
    np.savetxt(f,node.state.array.astype(int), fmt = "%d", delimiter = " ")
    f.write("\n")
    global max_node
    max_node += 1 
    explored[hash(node.state.array)] = limit
    #print(node.state.array)
    #result = None
    if(goal_test(node,n)):
        # f.close()
        return node
    elif(limit == 0):
        return 2
    else:
        #print(limit)
        cutoff_occurred = 0
        row = node.state.row
        col = node.state.col
        for i in range(4):
            if(row + dx[i] >= 0 and row + dx[i] <=n-1 and col + dy[i] >=0 and col + dy[i] <=n-1):
                child = child_node(node, row + dx[i], col + dy[i],i+1)
                if((hash(child.state.array) not in explored) or ((hash(child.state.array) in explored) and explored[hash(child.state.array)]<limit)):
                    result = dls(child,n,limit-1)
                    if(result == 2):
                        cutoff_occurred = 1
                    elif(result != None):
                        return result

        if(cutoff_occurred):
            return 2
        else:
            return None
                        

def ids(node,n):
    limit = 0
    while True:
        explored.clear()
        result = dls(node,n,limit)
        if result == 2:
            limit += 1
        else:
            return result
                        

def main(n,initArray):

    global max_node
    max_node = 0

    print(initArray)
    print("\nIDS")

    ftime = open("ids_time.txt","a")
    fnode = open("ids_node.txt","a")
    fpath = open("ids_path.txt","a")
    foutput = open("ids_output.txt","a")

    row=(np.where(initArray == -1)[0][0])
    col=(np.where(initArray == -1)[1][0])
    print(row,col)

    rootstate = state(row,col,initArray)

    action = -1
    root = node(rootstate,None,action,-1)

    time1 = time.time()
    ans=ids(root,n)
    time2 = time.time()
    ftime.write(str(time2-time1) + "\n")
    fnode.write(str(max_node)+"\n")

    if ans == None:
        print("Failed to produce any solution!")
    else:
        fpath.write(str(ans.path_cost)+"\n")
        foutput.write("input" + "\n")
        np.savetxt(foutput,initArray.astype(int), fmt = "%d", delimiter = " ")
        foutput.write("\n")
        print_states(ans,initArray,foutput)

# # print(ans.action)

    ftime.close()
    fnode.close()
    fpath.close()
    foutput.close()
# 
