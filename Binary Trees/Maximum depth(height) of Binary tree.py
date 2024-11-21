#updated
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#METHOD 1
#using dfs recursive method, tc=n,recursive space= n
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftdepth=self.maxDepth(root.left)
        rightdepth=self.maxDepth(root.right)
        return 1+max(leftdepth,rightdepth)
               
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
               
                




