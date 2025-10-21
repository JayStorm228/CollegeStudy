print('''Эта программа находит, каких чисел больше в введённой последовательности целых чисел
      Введите число 1, чтобы закончить ввод
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

while True:
    a = UserInput('Введите число: ',int)    
    if a == 1:
        break
    elif a > 0:
        PositiveNumbers.append(a)
    elif a<0:
        NegativeNumbers.append(a)

if len(PositiveNumbers)>len(NegativeNumbers):
    print(f'Больше Положительных на {len(PositiveNumbers)-len(NegativeNumbers)}')
elif len(PositiveNumbers)<len(NegativeNumbers):
    print(f'Больше отрицательных на {len(NegativeNumbers)-len(PositiveNumbers)}')
else:
    print(f'равное количество тех и других: {len(PositiveNumbers)}')