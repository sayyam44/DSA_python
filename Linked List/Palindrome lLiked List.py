class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #finding middle of ll
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #the slow pointer will be pointing to middle of ll
        #reversing the 2nd half ll
        prev=None
        while slow:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        # compare the first and second half nodes
        #prev is the 1st node of second half reversed list
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

        

