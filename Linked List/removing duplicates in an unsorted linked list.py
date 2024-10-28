from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Detect if there's a cycle and remove it
        slow, fast = head, head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        # Step 2: If a cycle exists, break it
        if has_cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            
            # Set the last node in the cycle to None to break it
            cycle_start = slow
            temp = cycle_start
            while temp.next != cycle_start:
                temp = temp.next
            temp.next = None  # Break the cycle

        # Step 3: Remove duplicates in the now acyclic, unsorted list
        seen_values = set()
        current = head
        prev = None
        while current:
            if current.val in seen_values:
                # Duplicate found, skip the current node
                prev.next = current.next
            else:
                # Not a duplicate, add value to set
                seen_values.add(current.val)
                prev = current
            current = current.next

        return head

# Helper function to print the linked list
def printList(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage with cycle and duplicates in an unsorted list
head = ListNode(1, ListNode(3, ListNode(2, ListNode(3, ListNode(2)))))
head.next.next.next.next.next = head.next  # Create a cycle

solution = Solution()
new_head = solution.deleteDuplicates(head)
print("Linked list after removing duplicates and breaking cycle if present:")
printList(new_head)
