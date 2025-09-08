# Updated new
import heapq
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def print_solution(self, dist, parent, dest):
        print("Vertex \tDistance from Source \tPath")
        path = self.get_path(parent, dest)
        print(f"{dest}\t{dist[dest]}\t\t\t{path}")

    # To reconstruct the actual path from the source to the 
    # destination, we need to start at the destination 
    # (Vertex 2 in this case) and trace back through the parent 
    # array until we reach the source(whos parent is -1)
    def get_path(self, parent, j):
        if parent[j] == -1:  # this means we have reached the souce node
            return str(j)
        return self.get_path(parent, parent[j]) + " -> " + str(j)

    def dijkstra(self, src, dest):
        dist = [float('inf')] * self.V
        parent = [-1] * self.V
        dist[src] = 0
        min_heap = [(0, src)]  # (distance, vertex)

        while min_heap:
            d, u = heapq.heappop(min_heap)

            if u == dest:
                break

            for v, weight in self.graph[u]:
                if  dist[v]>dist[u] + weight:
                    dist[v] = dist[u] + weight
                    #whenever a distance of node is updated in dist list at that
                    #time we update its parent also and also it is added to minheap
                    parent[v] = u
                    heapq.heappush(min_heap, (dist[v], v))

        self.print_solution(dist, parent, dest)

# Driver program
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 8, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

src = 0
dest = 5
g.dijkstra(src, dest)
