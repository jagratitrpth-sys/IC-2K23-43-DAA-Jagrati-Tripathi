# Graph Representations: Adjacency Matrix vs. Adjacency List

## 📝 Problem Statement
Before a graph can be traversed or processed (e.g., BFS, DFS, Dijkstra's), it must be represented in memory. The two most common representations are the Adjacency Matrix and the Adjacency List. The choice of representation dictates the time and space complexity of all subsequent graph algorithms.

## 💡 Concepts & Approaches

### 1. Adjacency Matrix
A 2D array `matrix[V][V]` where `V` is the number of vertices. 
* If there is an edge from vertex `i` to vertex `j`, `matrix[i][j] = 1` (or the edge weight).
* Otherwise, `matrix[i][j] = 0`.
* **Best for:** Dense graphs (where $E$ is close to $V^2$) and algorithms that need to quickly check if a specific edge exists (e.g., Prim's or Floyd-Warshall).

### 2. Adjacency List
An array of lists `adj_list[V]` where `adj_list[i]` contains all vertices adjacent to vertex `i`.
* **Best for:** Sparse graphs (where $E$ is much less than $V^2$) and algorithms that need to iterate over all neighbors of a vertex (e.g., BFS, DFS, Kruskal's).

## ⏱️ Time & Space Complexity Analysis

| Operation | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Space Complexity** | $O(V^2)$ | $O(V + E)$ |
| **Construction Time** | $O(V^2)$ | $O(V + E)$ |
| **Check Edge Exists `(u, v)`** | $O(1)$ | $O(\text{degree}(u))$ |
| **Iterate over Neighbors** | $O(V)$ | $O(\text{degree}(u))$ |

## 📊 Experimental Results & Performance Analysis
* **Analysis Tool:** Python (`Complexity_analyser.py`)
* The performance graphs demonstrate the severe allocation cost of a $V \times V$ matrix ($O(V^2)$) compared to the linear allocation of a list array ($O(V + E)$).

![Adjacency Matrix Performance Graph](./adjacency_matrix_construction_performance_graph.png)
![Adjacency List Performance Graph](./adjacency_list_construction_performance_graph.png)

## 🎯 Learning Outcomes
* Proved why Adjacency Lists are the default choice for modern graph algorithms due to memory constraints.
* Visualized the initialization overhead of 2D arrays in Python.