import numpy as np
from scipy.linalg import qr

A = np.array([[ЧИСЛА], [ЧИСЛА], [ЧИСЛА]], dtype=float)

# Выполняем QR-разложение с поворотом (pivoting=True)

# P возвращается как массив индексов, преобразуем его в матрицу перестановок
P_matrix = np.eye(A.shape[1])[P]
