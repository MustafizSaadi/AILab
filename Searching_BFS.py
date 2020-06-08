import numpy as np
import time
UP = 1
LEFT = 2
BOTTOM = 3
RIGHT = 4
dx = [-1,0,1,0]
dy = [0,-1,0,1]  #up,left,right,bottom
# n=3



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




def check(explored,state):
    #print(len(explored))
    for i in explored:
        #print(i.array,state.array)
#         print(len(explored))
        if(i.row == state.row and i.col == state.col and np.array_equal(i.array, state.array)):
            return True
    return False
            



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


def bfs(root,n):
    queue = []
    explored = {}
    f = open("BFS_states.txt","a")
    max_node = 0
    queue.append(root)
    if(goal_test(root,n)):
        np.savetxt(f,root.state.array.astype(int), fmt = "%d", delimiter = " ")
        # f.close()
        return root
    while True:
        #print(len(queue))
        max_node = max(len(queue),max_node)
        if(len(queue) == 0):
            return max_node,None
        u = queue.pop(0)
        np.savetxt(f,u.state.array.astype(int), fmt = "%d", delimiter = " ")
        f.write("\n")
        explored[hash(u.state.array)] = 1
        row = u.state.row
        col = u.state.col
        #print(row,col)
        for i in range(4):
            if(row + dx[i] >= 0 and row + dx[i] <=n-1 and col + dy[i] >=0 and col + dy[i] <=n-1):
                child = child_node(u, row + dx[i], col + dy[i],i+1)
                if(hash(child.state.array) not in explored):
                    if(goal_test(child,n)): 
                        np.savetxt(f,child.state.array.astype(int), fmt = "%d", delimiter = " ")
                        f.write("\n")
                        f.close()
                        return max_node,child
                    else:
                        queue.append(child)
                        




# # print(ans.action)
def main(n,initArray):

    print(initArray)
    print("\nBFS")

    ftime = open("bfs_time.txt","a")
    fnode = open("bfs_node.txt","a")
    fpath = open("bfs_path.txt","a")
    foutput = open("bfs_output.txt","a")


    row=(np.where(initArray == -1)[0][0])
    col=(np.where(initArray == -1)[1][0])
    print(row,col)


    rootstate = state(row,col,initArray)


    action = -1
    root = node(rootstate,None,action,-1)



    t1 = time.time()
    max_node,ans=bfs(root,n)
    t2 = time.time()
    ftime.write(str(t2-t1) + "\n")
    fnode.write(str(max_node)+"\n")

    if ans == None:
        print("Failed to produce any solution!")
    else:
        fpath.write(str(ans.path_cost)+"\n")
        foutput.write("input" + "\n")
        np.savetxt(foutput,initArray.astype(int), fmt = "%d", delimiter = " ")
        foutput.write("\n")
        print_states(ans,initArray,foutput)
    
    ftime.close()
    fnode.close()
    fpath.close()
    foutput.close()


