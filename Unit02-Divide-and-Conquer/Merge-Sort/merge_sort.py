import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

if __name__ == "__main__":
    # N log N is highly efficient, so we test with larger inputs
    sizes = [1000, 5000, 10000, 20000, 30000, 40000, 50000]
    
    data_generator = lambda n: [random.randint(0, 10000) for _ in range(n)]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[merge_sort],
        sizes=sizes,
        data_generator=data_generator,
        title="Merge Sort Performance",
        ylabel="Time (seconds) - O(N log N)"
    )