# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=UXDSeD9mN-k
#updated new
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

#tc=nlogn,sc=n
#As we iterate through the list 1stly check whether that value is present in the hashmap or not, if not then 
#use a hashmap to store (value,index) 
#if yes then return both the indices whose sum is equal to the target.

def sum(lst,target):
    dict={}
    for ind,val in enumerate(lst):
        find=target-val
        if find in dict:
            return (dict[find],ind)
        dict[val]=ind

