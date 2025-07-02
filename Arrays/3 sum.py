# updated new
# https://leetcode.com/problems/3sum/
# https://www.youtube.com/watch?v=jzZsG8n2R9A
# updated new
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

#tc=nlogn+n2=n2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                #in order to remove the same triplets in beginnings
                continue
            l, r = i + 1, len(nums) - 1 #now we have reduced our problem to 2 sum problem
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        #we are doing this step only in else case where we have already found a solution 
                        #as we dont want the same solutions more than once and we are not doing this in 
                        #the above if and ifelse because the pointer will eventually be moved accordingly.
                        l += 1
        return res

