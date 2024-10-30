# updated -1 
# tc=0(n)
from requests import head
class ListNode:
    def __init__(self,val=0,prev=None,next=None):
        self.prev=prev
        self.next=next
        self.val=val
class sol:
    def pairs(self,head,x):
        first=head
        last=head
        while last.next: #making last pointing to the last element of dll
            last=last.next
        
        found=False 
        
        while first!=last and last.next!=first: 
            #till first is not equal to last and first pointer should not exceed the first pointer
            if first.val+last.val==x:
                found=True
                print(first.val, "," , last.val)
                #if we found the pair with sum==x then make move both pointers by one
                first=first.next
                last=last.prev

            if (first.val+last.val)<x:  #if we found the pair with sum<x then make first pointer move by one
                first=first.next
            else:
                last=last.prev #if we found the pair with sum>x then make last pointer move by one

        if found==False:
            print("no pair found")
