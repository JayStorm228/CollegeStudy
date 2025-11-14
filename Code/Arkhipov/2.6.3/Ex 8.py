import numpy as np

Matrix = np.random.randint(1, 51, (5, 5))
print(
    f"""Матрица: \n{Matrix}\n
Главная диагональ: {Matrix.diagonal()}
Побочная диагональ: {Matrix[np.arange(Matrix.shape[0]), Matrix.shape[0] - 1 - np.arange(Matrix.shape[0])]}
      """
)
