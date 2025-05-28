# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# updated new
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        mini=float("inf")
        while l<=h:
            mid=(l+h)//2
            if nums[l]<=nums[mid]:
                mini=min(mini,nums[l])
                l=mid+1
            elif nums[h]>=nums[mid]:
                mini=min(mini,nums[mid])
                h=mid-1
        return mini
