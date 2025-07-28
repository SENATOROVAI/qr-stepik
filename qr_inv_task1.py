X = np.array([[ЧИСЛО], [ЧИСЛО], [ЧИСЛО]], dtype=float)
y = np.array([ЧИСЛО], dtype=float)

beta1 = Обратная_матрица(R) @ Q.T @ y

beta2 = np.linalg.solve(R, QTy)

beta1 == beta2
