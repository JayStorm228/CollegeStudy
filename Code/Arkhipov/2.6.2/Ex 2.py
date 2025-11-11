print('''Эта программа создаёт матрицу 5х5 со значениями от 1 до 40
После чего находит индексы строк максимальных элементов каждого столбца
''')
import numpy as np

Matrix = np.random.randint(1, 41, (5, 5))
IndexSum = np.sum(np.indices(Matrix.shape), axis=0)
Indexes = np.transpose(np.where(IndexSum == 4))
Sum = 0
for w in Indexes:
   Sum+=Matrix[tuple(w)] 
print(f'''Матрица: \n{Matrix}\n
Элементы: {Matrix[IndexSum==4]}
Их Сумма: {Sum}
      ''')

