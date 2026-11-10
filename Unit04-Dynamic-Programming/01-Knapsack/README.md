# 0/1 Knapsack Problem

## 📝 Problem Statement
Given a set of items, each with a weight and a value, determine the maximum value that can be accommodated in a knapsack of a fixed capacity. Unlike the Fractional Knapsack problem, items cannot be broken into smaller pieces; you must either take an entire item or leave it (0 or 1).

## 💡 Algorithm / Approach
The 0/1 Knapsack problem cannot be optimally solved using a Greedy approach. Instead, it is solved using **Dynamic Programming**. 
1. Create a 2D tabulation array `K[n+1][W+1]` where `n` is the number of items and `W` is the capacity.
2. The state `K[i][w]` represents the maximum value that can be attained with the first `i` items and a maximum weight of `w`.
3. For each item, decide whether to:
   * **Include it:** Add its value to the optimal subproblem solution for the remaining weight (`value[i] + K[i-1][w-weight[i]]`).
   * **Exclude it:** Carry forward the optimal solution without the item (`K[i-1][w]`).
4. Take the maximum of the two choices. The final answer resides at `K[n][W]`.

## 📜 Pseudocode
```text
Procedure 01Knapsack(items, capacity)
    n = length(items)
    Initialize 2D array K of size (n + 1) x (capacity + 1) to 0
    
    For i = 1 to n
        For w = 1 to capacity
            weight = items[i-1].weight
            value = items[i-1].value
            
            If weight <= w Then
                K[i][w] = max(value + K[i-1][w - weight], K[i-1][w])
            Else
                K[i][w] = K[i-1][w]
            End If
        End For
    End For
    
    Return K[n][capacity]
End Procedure


```
![0-1 Knapsack (dp) Performance Graph](./0-1_knapsack_(dp)_performance_graph.png)