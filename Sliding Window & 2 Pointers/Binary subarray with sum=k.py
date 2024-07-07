#count subarrays with sum=k
# https://leetcode.com/problems/binary-subarrays-with-sum/

#brute force approach
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt_sub=0

        for i in range(len(nums)):
            add=0
            for j in range(i,len(nums)):
                add+=nums[j]
                if add==goal:
                    cnt_sub+=1
                elif add>goal:
                    break
        return cnt_sub
    
#optimized solution (tc=2n,sc=1)
#1st i am counting the number of subarrays with sum<=k
#step1-if sum is < goal then add all the possible subarrays with the subarray
#length of (r-l+1)
#if at anypoint wew find the sum>goal then make the sum in control by 
# subtratcing value at l index from sum and moving l ahead 
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal<0:
            return 0
        l,r=0,0
        cnt=0
        add=0
        while r<len(nums):
            sum+=nums[r]
            if sum>goal:
                while sum>goal:
                    sum-=nums[l]
                    l+=1
            elif sum<=goal:
                cnt+=(r-l+1) #important thing to notice as we are adding all
                #the subarrays now from r till l
            r+=1
        return cnt


#now to get the subarrays with sum == k we will subtract the 
#function(nums,goal) - function(nums,goal-1)
#function(nums,goal) => It will give all the subarrays with sum <=goal
#function(nums,goal-1) => It will give all the subarrays with sum <=goal-1
#subtraction of this will give us the required no. of subarrays with = goal.
# tc=2x2n , sc=1

class Solution(object):
    def new_func(self,nums,goal):
        if goal<0:
            return 0
        l,r=0,0
        cnt=0
        add=0
        while r<len(nums):
            add+=nums[r]
            while add>goal:
                add-=nums[l]
                l+=1
            cnt+=(r-l+1)#important thing to notice as we are adding all
                #the subarrays now from r till l
            r+=1
        return cnt
    def numSubarraysWithSum(self, nums, goal):
        return self.new_func(nums,goal)-self.new_func(nums,goal-1)