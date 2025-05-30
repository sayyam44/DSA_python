# Floor of X is the largest element which is smaller than or equal to X. 
# updated new

#Brute force approach
#tc=n
# def findFloor(arr,n,x):
#         floor=-1
#         for i in arr:
#             if i < x or i==x:
#                 floor=max(floor,i)
        
#         print(floor)

# n = 7 
# x = 0 
# arr = {1,2,8,10,11,12,19}
# findFloor(arr,n,x)

#Optimized approach
#Since the given array is sorted so go for binary search 
#tc=log(n)
def findFloorIndex(arr, n, x):
    low = 0
    high = n - 1
    floor_index = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            floor_index = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return floor_index

# Test case
n = 7 
x = 5 
arr = [1,2,8,10,11,12,19]
print(findFloorIndex(arr, n, x))  # Output will be -1 because there is no element <= 0 in the array
