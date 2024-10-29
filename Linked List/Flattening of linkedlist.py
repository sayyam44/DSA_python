# Updated
# https://www.geeksforgeeks.org/flattening-a-linked-list/
#use first while loop to move through root values and the use another while 
#loop to move through the bottom of the linked list
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.bottom = None

def flatten(root):
    values = []
    while root is not None:
        values.append(root.data)
        temp = root.bottom
        while temp is not None:
            values.append(temp.data)
            temp = temp.bottom
        root = root.next

    values.sort()
    
    head,tail=None,None
    for newdata in values:
        newnode=Node(newdata)
        if not head:
            head=newnode
        else:
            tail.bottom=newnode
        tail=newnode
    return head

def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.bottom
    print()

if __name__ == "__main__":
  
    # Create a hard-coded linked list:
    # 5 -> 10 -> 19 -> 28
    # |    |     |
    # V    V     V
    # 7    20    22
    # |          |
    # V          V
    # 8          50
    # |
    # V
    # 30
    head = Node(5)
    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next = Node(10)
    head.next.bottom = Node(20)

    head.next.next = Node(19)
    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    head.next.next.next = Node(28)

    # Function call
    head = flatten(head)

    print_list(head)
