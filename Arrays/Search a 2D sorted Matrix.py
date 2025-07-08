# updated new
def searchMatrix(m,t):
    i,j=0,len(m)-1 #start from top right corner of matrix

    while (i<len(m) and j>=0):
        if t>m[i][j]:
            i+=1
        elif t<m[i][j]:
            j-=1
        else:
            return 1

    return 0

    
    
            