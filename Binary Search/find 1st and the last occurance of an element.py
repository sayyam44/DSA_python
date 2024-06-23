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

class Solution(object):
    def firstpos(self,nums,target):
        first=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1 #to move out of the loop 
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first
    def secondpos(self,nums,target):
        second=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                second=mid
                low=mid+1 #to move out of the loop
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return second
    def searchRange(self, nums, target):
        first=self.firstpos(nums,target)
        second=self.secondpos(nums,target)
        #if the first is -1 then it is for sure that we are not gonna get 
        #its second occurence so directly return [-1,-1] saving logn time 
        return [first,second] if first != -1 else [-1,-1]      
        

solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(solution.searchRange(nums, target)) 