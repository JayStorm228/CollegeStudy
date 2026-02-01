from random import randint as r

import F1_20 as F

Rows = r(1, 10)
Cols = r(1, 10)
Matrix1 = F.np.random.randint(1, 10, (Rows, Cols))
Matrix2 = F.np.random.randint(1, 10, (Rows, Cols))
Result = F.elementwise_multiply_2d(Matrix1, Matrix2)
print(
    f"{Rows=}, {Cols=}\nMatrix 1 = \n{Matrix1}\n\nMatrix2 = \n{Matrix2}\n\nResult = \n{Result}"
)
