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

def ols_qr(X, y):
    """Solve OLS regression using QR decomposition."""
    # Perform QR decomposition
    Q, R = gram_schmidt(X)
   
    # Compute Q^T * y
    Qt_y = np.dot(Q.T, y)
   
    # Solve R * beta = Q^T * y using back substitution
    beta = np.zeros(R.shape[1])
    for i in reversed(range(R.shape[1])):
        beta[i] = (Qt_y[i] - np.dot(R[i, i+1:], beta[i+1:])) / R[i, i]
   
    return beta
  
X = np.array([[ЧИСЛА], [ЧИСЛА], [ЧИСЛА], [ЧИСЛА]])
y = np.array([ЧИСЛА])
