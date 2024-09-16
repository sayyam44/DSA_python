# https://leetcode.com/problems/combination-sum/description/
# TC=2^target as the height of the tree is equal to the target
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        #curr is a list that holds the elements in the current subset that we 
        #are considering
        #total holds the sum of this curr subset
        def dfs(ind,curr,total):
            if total==target:
                final.append(curr.copy())
                return 
            if ind>=len(candidates) or total>target:
                return 

            curr.append(candidates[ind])
            #below the ind remain the same as the same element can be added
            #into the curr list many times
            #also since we are considering this element then we need to add it into the total
            dfs(ind,curr,total+candidates[ind])
            
            curr.pop() #this is because we will not consider this popped element
            #ever in out tree
            #now in the dfs call we are moving to the next index 
            #but the total remains the same as we have already added this element into the total
            dfs(ind+1,curr,total)

        dfs(0,[],0)
        return final