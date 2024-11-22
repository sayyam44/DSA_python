# updated
#TC=N,SC=1
#always print curr value in just 2 cases 1st when the curr is at the leftmost node and second when 
# just before moving curr to its right in last case.
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
def morris_traversal(root):
	current = root

	while current:

		if current.left is None: #base case 
			yield current.val
			current = current.right
		else:
 
			# MAKE THREAD BY MOVING TOWARDS RIGHT THEN YIELD VALUES FROM LEFT 
			pre = current.left
			while pre.right and pre.right is not current: #Find rightmost node in current left subtree OR node whose right child == current
				pre = pre.right                            #pre.right child must be present and no thread is created till now

			if pre.right is None: # no thread is created till now
				pre.right = current #creating the thread
				current = current.left  #now current is actually moved towards left 

			else:
				pre.right = None #since pre is pointing at the leaf node i.e. 6 in copy example
				yield current.val
				current = current.right