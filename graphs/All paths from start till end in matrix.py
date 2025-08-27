# Updated new
from typing import List, Tuple

class Solution:
    def findPath(self, m: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[str]:
        ROWS = len(m)
        COLS = len(m[0])
        res = []
        visited = set()

        def backtrack(i, j, path_till_now):
            if (i, j) == end:
                res.append(path_till_now)
                return
            
            visited.add((i, j))

            # Define possible directions: Right (R), Left (L), Down (D), Up (U)
            directions = [(0, 1, "R"), (0, -1, "L"), (1, 0, "D"), (-1, 0, "U")]

            for a, b, direction in directions:
                new_r = i + a
                new_c = j + b

                # Check bounds, if the cell is visited, or if the cell is blocked (0)
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited and m[new_r][new_c] == 1:
                    backtrack(new_r, new_c, path_till_now + direction)

            # Backtrack: remove the current cell from visited after all paths are explored
            visited.remove((i, j))

        # Start the backtracking from the start point
        if m[start[0]][start[1]] == 1:  # Check if start point is valid
            backtrack(start[0], start[1], "")

        return res

# Example usage
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]
start = (0, 0)
end = (3, 3)

solution = Solution()
paths = solution.findPath(maze, start, end)
print(paths)
