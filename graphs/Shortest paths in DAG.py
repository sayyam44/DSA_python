# Updated new
#THIS ALGORITHM WILL WORK FOR DIRECTED ACYCLIC GRAPH BUT DIJKISTRA'S CAN WORK FOR UNDIRECTED ACYCLIC GRAPH ONLY.
##this code is for finding shortest paths from source to every other nodes in graph.

#step 1- do the topological sort ang get the stack
#step2- make another array which initially will have infinity values in it and then then pop from stack one by one and 
# update the inf value by the value that is shorter than inf and so onn by adding the weights on each step, 

# for Directed Acyclic Graphs Complexity :O(V+E)
from collections import defaultdict

class Graph:
	def __init__(self,vertices):

		self.V = vertices # No. of vertices
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))

	def topologicalSortUtil(self,v,visited,stack):
		visited[v] = True
		if v in self.graph.keys():
			for node,weight in self.graph[v]:
				if visited[node] == False:
					self.topologicalSortUtil(node,visited,stack)
		stack.append(v)


	''' The function to find shortest paths from given vertex.
		It uses recursive topologicalSortUtil() to get topological
		sorting of given graph.'''
	def shortestPath(self, s):
		visited = [False]*self.V
		stack =[]
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(s,visited,stack)

		# Initialize distances to all vertices as infinite and distance to source as 0
		dist = [float("Inf")] * (self.V)
		dist[s] = 0

		# Process vertices in topological order
		while stack:
			# Get the next vertex from topological order
			i = stack.pop()
			# Update distances of all adjacent vertices
			for node,weight in self.graph[i]:
				if dist[node] > dist[i] + weight:#for finding the shortest distance
					dist[node] = dist[i] + weight
		# Print the calculated shortest distances
		for i in range(self.V):
			print(f"{dist[i]}" if dist[i] != float("Inf") else "Inf", end=" ")


g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

# source = 1
s = 1

print ("Following are shortest distances from source %d " % s)
g.shortestPath(s)
