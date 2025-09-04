# Updated new
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def is_cyclic(self):
        in_degree = defaultdict(int)
        
        # Initialize in-degree of each node
        for u in self.graph:
            if u not in in_degree:
                in_degree[u] = 0
            for v in self.graph[u]:
                in_degree[v] += 1
        
        # Collect nodes with in-degree 0
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        
        count = 0  # Number of nodes processed
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If count of processed nodes is less than total nodes, there's a cycle
        if count != len(in_degree):
            return True
        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
