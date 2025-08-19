# updated new
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def detect_cycle_start(self):
        slow = self.head
        fast = self.head

        # Step 1: Detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle found
            return None

        # Step 2: Find the start of the cycle
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data  # Both pointers now point to the start of the cycle

# Create a linked list with a cycle for testing
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

# Creating a cycle: 5 -> 3
ll.head.next.next.next.next.next = ll.head.next.next

# Find the start of the cycle
cycle_start_value = ll.detect_cycle_start()
if cycle_start_value is not None:
    print(f"Cycle starts at node with value: {cycle_start_value}")
else:
    print("No cycle detected")
