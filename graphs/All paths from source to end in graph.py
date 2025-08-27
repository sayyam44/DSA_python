# Updated new
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Corrected to `defaultdict(list)`
    
    def add_edge(self, a, b):
        self.graph[a].append(b)
    
    def all_paths(self, source, end):  # Added `self` as the first parameter
        res = []
        path = []
        
        def dfs(node):
            path.append(node)
            if node == end:
                res.append(path[:])  # Add a copy of the current path
            else:  # Only continue if the current node is not the destination
                for neighbor in self.graph[node]:
                    dfs(neighbor)
            path.pop()  # Backtrack
        
        dfs(source)
        return res

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
print(g.all_paths(0, 3))
