# approach 1 - Hashing , create an empty 
# hashmap of size n with all zeros, now trasverse through the arr and increase the value 
# the value in hashmap by i at the value ith index
# the index with value =2 is repeating element and index with value=0 is missing value
# tc=n+n,sc=n

def getTwoElements( arr, n): 
    
    global x, y
    x = 0
    y = 0

    xorr=arr[0]

    # Get the xor of all array elements
    for i in range(1,n):
        xorr=xorr^arr[i]
    # XOR the previous result with numbers 
    # from 1 to n
    for i in range(1,n+1):
        xorr=xorr^i
    # Will have only single set bit of xor1
    set_bit_no = xorr & ~(xorr - 1) # ~ reverses the binary of a given number, here we are taking the rightmost element of the xorr (eg set_bit_no=1 for 4 in copy)
    for i in range(n):
        if (arr[i] & set_bit_no)!=0: #here arr[i] defines the right most element of ith value in arr 
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    
    for i in range(1, n + 1):
        if (i & set_bit_no) != 0:
            x = x ^ i
        else:
            y = y ^ i 

arr = [ 1, 3, 4, 5, 5, 6, 2 ]
n = len(arr)
      
getTwoElements(arr, n)
  
print("The missing element is", x,
      "and the repeating number is", y)


    
    

