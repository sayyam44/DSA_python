# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={ i:[] for i in range(numCourses)} #creating a hashmap where keys=courses and values = list of all its prerequisites courses
        for crs,pre in prerequisites:
            premap[crs].append(pre)
            
        #visitSet = all courses along the current DFS path
        visitset=set() #set is always used in graph to detect a loop
        #we just need to find out whether or not the graph has a loop or not 
        def dfs(crs):
            if crs in visitset: #1st case- if the crs is in visitset already then we have a loop
                return False
            if premap[crs]==[]:#2nd case-if for some crs we dnt have any prerequsites then return true
                return True
            visitset.add(crs)
            #3rd case-now reached at a course who have some prerequisites and neither it is in visitset
            for pre in premap[crs]: #loop through all the prerequisites of thsi course
                if not dfs(pre) : return False #if we find even 1 course that cannot be completed we will return false
            visitset.remove(crs) #as we have completed visiting that particular course 
            premap[crs]=[] #when we complete visitng a node we will leave it as empty list this is because 
            #if in future if some course is dependent on this course whose dfs has returned true it would 
            #not need to check it again for this course .
            return True

        for crs in range(numCourses): #iterate through every single course from the number of courses that we have
            if not dfs(crs): return False
        return True
        #this last loop is if the graph is not fully connected 
            
                
                
        
