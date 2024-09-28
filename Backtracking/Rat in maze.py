# https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
# The time complexity of this backtracking approach is O(4^(n * m)), where:

# 4 represents the four possible directions (right, left, down, up) that are attempted at each step.
# (n * m) represents the total number of cells in the grid.

from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        final_row, final_col = len(m), len(m[0])
        res = []
        visited = set()

        def backtrack(r, c, path_till_now):
            if (r, c) == (final_row - 1, final_col - 1):
                res.append(path_till_now)
                return

            visited.add((r, c))  # Mark the current cell as visited
            
            # Define directions as (row_offset, col_offset, direction_string)
            directions = [(0, 1, "R"), (0, -1, "L"), (1, 0, "D"), (-1, 0, "U")]

            for i, j, d in directions:
                new_r, new_c = r + i, c + j
                
                # Check if the new position is within bounds, not visited, and the path is open (m[new_r][new_c] == 1)
                if new_r < 0 or new_r >= final_row or new_c < 0 or new_c >= final_col or (new_r, new_c) in visited or m[new_r][new_c] == 0:
                    continue

                # Call backtrack with the new position and updated path string
                backtrack(new_r, new_c, path_till_now + d)

            visited.remove((r, c))  #we are removing it outside as we need to explore one element fully the we can remove it from visited

        # Start the search from the top-left corner if it's valid (m[0][0] == 1)
        if m[0][0] == 1:
            backtrack(0, 0, "")

        return res

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

solution=Solution()
final=solution.findPath(maze)
print(final)
