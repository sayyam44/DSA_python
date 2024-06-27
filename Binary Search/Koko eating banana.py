# https://leetcode.com/problems/koko-eating-bananas/
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

import math

def findMax(v):
    maxi = float('-inf')
    n = len(v)
    # Find the maximum
    for i in range(n):
        maxi = max(maxi, v[i])
    return maxi

def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def minimumRateToEatBananas(v, h):
    low = 1
    high = findMax(v)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        totalH = calculateTotalHours(v, mid)
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")


