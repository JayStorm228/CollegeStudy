print('''Эта программа генерирует две случайные базы данных из 10 диаметров и 10 весов шин, а затем находит все пары шин, для которых разница в диаметре не превышает D, а разница в весе не превышает W.''')

import sys
import os
import random as r
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *

Weight = tuple()
Diametr = tuple()

while len(Weight) !=10 and len(Diametr) != 10:
    Weight+=(r.randint(10, 30),)
    Diametr+=(r.randint(10, 30),)

D = UserInput('Введите число D: ', int)
W = UserInput('Введите число W: ', int)

Output1 = []
Output2 = []

for i in range(len(Diametr)):
    for j in range(i+1, len(Diametr)):
        exp1 = abs(Diametr[i] - Diametr[j]) <= D
        exp2 = abs(Weight[i] - Weight[j]) <= W
        if exp1 and exp2: 
            Output1.append([Diametr[i], Weight[i]])
            Output2.append([Diametr[j], Weight[j]])
for w in range(len(Output1)-1):
    print(f'''Удовлетворяющая пара №{w+1}:
    Вес1: {Output1[w][1]}, Диаметр1: {Output1[w][0]}
    Вес2: {Output2[w][1]}, Диаметр2: {Output2[w][0]}
''')
input('Нажмите ENTER, чтобы выйти.')
