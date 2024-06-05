#Bellman ford algorithm 
#This algorithm is also used to find the shortest distance from source till every other node 
#The only difference b/w bellman ford and dijkistra's algorithm is that this algorithm can 
#be used in graph with negative weights i.e. for a graph with negative cycle.

#Negative cycle means a graph with sum of its weights as negative value.

#Bellman ford only works in the case of a directed graph

#1)The edges can be in any order.

#2) Relaxation of all nodes is done for n-1 times.Below is what relaxation is 
#if dist[node]+weight<dist[neighbor] 
#then dist[neighbor] = dist[node]+weight

#The reason why we will be doing relaxation n-1 times is that in the worst case you will
#take N-1 edges to reach from the first to the last node.

#If on Nth iterations we do the relaxation and we get a negative value in the distance arr
#then we can say it contains a negative cycle.

class Graph:

    def __init__(self, vertices):
        self.V = vertices  
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        #here we are doing nth relaxation to check negative cycle
        #and if we find some lower distance now at nth iteration then that is wrong 
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.printArr(dist)

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    g.BellmanFord(0)
