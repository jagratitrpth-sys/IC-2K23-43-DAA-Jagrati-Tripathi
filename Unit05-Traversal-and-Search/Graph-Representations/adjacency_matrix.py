import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def build_adjacency_matrix(data):
    V, edges = data
    # Initializing a V x V matrix takes O(V^2) time
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    
    # Adding edges takes O(E) time
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  # Undirected graph
        
    return matrix

def generate_graph_data(v):
    # Generate V vertices and E = V*2 random edges
    edges = []
    for _ in range(v * 2):
        edges.append((random.randint(0, v - 1), random.randint(0, v - 1)))
    return (v, edges)

if __name__ == "__main__":
    # Moderate input sizes due to O(V^2) memory and time allocation
    sizes = [500, 1000, 1500, 2000, 2500, 3000]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[build_adjacency_matrix],
        sizes=sizes,
        data_generator=generate_graph_data,
        title="Adjacency Matrix Construction",
        ylabel="Time (seconds) - O(V^2)"
    )