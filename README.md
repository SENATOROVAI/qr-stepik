# stepik: https://stepik.org/a/248961

# QR Factorization Solver — Course & Implementation

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Website](https://img.shields.io/badge/website-live-blue.svg)](https://senatorovai.github.io/QR-decomposition-solver-course/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18818738.svg)](https://doi.org/10.5281/zenodo.18820512)

> 🚀 Professional implementation of **QR Factorization** with mathematical derivation and Python solver.

---

## 🔥 Project Overview

This repository contains a **complete course-style implementation** of QR Factorization including:

- Mathematical derivation
- Geometric interpretation
- Gram–Schmidt algorithm
- Modified Gram–Schmidt
- Householder reflections
- Numerical stability analysis
- Python implementation from scratch

---

## Keywords

```

qr factorization
qr decomposition
qr solver python
qr factorization from scratch
numerical linear algebra
matrix decomposition
householder transformation
gram schmidt orthogonalization
least squares qr
linear algebra course

```

---

## 📚 Mathematical Definition

QR Factorization decomposes a matrix:

$$
A \in \mathbb{R}^{m \times n}
$$

into:

$$
A = QR
$$

Where:

- $$Q \in \mathbb{R}^{m \times m}$$ — orthogonal matrix  
  Q^T Q = I
- $$R \in \mathbb{R}^{m \times n}$$ — upper triangular matrix  

---

## 🧠 Geometric Meaning

QR Factorization represents:

- Rotation / reflection of vectors
- Orthogonal basis construction
- Projection onto orthonormal space

Householder transformation:

$$
H = I - 2vv^T
$$

Used for stable QR computation.

---

## ⚡ Applications

QR Factorization is used in:

- Solving linear systems
- Least squares problems
- Eigenvalue algorithms (QR algorithm)
- Machine learning optimization
- Numerical stability improvement

---

## 🏗 Project Structure

```

qr-factorization-solver/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── src/
│   ├── qr_gram_schmidt.py
│   ├── qr_modified.py
│   ├── qr_householder.py
│
├── examples/
│   └── demo.py
│
├── docs/
│   ├── theory.md
│   ├── stability.md
│
├── images/
│   └── qr_geometry.png
│
└── index.html

````

---

## 🐍 Example Implementation — Gram-Schmidt

```python
import numpy as np

def qr_gram_schmidt(A):
    A = A.astype(float)
    m, n = A.shape

    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for k in range(n):
        v = A[:, k]

        for j in range(k):
            R[j, k] = np.dot(Q[:, j], A[:, k])
            v = v - R[j, k] * Q[:, j]

        R[k, k] = np.linalg.norm(v)
        Q[:, k] = v / R[k, k]

    return Q, R
````

---

## 🚀 Installation

```bash
pip install -r requirements.txt
```

Run example:

```bash
python examples/demo.py
```
