# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
                
        for key,value in h.items():
            if value==1:
                return s.index(key)
        return -1