import sys
from pathlib import Path

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def binary_search_iterative(arr):
    target = -1  # Target not in array forces worst-case O(log N)
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr):
    target = -1 
    
    def _recursive_helper(a, low, high, t):
        if low > high:
            return -1
        mid = (low + high) // 2
        if a[mid] == t:
            return mid
        elif a[mid] < t:
            return _recursive_helper(a, mid + 1, high, t)
        else:
            return _recursive_helper(a, low, mid - 1, t)
            
    return _recursive_helper(arr, 0, len(arr) - 1, target)

if __name__ == "__main__":
    # Massive input sizes needed to visualize logarithmic time
    sizes = [10000, 50000, 100000, 500000, 1000000, 2500000, 5000000]
    
    # Binary Search REQUIRES a sorted array
    data_generator = lambda n: list(range(n))
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[binary_search_iterative, binary_search_recursive],
        sizes=sizes,
        data_generator=data_generator,
        title="Binary Search Performance",
        ylabel="Time (seconds) - O(log N)"
    )