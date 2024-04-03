class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify(0)
        return min_val
    
    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)
    
    def find_kth_smallest(self, k):
        if k <= 0 or k > len(self.heap):
            return None
        temp_heap = MinHeap()
        temp_heap.heap = self.heap.copy()
        for _ in range(k-1):
            temp_heap.extract_min()
        return temp_heap.extract_min()

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
min_heap = MinHeap()
for num in arr:
    min_heap.insert(num)
result = min_heap.find_kth_smallest(k)
print(f"The {k}th smallest element is: {result}")
