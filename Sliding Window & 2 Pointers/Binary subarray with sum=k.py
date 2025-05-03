# updated new
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
#if at anypoint we find the sum>goal then make the sum in control by 
# subtratcing value at l index from sum and moving l ahead 
class Solution(object):
    def atMost(self, nums, goal):
        if goal < 0:
            return 0
        l, curr_sum, cnt = 0, 0, 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum > goal:
                curr_sum -= nums[l]
                l += 1
            cnt += (r - l + 1)  # Counts all subarrays with sum ≤ goal
        return cnt

    def numSubarraysWithSum(self, nums, goal): 
        # Subarrays with sum exactly goal=Subarrays with sum ≤ goal−Subarrays with sum ≤ goal - 1
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
