class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def remove_nth_from_front(self, n):
        # Special case for removing the head node
        if n == 1 and self.head:
            self.head = self.head.next
            return

        curr = self.head
        cnt = 1
        # Traverse to the (n-1)th node
        while cnt < n - 1 and curr:
            curr = curr.next
            cnt += 1
        if curr and curr.next:
            curr.next = curr.next.next

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

print("Original List:")
ll.printll()

ll.remove_nth_from_front(2)

print("List after removing 2nd node from the front:")
ll.printll()
