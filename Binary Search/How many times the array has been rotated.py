# https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation
# https://www.youtube.com/watch?v=jtSiWTPLwd0
# Almost same as find min in rotated sorted array
#To check how many times the array ha been rotated we need to find 
#the index of the min element in that array

class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1
        val=-1
        idx=-1

        while low<=high:
            mid=(low+high)//2
            #this case is when we get some search space that is sorted 
            #in that case the arr[low] will be the lowest value
            if (nums[low]<nums[high]):
                if nums[low]<val:
                    idx=low
                    val=nums[low]
                break

            elif nums[low]<=nums[mid]: #if left side is sorted
                if nums[low]<val:
                    idx=low
                    val=nums[low]
                low=mid+1
            else:
                if nums[mid]<val:
                    idx=mid
                    val=nums[mid]
                high=mid-1
                
        return idx