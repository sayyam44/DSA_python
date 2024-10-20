#[1,3,2,0,2]= True
#[1,2,0,0,0]=False
#updated - 1
#we will take a parameter reachable initially be 0, now iterate through the array and check the maximum 
#jumps that can happen at that point and if after taking that much of jumps we reach to an index that 
# is greater than the reachable variable then update reachable= i+nums[i] or else reachable will remain 
# same and if at last reachable is == length of array then yes/True and if the pointer's index while
#  iterating the array is greater than the reachable variable then return False.

class Solution(object):
    def canJump(self, nums):
        n=len(nums)
        reachable=0 #reachable is basically the max point that we can reach before the ith point. 
        for i in range(n):
            if reachable < i: #here if reachable value is < i index
                return False
            reachable=max(reachable,i+nums[i]) #i+nums[i] because we are now at i and can have nums[i] jumps at max
        return True







