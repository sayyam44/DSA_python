# https://leetcode.com/problems/search-insert-position/description/
# Given a sorted array of distinct integers and a target value, return 
# the index if the target is found. If not, return the index where it 
# would be if it were inserted in order.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        return low #because if we never find the value then 
    # the required value will be always on left of mid.