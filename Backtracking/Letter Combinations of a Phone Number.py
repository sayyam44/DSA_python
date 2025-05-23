# updated new
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#TC= 4^n (n-> length of given string (digits))
class Solution:
    def letterCombinations(self, digits):
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
        curr=[]
        def dfs(ind):
            if len(curr)==len(digits):
                res.append("".join(curr))
                return 
            for c in digitToChar[digits[ind]]:
                curr.append(c)
                dfs(ind+1)
                curr.pop()
        if digits:
            dfs(0)
        return res