# updated
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
#tc=E*K

class Solution:
    def findCheapestPrice(self,n, flights, src, dst, k):
        prices=[float("inf")]*n
        prices[src]=0
        
        for i in range(k+1): #k means number of stops so 1stly do for k=0 that is no stop then do for k+1=1 that is 1 stop at max
            temp=prices[:]
            
            for src,dst,price in flights: #here it is doing bfs s#s=source,d=destination,p=price (weight)
                if prices[src]!=float("inf"):# we only relax an edge (src->dst) if we have already found a valid cost to reach node src.
                    temp[dst]=min(temp[dst],prices[src]+price)

            # Update prices after processing all edges in this iteration
            prices=temp
        return prices[dst] if prices[dst] != float('inf') else -1

solution = Solution()

# Example graph: 3 cities (0, 1, 2), with edges (src, dst, price)
n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1

# Find the cheapest price from src to dst with at most k stops
result = solution.findCheapestPrice(n, flights, src, dst, k)
print(f"Cheapest price: {result}")  



#USING DIJKISTRA'S Algorithm 
from collections import defaultdict, deque
import math

def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    
    queue = deque([(0, src, 0)]) #(stops, current_city, cost)
    dist = [math.inf] * n
    dist[src] = 0
    
    while queue:
        stops, current_city, cost = queue.popleft()
        
        if stops <= k:
            for neighbor, weight in graph[current_city]:
                next_cost = cost + weight
                if next_cost < dist[neighbor]:
                    dist[neighbor] = next_cost
                    queue.append((stops + 1, neighbor, next_cost))
    
    return dist[dst] if dist[dst] != math.inf else -1
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))  

