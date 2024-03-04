class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        i=0
        while i<a:
            nums.remove(0)
            nums.append(0)
            i+=1
        return nums
            
