# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

#step1-find out which side of the mid element is sorted
#step2-find the min element from the sorted side of the array
#step3-now move low or high pointer accordingly
class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1
        val=float('inf')

        while low<=high:
            mid=(low+high)//2
            #this case is when we get some search space that is sorted 
            #in that case the arr[low] will be the lowest value
            if (nums[low]<nums[high]):
                val=min(val,nums[low])
                break

            if nums[low]<=nums[mid]: #if left side is sorted
                val=min(val,nums[low])
                low=mid+1
            else:
                val=min(val,nums[mid])
                high=mid-1
                
        return val
        

        