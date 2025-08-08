# updated new
# https://www.youtube.com/watch?v=pUAPcVlHLKA
# https://leetcode.com/problems/rotting-oranges/

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#tc=n*m
#sc=n*m
# Determine what is the minimum time required so that all the oranges become rotten. A rotten orange at index
#  [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right). If it is impossible to rot every orange then simply return -1.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        Q = collections.deque([])
        cnt = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1  #counting the number of fresh oranges
                if grid[i][j] == 2:
                    Q.append((i,j, 0)) #row, col, minutes_passed
                    #here we are adding the indices of the oranges which are rotten in the starting
        #target is to make all fresh oranges to be rotten           
        res = 0
        while Q: #checking for each rotten orange seperately 
            i, j, steps = Q.popleft() #poping the 1st rotten orange index from queue
            res = steps
            #BFS is being followed over here
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:#checking all the adjacent elements of the rotten orange , if it is fresh then make it rotten
                if 0<=x<n and 0<=y<m and grid[x][y] == 1: #here 0<=x<n means the current element must be smaller than the num of rows and same for y
                    grid[x][y] = 2
                    cnt -= 1  
                    Q.append((x,y, steps + 1))##here we are adding the rest rotten oranges indices into the queue
        
        return res if cnt == 0 else -1
        





