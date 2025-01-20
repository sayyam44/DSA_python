# updated
#for this we will append the values,parent values into the queue as we iterate through them by bfs rule
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since it's an undirected graph

    def is_cyclic_bfs(self, v, visited):#parent node is the previous node of current node , significance
        #  of parent node is that parent node is already True in visited just before  so we need not
        #  to return if we get True for parent node in visited we just need to return False that there is no cycle
        #logic---------> we will go through each adjacent node of the particular node if any adjacent node is 
        #already visited (visited=true) except the parent node then there is cycle
        parent = {v: -1}
        q = deque([v])
        visited[v] = True

        while q:
            node = q.popleft()
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
                    parent[neighbor] = node
                elif parent[node] != neighbor: #if the current node (neighbor) that we are iterating is not 
                    # a direct neighbor of node then there must a cycle.
                    return True  # Cycle detected
        return False

    def bfs(self):
        visited = [False] * (max(self.graph) + 1)
        for i in range(len(visited)):
            if not visited[i] and self.graph[i]:  # Ensure that we start BFS for every connected component
                if self.is_cyclic_bfs(i, visited):
                    return True
        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # Adding this edge creates a cycle
g.add_edge(3, 4)

print("Graph contains cycle" if g.bfs() else "Graph doesn't contain cycle")




