# updated new
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#brute force method
# def searchRange(nums, target):
#     first,last=-1,-1
#     lst=[]
#     for i in range(len(nums)):
#         if nums[i]==target:
#             if first==-1:
#                 first=i
#             last=i
#     return [first,last]

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(searchRange(nums, target))


#brute force approach - tc=n
# def searchRange(nums, target):
#     lst = [-1, -1]
#     for i in range(len(nums)):  
#         if nums[i] == target:
#             lst[0] = i
#             break

#     for i in range(len(nums) - 1, -1, -1):
#         if nums[i] == target:
#             lst[1] = i  
#             break
#     return lst

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(searchRange(nums, target))


# Optimized approach using binary search
# tc=log(n)

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# https://www.youtube.com/watch?v=hjR1IYVx9lY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=4
#brute force method
# def searchRange(nums, target):
#     first,last=-1,-1
#     lst=[]
#     for i in range(len(nums)):
#         if nums[i]==target:
#             if first==-1:
#                 first=i
#             last=i
#     return [first,last]

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(searchRange(nums, target))


#brute force approach - tc=n
# def searchRange(nums, target):
#     lst = [-1, -1]
#     for i in range(len(nums)):  
#         if nums[i] == target:
#             lst[0] = i
#             break

#     for i in range(len(nums) - 1, -1, -1):
#         if nums[i] == target:
#             lst[1] = i  
#             break
#     return lst

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(searchRange(nums, target))


# Optimized approach using binary search
# tc=log(n)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_func(nums,target,is_searching_left):
            low=0
            high=len(nums)-1
            ind=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ind=mid
                    if is_searching_left:
                        high=mid-1
                    else:
                        low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return ind
                
        
        left=search_func(nums,target,True)
        right=search_func(nums,target,False)

        return [left,right]