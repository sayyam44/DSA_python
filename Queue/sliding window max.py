# updated new
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        d = collections.deque() 
        out = []
        for i, n in enumerate(nums): 
            while d and nums[d[-1]] < n: #nums[d[-1]] means the topmost element in dequeue from back 
                d.pop()
            d.append(i)
            if d[0] == i - k: #window out of range case here d[0] means the topmost element from front in deque
                d.popleft()
            if i>=k-1:
                out.append(nums[d[0]]) #as the elements are always stored in decreasing format in deque
                #so the elemets at the top of deque will alwys be the largest value 
        return out