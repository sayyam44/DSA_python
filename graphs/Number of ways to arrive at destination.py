# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
# https://www.youtube.com/watch?v=_-0mx0SmYxA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=40
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/

import heapq,defaultdict
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph_new = defaultdict(list)  # from -> (to, weight)
        for frm, to, weight in roads:
            graph_new[frm].append([to, weight])
            graph_new[to].append([frm, weight])

        visited = [float('inf')] * n
        visited[0] = 0  # Start node has a distance of 0
        minH = [(0, 0)]  # Min-heap: (distance, node)
        ways = [0] * n
        ways[0] = 1  # There is one way to reach the start node

        while minH:
            dist, node = heapq.heappop(minH)

            # Traverse all neighbors of the current node
            for neighbor, weight in graph_new[node]:
                new_dist = dist + weight

                # If a shorter path to the neighbor is found
                if visited[neighbor] > new_dist:
                    visited[neighbor] = new_dist
                    ways[neighbor] = ways[node]  # Reset the number of ways to reach this neighbor
                    heapq.heappush(minH, (new_dist, neighbor))

                # If an equal distance path to the neighbor is found
                elif visited[neighbor] == new_dist:
                    ways[neighbor] += ways[node]  # Increment the number of ways to reach this neighbor

        return ways[n - 1] % (10**9 + 7)