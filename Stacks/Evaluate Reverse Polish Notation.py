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
            if i == '+':
                stack.append(int(stack.pop())+int(stack.pop()))
            elif i=='*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i=='-':
                a,b=int(stack.pop()),int(stack.pop())
                stack.append(b-a)
            elif i=='/':
                a,b=int(stack.pop()),int(stack.pop())
                stack.append(b/a)
            else:
                stack.append(i)
        return int(stack[0])