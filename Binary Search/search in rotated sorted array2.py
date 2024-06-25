# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#This ques is same as search in rotated sorted array but here we can have 
#Duplicate values in the list

#This won't work in the case where array=[4,2,3,4,4,4,4],here mid=low=high

#Solution - if arr[mid]=arr[low]=arr[high] then if target is != arr[mid] then
#shrink the search space by making low+=1 and high-=1

def search(self, nums, target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        #only this special case is added 
        elif nums[low]==nums[mid]==nums[high]: 
            low+=1
            high-=1
            continue #because if after shrinking the range again we get 
                     #same case where all 3 are equal then we need not to 
                     #waste time
        elif nums[mid]>=nums[low]:
            if target<=nums[mid] and target>=nums[low]:
                high=mid-1
            else:
                low=mid+1
        else:
            if target>=nums[mid] and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return False