# updated new
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#Given a binary array nums and an integer k, return the maximum number of 
# consecutive 1's in the array if you can flip at most k 0's.

#We can change the ques to maximum length subarray with atmost k 0's.

#Brute force approach (tc=n2)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length=0
        for i in range(len(nums)):
            count_zeroes=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    count_zeroes+=1
                elif count_zeroes<=k: #this includes the case when nums[j]==1
                    length=j-i+1
                    max_length=max(max_length,length)
                else:
                    break
        return max_length


#Optimized approach (tc=2n)-> for 2 while loops 
#Sliding window approach 
#move the right pointer one by one towards right and count the no. of 0s
#if the number of zeroes increases more than k then move the left pointer 
#towards right such that if it counter any 0 then reduce the count of zeroes
#till the time zeroes>k 
#everytime zeroes count < k , i will calculate the new legth and hence find 
#max length
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len=0
        left=0
        right=0
        zeroes=0
        while right<len(nums):
            if nums[right]==0:
                zeroes+=1
            while (zeroes>k):
                if nums[left]==0:
                    zeroes-=1
                left+=1
            if (zeroes<=k):
                length=right-left+1
                max_len=max(max_len,length)
            right+=1
        return max_len
