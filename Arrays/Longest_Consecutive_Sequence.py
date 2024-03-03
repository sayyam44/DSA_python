# https://leetcode.com/problems/longest-consecutive-sequence/
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


def longestConsecutive(nums):
    #sc=n,tc=n(as req)
    # we will iterate through the set and will check for each number whether it have a left neighbour(x-1)
    # or not , if it does not have left neighbor then start a sequence from that number and end the 
    # sequence where it stop finding its right neighbor also x+1,...x+n
    longest=0
    numSet=set(nums) #set always retruns sorted values
    
    for n in numSet:
        #check if its the start of the sequence
        if (n-1) not in numSet:# by doing n-1 clearly shows this is gonna be the beginning of some subset 
            #but if we do n+1 then that then that doesnt show it is beginniing of some required subset or not
            #this is for the 2nd time we perform iteration we will go directly to an element
            #that is not a part of previous length
            length=0 #1st case 
            while (n+length) in numSet:
                length+=1
            longest=max(length,longest)
    return longest



