# Unit 6: Backtracking

## 📝 Overview
Backtracking is a systematic algorithmic technique for solving computational problems, particularly constraint satisfaction problems. It incrementally builds candidates for the solutions and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## 🧠 Core Concepts

### 1. State-Space Tree
The set of all possible configurations (states) of a problem is represented as a tree. The root represents the initial state (an empty solution), and branches represent choices made at each step.

### 2. Bounding Function (Pruning)
A rule or condition used to evaluate if a current node can lead to a valid solution. If the bounding function determines it cannot, the entire subtree rooted at that node is "pruned" (ignored), saving massive amounts of computational time compared to a brute-force approach.

### 3. Node Terminology
* **Live Node:** A node that has been generated but whose children have not yet been fully explored.
* **E-Node (Expanded Node):** The live node currently being explored to generate children.
* **Dead Node:** A generated node that is either not to be expanded further (because it was pruned) or whose children have all been completely explored.

## 🔍 Standard Backtracking Problems
* **N-Queens Problem:** Placing $N$ queens on an $N \times N$ chessboard such that no two queens attack each other.
* **Sum of Subsets:** Finding all subsets of a given set whose elements sum to a specific target value.
* **Graph Coloring (m-Coloring):** Coloring the vertices of a graph using at most $m$ colors such that no two adjacent vertices share the same color.
* **Hamiltonian Cycle:** Finding a closed loop in a graph that visits every vertex exactly once.

## ⏱️ Computational Complexity
Because Backtracking fundamentally relies on exploring combinations or permutations, the worst-case time complexity is typically **exponential** (e.g., $O(2^N)$ for subsets) or **factorial** (e.g., $O(N!)$ for permutations like N-Queens). While bounding functions significantly improve average performance, the theoretical upper bound remains high.