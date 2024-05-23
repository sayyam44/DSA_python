#we are traversing DFS in such a way that when we move from one edge to the other edge the ending adjacentvertex
#of that edge should be the 1st one to go into the stack after that the 1st vertex will go into the stack
#eg if we traverse through 1->2 , then 2 will go into stack before 1.
#whenever the dfs call for some vertex is over we add that to the stack

#tc=n+e
#sc=n for the visited array
#asc=n for recursion call of dfs

from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    
    def dfs_recur(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False: #means he have some unexplored adjacent nodes
                self.dfs_recur(i,visited,stack)
        stack.append(v) #append in stack if all the adjacent elements of the node has already been visited and the 2nd case is when there are no adjacent elements of that node.
    def dfs(self):
        visited=[False]*(max(self.graph)+1)
        stack=[]
        for i in range(max(self.graph)+1):
            if visited[i]==False:
                self.dfs_recur(i,visited,stack)
