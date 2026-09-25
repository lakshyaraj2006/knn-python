# KNN with Jaccard Distance (`knn_jaccard.py`)

This document describes the implementation of the **K-Nearest Neighbors (KNN)** classifier in [`knn_jaccard.py`](../knn_jaccard.py), using **Jaccard Distance** alongside continuous-to-binary feature thresholding.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Feature Binarization](#feature-binarization)
- [Mathematical Formulation](#mathematical-formulation)
- [Dataset & Features Used](#dataset--features-used)
- [Code Implementation Breakdown](#code-implementation-breakdown)
- [How to Run](#how-to-run)
- [Sample Input & Output](#sample-input--output)
- [Main README](#main-readme)

---

## 📖 Overview

[`knn_jaccard.py`](../knn_jaccard.py) applies the **Jaccard Distance** metric to classify Iris flowers. Because standard Jaccard distance operates on binary indicator attributes or sets, continuous numeric features (`sepal_length` and `sepal_width`) are first transformed into binary flags ($0$ or $1$) via a threshold rule.

---

## 🔢 Feature Binarization

Continuous feature values are converted into binary attributes using the `binarize(x)` function:

$$\text{binarize}(x) = \begin{cases} 1 & \text{if } x \ge 5.0 \\ 0 & \text{if } x < 5.0 \end{cases}$$

In Python:
```python
def binarize(x):
    return 1 if x >= 5 else 0
```

---

## 📐 Mathematical Formulation

### 1. Jaccard Similarity Coefficient ($J$)
Measures the ratio of the size of intersection to the size of union between binary vectors $A$ and $B$:

$$J(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{\sum_{i=1}^n (A_i \land B_i)}{\sum_{i=1}^n (A_i \lor B_i)}$$

### 2. Jaccard Distance ($d_J$)
Represents the dissimilarity (complement of similarity):

$$d_J(A, B) = 1 - J(A, B) = 1 - \frac{|A \cap B|}{|A \cup B|}$$

In Python:
```python
def jaccard_distance(a, b):
    intersection = 0
    union = 0

    for x, y in zip(a, b):
        if x == 1 and y == 1:
            intersection += 1

        if x == 1 or y == 1:
            union += 1

    return 1 - (intersection / union)
```

---

## 📊 Dataset & Features Used

- **Dataset File**: [`iris.csv`](../iris.csv) (150 total records)
- **Features Used**:
  - `x1`: `sepal_length` $\rightarrow$ Binarized (`1` if $\ge 5.0$, else `0`)
  - `x2`: `sepal_width` $\rightarrow$ Binarized (`1` if $\ge 5.0$, else `0`)
- **Target Class**: `species` (`setosa`, `versicolor`, `virginica`)

---

## 🔍 Code Implementation Breakdown

1. **`binarize(x)` & `jaccard_distance(a, b)`**:
   - Converts continuous measurements into boolean states.
   - Computes set-theoretic intersection and union over boolean vectors.
   - Returns distance $1 - (\text{intersection} / \text{union})$.

2. **Dataset Processing**:
   - Parses [`iris.csv`](../iris.csv) using `csv.DictReader`.

3. **Input Transformation**:
   - Accepts floating point user input for `sepal_length` and `sepal_width`.
   - Binarizes the query point: `query = [binarize(x1), binarize(x2)]`.

4. **Distance Evaluation & Classification**:
   - Binarizes each row in the dataset: `point = [binarize(float(row["x1"])), binarize(float(row["x2"]))]`.
   - Computes Jaccard distance between `query` and `point`.
   - Sorts, picks $k$ nearest neighbors, and outputs majority vote.

---

## 🚀 How to Run

```bash
python knn_jaccard.py
```

---

## 💻 Sample Input & Output

```text
Enter the data to get predicted species: 
Enter sepal length: 6.2
Enter sepal width: 3.4
Enter the number of nearest neighbors: 5

Nearest neighbors
Distance: 0.0, Species: setosa
Distance: 0.0, Species: setosa
Distance: 0.0, Species: setosa
Distance: 0.0, Species: setosa
Distance: 0.0, Species: setosa

Votes: {'setosa': 5}

Predicted species: setosa
```

---

## 🔗 Main README

Return to the root [README.md](../README.md).
