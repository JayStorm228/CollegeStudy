print('''Эта программа вычисляет сумму всех введённых не равных нулю чисел
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

AllNumbers = []
a = None
while True:
    a = UserInput('Введите число: ', float)
    if a == 0:
        print('Вы ввели ноль! Ввод чисел завершён')
        break
    else: AllNumbers.append(a)
print(f'''Введённые числа: {', '.join(map(str, AllNumbers))}
Их сумма: {sum(AllNumbers)}
      ''')