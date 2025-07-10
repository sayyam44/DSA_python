# updated new
# https://leetcode.com/problems/rotate-image/
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        #brute force--tc=n2,sc=n2
        #use another empty matrix and directly change the rows with columns
        
        #optimized sol---reverse the matrix on rows and then find transpose(change all rows with columns) of the matrix 
        #tc=n2+n2=n2 --- to transpose and reverse the matrix
        #sc=1 (as no extra matrix is being used)
        
        #step1-making 1st row as last row and similarly other rows.
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        #step2-transposing the matrix(i.e. swapping without doing anything to the diagnol matrix)
        for i in range(len(matrix)): 
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
        return matrix