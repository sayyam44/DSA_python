# Updated new
#we are traversing DFS in such a way that when we move from one edge to the other edge the ending adjacentvertex
#of that edge should be the 1st one to go into the stack after that the 1st vertex will go into the stack
#eg if we traverse through 1->2 , then 2 will go into stack before 1.
#whenever the dfs call for some vertex is over we add that to the stack

#tc=n+e
#sc=n for the visited array
#asc=n for recursion call of dfs
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices  # Number of vertices in the graph

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_recur(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:  # If the adjacent node has not been visited
                self.dfs_recur(i, visited, stack)
        stack.append(v)  # Append to stack after visiting all adjacent nodes

    def dfs(self):
        visited = [False] * self.vertices
        stack = []
        for i in range(self.vertices):
            if not visited[i]:
                self.dfs_recur(i, visited, stack)
        print("Topological Sort:", stack[::-1])  # Print stack in reverse order

# Example usage
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.dfs()