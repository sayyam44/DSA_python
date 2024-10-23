# https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
#since the rows are sorted use binary search
# The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.

def maxnum1(m):
    r=len(m)
    c=len(m[0])
    required_index=0 
    index=c-1 #as we have to check from back the number of 1's in each sorted array

    for i in range(r):
        while (m[i][index]==1 and index>=0): 
            index-=1 #we are not updating index=0 for each i 
            # therefore we will start checking 1s in the next 
            #row right after the index for finding the max index
            required_index=i
        # if required_index==0 and m[0][c-1]==0:
        #     return 0
    return required_index
 
# Driver Code
mat = [[0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
    maxnum1(mat))


