# updated
#In this ques we have to begin from top left corner and reach upto the bottom right corner
#now among all the paths we need to find the maximum valued node that is visited in
#all these nodes in all the paths seperately for example if we have 2 paths to reach the 
# bottom right node i.e. 1->5->9->2 and nother one is 1->3->6->2 then the 1st path's max 
# value is 9 and the second path's max value is 6 so our code should return the minimum 
# value among these max values i.e. among 9 and 6 our code will return this path 
# followed to reach the target node i.e.1->3->6->2 

#here we will use min_heap 
#with every node that we visit we will append into the min heap (a,b,c) 
#where a is the maximum valued node visited till now in this path 
#and b,c is that node's row,col

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t
            for row, col in directions:
                dr = r + row
                dc = c + col
                if (dr == N or dc == N or dr < 0 or dc < 0 or (dr, dc) in visited):
                    continue
                visited.add((dr, dc))
                heapq.heappush(minH, [max(t, grid[dr][dc]), dr, dc])

# Example usage
grid = [
    [0, 2, 1],
    [3, 6, 5],
    [8, 4, 7]
]
solution = Solution()
print(solution.swimInWater(grid))
