print('''Эта программа принимает на ввод критическое число.
      После чего считает сумму всех введённых чисел, до тех пор пока она не превышает критическое значение.
      Программа выводит количество чисел, которое потребовалось, чтобы превысить критическое значение
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

CriticalNumber = UserInput('Введите критическое значение: ',float)
Sum = 0 
counter = 0

while Sum <= CriticalNumber:
    Number = UserInput('Введите число: ', float)
    Sum+=Number
    counter+=1

print(f'''
Итоговая сумма: {Sum}
Количество значений, которое потребовалось ввести: {counter}
      ''')