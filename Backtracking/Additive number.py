# https://leetcode.com/problems/additive-number/

# The number of recursive calls for each valid sequence is O(N) and 
#the process of picking the first and second numbers involvesO(N^2)
#Overall TC= O(n^3)
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        def dfs(first,second,start):
            if start==n:
                return True
            
            next_num=str(int(first)+int(second))
            next_len=len(next_num)

            if next_num == num[start:start+next_len]:
                return dfs(second,next_num,start+next_len)
            return False

        for i in range(1,n):
            for j in range(i+1,n):
                first=num[:i]
                second=num[i:j]
                # Skip numbers with leading zeros (except the number "0" itself)
                if (first[0]=='0' and len(first)>1) or (second[0]=='0' and len(second)>1):
                    continue
                
                if dfs(first,second,j):
                    return True
        return False