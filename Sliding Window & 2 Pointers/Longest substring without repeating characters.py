# updated new
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Brute Force Approach (tc-n2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst=[]
        max_len=0
        for i in s:
            if i not in lst:
                lst.append(i)
            else:
                max_len=max(len(lst),max_len)
                lst=[i]
        return max_len

    
#Optimized solution (2 Pointers approach)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        max_len=0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]]>=l:
                l=dic[s[r]]+1
            dic[s[r]]=r
            max_len=max(max_len,r-l+1)
        return max_len