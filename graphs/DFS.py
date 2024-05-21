from collections import defaultdict

class graph():
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)

    def dfs_recur(self,v,visited):
        visited[v]=True
        print(v,end=" ")
        for i in self.graph[v]:
            if visited[i]==False:
                self.dfs_recur(i,visited)
    def dfs(self,v):
        visited=[False]*(max(self.graph)+1)
        self.dfs_recur(v,visited)


g=graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)
g.dfs(2)


