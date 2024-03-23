# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #brute force - tc=n,sc=n
        #create a hash table and hash through each element in linked list into the hashtable and if the node occurs again and did not reached null then this node will be the starting node of the circular ll
        
        #optimal approach,tc=n,sc=1
        #find colliding point of slow and fast pointer
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        
        #take another start pointer at head , and now move both slow and start pointer by one until they collide, and the colliding point will be the starting point of circular ll
        slow=head
        while fast:
            if slow.val==fast.val:
                return fast
            slow=slow.next
            fast=fast.next
        
               