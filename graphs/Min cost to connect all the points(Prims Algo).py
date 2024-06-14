# https://leetcode.com/problems/min-cost-to-connect-all-points/
# tc=(n2)logn
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)  #in order to create an adjacency list
        #here we are considering each point in form of index 0,1,2,3,4....
        adj={i:[] for i in range(N)} # for each i : we are getting [cost,node]
        
        for i in range(N): #for each point in adjacency list
            x1,y1=points[i] #getting the coordinates at index i
            for j in range(i+1,N): #we need to compare each point with every other vertex other than itself
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j]) #for each node i we are appending its dist from jth node
                adj[j].append([dist,i])#becasue we have undirected edges 
        #Prims algo       
        res=0 #to add the final cost
        vis=set()
        minH=[[0,0]] #[cost,point in form of index]
        while len(vis)<N:
            #min heap put the values already in ascending order thatswhy we need not to check manually the smallest val according to in copy
            cost,v=heapq.heappop(minH) #poping from the minH
            if v in vis:
                continue
            res+=cost #adding cost 
            vis.add(v) #adding the v in set so that it wont be repeated again 
            for neicost,nei in adj[v]: #checking for all the adjacent nodes of v (whereas in normal prims algo we used to check the neighbors of thenode)
                if nei not in vis:
                    heapq.heappush(minH,(neicost,nei)) #pushing the adjacent values (neicost,nei) in minh which are not present in visit set
        return res



            
                
                