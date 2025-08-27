# Updated new
#Bellman ford algorithm 
#This algorithm is also used to find the shortest distance from source till every other node 
#The only difference b/w bellman ford and dijkistra's algorithm is that this algorithm can 
#be used in graph with negative weights i.e. for a graph with negative cycle.

#Negative cycle means a graph with sum of its weights of the current path as negative value.

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
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append((u,v,w))

    def BellmanFord(self,start):
        dist=[float("inf")]*(self.V)
        dist[start]=0

        for _ in range(self.V-1):
            for parent,child,weight in self.graph:
                if dist[parent]!=float("inf") and dist[parent]+weight<dist[child]:
                    dist[child]=dist[parent]+weight
            
        for parent,child,weight in self.graph: #negative cycle
                if dist[parent]!=float("inf") and dist[parent]+weight<dist[child]:
                    print('NEGATIVE WEIGHT')
                    return None

        self.print_solution(dist)

    def print_solution(self,dist):
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")



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

