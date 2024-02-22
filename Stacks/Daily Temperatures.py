# https://leetcode.com/problems/daily-temperatures/
#tc=n*n,sc=n
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#create a stack which will append the temp,its index if the iterated temp value is not greater than the 
# stack's top value
class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        res=[0]*len(tem) #because we need to get 0 vals if we dnt find any greater values 
        # ahead of current val
        stack=[] #pair:[temp,index]
        for i,t in enumerate(tem):
            while stack and t>stack[-1][0]: #iterating till the stack is empty and till the stack's 
                # topmost value is smaller than the t(current value)
                stackT,stackI=stack.pop() #storing the temp,index value of the poped value
                res[stackI]=(i-stackI) #now storing the difference in the same index of the poped 
                # value in res
            stack.append([t,i])#if the current t is smaller than the previos vals
        return res
        