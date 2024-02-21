#^^^^^COPY^^^^^^
# https://leetcode.com/problems/valid-parentheses/
# Input: s = "()[]{}"
# Output: true
#tc=n,sc=n
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={")":"(","]":"[","}":"{"} #keys are closing and vals are opening brackets
        
        for c in s:
            if c not in closetoopen: #if c is not any closing bracket
                stack.append(c)
                continue
            if not stack or stack[-1]!=closetoopen[c]: #the corresponding value of c in close to open must be same as stack's top value
                return 0
            stack.pop()
        return not stack #RETURN TRUE IF STACK IS EMPTY

#method is same as above but this is bit easier
class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        stack=[]
        for i in s:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                if not stack: 
                    return 0
                pos=close_list.index(i)
                if (stack.pop()!=open_list[pos]):
                    return 0
            else:
                return 0
        return not stack 