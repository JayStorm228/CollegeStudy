import numpy as np
import sys
import os

try:
    from CollegeStudy.Code.Mods.custom_assertions import *
except ImportError:
    pass

# всё что идёт для принта - для импорта модуля)
current_file = os.path.abspath(__file__)
repo_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
mods_path = os.path.join(repo_root, "Mods")
if mods_path not in sys.path:
    sys.path.insert(0, mods_path)
try:
    from custom_assertions import *
except ImportError as e:
    print(f"Модуль custom_assertions не найден: {e}")
    exit()


Matrix = np.random.randint(1, 40, (5, 5))

print(f"Созданная матрица: \n{Matrix}\n")
LowerBound = UserInput("Введите нижний предел диапозона: ", int)
UpperBound = UserInput("Введите верхний предел диапозона: ", int)

Matrix[Matrix > UpperBound] = 0
Matrix[Matrix < LowerBound] = 0
print(f"Неподходящие значения заменены нулевыми: \n{Matrix}\n")

for w in range(Matrix.shape[0]):
    zeros = len(np.where(Matrix[w, :] == 0)[0])
    Sum = sum(Matrix[w, :])
    Len = Matrix[w, :].shape[0] - zeros
    if Len != 0:
        print(f"Среднее арифметическое {w+1} строки: {Sum/Len}")
    else:
        print(f"В строке {w+1} нет подходящих значений")
input("Нажмите Enter чтобы выйти")
