# updated
#A graph that can be colored using 2 different colors such that no 2 adjacent nodes have same color is called bipartite graph.
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bipartite(self):
        # Initialize visited array with 2 (unvisited nodes)
        visited = [2] * (max(self.graph) + 1)

        for i in range(len(visited)):
            if visited[i] == 2:  # Start BFS for unvisited nodes
                q = deque()
                q.append((i, 1))  # Node and color

                while q:
                    node, color = q.popleft()

                    # If node has already been visited
                    if visited[node] != 2:
                        if visited[node] != color:  # Conflict in coloring
                            return False
                        continue

                    # Mark the node as visited with the current color
                    visited[node] = color

                    # Traverse neighbors
                    for nei in self.graph[node]:
                        if visited[nei] == 2:  # If neighbor is unvisited
                            q.append((nei, -color))  # Assign opposite color
                        elif visited[nei] == color:  # Conflict in coloring
                            return False

        return True


# Example usage
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(2, 3)

print("Is the graph bipartite?", g.bipartite())


# Time = number of nodes + number of edges
# Time: O(n) + O(e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)





            


        
