# Updated new
# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implementing-floyd-warshall
# updated
#Floyd Warshall Algorithm helps to find the shortest distance between all the pairs of nodes and not just 
#from a 1 source unlike Dijkistra's and Bellman Ford algorithm does.

#It is also used to detect a negative cycle i.e. if the cost from a node to itself becomes 
#negative at the end of the loop then we say it have a negative cycle.

#tc=n3

def floyd_warshall(graph):
    num_vertices = len(graph)
    
    # Initialize the distance matrix
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    # Set diagonal to 0 and copy initial graph values
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example graph represented as an adjacency matrix
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

# Run Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Print result
print("Shortest distance matrix:")
for row in shortest_paths:
    print(row)
