# updated
#tc=n,sc=n
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs_recur(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.dfs_recur(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False
    
    def dfs(self):
        visited = [False] * (max(self.graph) + 1)
        for i in range(visited):
            if not visited[i] and self.graph[i]:  # Ensure the node exists in the graph
                if self.dfs_recur(i, visited, -1):
                    return True
        return False

# Example usage:
g = Graph()
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

if g.dfs():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")

g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(1, 2)

if g1.dfs():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
