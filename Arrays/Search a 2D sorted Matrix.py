
# https://leetcode.com/problems/search-a-2d-matrix/
# # https://www.youtube.com/watch?v=ZYpYur0znng&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=15

def searchMatrix(m,t):
    #approach 1(linear search) --- tc=m*n , sc=1
#         if len(m)==0:
#             return-1
        
#         for i in range(len(m)):
#             for j in range(len(n)):
#                 if m[i][j]==t:
#                     return 1
#         return 0
    
    #approach 2(go on each column and do binary search in each column)
    #tc=n*mlogm
    
    #optimal sol ,tc=n,sc=1
# Let the given element be x, create two variable i = 0, j = n-1 as index of row and column
# Run a loop until i = n
# Check if the current element is greater than x then decrease the count of j. Exclude the current column.
# Check if the current element is less than x then increase the count of i. Exclude the current row.
# If the element is equal, then print the position and end.

    i,j=0,len(m)-1 #start from top right corner of matrix

    while (i<len(m) and j>=0):
        if t>m[i][j]:
            i+=1
        elif t<m[i][j]:
            j-=1
        else:
            return 1

    return 0

    
    
            