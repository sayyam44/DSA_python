# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
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
