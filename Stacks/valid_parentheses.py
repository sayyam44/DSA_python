# updated
# Input: s = "()[]{}"
# Output: true
#tc=n,sc=n
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        paren={')':'(','}':'{',']':'['}
        for p in s:
            if p not in paren:
                stack.append(p)
            else:
                if stack and stack[-1]==paren[p]:
                    stack.pop()
                else:
                    return False
        return not stack