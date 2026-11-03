import sys
import os
import random
from pathlib import Path

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    sizes = [20, 40, 60, 80, 100, 120, 140]
    data_generator = lambda n: [random.randint(0, 10000) for _ in range(n)]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[selection_sort],
        sizes=sizes,
        data_generator=data_generator,
        title="Selection Sort Performance"
    )