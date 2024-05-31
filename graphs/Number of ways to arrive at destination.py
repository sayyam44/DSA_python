# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
import heapq
def count_paths(n, edges):
	graph = [[] for _ in range(n+1)]

	for edge in edges:
		graph[edge[0]].append([edge[1], edge[2]])
		graph[edge[1]].append([edge[0], edge[2]])

	dis = [float("inf")] * n
	path = [0] * n
	minH = [(0, 0)]
	dis[0] = 0
	path[0] = 1
	while minH:
		curr_dist,curr_node=heapq.heappop(minH)
		for nei in graph[curr_node]:
			nei_node,nei_dist=nei
			if dis[nei_node]>curr_dist+nei_dist:
				dis[nei_node]=curr_dist+nei_dist
				path[nei_node]=path[curr_node]
				heapq.heappush(minH,(dis[nei_node],nei_node))
			elif dis[nei_node]==curr_dist+nei_dist:
				path[nei_node]+=path[curr_node]

	return path[n-1]

n = 7
edges = [
	[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
	[3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]
]
num_paths = count_paths(n, edges)
print("Number of paths from 0 to {}: {}".format(n-1, num_paths))
