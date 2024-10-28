#Updated
#https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #most optimal solution using 2 pointer ,tc=2m=m, sc=1
        if headA is None or headB is None:
            return None
        
        pa=headA
        pb=headB
        
        while pa != pb: 
            # if either pointer hits the end, make that pointer point towards the head  
            # of the other linked list and continue the second traversal, 
            # if not hit the end, just move on to next
            pa=headB if pa is None else pa.next
            pb=headA if pb is None else pb.next
        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
        
# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None 

#Updated read this solution
#optimal 1- using hash map, tc=m+n,sc=n
# use hash map/set and put all values of 1st head in hash map and then iterate through
#  the 2nd head and check if this value is already present in the hash map 

# hs=set()
# while headA:
#     curr=headA #curr is initially pointing towards the address of head of headA
#     hs.add(curr)
#     curr=curr.next
# while headB:
#     curr2=headB
#     if curr2 not in hs:
#         curr2=curr2.next
#     else:
#         return curr2
# return None

#This is not imp 
#optimal 2- tc=m+(m-n)+n=2m=m, sc=1
# step1- find the length of both the linked list using dummy nodes
#step2- find the difference between their lengths
#step3-put dummy 2 at the nth position of longer linked list 
#step4= move both the dummy1 and dumm2  simultaneously and the point where they collide is the point of intersection.
#         c1=getcount(headA)
#         c2=getcount(headB)
        
#         if c1>c2:
#             d=c1-c2
#             return getintersection(d,headA,headB)
#         else:
#             d=c2-c1
#             return getintersection(d,headB,headA)

# def getintersection(d,headA,headB):
#     p1=headA

#     while d>0 and p1:
#         p1=p1.next

#     p2=headB
#     while p2 and p1:
#         if p1.val==p2.val:
#             # return p1.val
#             print("Intersected at ",p1.val)
#             break

#         else:
#             p1=p1.next
#             p2=p2.next
#     # return -1
#     print('No intersection')
            
        
# def getcount(headc):
#     cur=headc
#     c=0
#     while cur:
#         c+=1
#         cur=cur.next
#     return c

 

    

