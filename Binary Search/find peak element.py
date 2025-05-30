# https://leetcode.com/problems/find-peak-element/description/
# updated new

#step1- write code for the base cases (i.e for 1st and the last element)
#step2- point low at 1 and high at len-1
#step3-find mid element and check if the mid is the peak element or not
#step4-if not then check if this mid point is on the left side of the peak 
#or at the right side of the peak 
#for left side -> increasing slope -> arr[mid]<arr[mid+1] ->eliminate left side
#for right side -> decreasing slope -> arr[mid]>arr[mid-1] ->eliminate right side

class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)==1:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return (len(nums)-1)
        low=1
        high=len(nums)-2
        while (low<=high):
            mid=(low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            #now check if the mid lies on left of peak or right of peak
            elif nums[mid]<nums[mid+1]: #increasing slope
                low=mid+1
            else: #in case of decreasing slope or MULTIPLE PEAKS
                high=mid-1
        return -1

