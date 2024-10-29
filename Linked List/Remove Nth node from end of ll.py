#updated-1
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]

#tc=n
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        
        #optimized approach
        dummy=ListNode(0) 
        dummy.next=head
        right=head
        left=dummy
        
        while n>0 and right: #here we are moving right pointer with the difference equal to n 
            right=right.next
            n-=1
        while right:#shifing both the pointers until right reaches end of the list
            left=left.next
            right=right.next
        #now left's next node have to be deleted
        left.next=left.next.next #in order to delete nth node of ll
        return dummy.next
    

#brute force method-
#reverse then remove nth element from front then again reverse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Remove:
    def __init__(self):
        self.head = None

    def printll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def reversell(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def removenth(self, n):
        # Reverse the linked list
        self.reversell()
        # Remove the nth node from the start of the reversed list
        if n == 1 and self.head: #if n=1 then we have to remove the head of ll
            self.head = self.head.next
            return
        
        cnt = 1
        curr = self.head
        while cnt < n - 1 and curr:
            curr = curr.next
            cnt += 1
        if curr and curr.next:
            curr.next = curr.next.next

        # Reverse the list back to its original order
        self.reversell()

# Manually create the linked list 1 -> 2 -> 3 -> 4
rem_ll = Remove()
rem_ll.head = Node(1)
rem_ll.head.next = Node(2)
rem_ll.head.next.next = Node(3)
rem_ll.head.next.next.next = Node(4)

print("Original List:")
rem_ll.printll()

# Remove the 2nd node from the end (which is '3')
rem_ll.removenth(2)

print("List after removing 2nd node from the end:")
rem_ll.printll()



#Method-3 (remove (length of ll-k)th element from front)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeKthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Calculate the position from the front
        pos_from_front = length - k
        
        # Edge case: If we're removing the head node
        if pos_from_front == 0:
            return head.next
        
        # Step 3: Traverse to the (pos_from_front - 1)-th node
        current = head
        for _ in range(pos_from_front - 1):
            current = current.next
        
        # Step 4: Remove the node by adjusting pointers
        if current.next:
            current.next = current.next.next
        
        return head

# Example usage
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
# Remove the 2nd node from the end, which is "4" in this case
updated_head = solution.removeKthFromEnd(head, 2)

# Printing the updated list
current = updated_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")





