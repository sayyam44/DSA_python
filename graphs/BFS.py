from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s): #s is the value from which bfs will begin 
        visited = [False] * (max(self.graph) + 1) #we are doing max(self.graph) because the graph may not be a connected graph
        q=[]
        q.append(s)
        visited[s]=True

        while q:
            s=q.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:#iterating through all the neighbors of s
                if visited[i]==False:
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