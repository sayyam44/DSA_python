# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=UXDSeD9mN-k
#updated
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

#1st brute force=tc=nlogn,sc= almost 0
def sum(lst,target):
    lst.sort()
    start=0
    end=len(lst)-1
    while start<=end:
        if (lst[start]+lst[end])>target:
            end-=1
        elif (lst[start]+lst[end])<target:
            start+=1
        else:
            lstfinal=[lst[start],lst[end]]
            return lstfinal
    return 

        
#brute force method 
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

