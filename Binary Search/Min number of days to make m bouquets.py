# updated new
#For these type of questions to solve with binary search find the minimum 
# and maximum of the range of possible ouput values

# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

#BRUTE FORCE APPROACH
#TC= N*((max)-(min)+1)
class Solution:
    def new_func(self, bloomDay, day, m, k):
        flowers = 0  # this will tell how many flowers have bloomed in 'day' no. of days
        bouquets = 0
        for i in range(len(bloomDay)):
            if day >= bloomDay[i]:
                flowers += 1
                if flowers == k:
                    bouquets += 1 #abhi tak jitne flowers bane hain usse kitne boq ban sakte
                    flowers = 0 #from here we have to start making new boq
            else:
                flowers = 0

        return bouquets >= m #same thing for the last iteration
    
# Max of the array will surely give us the answer as till that time all the flowers will be bloomed
#The min of the array will atleat bloom 1 flower so range will be(min(arr),max(arr))

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:  # edge case when there are more flowers required than present
            return -1
        min_day = min(bloomDay)
        max_day = max(bloomDay)
        for day in range(min_day, max_day + 1):
            if self.new_func(bloomDay, day, m, k):
                return day
        return -1
    

#BINARY SEARCH
#TC= N*log((max)-(min)+1)
# Max of the array will surely give us the answer as till that time all the flowers will be bloomed
#The min of the array will atleat bloom 1 flower so range will be(min(arr),max(arr))

class Solution:
    def new_func(self, bloomDay, day, m, k):
        flowers = 0  # this will tell how many flowers have bloomed in 'day' no. of days
        bouquets = 0
        for i in range(len(bloomDay)):
            if day >= bloomDay[i]:
                flowers += 1
                if flowers == k:
                    bouquets += 1 #abhi tak jitne flowers bane hain usse kitne boq ban sakte
                    flowers = 0 #from here we have to start making new boq
            else:
                flowers = 0

        return bouquets >= m #same thing for the last iteration

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:  # edge case when there are more flowers required than present
            return -1

        low=min(bloomDay)
        high = max(bloomDay)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if self.new_func(bloomDay, mid, m, k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans #we could also return low
