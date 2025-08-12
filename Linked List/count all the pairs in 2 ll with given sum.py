# updated new
#1st approach->Sort the 1st linked list in ascending order 
# and the 2nd linked list in descending order using merge 
# sort technique
# tc= O(n1*logn1) + O(n2*logn2)

#2nd approach->We store all first linked list elements in 
# hash table. For elements of second linked list, 
# we subtract every element from x and check the result 
# in hash table. If result is present, we increment the 
# count.using hashmap ,tc=n1+n2

#approach-2 implementation
def sol(l1,l2,sum):
    hash=set()
    count=0

    while l1:
        hash.append(l1.val)
        l1=l1.next

    while l2:
        if (sum-l2.val) in hash:
            count+=1
        l2=l2.next
    return(count)






