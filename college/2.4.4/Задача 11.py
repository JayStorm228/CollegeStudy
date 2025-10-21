print('''Эта программа попытается удалить первые попадающиеся четыре нулевых значения из списка
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

Array = CreateList(UserInput('Введите размер списка: ', int), float)
for w in range(3):
    Array.remove(0)
print(f'Изменённый список: {Array}')

input('Нажмите ENTER, чтобы выйти.')
