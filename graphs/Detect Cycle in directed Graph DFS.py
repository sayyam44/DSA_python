#we will make two visited arrays , first array will be normally become true when the element's dfs is called 
#and in 2nd array it will become true same way but again will become false when it moves recursively backwards
# If for an element both the arrays have true value this means there is a cycle in graph.
#when the dfs call for some node is over mark that as true in recStack array 

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_recur(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.dfs_recur(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[v] = False
        return False
    
    def dfs(self):
        visited = [False] * (max(self.graph) + 1)
        rec_stack = [False] * (max(self.graph) + 1)
        
        for node in range(max(self.graph) + 1):
            if not visited[node] and self.graph[node]:  # Ensure the node exists in the graph
                if self.dfs_recur(node, visited, rec_stack):
                    return True
        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

if g.dfs():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")

g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(1, 2)

if g1.dfs():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
