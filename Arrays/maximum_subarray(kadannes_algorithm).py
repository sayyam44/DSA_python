# Updated new
# https://leetcode.com/problems/maximum-subarray/
#    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#    Output: 6
#    Explanation: [4,-1,2,1] has the largest sum = 6.
#kadane's algorithm --
# At each step, decide whether to include the current element in the existing subarray or start a new subarray.
#optimized solution
#tc=n,sc=1(THIS CODE DOESNT WORK IF WE HAVE ALL THE NEGATIVE VALUES IN THE ARRAY)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maxi=float("-inf")
        for i in nums:
            s+=i
            maxi=max(maxi,s)
            if s<0:
                s = 0 #sum with negative value will be of no use in making the sum to be max so make it = 0,if it is<0
        return maxi


  #brute-force method[THIS CODE WORKS]
    #tc=n2,
    # def maxSubArray(nums):
    #     maxi=float('-inf')
    #     for i in range(len(nums)):
    #         summ=0
    #         for j in range(i,len(nums)):
    #             summ+=nums[j]
    #             maxi=max(maxi,summ)
    #     return maxi
