import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *
print('''Эта программа создаёт список случайных значений, в который вы можете вставить целое число.
      После чего список будет отсортирован по возрастанию.
      ''')
a = CreateRandomList(UserInput('Введите размер списка: ', int), [0, 10], int)
print(f'Исходный список: {a}')
Number = UserInput('Введите число, которое хотите вставить в этот список: ', int)
a.append(Number)
print(f'Отсортированный список: {sorted(a)}')



    
