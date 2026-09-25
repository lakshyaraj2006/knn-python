# KNN with Bray-Curtis Distance (`knn_bray_curtis.py`)

This document describes the implementation of the **K-Nearest Neighbors (KNN)** classifier in [`knn_bray_curtis.py`](../knn_bray_curtis.py), using the **Bray-Curtis Dissimilarity** metric.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Mathematical Formulation](#mathematical-formulation)
- [Key Characteristics of Bray-Curtis](#key-characteristics-of-bray-curtis)
- [Dataset & Features Used](#dataset--features-used)
- [Code Implementation Breakdown](#code-implementation-breakdown)
- [How to Run](#how-to-run)
- [Sample Input & Output](#sample-input--output)
- [Main README](#main-readme)

---

## 📖 Overview

[`knn_bray_curtis.py`](../knn_bray_curtis.py) demonstrates non-Euclidean classification using the **Bray-Curtis Dissimilarity** index, widely used in ecology, bio-statistics, and abundance data analysis. It evaluates relative differences normalized by total magnitude.

---

## 📐 Mathematical Formulation

The Bray-Curtis dissimilarity between vectors $\mathbf{u}$ and $\mathbf{v}$ is defined as:

$$d(u, v) = \frac{\sum_{i=1}^{n} |u_i - v_i|}{\sum_{i=1}^{n} |u_i + v_i|}$$

For two 2D points $A = [x_1, x_2]$ and $B = [y_1, y_2]$ with non-negative values:

$$d(A, B) = \frac{|x_1 - y_1| + |x_2 - y_2|}{|x_1 + y_1| + |x_2 + y_2|}$$

In Python:
```python
def bray_curtis(a, b):
    numerator = 0
    denominator = 0

    for x, y in zip(a, b):
        numerator += abs(x - y)
        denominator += abs(x + y)

    return numerator / denominator
```

---

## 🌟 Key Characteristics of Bray-Curtis

- **Bounded Range**: When all feature values are non-negative ($x_i \ge 0$), the dissimilarity is strictly bounded in the range $[0, 1]$.
  - $0$: Identical samples.
  - $1$: Maximum dissimilarity (no overlap).
- **Scale Normalization**: Automatically scales differences against the magnitude of coordinate sums.

---

## 📊 Dataset & Features Used

- **Dataset File**: [`custom_iris.csv`](../custom_iris.csv) (curated Iris sample subset)
- **Features Used**:
  - `x1`: `sepal_length` (float)
  - `x2`: `sepal_width` (float)
- **Target Class**: `species` (`Setosa`, `Versicolor`, `Virginica`)

---

## 🔍 Code Implementation Breakdown

1. **`bray_curtis(a, b)` Function**:
   - Takes two vector lists `a` and `b`.
   - Uses `zip(a, b)` to aggregate absolute differences into `numerator` and absolute sums into `denominator`.
   - Returns `numerator / denominator`.

2. **Dataset Loading**:
   - Loads [`custom_iris.csv`](../custom_iris.csv) into structured dictionaries with `sepal_length`, `sepal_width`, and `species`.

3. **Query Point Construction & Distance Loop**:
   - Constructs query list `query = [x1, x2]`.
   - Iterates over each point `[float(row["x1"]), float(row["x2"])]` and calls `bray_curtis()`.

4. **K-Nearest Neighbors & Voting**:
   - Sorts distances ascendingly.
   - Extracts top $k$ nearest instances.
   - Tally class frequencies and announces the winning species.

---

## 🚀 How to Run

```bash
python knn_bray_curtis.py
```

---

## 💻 Sample Input & Output

```text
Enter the data to get predicted species: 
Enter sepal length: 5.2
Enter sepal width: 3.5
Enter the number of nearest neighbors: 3

Nearest neighbors
Distance: 0.019417475728155338, Species: Setosa
Distance: 0.021505376344086023, Species: Setosa
Distance: 0.022727272727272728, Species: Setosa

Votes: {'Setosa': 3}

Predicted species: Setosa
```

---

## 🔗 Main README

Return to the root [README.md](../README.md).
