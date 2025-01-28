# updated
import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Fix: Use list instead of List
        self.V = vertices  # Store number of vertices

    def addEdge(self, frm, to, weight):
        """Add an edge to the graph (undirected by default)."""
        self.graph[frm].append((to, weight))
        self.graph[to].append((frm, weight))  # Add reverse edge for undirected graph

    def mst_prims(self, start):
        """Find the Minimum Spanning Tree (MST) using Prim's Algorithm."""
        visited = [False] * self.V
        minH = [(0, start, -1)]  # (weight, node, parent)
        new_graph = Graph(self.V)  # Create a new graph for MST

        while minH:
            wt, node, parent = heapq.heappop(minH)

            # this is to process a node only once (as there might be some nodes withdifferent weights added in the heap)
            # and we only want to process this node with minimum weight that is only once
            if visited[node]:  
                continue

            visited[node] = True  # Mark node as visited

            if parent != -1:  # Avoid adding root node itself
                new_graph.addEdge(node, parent, wt)

            for to, weight in self.graph[node]:
                # just adding those neighbors those are not visited yet
                if not visited[to]:
                    heapq.heappush(minH, (weight, to, node))

        return new_graph  # Return MST as a new graph

# Example Usage
g = Graph(5)
g.addEdge(0, 1, 2)
g.addEdge(0, 3, 6)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 8)
g.addEdge(1, 4, 5)
g.addEdge(2, 4, 7)
g.addEdge(3, 4, 9)

mst = g.mst_prims(0)

# Print MST edges
print("Edges in the Minimum Spanning Tree:")
for node in mst.graph:
    for to, weight in mst.graph[node]:
        if node < to:  # Avoid printing duplicate edges
            print(f"{node} -- {to} == {weight}")