# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


#TC= 4^n (n-> length of given string (digits))
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtrack(i,curr): #i->digits, curr->current string
            if len(curr)==len(digits):
                res.append(curr)
                return 
            
            for j in digitToChar[digits[i]]:
                backtrack(i+1,curr+j)
                # curr=curr[:-1]

        if digits:
            backtrack(0,"")

        return res

        # there's no append or pop (similar to the other backtracking 
        # approaches) it's because strings are immutable. Everytime 
        # the call is made to the backtrack method, python creates a 
        # new string so when the method returns up the stack, the 
        # caller still has the original string without the concatenated letter.