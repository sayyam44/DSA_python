# updated
# https://leetcode.com/problems/additive-number/

# The number of recursive calls for each valid sequence is O(N) and 
#the process of picking the first and second numbers involvesO(N^2)
#Overall TC= O(n^3)
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(num1,num2,start):
            if start==len(num):
                return True
            summation=str(int(num1)+int(num2))
            sum_len=len(summation)
            if summation==num[start:start+sum_len]:
                return dfs(num2,summation,start+sum_len)
            return False
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                num1=num[:i]
                num2=num[i:j]
                if (num1[0]=='0' and len(num1)>1) or (num2[0]=='0' and len(num2)>1):
                    continue
                if dfs(num1,num2,j):
                    return True
        return False