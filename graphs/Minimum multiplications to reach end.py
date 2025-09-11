# Updated new
# https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
import sys
from collections import deque
def min_mult(start,end,mod_,arr):
    #the below dis is an array which holds 0-9999 values with infinity in each 
    dis= [sys.maxsize]*mod_ #this hold the steps that has been travelled till now
    q=deque()
    q.append((0,start)) #steps,multiplication value
    dis[start]=0

    while q:
        steps,mult=q.popleft()
        if mult==end:
            return steps
        for i in arr:
            new_mult=(mult*i)%mod_
            new_steps=steps+1
            if dis[new_mult]>new_steps:
                dis[new_mult]=new_steps
                q.append((new_steps,new_mult))
    return -1

start=3
end=75
mod_=10000
arr=[2,5,7]
result=min_mult(start,end,mod_,arr)

print("The minimum multiplications to reach end is", result)
