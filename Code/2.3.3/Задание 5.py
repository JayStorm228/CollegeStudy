print('''Эта программа вычисляет сумму всех введённых целых положительных чисел вплоть до первого введённого отричательного числа.
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

PositiveNumbers = []
a = 1
while True:
    a = UserInput('Введите число: ', int)
    if a < 0:
        break
    elif a > 0:
        PositiveNumbers.append(a)
    else: print('Вы ввели ноль.')
print(f'''Введённые положительные значения: {', '.join(map(str, PositiveNumbers))}
Сумма всех положительных элементов: {sum(PositiveNumbers)}
      ''')