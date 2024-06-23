# Same as find 1st and last occurance of an elemnt just subtract the second occurance - first occurane
# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-occurrence
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
    def countduplicates(self, nums, target):
        first=self.firstpos(nums,target)
        second=self.secondpos(nums,target)
        #if the first is -1 then it is for sure that we are not gonna get 
        #its second occurence so directly return [-1,-1] saving logn time 
        return (second-first) if first != -1 else -1     
        
solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(solution.countduplicates(nums, target)) 
