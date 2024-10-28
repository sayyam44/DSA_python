#https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow=fast=head
        while fast and fast.next:#because the cycle will be countered from 
            #fast side first as fast is moving faster
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



#Full implementation using tortoise method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next          # Move slow pointer by one
            fast = fast.next.next     # Move fast pointer by two

            if slow == fast:          # If they meet, there's a cycle
                return True
        return False                  # If fast reaches end, no cycle

# Create a linked list with a cycle for testing
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

# Creating a cycle: 4 -> 2
ll.head.next.next.next.next = ll.head.next

if ll.detect_cycle():
    print("Cycle detected")
else:
    print("No cycle detected")
