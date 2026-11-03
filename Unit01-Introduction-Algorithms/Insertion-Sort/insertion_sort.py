import sys
import os
import random
from pathlib import Path

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def insertion_sort_iterative(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_recursive(arr, n=None):
    if n is None: 
        n = len(arr)
    if n <= 1: 
        return arr
    
    # Recursively sort the first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert the last element into its correct position
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
    return arr

if __name__ == "__main__":
    sizes = [20, 40, 60, 80, 100, 120, 140]
    data_generator = lambda n: [random.randint(0, 10000) for _ in range(n)]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[insertion_sort_iterative, insertion_sort_recursive],
        sizes=sizes,
        data_generator=data_generator,
        title="Insertion Sort Performance"
    )