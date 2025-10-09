# Updated new
#method-1
import heapq
class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # Step 1: Build a Max-Heap with the first k elements (store negative values)
        heap = [-num for num in nums[:k]]  # Convert values to negative for Max-Heap
        heapq.heapify(heap)
        
        # Step 2: Process the remaining elements in the array
        for i in nums[k:]:
            if -i > heap[0]:  # Compare negative value to simulate Max-Heap
                heapq.heappop(heap)  # Remove the largest (root) of the Max-Heap
                heapq.heappush(heap, -i)  # Add the new smaller element

        # Step 3: Return the root of the heap (convert it back to positive)
        return -heap[0]
    
#method-2
class MinHeap:
    def __init__(self):
        # Initialize an empty heap
        self.heap = []
    
    def parent(self, i):
        # Returns the index of the parent node of the node at index i
        return (i - 1) // 2
    
    def left_child(self, i):
        # Returns the index of the left child node of the node at index i
        return 2 * i + 1
    
    def right_child(self, i):
        # Returns the index of the right child node of the node at index i
        return 2 * i + 2
    
    def insert(self, x):
        # Inserts element x into the min-heap
        self.heap.append(x)
        i = len(self.heap) - 1
        # Adjusts the heap by swapping elements to maintain the min-heap property
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    def extract_min(self):
        if not self.heap:
            return None
        # Extracts the minimum element from the min-heap
        min_val = self.heap[0]
        # Replaces the root with the last element and maintains the min-heap property
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify(0)
        return min_val
    
    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        # Finds the smallest among the node, left child, and right child
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        # Swaps the smallest element with the current node if necessary and continues heapifying
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)
    
    def find_kth_smallest(self, k):
        if k <= 0 or k > len(self.heap):
            return None
        # Creates a temporary heap to avoid modifying the original heap
        temp_heap = MinHeap()
        temp_heap.heap = self.heap.copy()
        # Extracts k-1 minimum elements from the temporary heap
        for _ in range(k-1):
            temp_heap.extract_min()
        # Returns the kth smallest element from the temporary heap
        return temp_heap.extract_min()

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
min_heap = MinHeap()
for num in arr:
    min_heap.insert(num)
result = min_heap.find_kth_smallest(k)
print(f"The {k}th smallest element is: {result}")
