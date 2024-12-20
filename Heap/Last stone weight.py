# updated
# https://leetcode.com/problems/last-stone-weight/
#since we cannot directly implement max heaps in python so we 
# will use min heap for that case by multiplying 
# each element of the min heap by -1 and will focus on the min 
# values and not on the max values

#tc= nlogn---logn for finding tha max value in the max heap and making its collision so for n 
#elements we have tc=nlogn
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            first=heapq.heappop(stones) #poping the 1st smallest value
            second=heapq.heappop(stones) #poping the 2nd smallest value
            #if first=second then remain as it is as we need to pop them only 
            if second>first: #first=-8,second=-7
                heapq.heappush(stones,first-second) #as first-second will give -1 and thats what we want , negative of the number
        stones.append(0) #append 0 into the stones everytime because if stones is empty it will return 0
        return abs(stones[0]) #abs because we need a positive value
        
                
            