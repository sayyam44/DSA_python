# https://www.codingninjas.com/codestudio/problems/house-robber_839733
# https://leetcode.com/problems/house-robber-ii/

#according to the ques you cannot take both last and first indeices as they both are adjacent

#logic- firstly leave the last element of the array and apply the same logic on rest of the array i.e ans1
# then leave the first element of the array and apply the same logic on rest of the array i.e.ans2
#then our final_ans=max(ans1,ans2)


def maximumNonAdjacentSum(nums): #same function of house_robber1 ques
    n=len(nums)
    prev=nums[0]
    prev2=0
    for i in range(1,n):
        take=nums[i]
        if i>1:
            take+=prev2
        not_take=0+prev

        curri=max(take,not_take)
        prev2=prev
        prev=curri
    return prev

def rob(self, numss: List[int]) -> int:
    temp1=[]
    temp2=[]
    n=len(numss) #if len of the given array is 1 then just return that value
    if n==1:
        return numss[0]
    for i in range(n): 
        if i!=0:  #firstly leave the last element of the array and apply the same logic on rest of the array
            temp1.append(numss[i])
        if i!=n-1: #then leave the first element of the array and apply the same logic on rest of the array
            temp2.append(numss[i])
    return max(maximumNonAdjacentSum(temp1), maximumNonAdjacentSum(temp2))



