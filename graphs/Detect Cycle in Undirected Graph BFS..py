# Updated new
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since it's an undirected graph

    def is_cyclic_bfs(self, v, visited):
        q = deque([(v, -1)])  # Store (node, parent)
        visited[v] = True

        while q:
            node, parent = q.popleft()
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, node))  # Append with parent tracking
                elif neighbor != parent:  # If visited and not parent, cycle detected
                    return True
        return False

    def bfs(self):
        visited = {node: False for node in self.graph}  # Use dictionary for sparse graphs
        for node in self.graph:
            if not visited[node]:  
                if self.is_cyclic_bfs(node, visited):
                    return True
        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # Creates a cycle
g.add_edge(3, 4)

print("Graph contains cycle" if g.bfs() else "Graph doesn't contain cycle")




