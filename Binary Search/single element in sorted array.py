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
#The speacial property of the single element in the array is that the 
#elements in the left side of this single element should be odd,even format
#and the elements in the right side of this single element should be in 
#even,odd format

#step1- remove the base conditions 
#step2- find the mid and check if the mid is the single element or not by
#using 3 pointers
#step3-if its not then check this mid is on left half or right half of the 
#single element, using the same odd,even approach depending upon the index
#of the mid element and the previous or next index it is equal to

class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums)==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[-2]!=nums[-1]:
            return nums[-1]
        low=1
        high=len(nums)-2
        while low<=high:
            mid=(low+high)//2
            #now checking if mid is the single element or not
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid] #this is the single element

            #now we need to check if this mid is on left side or right side 
            # of the single element
            elif (mid%2==1 and (nums[mid-1]==nums[mid])) or (mid%2==0 and (nums[mid+1]==nums[mid])):
                low=mid+1 #eliminating the left half of mid
            else: #we are on the right half of the single element
                high=mid-1
        return -1
                


                
