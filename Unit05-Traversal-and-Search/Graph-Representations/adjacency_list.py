import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def build_adjacency_list(data):
    V, edges = data
    # Initializing an array of V empty lists takes O(V) time
    adj_list = [[] for _ in range(V)]
    
    # Adding edges takes O(E) time
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Undirected graph
        
    return adj_list

def generate_graph_data(v):
    edges = []
    for _ in range(v * 2):
        edges.append((random.randint(0, v - 1), random.randint(0, v - 1)))
    return (v, edges)

if __name__ == "__main__":
    # We can use much larger input sizes here because O(V + E) is highly efficient
    sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[build_adjacency_list],
        sizes=sizes,
        data_generator=generate_graph_data,
        title="Adjacency List Construction",
        ylabel="Time (seconds) - O(V + E)"
    )