# https://leetcode.com/problems/longest-palindromic-substring/
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #we are checking palindrom from centre of the pamnlindrome eg for aba we are starting from b 
        # and taking a left pointer to b's left and a right pointer to b's right

        res=""
        res_len=0
        
        #for odd length of palindrome in the fiven string
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
            #moving l on left of current and moving r on right of current and also for a palindrome 
            # both these elements must be same 
                if r-l+1>res_len: #since we want to find the max len palindromic substring among all 
                    #the palindromic substrings present
                    res_len=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        #**********till now we have just found maximum length of palindrome that is odd odd length
        #for even length of palindrome in the fiven string
        for i in range(len(s)):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>res_len:  #since we want to find the max len palindromic substring among all 
                    #the palindromic substrings present
                    res_len=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res
        