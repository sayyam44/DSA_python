# updated - 1
# Input:
# K = 3, N = 5
# Arr[] = {3, 9, 12, 16, 20}
# Output:
# 11
# Explanation:
# The array can be modified as
# {6, 12, 9, 13, 17}. The difference between 
# the largest and the smallest is 17-6 = 11.

def funcc(k,n,arr):
   
        # arr.sort()
        # s=arr[0]+k smallest value in the starting 
        # l=arr[n-1]-k largest value in the starting 
        # min_val=arr[n-1]-arr[0] for initial case
        # mi,ma=0,0
        # for i in range(1,n)
        #     mi=min(s,arr[i+1]-k) mi is the minimum of current smallest and the current's next-k 
        #     ma=max(l,arr[i]+k) ma is the max of current largest and current value+k
        #     if mi<0: min value may also be negative
        #         continue
        #     min_val=min(min_val,ma-mi)
        # return min_val
        # code here
    arr.sort() #sorted elements will provide the best outcome for ith and (i+1)th element
    ans = arr[n - 1] - arr[0]  # Maximum possible height difference initially as it is sorted already
 
    tempmin = arr[0] #smallest heighted tower
    tempmax = arr[n - 1] #highest heighted tower
 
    for i in range(1, n): #i is on the 2nd tower , as weare comparing 1st 2 towers
        tempmin = min(arr[0] + k, arr[i] - k)
        tempmax = max( arr[n - 1] - k, arr[i - 1] + k)
         #in upper case max means current's prev+k i.e. arr[i-1]+kk
        # subtract k from whole array
        ans = min(ans, tempmax - tempmin)
 
    return ans

#actual code from video
def heights(arr,k,n):
    arr.sort()
    ans=arr[n-1]-arr[0]
    tempmin=arr[0]-k
    tempmax=arr[n-1]+k

    tmin,tmax=0,0

    for i in range(0,n-1):
        tmin=min(tempmin,arr[i+1]-k) #2nd vale tower ki min height chahiye
        tmax=max(tempmax,arr[i]+k) #1st vale ki maxheight chahiye
        if tmin<0:
            continue #to discard if tmin becomes negative
        ans=min(ans,tmax-tmin)
    return ans