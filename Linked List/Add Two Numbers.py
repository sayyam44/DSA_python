# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy= ListNode()
        curr=dummy
        
        carry=0
        while l1 or l2 or carry : #here carry is added for 8+7 condition when we only have single digits in both the lists
            v1= l1.val if l1 else 0 
            v2= l2.val if l2 else 0
            
            #new digit
            val=v1+v2+carry
            carry=val//10 #floor division 
            val=val%10 #remainder value v1+v2
            curr.next=ListNode(val)
            
            #moving curr,l1 and l2 pointers forward
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        return dummy.next
            


#2,6,6
#4,5,2
#6,1,9

