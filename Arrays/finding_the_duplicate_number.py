# updated new
# https://www.youtube.com/watch?v=32Ll35mhWg0&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=2
# https://leetcode.com/problems/find-the-duplicate-number/
def findDuplicate(nums):
        #brute force method
        #tc=nlogn+n,sc=n
        #firstly sort the array then traverse through array and check if at any traversal nus[i]=nums[i+1], if yes then return nums[i]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return nums[i]
                
        #optimized(hashmap) tc=n ,sc=n
        #create a hashmap of all 0's of same size as nums and traverse through nums and update the value in hashmap according to index as 1 whos value actually occurs in list.
        

        #THIS METHOD IS CALLED LINKED LIST CYCLE METHOD
        ##the cycle is created on the basis of values stored at particular indices 
        #most optimized method - tortoise method , move 1 pointer by 1, move fast pointer by 2 , and check where 
        # they meet , then assign nums[0] to fast then again move both by 1, and the value at which they meet 
        # is the duplicate value.,the circle is made according to the values and indexes in list
def findDuplicate(nums):
        slow,fast=nums[0],nums[0]
        
        while True: #runs without any conditions until the break statement executes inside the loop
            slow,fast= nums[slow],nums[nums[fast]] #moving slow and fast on the basis of the indices of the values in array not the actual values
            if slow == fast: break #this shows the array have duplicate value in it
           
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow

       




