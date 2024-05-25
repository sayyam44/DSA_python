#DIKSTRA'S ALGORITHM- it helps us to find the shortest path between a source and every other node 
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet): #this function is to reach to index that is currently at min dist

		# Initialize minimum distance for next node
		min = sys.maxsize

		# Search not nearest vertex not in the
		# shortest path tree
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False: #till this time dist[u]=0 is only for one case i.e. for index 1
				min = dist[u] #min =0 for 1st case in copy 
				min_index = u #min_index=1 for 1st case in copy

		return min_index

	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V 
		dist[src] = 0 #beacaue 1st dist will always be 0
		sptSet = [False] * self.V #we are creating set because there may occur some duplicate values 
                                  #that we dont want

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# x is always equal to src in first iteration
			x = self.minDistance(dist, sptSet) #it will return 1 in the example in copy

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[x] = True #make index 1 == True for 1st time.

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current(already existing)
			# distance(dist[y]) is greater than new distance(dist[x] + self.graph[x][y]) and
			# the vertex in not in the shortest path tree
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
						dist[y] = dist[x] + self.graph[x][y]
						#dist[y]=inf in 1st case
						#dist[x]=0 in 1st case that we just calculated above
						#self.graph[x][y]=prev val.
		self.printSolution(dist)

# Driver program
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0], # Edges from vertex 0 to vertices 1 and 7
    [4, 0, 8, 0, 0, 0, 0, 11, 0], # Edges from vertex 1 to vertices 0, 2, and 7
    [0, 8, 0, 7, 0, 4, 0, 0, 2], # Edges from vertex 2 to vertices 1, 3, 5, and 8
    [0, 0, 7, 0, 9, 14, 0, 0, 0], # Edges from vertex 3 to vertices 2, 4, and 5
    [0, 0, 0, 9, 0, 10, 0, 0, 0], # Edges from vertex 4 to vertices 3 and 5
    [0, 0, 4, 14, 10, 0, 2, 0, 0], # Edges from vertex 5 to vertices 2, 3, 4, and 6
    [0, 0, 0, 0, 0, 2, 0, 1, 6], # Edges from vertex 6 to vertices 5, 7, and 8
    [8, 11, 0, 0, 0, 0, 1, 0, 7], # Edges from vertex 7 to vertices 0, 1, 6, and 8
    [0, 0, 2, 0, 0, 0, 6, 7, 0] # Edges from vertex 8 to vertices 2, 6, and 7
]

g.dijkstra(0);