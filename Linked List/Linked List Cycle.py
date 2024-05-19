# https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False

#approach 1 - by using hash map
# iterate through each element and put that node into the hash map and if the same node occurs twice then return 2 i.e. there must be a cycle present
        
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class solution:
    def cycle(self, head):
        hs=set()
        curr=head
        while curr :
            if curr not in hs:
                hs.add(curr)
                curr=curr.next
            return False
        return True
            