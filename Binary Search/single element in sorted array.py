# updated new
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

#brute force approach 
class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
        
        return None
            
#USING BINARY SEARCH
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                l=mid+2
            else:
                h=mid
        return nums[l]
