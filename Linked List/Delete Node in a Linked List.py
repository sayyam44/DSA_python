# updated new
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        """
        Deletes the given node from the linked list by copying the next node's value
        to the current node and updating the next pointer to skip the next node.
        :type node: ListNode
        :rtype: void
        """
        if node is None or node.next is None:
            return  # Cannot delete if node is None or it's the last node

        node.val = node.next.val
        node.next = node.next.next

# Helper function to print the list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Create the linked list 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

print("Original List:")
printList(head)

# Suppose we want to delete the node with value 5
node_to_delete = head.next  # Node with value 5

# Delete the node
sol = Solution()
sol.deleteNode(node_to_delete)

print("List after deleting node with value 5:")
printList(head)
