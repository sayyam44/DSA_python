# updated new
# https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation
# https://www.youtube.com/watch?v=jtSiWTPLwd0
# Almost same as find min in rotated sorted array
#To check how many times the array ha been rotated we need to find 
#the index of the min element in that array
from typing import List

class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        mini = float("inf")
        min_ind = -1

        while l <= h:
            mid = (l + h) // 2

            # If the array is already sorted, return the first element's index
            if nums[l] <= nums[h]:
                if nums[l] < mini:
                    mini = nums[l]
                    min_ind = l
                return min_ind  

            # Check if mid is the minimum element
            if nums[mid] < mini:
                mini = nums[mid]
                min_ind = mid

            # If left half is sorted, the pivot is on the right
            if nums[l] <= nums[mid]:  
                l = mid + 1
            else:  
                h = mid - 1

        return min_ind  # Returns index of the minimum element

# Example Usage
sol = Solution()
arr = [5, 1, 2, 3, 4]
print(sol.findMinIndex(arr))  # Output: 1 (index of 1)
