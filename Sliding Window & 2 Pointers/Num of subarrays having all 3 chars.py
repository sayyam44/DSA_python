# updated
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

#Brute force-n2
class Solution(object):
    def numberOfSubstrings(self, s):
        count=0
        for i in range(len(s)):
            hash_set={i:0 for i in range(3)} #0 for a,1 for b, 2 for c
            for j in range(i,len(s)):
                hash_set[ord(s[j])-ord('a')]=1 #i am not calculating the 
                # number of occurances here instead i ma calculating 
                # wheather that char has occured in that substring or not
                if hash_set[0]+hash_set[1]+hash_set[2]==3:
                    count+=(len(s)-j) #so the thing is when at some jth 
                    #position we get the sum==3 that means after 
                    #that jth position upto the len(s) this condition is 
                    #gonna be true so break after this
                    break
        return count


#optimized solution
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        cnt = 0
        dc = {}
        for r in range(len(s)):
            dc[s[r]] = dc.get(s[r], 0) + 1  # Increment character count

            while len(dc) == 3:  # Valid substring condition
                dc[s[l]] -= 1
                if dc[s[l]] == 0:
                    del dc[s[l]]  # Remove key if count is zero
                l += 1
            cnt += l  # Count valid substrings
        return cnt

 