print('''Эта программа вычисляет период, через который ваш вклад превысит 1 млн рублей
      Программа выведет сам период(года), и итоговое значение вклада
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

# формула сложных процентов: S = P * (1+r)^n
# S - Значение к концу срока
# p - Начальный вклад
# r - Ставка за период(год)
# n - количество периодов(годы)

P = UserInput('Введите ваш начальный вклад: ', int)
r = UserInput('Введите вашу процентную ставку: ', int) / 100
S = P
n = 1
while S < 1000000:
    S = P * (1+r)**n
    n+=1
else: n-=1
print(f''' Ваш первоначальный вклад был: {P}
Ваша процентная ставка: {r}
Срок, через который итоговый вклад превысил 1млн рублей: {n}
Итоговый вклад при этом составил: {round(S, 2)}
      ''')