#1st approach==2nd approach from gfg tc= O(n1*logn1) + O(n2*logn2)
#2nd approach==3rd approach in gfg using hashmap ,tc=n1+n2

import hashlib


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






