import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def dfs_traversal(data):
    V, adj_list, start_node = data
    
    visited = [False] * V
    traversal_order = []
    
    # Use an explicit stack (list) instead of system recursion
    stack = [start_node]
    
    while stack:
        # Pop the last element from the stack
        node = stack.pop()
        
        if not visited[node]:
            visited[node] = True
            traversal_order.append(node)
            
            # Push neighbors to stack
            # Reversing ensures we visit in the same order as recursive DFS
            for neighbor in reversed(adj_list[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)
                    
    return traversal_order

def generate_graph_data(v):
    # Generate an adjacency list for a connected graph
    adj_list = [[] for _ in range(v)]
    
    # First, create a linear path to ensure all vertices are reachable
    for i in range(v - 1):
        adj_list[i].append(i + 1)
        adj_list[i + 1].append(i)
        
    # Then add additional random edges to simulate a more complex graph
    for _ in range(v):
        u = random.randint(0, v - 1)
        w = random.randint(0, v - 1)
        if u != w:
            adj_list[u].append(w)
            adj_list[w].append(u)
            
    return (v, adj_list, 0)

if __name__ == "__main__":
    # O(V + E) allows for large datasets
    sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[dfs_traversal],
        sizes=sizes,
        data_generator=generate_graph_data,
        title="DFS Performance",
        ylabel="Time (seconds) - O(V + E)"
    )