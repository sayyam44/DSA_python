# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Brute Force Approach (tc-n2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        max_val=-1
        for i in range(len(s)):
            dict={} #storing key,value pairs as key be the charater and 
            # value be 1 if present in that substring
            for j in range(i,len(s)):
                if s[j] in dict:
                    max_val=max(max_val,j-i)
                    break
                dict[s[j]]=1
        return max_val
    
#Optimized solution (2 Pointers approach)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Take 2 pointers l,r at 0
        #keep l steady and move r ahead by 1 step 
        #if str[r] is not present in the dictionary then update maxlength = r-l+1 and add 
        # str[r]-->r in the dictionary
        #if str[r] is present in the dictionary at r index and also this r should be greater 
        # than l then move l->r+1 and update the r as we have found this character again.
        mpp = [-1] * 256
        left = 0
        right = 0
        n = len(s)
        length = 0
        while right < n:
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])] + 1, left)
            mpp[ord(s[right])] = right
            length = max(length, right - left + 1)
            right += 1
        return length







 




