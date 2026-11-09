class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        
        # Fix the min-heap property if it is violated
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the minimum value, move the last element to root, and heapify
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        
        return root

if __name__ == "__main__":
    print("--- Min-Heap Demonstration ---")
    min_heap = MinHeap()
    elements = [15, 20, 9, 2, 45, 12, 7]
    
    print(f"Inserting elements: {elements}")
    for el in elements:
        min_heap.insert(el)
        
    print(f"Internal Heap Array: {min_heap.heap}")
    
    print("Extracting elements in ascending order:")
    sorted_output = []
    while min_heap.heap:
        sorted_output.append(min_heap.extract_min())
        
    print(f"Extracted: {sorted_output}")