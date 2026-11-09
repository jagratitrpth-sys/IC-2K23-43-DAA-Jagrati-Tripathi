import sys
from pathlib import Path
import random
from collections import deque

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def radix_sort_queue(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    
    # Initialize 10 queues (buckets) for digits 0-9
    queues = [deque() for _ in range(10)]
    
    while max_val // exp > 0:
        # Enqueue elements into appropriate queues based on the current digit
        for num in arr:
            digit = (num // exp) % 10
            queues[digit].append(num)
            
        # Dequeue elements back into the main array to maintain stable order
        idx = 0
        for q in queues:
            while q:
                arr[idx] = q.popleft()
                idx += 1
        
        exp *= 10
        
    return arr

if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 20000, 30000, 40000, 50000]
    data_generator = lambda n: [random.randint(0, 10000) for _ in range(n)]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[radix_sort_queue],
        sizes=sizes,
        data_generator=data_generator,
        title="Radix Sort Performance",
        ylabel="Time (seconds) - O(N)"
    )