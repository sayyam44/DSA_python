# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]

#tc=n
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        
        #optimized approach
        dummy=ListNode(0,head) #dummy must be pointing towards head
        right=head
        left=dummy
        
        while n>0 and right: #here we are moving right pointer with the difference equal to n 
            right=right.next
            n-=1
        while right:#shifing both the pointers until right reaches end of the list
            left=left.next
            right=right.next
        
        left.next=left.next.next #in order to delete nth node of ll
        return dummy.next
    

#brute force method-
#directly reverse the list and remove the nth node from  front
class solution:
    def solution(self,head,n):
        a=self.reverseList(head)
        b=a
        count=1
        while count<=(n):
            b=b.next
            count+=1
        b.next=b.next.next

    def reverseList(self, head):
        
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr= nxt
        return prev







