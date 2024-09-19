# https://leetcode.com/problems/permutations/
# TC= n! * n2
# SC=n!*
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]] #base case 
        for n in nums: #for each element that needed to be inserted
            new_perms=[]
            for p in perms: #for each permutation where we need to insert this element
                for i in range(len(p)+1): #the position in p where we want to insert element n
                    p_copy=p.copy()
                    p_copy.insert(i,n) #as we need to make changes in the already 
                    #existing permutation
                    new_perms.append(p_copy)
                perms=new_perms
            return perms

