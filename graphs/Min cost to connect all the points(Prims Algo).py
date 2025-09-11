# Updated new
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# tc=(n2)logn
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points) 
        adj={i:[] for i in range(N)} #node,dist

        for j in range(N):
            for k in range(j+1,N):
                dist = abs(points[j][0] - points[k][0]) + abs(points[j][1] - points[k][1])
                adj[j].append((k,dist))
                adj[k].append((j,dist))

        minH=[[0,0]] #distance,node
        visited=[False]*N
        result=0
        while minH:
            distance,node=heapq.heappop(minH)
            if visited[node]:
                continue
            visited[node]=True
            result+=distance
            for new_node,dist in adj[node]:
                if not visited[new_node]:
                    heapq.heappush(minH,(dist,new_node))
        
        return result