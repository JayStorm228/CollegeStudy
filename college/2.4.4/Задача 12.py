print('''Эта программа считает количество знакопеременных пар
''')
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from custom_assertions import *
Size = UserInput('Размер массива: ', int)
Array = CreateRandomList(Size, [-2, 2], int)
count = 0
for w in range(len(Array)-1):
    Expression1 = (Array[w]>0 and Array[w+1]<0) #+ -
    Expression2 = (Array[w]<0 and Array[w+1]>0) #- +
    if Expression1 or Expression2:
        count+=1
    
print(f'''Созданныйй массив: {Array}
Количество знакочередующихся пар: {count}
''')


input('Нажмите ENTER, чтобы выйти.')
