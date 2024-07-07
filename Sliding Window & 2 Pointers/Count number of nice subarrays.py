# https://leetcode.com/problems/count-number-of-nice-subarrays/

# Given an array of integers nums and an integer k. A continuous subarray 
# is called nice if there are k odd numbers on it.

#this is similar to count the number of subarrays with sum==k
#here just consider 1s instead of odd numbers
#and consider 0s instead of even numbers.

class Solution(object):
    def new_func(self, nums, goal):
        if goal<0:
            return 0
        l,r=0,0
        cnt=0
        add=0
        while r<len(nums):
            #if odd number then add 1 and if even number then add 0
            add+=(nums[r]%2)
            while add>goal:
                #if odd number then sub 1 and if even number then sub 0
                add-=(nums[l]%2)
                l+=1
            cnt+=(r-l+1)
            r+=1
        return cnt
    def numberOfSubarrays(self, nums, goal):
        return self.new_func(nums,goal)-self.new_func(nums,goal-1)
        