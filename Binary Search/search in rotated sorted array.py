# updated new
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

#ALL THE VALUES ARE UNIQUE IN THE ARRAY

#step1- In this type of ques one side of the mid either left side or the 
#right side of the mid will be sorted then firstly find which side is the sorted side

#step2- Check if the target is present in the sorted side or not if yes
#then search in that side, if no then search in the unsorted side

def search(nums, target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        #step 1 - checking if left side of the mid index is sorted or not
        elif nums[mid]>=nums[low]:
            #step2 - checking if the target value lies in the sorted side of array or not
            if target<=nums[mid] and target>=nums[low]:
                #if yes then discard the other side of the array
                high=mid-1
            else:
                low=mid+1
        else: #step-1 - here we are checking if right side of the mid index is sorted or not
            if target>=nums[mid] and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return -1



        


    