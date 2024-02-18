# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#https://www.youtube.com/watch?v=iu0082c4HDE
#tc=2n,sc=n
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i == "+":
                stack.append(stack.pop()+stack.pop())
            elif i == "*":
                stack.append(stack.pop()*stack.pop())
            elif i == "-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a) 
            elif i == "/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a)) #in order to round the decimal division(b/a) towards zero
            else:
                stack.append(int(i))
        return stack[0] #after all the process only single value will be left 