# Updated new
# https://leetcode.com/problems/task-scheduler/description/
 
from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts=Counter(tasks)
        max_heap=[-val for val in task_counts.values()]
        heapq.heapify(max_heap)

        q=deque()
        time=0
        while max_heap or q:
            time+=1
            if max_heap:
                freq=1+heapq.heappop(max_heap) #freq=how many times the current elements need to be resolved yet
                if freq:
                    q.append([freq,time+n])#time + n = after how long this element can be used again
            if q and q[0][1]==time:
                left_freq=q.popleft()[0]
                heapq.heappush(max_heap,left_freq)
        return time
            