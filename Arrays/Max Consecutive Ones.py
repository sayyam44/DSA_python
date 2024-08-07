# Updated
# Input: nums = [1,1,0,1,1,1]
# Output: 3

#Brute force approach tc=n,sc=n
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        lst=[]
        for i in nums:
            if i==1:
                cnt+=1
                lst.append(cnt)
            if i!=1:
                cnt=0
        return max(lst)

#optimized approach tc=n,sc=1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxi=max(maxi,count)
                
            else:
                count=0
               
        return maxi




      