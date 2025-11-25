import numpy as np

print(
    """"Эта программа
"""
)

Matrix = np.random.randint(1, 21, (5, 5))
MainDiag = ""
OffDiag = ""
for w in range(Matrix.shape[0]):
    MainDiag += ", ".join(map(str, Matrix.diagonal(offset=w))) + ", "
    OffDiag += ", ".join(map(str, Matrix.diagonal(offset=-w - 1))) + ", "
print(
    f"""Матрица: \n{Matrix}\n
Элементы главной диагонали и выше: {MainDiag.rstrip(', ')}
Элементы ниже главное диагонали: {OffDiag.strip(', ')}
"""
)
input("\nНажмите ENTER, чтобы выйти.")
