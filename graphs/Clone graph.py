# Updated new
## https://leetcode.com/problems/clone-graph/
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldtonew={} #creating a hashmap which stores old nodes and new nodes as it is visited 

        def dfs(node): #here we are using dfs approach as this is a recurssion type of problem
            if node in oldtonew:
                return oldtonew[node]# for backtracking - if the node is already present in the hashmap then it returns the clone of this node

            #old value is node and new value for that node is copy
            copy=Node(node.val) #creating a new node 'copy' of the graph as copy if the node is already not present in hashmap
            oldtonew[node]=copy #in order to add all the nodes into hashmap(old->new)

            for n in node.neighbors: #as we need to create a copy of every neighbor of the current clone node
                #dfs(n) it returns the copy(clone) we will create for this node 
                #hence we need to add these copies of the current node to the current node's neighbors list
                copy.neighbors.append(dfs(n)) #creating all the neighbors of new cloned node 'Copy'
            return copy
        return dfs(node) if node else None #inotrder to get a connected graphs

