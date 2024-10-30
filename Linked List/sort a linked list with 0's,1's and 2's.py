# updated
def sort_ll(self,head):
    count=[0,0,0] #counts of 0's,1's,2's
    curr=head
    while curr:
        count[curr.val]+=1 #incrementing the count of the same number(0,1,2) as on curr.data
        curr=curr.next 
    i=0 #for counting that how many 0s 1s or 2s are left in count 
    curr=head
    while curr:
        if count[i]==0: #if counts of 0's 1's or 2's is zero then go to next element
            i+=1
        curr.val=i #if counts of 0's 1's or 2's is not zero then interchange the value of i at count[i]
        curr=curr.next 
        count[i]-=1 #decrementing the count of above no. by 1
