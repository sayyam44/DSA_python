# Updated new
from collections import deque

def shortest_path_in_binary_maze(grid, src, dest):
    rows, cols = len(grid), len(grid[0])
    
    # If the source or destination is blocked, return -1
    if grid[src[0]][src[1]] == 0 or grid[dest[0]][dest[1]] == 0:
        return -1
    
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize visited array
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[src[0]][src[1]] = True

    # Queue for BFS: (current_row, current_col, distance)
    q = deque([(src[0], src[1], 0)])
    
    while q:
        r, c, dist = q.popleft()
        
        # If we reach the destination, return the distance
        if (r, c) == dest:
            return dist
        
        # Explore neighbors
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c] and grid[new_r][new_c] == 1:
                visited[new_r][new_c] = True
                q.append((new_r, new_c, dist + 1))
    
    # If destination is not reachable
    return -1

# Example usage
grid = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 1]
]

src = (0, 0)  # Starting cell
dest = (3, 3)  # Destination cell

result = shortest_path_in_binary_maze(grid, src, dest)
print("Shortest path length:", result)
