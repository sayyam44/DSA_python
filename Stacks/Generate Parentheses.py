# https://leetcode.com/problems/generate-parentheses/
#using recursion method
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack=[] #creating stack in order to store opening or closing parenthesis for each iteration , 
        #eg, ["(","(",")",")"]
        res=[] #for final result 
        def backtrack(openn,closee):#openn and closee is the count of open and close parenthesis begin from 0,0
            
            if openn==closee==n:#thi means we have reached the end of one combination
                res.append("".join(stack))
                return 
            
            if openn<n:
                stack.append("(")
                backtrack(openn+1,closee)#since we have added an open parenthesis now call the backtrack 
                #function by incrementing the count of open by 1  
                stack.pop() #this is because we have defined stack as a global parameter and we will store 
                #each parentheses for each iteration seperately so after appending all the parentheses in 
                # each iteration we will pop that full iteration
                
            if closee<openn:
                stack.append(")")
                backtrack(openn,closee+1)
                stack.pop()
            
        backtrack(0,0)
        return res