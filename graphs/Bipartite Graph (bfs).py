#A graph that can be colored using 2 different colors such that no 2 adjacent nodes have same color is called bipartite graph.
import collections

class Solution:
    def isBipartite(self, graph):
        seen = {}  # Dictionary with key as node and value as its color
        
        for node in range(len(graph)):  # Graph may have different disjoint components
            if node not in seen:  # The node has not already been colored
                q = collections.deque([(node, 1)])  # Start BFS from this node with color 1
                while q:
                    n, color = q.popleft()
                    
                    if n in seen:  # If the node has already been seen
                        if seen[n] == color:  # If the color matches the current color, continue
                            continue  # Cyclic graph with even length
                        else:  # If the color does not match, the graph is not bipartite
                            return False  # Cyclic graph with odd length
                    
                    seen[n] = color  # Put the node along with its color in seen
                    # Store neighbor nodes with the opposite color
                    for nei in graph[n]:
                        if nei not in seen:  # Only add unseen neighbors to the queue
                            q.append((nei, color * -1))  # Alternate the color between 1 and -1

        return True  

graph1 = [[1,3], [0,2], [1,3], [0,2]]
graph2 = [[1,2,3], [0,2], [0,1,3], [0,2]]
solution = Solution()
print(solution.isBipartite(graph1))  # Output: True
print(solution.isBipartite(graph2))  # Output: False


# Time = number of nodes + number of edges
# Time: O(n) + O(e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)





            


        
