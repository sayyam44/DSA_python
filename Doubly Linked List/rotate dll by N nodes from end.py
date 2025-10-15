# Updated new
from sklearn.cluster import k_means
class ListNode:
    def __init__(self,val=0,prev=None,next=None):
        self.prev=prev
        self.next=next
        self.val=val

class sol:
    def rotate(head,n):
        if not head:
            return None
        curr=head
        l=0
        while curr:
            l+=1
            curr=curr.next
        
        if l<k:
            rot=k%l
        if k<l:
            rot=k
        else:
            rot=0
        
        curr.next=head
        head.prev=curr
        b=head
        steps_from_front=l-rot
        for i in range(steps_from_front-1):
            b=b.next
        head=b.next
        head.prev=None
        b.next=None
        return head
