#updated
# https://leetcode.com/problems/non-decreasing-subsequences/
def main(nums):
    res=set()
    def backtrack(ind,path_till_now):
        if len(path_till_now)>=2:
            res.add(tuple(path_till_now))
        for i in range(ind,len(nums)):
            if not path_till_now or path_till_now[-1]<=nums[i]:
                backtrack(i+1,path_till_now+[nums[i]])

    backtrack(0,[])
    return list(res)

print(main([4, 6, 7, 7]))
