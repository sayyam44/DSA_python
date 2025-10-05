# Updated new
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#Method-1
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            if i>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,i)
        return heap[0]


#Method-2
#Optimized approach- n (for converting array into heap) + klogn(logn for poping from the heap and we need to pop k times)

#most optimized approach tc=o(n) avg case , o(n2) worst case
#QUICK SORT 
#eg - given 3,2,1,5,6,4 lets take 4 as a pivot point 
#then start from 3 and go upto pivot point 
#if the ith value is smaller then the pivot point then put the ith value in the 1st half 
#but not necessarily in sorted order
#3,2,1,5,6,4(p)  swap p with 5---->>>> 3,2,1,4(p),6,5
# 3,2,1,4(p),6,5 this shows that the 3rd(index of 4) largest value == 4. 
#now if we want 3rd larget value then 4 will be the output directly as 4 is the pivot point
#but other thrn 4 if we want 4th largest then go to 4th value that is 6 and repeat the process
#that turns it into 3,2,1,4(p),5,6 return 5 as required

#Average case tc= O(N) -->rightmost element is pivot and this pivot point ends up in the middle of the array

#unlike quich sort(NLOGN) this method will take o(N) time because in quick sort we used to sort both the sides of pivot 
#point but here we are sorting only one side of pivot value where we want our answer lies 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #eg given ---- 3,2,1,5,6,4
        k = len(nums) - k

        def quickSelect(l, r):
            if l == r:
                return nums[l]

            pivot, p = nums[r], l  #pivot is the rightmost value and p is the leftmost value
            for i in range(l, r):
                if nums[i] <= pivot: #and if it is greater then dont move p pinter and dont put any value
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1    #p pointer is moved by 1 everytime that is to an empty space
            #here we will reach to a point p which tells that every element before p pointer is <= poiner value and towards p's right is greater than pointer value 
            # 3,2,1,5(p),6,4(r)
            nums[p], nums[r] = nums[r], nums[p] #here nums[r]==pivot value
            #3,2,1,4(p),6,5

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                # this case will run as p=4,k=6
                #so again run quickselect for 6(p),5
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
                

class MinHeap:

    # Constructor
    def __init__(self, a, size):

        # list of elements in the heap
        self.harr = a

        # maximum possible size of min heap
        self.capacity = None

        # current number of elements in min heap
        self.heap_size = size

        i = int((self.heap_size - 1) / 2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    def parent(self, i):
        return (i - 1) / 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # Returns minimum
    def getMin(self):
        return self.harr[0]

    # Method to remove minimum element (or root)
    # from min heap
    def extractMin(self):
        if self.heap_size == 0:
            return float("inf")

        # Store the minimum value
        root = self.harr[0]

        # If there are more than 1 items, move the last item
        # to root and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.minHeapify(0)
        self.heap_size -= 1
        return root

    # A recursive method to heapify a subtree with root at
    # given index. This method assumes that the subtrees
    # are already heapified
    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if ((l < self.heap_size) and
                (self.harr[l] < self.harr[i])):
            smallest = l
        if ((r < self.heap_size) and
                (self.harr[r] < self.harr[smallest])):
            smallest = r
        if smallest != i:
            self.harr[i], self.harr[smallest] = (
                self.harr[smallest], self.harr[i])
            self.minHeapify(smallest)