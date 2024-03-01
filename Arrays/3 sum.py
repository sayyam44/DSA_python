# https://leetcode.com/problems/3sum/
# https://www.youtube.com/watch?v=jzZsG8n2R9A

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
                        #e are doing this step only in else case where we have already found a solution 
                        #as we dont want the same solutions more than once and we are not doing this in 
                        #the above if and ifelse because the pointer will eventually be moved accordingly.
                        l += 1
        return res



# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #best approach(tc=n*n), sc=m for storing triplets
        #b+c=-a
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: # this condition is for not finding the triplet for the same value again
                continue 
            a=nums[i]*-1
            low=i+1 #just the next index of a
            high=len(nums)-1 #the last index of nums
            
            while low<high:          
                if nums[low]+nums[high]== (a): #b+c== -a
                    result.append([nums[i],nums[low],nums[high]])
                    low+=1
                    while low<high and nums[low]==nums[low-1]:
                        low+=1 #when we find a triplet then move the low pointer to the next index that is not equal to the previous value of low
                   
                elif nums[low]+nums[high]<(a):
                    low+=1 
                else:
                    high-=1
        return result
            
        
            
        
        #bruteforse 
        # use 3 loops for finding i,j,k and put it in set for uniques sol, tc=n3*logm(for putting all 3 in set),sc=m
        
        #better approach-use hashing 
        #hash app the numbers in nums into a hashmap along with their occurences eg, (-1,2),(0,1),......
        #for i in range(0,len(nums)):
        #hash(nums[i])-- (decrease a count by one for i value)
        #for j in range (i+1,len(nums)):
        #hash(nums[j])-- (decrease a count by one for j value)
        # now find a number in hash table with value ==                 -(a[i]+a[j])
        #if we get the value with count at least 1 then reducethe values's count by 1 in hash table and put this triplet into a set for sorting each triplet like this 
        #tc=n2*logm(for inserting inti set)
        #sc=m+n


