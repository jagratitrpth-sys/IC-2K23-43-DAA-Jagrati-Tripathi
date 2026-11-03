# Unit 1: Introduction to Algorithms

This unit covers the foundational concepts of algorithmic design, analyzing asymptotic complexity (Big-O, Big-Omega, Big-Theta), and implementing elementary sorting and searching techniques. 

All algorithms in this unit are benchmarked using a custom `Complexity_analyser.py` engine to compare theoretical time complexities with experimental execution times.

## 🗂️ Algorithms Implemented

### Sorting Algorithms
* [Bubble Sort](./Bubble-Sort/) - $O(N^2)$ complexity, implemented iteratively and recursively.
* [Selection Sort](./Selection-Sort/) - $O(N^2)$ complexity, minimizes the number of swaps.
* *(Pending)* [Insertion Sort](./Insertion-Sort/) - $O(N^2)$ complexity, efficient for nearly sorted data.

### Searching Algorithms
* *(Pending)* [Linear Search](./Linear-Search/) - $O(N)$ complexity.
* *(Pending)* [Binary Search](./Binary-Search/) - $O(\log N)$ complexity, implemented iteratively and recursively.

## 📊 Core Benchmarking Engine
The performance analysis across these algorithms utilizes a modular Python engine located at the repository root. It executes the sorting functions dynamically, measures precise hardware execution time, and plots the theoretical vs. experimental curves using `matplotlib`.