# https://www.youtube.com/watch?v=eD3tmO66aBA&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=15
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#BFS IS A LEVEL ORDER TRAVERSAL TECHNIQUE.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#METHOD 1
#using dfs recursive method, tc=n,recursive space= n
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

#METHOD-2
#BFS method,tc=n,sc=n(counting the levels)
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #BFS method,tc=n,sc=n
        if root is None:
            return 0
        level=0
        q=deque([root]) #only the root node is added initially
        
        while q: #we are adding all the nodes at same level from left and right and increasing a 
            # level by one in each case
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level

#METHOD-3   
#DFS iterative method  
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack=[[root,1]] #[node,depth]
        res=0
        
        while stack:
            node,depth=stack.pop()
            
            if node:
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res 
               