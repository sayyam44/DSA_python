# https://leetcode.com/problems/maximum-subarray/
def maxSubArray(nums):
#    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#    Output: 6
#    Explanation: [4,-1,2,1] has the largest sum = 6.

    #kadane's algorithm(in copy)
    #optimized solution
    #tc=n,sc=1(THIS CODE DOESNT WORK IF WE HAVE ALL THE NEGATIVE VALUES IN THE ARRAY)
    s = 0 
    max_sum = float('inf')
    for i in range(len(nums)):
        s+=nums[i]
        if s<0:
            s = 0 #sum with negative value will be of no use in making the sum to be max so make it = 0,if it is<0
        if s>max_sum:
            max_sum=s
    return max_sum

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
