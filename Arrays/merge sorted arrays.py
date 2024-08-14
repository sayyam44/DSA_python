#updated
def merge(nums1,nums2,m,n):
        #brute force method - use an empty array of size = size1+size2 , then add all the nums from arr1 and arr2 into that arr and sort that array 
        #tc=nlogn(sorting)+n(for putting all nums from arr1 and arr2 to empty arr)=nlogn
        #sc=n
        
        #optimized approach (insertion sort)
        #step1- check smaller among a1[0],a2[0], whichever array has smaller element then start traversing through that array lets say a1
        #step2-if a1[1] > a2[0] then swap both these 
        #step3- sort arr 2 , again follow this 
        
        # tc=n(for iterating arr1)+m (for sorting arr2)=n+m
        #sc=1
    
        while m > 0 and n > 0: #m= length of nums1 till non zero values only
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n] #copy all the elements left in nums2 into nums1 
        return nums1

def merg(self,nums1,n,nums2,m):
    arr=[None]*(n+m)
    i=0
    j=0
    k=0

    while i<n and j<m:
        if nums1[i]<nums2[j]:
            arr[k]=nums1[i]
            i+=1
            k+=1
        else:
            arr[k]=nums2[j]
            j+=1
            k+=1
    return arr

