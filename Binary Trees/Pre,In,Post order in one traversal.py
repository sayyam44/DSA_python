# updated
# https://www.geeksforgeeks.org/preorder-postorder-and-inorder-traversal-of-a-binary-tree-using-a-single-stack/

def allTraversal(root):
    pre=[]
    post=[]
    inn=[]
    s=[]
    s.append([root,1]) #node,num we will increment 1 when we put this 
    # into any of the above 3 lists keep one thing in mind that we 
    # will only pop in postorder traversal because we need all the 
    # nodes in all the 3 traversals.
    while (len(s)):
        p=s[-1] # Stores the top element of the stack both node and num
        if p[1]==1:
            pre.append(p[0].val) #appending only the node.val part
            s[-1][1]+=1 # Update the status of top node
            if p[0].left:
                s.append(p[0].left,1)
        
        elif p[1]==2:
            inn.append(p[0].val)
            s[-1][1]+=1
            if p[0].rght:
                s.append(p[0].right,1)
            
        elif p[1]==3:
            post.append(p[0].val)
            s.pop()




