import sys
import os
import random

# 1. Manually build the path going up two directories
current_dir = os.path.dirname(os.path.abspath(__file__))
unit_dir = os.path.dirname(current_dir)
root_dir = os.path.dirname(unit_dir)

# 2. Force it to the very front of Python's search path
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# 3. DIAGNOSTIC CHECK: Let's see exactly what Python sees!
print("--- DEBUG INFO ---")
print(f"Looking in: {root_dir}")
if os.path.exists(root_dir):
    print(f"Files found here: {os.listdir(root_dir)}")
print("------------------\n")

# Now attempt the import
from Complexity_analyser import PerformanceAnalyzer

def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_recursive(arr, n=None):
    if n is None: n = len(arr)
    if n <= 1: return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
    return bubble_sort_recursive(arr, n - 1)

if __name__ == "__main__":
    # Define test parameters
    sizes = [20, 40, 60, 80, 100, 120, 140]
    
    # Lambda function to tell the analyzer how to generate random arrays
    data_generator = lambda n: [random.randint(0, 10000) for _ in range(n)]
    
    # Run the analyzer dynamically
    PerformanceAnalyzer.run_and_plot(
        algorithms=[bubble_sort_iterative, bubble_sort_recursive],
        sizes=sizes,
        data_generator=data_generator,
        title="Bubble Sort Performance"
    )