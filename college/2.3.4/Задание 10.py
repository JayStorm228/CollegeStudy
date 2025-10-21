print('''Эта программа вычисляет идеальный вес для взрослых людей по формуле:
    Идеальный вес = Рост - 100
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

while True:
    Height = UserInput('Введите значение вашего роста(см): ',int)
    if Height == 250:
        print('Вы вышли из программы.')
        break
    else:
        print(f'Ваш идеальный вес: {Height-100}')