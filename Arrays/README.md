# Array

This folder contains the following Python code files:

- [RemoveDuplicates](removeduplicates.py)
- [Distinctaverages](distinctaverages.py)

---
# List Operations and Their Time Complexity

| Operation                 | Time Complexity |
|---------------------------|----------------|
| **Access (indexing)**     | `O(1)`         |
| **Append (add to end)**   | `O(1)`         |
| **Insert (middle/begin)** | `O(n)`         |
| **Pop (remove last)**     | `O(1)`         |
| **Pop (remove at index)** | `O(n)`         |
| **Remove (by value)**     | `O(n)`         |
| **Search (by value)**     | `O(n)`         |
| **Sort**                  | `O(n log n)`   |
| **Reverse**               | `O(n)`         |
| **Concatenation (`+`)**   | `O(n + m)`     |
| **Extend (`.extend()`)**  | `O(m)`         |
| **Copy (`.copy()`)**      | `O(n)`         |
| **Count occurrences**     | `O(n)`         |
| **Slice (`lst[a:b]`)**    | `O(b - a)`     |
| **Clear (`.clear()`)**    | `O(n)`         |


# Techniques to solve problems in List (array)

| Technique            | Best for Problems Related to         | Time Complexity  |
|----------------------|------------------------------------|------------------|
| **Brute Force**      | Small constraints, simple cases   | `O(n^2)` or worse |
| **Two Pointers**     | Sorted arrays, pair/triplet sum problems | `O(n)` |
| **Sliding Window**   | Contiguous subarrays, max/min sum problems | `O(n)` |
| **Hashing**         | Checking duplicates, missing elements | `O(n)` |
| **Kadane's Algorithm** | Maximum sum subarray problems | `O(n)` |
| **Binary Search**    | Searching in sorted/rotated arrays | `O(log n)` |
---