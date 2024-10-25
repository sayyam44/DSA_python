# Updated
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Method to display the list
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next

	# Method to add element to list
	def addToList(self, newData):
		newNode = Node(newData)
		if self.head is None:
			self.head = newNode
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = newNode

#Function to merge 2 linked lists
def mergeLists(headA, headB):
	dummynode=Node(0)
	tail=dummynode
	while headA and headB:
		if headA.data < headB.data:
			tail.next=headA
			headA=headA.next
			tail=tail.next
		else:
			headB.data<headA.data
			tail.next=headB
			headB=headB.next
			tail=tail.next
	if headA:
		tail.next=headA
	else:
		tail.next=headB
	return dummynode.next

# Create 2 lists
listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

# Merge the two lists
mergedHead = mergeLists(listA.head, listB.head)

# Create a new LinkedList instance for merged result
mergedList = LinkedList()
mergedList.head = mergedHead  # Set the head of mergedList to mergedHead

# Print the merged list
print("Merged Linked List:")
mergedList.printList()