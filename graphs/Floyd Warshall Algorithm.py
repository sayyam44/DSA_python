# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implementing-floyd-warshall

#Floyd Warshall Algorithm helps to find the shortest distance between all the pairs of nodes and not just 
#from a 1 source unlike Dijkistra's and Bellman Ford algorithm does.

#It is also used to detect a negative cycle i.e. if the cost from a node to itself becomes 
#negative at the end of the loop then we say it have a negative cycle.

#tc=n3
def floydWarshall(matrix):
    n = len(matrix)
    inf = float('inf')
    
    # Step 1: Initialize the adjacency matrix
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == -1:
                matrix[i][j] = inf
        matrix[i][i] = 0  # Distance to self is zero
    
    # Step 2: Apply the Floyd-Warshall algorithm
    for via in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][via] < inf and matrix[via][j] < inf:  # Check for valid intermediate path
                    matrix[i][j] = min(matrix[i][j], matrix[i][via] + matrix[via][j])
    
    # Step 3: Final update to replace inf with -1 for no path
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == inf:
                matrix[i][j] = -1

# Example usage:
matrix = [
    [0, 3, -1, 7],
    [-1, 0, 2, -1],
    [-1, -1, 0, 1],
    [6, -1, -1, 0]
]

floydWarshall(matrix)
print(matrix)
