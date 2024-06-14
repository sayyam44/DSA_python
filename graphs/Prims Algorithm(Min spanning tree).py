import heapq
def min_spanning(adj,V):
    minH=[] #weight,to_node,from_node(wt,node,parent)
    mst=[] #this will contain all the edges for the outcome Min spanning tree
    visited=[False]*V
    mst_sum=0
    heapq.heappush(minH,(0,0,-1))

    while minH:
        weight,to_node,parent=heapq.heappop(minH)

        if visited[to_node]:
            continue

        visited[to_node]=True
        mst_sum+=weight

        if parent != -1:
            mst.append((parent,to_node,weight))

        for to,wt in adj[to_node]:
            if not visited[to]:
                heapq.heappush(minH,(wt,to,to_node))
    
    print("Sum of weights of edges in the MST:", mst_sum)
    print("Edges in the MST:")
    for from_vertex, to_vertex, weight in mst:
        print(f"{from_vertex} -- {to_vertex} [weight: {weight}]")  

V = 4
adj = [
    [(1, 1), (2, 3), (3, 4)],  # Edges from vertex 0
    [(0, 1), (2, 2), (3, 5)],  # Edges from vertex 1
    [(0, 3), (1, 2), (3, 6)],  # Edges from vertex 2
    [(0, 4), (1, 5), (2, 6)]   # Edges from vertex 3
]
min_spanning(adj,V)