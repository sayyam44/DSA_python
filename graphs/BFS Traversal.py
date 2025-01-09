from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def bfs(self,start):
        visited=[False]*(max(self.graph)+1)
        q=[]
        q.append(start)
        visited[start]=True

        while q:
            val=q.pop(0)
            print(val,end=" ")
            for i in self.graph[val]:
                if not visited[i]:
                    q.append(i)
                    visited[i]=True
        

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)