# Updated new
# https://leetcode.com/problems/daily-temperatures/
#tc=n*n,sc=n
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#create a stack which will append the temp,its index if the iterated temp value is greater than the 
# stack's top value
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res=[0]*len(temps)
        stack=[]
        for i,temp in enumerate(temps):
            while stack and temp>stack[-1][0]:
                t,ind=stack.pop()
                res[ind]=(i-ind)
            stack.append([temp,i])
        return res
