#https://www.youtube.com/watch?v=Fm_p9lJ4Z_8&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=44
#tc=n,sc=1
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #using 2 pointer method
        start = 0 #1st pointer
        if len(nums) == 0: return 0
        for i in range(1,len(nums)):
            if nums[start] != nums[i]:
                start += 1
                nums[start] = nums[i]
        return nums[:start+1]

#brute force method - sc=n
def rd(nums):
    if len(nums)==0: return 0
    lst=[nums[0]]
    for i in nums[1:]:
        if i not in lst:
            lst.append(i)


                

