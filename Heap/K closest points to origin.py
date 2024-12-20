# https://leetcode.com/problems/k-closest-points-to-origin/description/
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i,j in points:
            dist=i*i+j*j
            heapq.heappush(heap,(dist,[i,j]))
        
        final_lst=[]
        for i in range(k):
            i,point_req=heapq.heappop(heap)
            final_lst.append(point_req)
        return final_lst

