# https://leetcode.com/problems/rearrange-array-elements-by-sign/
# updated - 1
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            if i>0:
                pos.append(i)
        ans=[]
        for i in range(len(nums)//2):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans