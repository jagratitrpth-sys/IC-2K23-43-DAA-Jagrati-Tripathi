import sys
from pathlib import Path
import random
from collections import deque

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def bfs_traversal(data):
    V, adj_list, start_node = data
    
    visited = [False] * V
    queue = deque([start_node])
    visited[start_node] = True
    
    traversal_order = []
    
    while queue:
        # Dequeue a vertex from queue
        current = queue.popleft()
        traversal_order.append(current)
        
        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent vertex has not been visited, mark it visited and enqueue it
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
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
            
    return (v, adj_list, 0)  # Returning (Vertices, Adjacency List, Start Node)

if __name__ == "__main__":
    # O(V + E) allows for large datasets
    sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[bfs_traversal],
        sizes=sizes,
        data_generator=generate_graph_data,
        title="BFS Performance",
        ylabel="Time (seconds) - O(V + E)"
    )