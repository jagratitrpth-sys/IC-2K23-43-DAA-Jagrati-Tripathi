import sys
import os
from pathlib import Path

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def linear_search(arr):
    target = -1 # Searching for an element not in the array triggers worst-case O(N)
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    # Larger sizes are needed because O(N) is extremely fast
    sizes = [1000, 5000, 10000, 50000, 100000, 200000, 500000]
    
    # Generate a sequential array for searching
    data_generator = lambda n: list(range(n))
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[linear_search],
        sizes=sizes,
        data_generator=data_generator,
        title="Linear Search Performance",
        ylabel="Time (seconds) - O(N)"
    )