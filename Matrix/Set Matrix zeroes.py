# updated new
#https://leetcode.com/problems/set-matrix-zeroes/
#sc=1,tc=m*n
#https://www.geeksforgeeks.org/a-boolean-matrix-question/

#method 1
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols_lst=[1]*len(matrix[0])
        rows_lst=[1]*len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    cols_lst[j]=0
                    rows_lst[i]=0
        for i in range(len(rows_lst)):
            if rows_lst[i]==0:
                matrix[i]=[0]*len(matrix[0])
        for j in range(len(cols_lst)):
            if cols_lst[j]==0:
                for i in range(len(matrix)):
                    matrix[i][j]=0
        return matrix

#Method 2
class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag=False
        col_flag=False
        
        r=len(m)
        c=len(m[0])
        
        for i in range(r):
            for j in range(c):
                if i==0 and m[i][j]==0:
                    row_flag=True
                if j==0 and m[i][j]==0:
                    col_flag=True
                if m[i][j]==0:
                    m[0][j]=0
                    m[i][0]=0
                
        for i in range(1,r):
            for j in range(1,c):
                if m[0][j]==0 or m[i][0]==0:
                    m[i][j]=0
        if row_flag:
            for j in range(c):
                m[0][j]=0
        
        if col_flag:
            for i in range(r):
                m[i][0]=0
        return m

