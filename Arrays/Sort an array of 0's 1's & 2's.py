def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    #approach 1- brute force - sort the array directly ]
    #tc=nlogn,sc=1
    
    #approach 2-brute force-count sort-count the num of 0,1,2 and append that many nus of 0,1,2 in some extra list
    #tc=n(for traversing through arr)+n(for putting that num of 0s,1s,2s in arr)
    
    
    #approach 3,optimized sol(Dutch national flag algo),in copy,tc=n,sc=1
    
    low,mid,high=0,0,len(nums)-1
    
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid], nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else : #nums[mid]==2
            nums[high],nums[mid]=nums[mid],  nums[high]
            high-=1
    return nums



