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

# Go opposite 
# With every character there is a substring that ends with that char
# Begin with a=-1,b=-1,c=-1 , these all represent the last seen index of a,b,c
# move the i pointer update the values of above variables
class Solution(object):
    def numberOfSubstrings(self, s):
        last_seen={i:-1 for i in range(3)} #last seen indices of a,b,c
        cnt=0
        for i in range(len(s)):
            last_seen[ord(s[i])-ord('a')] = i #updating the last seen of ith char
            if (last_seen[0]!=-1 and last_seen[1]!=-1 and last_seen[2]!=-1): 
                #this means we have all the three chars in this substring ending with 
                #jth index value 
                #now i will find the min of all the 3 occurances till now 
                #that means the elements to the left of the min occurance index
                #will be also parts of the subarray having all 3 chars
                cnt+=(1+min(last_seen[0],last_seen[1],last_seen[2]))
        return cnt

 