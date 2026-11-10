# Unit 5: Graph Traversals and Search

This unit covers the foundational methods for storing and exploring graph data structures in memory. Efficient graph traversal is the prerequisite for solving complex network problems, ranging from pathfinding and cycle detection to topological sorting.

## 🗂️ Algorithms Implemented

### Graph Representations
- [Adjacency Matrix & Adjacency List](./Graph-Representations/) - Benchmarks the stark $O(V^2)$ vs $O(V + E)$ memory allocation and construction differences when representing dense versus sparse graphs.

### Search & Traversal Algorithms
- [Breadth-First Search (BFS)](./BFS/) - $O(V + E)$ complexity, explores the graph level-by-level using a FIFO Queue. Optimal for finding the shortest path in unweighted graphs.
- [Depth-First Search (DFS)](./DFS/) - $O(V + E)$ complexity, explores as far as possible along each branch before backtracking using a LIFO Stack (implemented via recursion). Optimal for cycle detection and maze solving.

## 📊 Core Benchmarking Engine
The performance analysis across these algorithms utilizes a modular Python engine located at the repository root. It executes the algorithm functions dynamically, measures precise hardware execution time, and plots the theoretical vs. experimental curves using `matplotlib`.