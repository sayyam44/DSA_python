# #there can be many combinations of topological sort
#Topological Sort or KAHNS algorithm
#Topological Sorting means sorting/linear ordering of all the vertices of graph in such a
#  format that 
#if we have any vertex u->v, then u must always occur before v in the sorting .

#TOPOLOGICAL SORTING CAN ONLY OCCUR FOR DIRECTED ACYCLIC GRAPHS(DAG) ONLY

#step1- create an array containing the indegrees of all the elements
#step2-traverse through the above array the elements which have their indegree = 0, append
#  them to a queue
#step3- pop from the queue and add them to the output and also decrease the indegrees of 
# all its adjacent nodes by 1
#step4- Now after decreasing the indegrees by 1 check if some node's indegree has become 0
#  or not,
#if yes then append that element to the que and repeat the process till queue is empty.

from collections import defaultdict
 
class graph():
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    
    def kahns(self):
        c=max(self.graph)+1
        indegree=[0]*(c)

        for i in range(c): #grabbing one node
            for j in self.graph[i]: #grabbing its adjacent nodes
                indegree[j]+=1 #increase the indegree of jth element by 1
        
        queue=[]
        for i in range(c):
            if indegree[i]==0:
                queue.append(i)

        cnt=0 #in order to check a cycle
        result=[]
        while queue:
            s=queue.pop(0)
            result.append(s)

            for i in self.graph(s): #checking the adjacent elements of the poped value only
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
            cnt+=1
        
        if cnt != c: #if this loop havent run the no. of times that is equal to the length of graph
            print ("There exists a cycle in the graph")
        else:
            print(result)

g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
g.kahns()

