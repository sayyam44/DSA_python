from collections import deque
def shortest_path(matrix,src,dest):
    rows=len(matrix)
    cols=len(matrix[0])
    visited=[[False for _ in range (cols)]for _ in range (rows)]
    directions=[(-1,0),(1,0),(0,1),(0,-1)]
    q=deque()

    src_r,src_c=src
    des_r,des_c=dest

    q.append((0,src_r,src_c))
    visited[src_r][src_c]=True

    while q:
        dist,r,c=q.popleft()
        if r==des_r and c==des_c:
            return dist

        for row,col in directions:
            dr=row+r
            dc=col+c
            if (dr<0 or dr==rows or dc<0 or dc==cols or visited[dr][dc] or matrix[dr][dc]==0):
                continue
            dist+=1
            q.append((dist,dr,dc))
            visited[dr][dc]=True
    return -1
            
matrix = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 1]
]

src = (0, 0)  # Starting cell (row, col)
dest = (3, 3)  # Destination cell (row, col)

result = shortest_path(matrix, src, dest)
print("Shortest path length:", result)