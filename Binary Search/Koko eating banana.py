# updated new
# https://leetcode.com/problems/koko-eating-bananas/
# Why binary search is applied in this ?
# eg- Input: piles = [3,6,7,11], h = 8 Output: 4
# In the above case we can see the pattern that all the possible 
# cases for eating bananas in 1 hour lies from 1 to 11 .
# And when we apply the solution we get to know that from 1 to 3 will not
# return the answer instead all the values from 4 to 11 can solve this ques
# we just return the minimum among all the possible cases here 4.
#now l=1 and h=11 and now check if mid is satisfying the condition 
# if yes then move the high at mid-1 as all the values above mid will
# be greater than mid but we need to find the minimum bananas that 
# can be eaten in one hour to complete all the piles within 8 hours.

# For these type of questions to solve with binary search find the minimum 
# and maximum of the range and make the array yourself.

#Brute force approach 
import math
class Solution(object):
    def time_by_eating_i_bananas(self,i,piles):#here we are calculating 
        #the number of hrs it will require to eat all the bananas if we eat
        #i bananas at atime
        hrs=0
        for j in range(len(piles)):
            hrs+=math.ceil(piles[j]/i)
        return hrs
        
    def minEatingSpeed(self, piles, h):
        for i in range(1,max(piles)+1): #In 1 hr we can eat min of 1 banana or max of max(piles) bananas
            hrs_req=self.time_by_eating_i_bananas(i,piles)
            if (hrs_req<=h):
                return i
        return -1
    

#Binary search
from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        h=max(piles)
        
        while l<=h:
            mid=(l+h)//2
            curr_hrs=self.hrs_calculate(piles,mid)
            if curr_hrs<=h:
                h=mid-1
            else:
                l=mid+1
        return l
    def hrs_calculate(self, piles: List[int], b: int) -> int:
        # Calculates the number of hours required to eat all bananas at speed b
        totalH = 0
        n = len(piles)
        for i in range(n):
            totalH += math.ceil(piles[i] / b)
        return totalH

    