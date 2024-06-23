# https://leetcode.com/problems/search-insert-position/description/
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