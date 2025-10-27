print('''Эта программа попытается удалить первые попадающиеся четыре нулевых значения из списка
''')
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Mods')))
from custom_assertions import *

Array = CreateList(UserInput('Введите размер списка: ', int), float)
for w in range(3):
    Array.remove(0)
print(f'Изменённый список: {Array}')

input('Нажмите ENTER, чтобы выйти.')
