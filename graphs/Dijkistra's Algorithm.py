# Updated new
#THIS ALGORITHM WILL WORK FOR UNDIRECTED ACYCLIC GRAPH BUT 
# DAG ALGO CAN WORK FOR DIRECTED ACYCLIC GRAPH ONLY.
#Dijkistra algo cannot even take negative weights. 

#DIKSTRA'S ALGORITHM- it helps us to find the shortest path 
# between a source and every other node 

# Initialize Distances: Set the distance of all vertices to infinity (inf), except the source, which is set to 0.
# Create Priority Queue: Use a min-heap (priority queue) to store (distance, vertex) pairs, starting with (0, source).
# Process Queue: Extract the vertex with the smallest distance from the min-heap.
# Visit Neighbors: For each neighbor of the current vertex, calculate the potential new distance through the current vertex.
# Update Distance: If the new distance is smaller than the currently known distance, update it and push the neighbor into the min-heap.
# Mark Processed: Mark the current vertex as processed once all its neighbors are evaluated.
# Repeat: Continue processing vertices from the priority queue until it is empty.
import heapq
from collections import defaultdict

class Graph:
    def __init__(self, num):
        self.graph = defaultdict(list)  # Adjacency list
        self.V = num                   # Number of vertices

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))   # Edge from u to v with weight w

    def dijkstra(self, src):
        # Distance array initialized to infinity
        dist = [float('inf')] * self.V
        dist[src] = 0  # Distance to source is 0

        # Priority queue (min-heap) to store (distance, vertex)
        min_heap = [(0, src)]  # (distance, vertex)

        while min_heap:
            current_dist, current_vertex = heapq.heappop(min_heap)

            # Process neighbors of the current vertex
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_dist + weight
                # If a shorter path is found
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        # Print the shortest distances
        for i in range(self.V):
            print(f"Vertex {i}: {dist[i]}" if dist[i] != float('inf') else f"Vertex {i}: Inf")

# Example Usage
g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)  # Dijkstra's doesn't support negative weights properly
g.addEdge(4, 5, -2)  # Negative weights can lead to incorrect results

g.dijkstra(0)
