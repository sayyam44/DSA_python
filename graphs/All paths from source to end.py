
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []
        n = len(graph)
        
        def dfs(curr):
            path.append(curr)
            if curr == n - 1:  # If the current node is the last node
                result.append(path[:])
                path.pop()  # Remove the current node to backtrack
                return
            else:
                for neighbor in graph[curr]:
                    dfs(neighbor)
                # Done exploring all neighbors of the current node
                path.pop()
            
        dfs(0)  # Start DFS from node 0
        return result
    
sol = Solution()
graph = [[1,2], [3], [3], []]
print(sol.allPathsSourceTarget(graph))  # Output: [[0, 1, 3], [0, 2, 3]]
