import numpy as np

Matrix = np.random.randint(1, 41, (5, 5))
Size = Matrix.shape[0]
AntiDiag = Matrix[np.arange(Size), Size - 1 - np.arange(Size)]
Max = np.max(AntiDiag)
print(f'''Матрица \n{Matrix}\n
Побочная диагональ: {AntiDiag}
Максимальный элемент диагонали: {Max}
      ''')