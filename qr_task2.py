import numpy as np
def gram_schmidt(A):
    """Perform QR factorization using the Gram-Schmidt process."""
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        # Orthogonalization
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
       
        # Forming Q and R matrices
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R

A = np.array([[числа], [числа], [числа]])

print((Q @ R) == A)
