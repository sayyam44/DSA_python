# Updated new
# Time Complexity: 𝑂 ( 𝑀 ⋅ 𝑁 ⋅ log ⁡ ( 𝑀 ⋅ 𝑁 ) ) O(M⋅N⋅log(M⋅N))
# https://leetcode.com/problems/path-with-minimum-effort/description/
import heapq
class Solution:
    def minimumEffortPath(self, heights):
        rows=len(heights)
        cols=len(heights[0])
        efforts=[[float('inf')]*cols for _ in range (rows)]
        efforts[0][0]=0
        minh=[(0,0,0)] #efforts,rows,cols
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while minh:
            effort,r,c=heapq.heappop(minh)

            for a,b in directions:
                new_r,new_c=r+a,c+b
                if 0<=new_r<rows and 0<=new_c<cols:
                    new_effort=max(effort,abs(heights[new_r][new_c]-heights[r][c]))
                    if efforts[new_r][new_c]>new_effort:
                        efforts[new_r][new_c]=new_effort
                        heapq.heappush(minh,(new_effort,new_r,new_c))
        return efforts[rows-1][cols-1]

# Example usage:
solution = Solution()
heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]
print(solution.minimumEffortPath(heights))  # Output: 2

