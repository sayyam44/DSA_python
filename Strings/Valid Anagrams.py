# https://leetcode.com/problems/valid-anagram/
# Input: s = "anagram", t = "nagaram"
# Output: true

#Easy Approach 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        
        # Count the occurrences of each stone
        for i in s:
            if i not in dic:
                dic[i] = 1  # Initialize the count to 1 if the stone is not in the dictionary
            else:
                dic[i] += 1
        
        for c in t:
            if c not in dic or (dic[c]<=0):
                return False
            dic[c]-=1
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a,b={},{} 
        for i in range(len(s)):
            # if s[i] not in a:
            #     a[s[i]]=1
            # else:
            #     a[s[i]]+=1 same method below 
            a[s[i]]=1+a.get(s[i],0)
            b[t[i]]=1+b.get(t[i],0)

        for j in a:
            if a[j]!=b.get(j,0): #checking the counts of each alphabet
                return False
            return True

