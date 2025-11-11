import numpy as np

Matrix = np.random.randint(1, 81, (5, 5))
Even = Matrix[Matrix%2==0]
print(f'''Матрица: \n{Matrix}\n
Чётные элементы: {Even}
      ''')