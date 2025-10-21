print('''Эта программа находит сумму всех чётных чисел на указанном отрезке.
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

LowerBound = UserInput('Введите значение нижнего предела: ', int)
UpperBound = UserInput('Введите значение верхнего предела: ', int)
EvenValues = []
for w in range(LowerBound, UpperBound):
    if w%2 == 0:
        EvenValues.append(w)
print(f'''Все чётные значения этого предела: {', '.join(map(str, EvenValues))}
Их сумма: {sum(EvenValues)}
      ''')