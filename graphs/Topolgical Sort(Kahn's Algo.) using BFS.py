# updated
#there can be many combinations of topological sort
#Topological Sort or KAHNS algorithm
#Topological Sorting means sorting/linear ordering of all the vertices of graph in such a
#  format that 
#if we have any vertex u->v, then u must always occur before v in the sorting .

#TOPOLOGICAL SORTING CAN ONLY OCCUR FOR DIRECTED ACYCLIC GRAPHS(DAG) ONLY

#step1- create an array containing the indegrees of all the elements
#step2-traverse through the above array the elements which have their indegree = 0, append
#  them to a queue
#step3- pop from the queue and add them to the output and also decrease the indegrees of 
# all its adjacent nodes by 1
#step4- Now after decreasing the indegrees by 1 check if some node's indegree has become 0
#  or not,
#if yes then append that element to the que and repeat the process till queue is empty.
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def kahns(self):
        c = self.vertices
        indegree = [0] * c

        # Calculate in-degrees of all vertices
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] += 1

        queue = []
        # Add all vertices with in-degree 0 to the queue
        for i in range(c):
            if indegree[i] == 0:
                queue.append(i)

        cnt = 0  # Counter for the number of vertices processed
        result = []  # List to store the topological order

        while queue:
            s = queue.pop(0)
            result.append(s)

            # Decrease the in-degree of adjacent vertices
            for i in self.graph[s]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

            cnt += 1

        # Check for a cycle in the graph
        if cnt != c:
            print("There exists a cycle in the graph")
        else:
            print("Topological Sort:", result)


# Example usage
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.kahns()
