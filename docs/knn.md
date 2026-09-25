# KNN with Euclidean Distance (`knn.py`)

This document provides a detailed breakdown of the standard **K-Nearest Neighbors (KNN)** implementation in [`knn.py`](../knn.py), utilizing **Euclidean Distance** ($L_2$ norm) as the similarity metric.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Mathematical Formulation](#mathematical-formulation)
- [Dataset & Features Used](#dataset--features-used)
- [Code Implementation Breakdown](#code-implementation-breakdown)
- [How to Run](#how-to-run)
- [Sample Input & Output](#sample-input--output)
- [Main README](#main-readme)

---

## 📖 Overview

[`knn.py`](../knn.py) is the baseline implementation of the K-Nearest Neighbors classifier. It calculates the direct straight-line distance between a user-provided input query $(x_1, x_2)$ and all recorded data points in the Iris dataset.

---

## 📐 Mathematical Formulation

Euclidean distance calculates the shortest straight-line distance between two points in $n$-dimensional Euclidean space:

$$d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}$$

For two 2D points $P = (x_1, x_2)$ and $Q = (y_1, y_2)$:

$$d(P, Q) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$$

In Python (`math.sqrt`):
```python
euclidean_dist = math.sqrt((x1 - float(row['x1']))**2 + (x2 - float(row['x2']))**2)
```

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
   - Verifies the file extension is `.csv`.
   - Uses `csv.DictReader` to map `sepal_length`, `sepal_width`, and `species` into structured dictionaries.

2. **User Input Validation**:
   - Takes `sepal_length` and `sepal_width` as floating-point inputs.
   - Handles `ValueError` gracefully if the user enters non-numeric text.

3. **Distance Calculation Loop**:
   - Iterates through all 150 records in the dataset.
   - Computes Euclidean distance to the query point.
   - Stores pairs of `(distance, species)`.

4. **Nearest Neighbor Selection**:
   - Sorts candidate distances in ascending order (`distances.sort(key=lambda x: x[0])`).
   - Slices the top $k$ nearest elements (`neighbors = distances[:k]`).

5. **Majority Voting**:
   - Counts frequency of each species in the top $k$ neighbors using a dictionary `votes`.
   - Determines winner with `max(votes, key=votes.get)`.

---

## 🚀 How to Run

```bash
python knn.py
```

---

## 💻 Sample Input & Output

```text
Enter the data to get predicted species: 
Enter sepal length: 5.0
Enter sepal width: 3.4
Enter the number of nearest neighbors: 5

Nearest neighbors
Distance: 0.0, Species: setosa
Distance: 0.10000000000000053, Species: setosa
Distance: 0.10000000000000053, Species: setosa
Distance: 0.14142135623730964, Species: setosa
Distance: 0.14142135623730964, Species: setosa

Votes: {'setosa': 5}

Predicted species: setosa
```

---

## 🔗 Main README

Return to the root [README.md](../README.md).
