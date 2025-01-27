# updated
# Time Complexity: 𝑂 ( 𝑀 ⋅ 𝑁 ⋅ log ⁡ ( 𝑀 ⋅ 𝑁 ) ) O(M⋅N⋅log(M⋅N))
# https://leetcode.com/problems/path-with-minimum-effort/description/
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)]  # (effort, row, col)
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            
            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
        
        return 0  # This line should never be reached if the input is valid

# Example usage:
# solution = Solution()
# heights = [
#     [1, 2, 2],
#     [3, 8, 2],
#     [5, 3, 5]
# ]
# print(solution.minimumEffortPath(heights))  # Output: 2

