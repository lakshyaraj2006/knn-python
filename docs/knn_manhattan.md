# KNN with Manhattan Distance (`knn_manhattan.py`)

This document describes the implementation of the **K-Nearest Neighbors (KNN)** classifier in [`knn_manhattan.py`](../knn_manhattan.py), using **Manhattan Distance** ($L_1$ norm / City Block distance).

---

## 📌 Table of Contents
- [Overview](#overview)
- [Mathematical Formulation](#mathematical-formulation)
- [Euclidean vs. Manhattan Comparison](#euclidean-vs-manhattan-comparison)
- [Dataset & Features Used](#dataset--features-used)
- [Code Implementation Breakdown](#code-implementation-breakdown)
- [How to Run](#how-to-run)
- [Sample Input & Output](#sample-input--output)
- [Main README](#main-readme)

---

## 📖 Overview

[`knn_manhattan.py`](../knn_manhattan.py) determines the nearest neighbors by calculating the absolute coordinate differences across feature axes instead of direct diagonal lines. It is particularly useful in grid-like feature spaces or when reducing sensitivity to extreme feature outliers.

---

## 📐 Mathematical Formulation

Manhattan distance (also known as $L_1$ distance or taxicab metric) represents the distance a taxi would travel on a rectangular grid street network:

$$d(p, q) = \sum_{i=1}^{n} |p_i - q_i|$$

For two 2D points $P = (x_1, x_2)$ and $Q = (y_1, y_2)$:

$$d(P, Q) = |x_1 - y_1| + |x_2 - y_2|$$

In Python (`abs()`):
```python
manhattan_dist = abs(x1 - float(row['x1'])) + abs(x2 - float(row['x2']))
```

---

## ⚖️ Euclidean vs. Manhattan Comparison

| Characteristic | Euclidean ($L_2$) | Manhattan ($L_1$) |
| :--- | :--- | :--- |
| **Path Trajectory** | Direct straight line | Axis-parallel step path |
| **Formula** | $\sqrt{\Delta x^2 + \Delta y^2}$ | $\|\Delta x\| + \|\Delta y\|$ |
| **Outlier Sensitivity** | High (squares penalize large deviations) | Moderate (linear penalty) |
| **Computation** | Requires square roots (`math.sqrt`) | Simple addition and `abs()` |

---

## 📊 Dataset & Features Used

- **Dataset File**: [`iris.csv`](../iris.csv) (150 total records)
- **Features Used**:
  - `x1`: `sepal_length` (float)
  - `x2`: `sepal_width` (float)
- **Target Class**: `species` (`setosa`, `versicolor`, `virginica`)

---

## 🔍 Code Implementation Breakdown

1. **Dataset Ingestion (`load_dataset`)**:
   - Reads CSV records using `csv.DictReader`.
   - Extracts `sepal_length`, `sepal_width`, and class `species`.

2. **User Input Validation**:
   - Prompts the user for `sepal_length` ($x_1$) and `sepal_width` ($x_2$).
   - Validates integer input for neighbor count $k$.

3. **Distance Calculation**:
   - Iterates through training points and computes $L_1$ distance using `abs()`.
   - Collects `(manhattan_dist, species)` tuples.

4. **Ranking & Voting**:
   - Sorts distances in ascending order.
   - Slices top $k$ items and tallies class votes.
   - Outputs the winner based on majority count.

---

## 🚀 How to Run

```bash
python knn_manhattan.py
```

---

## 💻 Sample Input & Output

```text
Enter the data to get predicted species: 
Enter sepal length: 6.0
Enter sepal width: 2.8
Enter the number of nearest neighbors: 4

Nearest neighbors
Distance: 0.0, Species: versicolor
Distance: 0.10000000000000009, Species: versicolor
Distance: 0.20000000000000018, Species: versicolor
Distance: 0.20000000000000018, Species: virginica

Votes: {'versicolor': 3, 'virginica': 1}

Predicted species: versicolor
```

---

## 🔗 Main README

Return to the root [README.md](../README.md).
