# tc=n,sc=1
def revListInGroupOfGivenSize(head, k):
    if head is None:
        return head
    st = head
    globprev, ans = None, None
    while (st != None):
        # Count the number of nodes.
        count = 1
        curr = st
        prev, next_node = None, None
        while (curr != None and count <= k):
            # Reversing k nodes.
            next_node = curr.next
            curr.prev = next_node
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
  
        if ans is None:
            ans = prev
            ans.prev = None
  
        if globprev is None:
            globprev = st
  
        else:
            globprev.next = prev
            prev.prev = globprev
            globprev = st
  
        st = curr
  
    return ans