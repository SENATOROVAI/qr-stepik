from scipy.linalg import lstsq

X = np.array([[ЧИСЛА], [ЧИСЛА], [ЧИСЛА]], dtype=float)
y = np.array([ЧИСЛА], dtype=float)

beta_lstsq, residuals, rank, singular_values = lstsq('gelsy')
