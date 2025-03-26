# updated
# https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1

#This ques can be assumed as maximum length of the subarray with atmost of
#2 types of fruits

#Brute force approach, tc=n2
#I will put elements in set when the length of the set increases more than 2
# then break if no then find the new max_length
class Solution:
    def sumSubarrayMins(self, N, fruits):
        max_len=0
        for i in range(N):
            set_new=set()
            for j in range(i,N):
                set_new.add(fruits[j])
                if len(set_new)<=2:
                    max_len=max(max_len,j-i+1)
                else:
                    break
        return max_len

#Optimized solution
#Take 2 pointer l and r 
#move r pointer towards right and increase its occurance in dict by 1 
#if the size of dict is more than k that means we have more than 2 types of fruits
#so now we will move left pointer towards right and decrease the occurance of l
# l index value by 1 in dict , if someone's value in dict becomes 0 then 
# delete that from dict
class Solution:
    def sumSubarrayMins(self, N, fruits):
        dic={}
        l=0
        r=0
        max_len=0
        while r<N:
            if fruits[r] in dic:
                dic[fruits[r]]+=1
            else:
                dic[fruits[r]]=1
            while (len(dic)>2):
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:
                    del dic[fruits[l]]
                l+=1
            if len(dic)<=2:
                max_len=max(max_len,r-l+1)
            r+=1
        return max_len