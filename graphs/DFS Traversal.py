from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,v,visited):
        print(v,end=" ")
        visited[v]=True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i,visited)
        return 
    def func(self,start):
        visited=[False]*(max(self.graph)+1)
        self.dfs(start,visited)


g=graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)
g.func(2)


