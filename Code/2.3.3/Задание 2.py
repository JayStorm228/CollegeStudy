print('''Эта программа находит количество положительных значений в вещественной последовательности чисел, а также минимальное из них.
      Введите число 5, чтобы прекратить ввод последовательности и получить ответ.
      ''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *
a = None
output = []

while True:
    if a == 5:
        break
    a = UserInput('Введите число: ',float)
    if a > 0:
        output.append(a)
    
print(f'''
Количество положительных значений, среди введённых: {len(output)}
Минимальное из них: {min(output)}
      ''')