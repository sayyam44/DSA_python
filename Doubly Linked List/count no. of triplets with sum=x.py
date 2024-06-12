# Traverse the doubly linked list from left to right. For each current node during the traversal, 
# initialize two pointers first = pointer to the node next to the current node and last = pointer to the 
# last node of the list. Now, count pairs in the list from first to last pointer that sum up to value 
# (x – current node’s data). Add this count to the total_count of triplets. Pointer to the last node can 
# be found only once in the beginning.

class ListNode:
    def __init__(self,val=0,prev=None,Next=None):
        self.val=val
        self.prev=prev
        self.next=next
    
class solution:
    def countpairs(first,last,value): #this is to find all the pairs of first and last such that first+last=x-curr.val
        count=0
        while first and last and first!=last and last.next!=first:
            if first.val+last.val==value:
                count+=1
                first=first.next
                last=last.prev

            if first.val+last.val<value:
                first=first.next
            
            if first.val+last.val>value:
                last=last.prev
        return count


    def counttriplets(self,head,x):
        if not head:
            return None

        curr,first,last=head,None,None
        count=0

        last=head
        while last: #making last pointing to thr last node of dll
            last=last.next
        
        while curr:
            first=curr.next #first will be pointing to just next element of curr
            count+=self.countpairs(first,last,x-curr.val),curr.next
        return count

