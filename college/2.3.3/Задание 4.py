print('''Эта программа вычисляет сумму всех положительных и сумму всех отрицательных значений в введённой последовательности.
      Введите 0, чтобы закончить ввод
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

a = None
PositiveNumbers = []
NegativeNumbers = []
AllNumbers = []
while True:
    a = UserInput('Введите число: ',int)
    if a == 0:
        break
    AllNumbers.append(a)
    if a > 0:
        PositiveNumbers.append(a)
    elif a<0:
        NegativeNumbers.append(a)

print(f'''Введённые значения: {', '.join(map(str, AllNumbers))}
Сумма положительных: {sum(PositiveNumbers)}
Сумма отрицательныъ: {sum(NegativeNumbers)}
      ''')