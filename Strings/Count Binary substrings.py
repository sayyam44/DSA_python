# https://leetcode.com/problems/count-binary-substrings/
# Input: s = "00110011"
# Output: 6
#"0011", "01","1100", "10", "0011", and "01".

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans,prev,curr=0,0,1
        #prev stores the number of values that are same in the previous set.
        #curr stores the number of values that are same in the curent set.
        #and current is initially set to be 1 because initially atleast one
        # of the char is same and we are
        #starting from 1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                ans+=min(prev,curr) #binary substrins will always be the min of the 2 continoust
                # substrings of 0's and 1's eg for 0000111 ans=3
                prev=curr
                curr=1
            else:
                curr+=1
        ans+=min(prev,curr) #this is if i reaches the len(s) 
        return ans
