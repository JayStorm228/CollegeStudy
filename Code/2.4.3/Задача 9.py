from custom_assertions import *
print('''Эта программа создаёт список случайных значений, после чего меняет местами первое и максимальное значение.
      ''')
a = CreateRandomList(UserInput('Введите размер списка: ', int), [1, 30], int)
print(f'Исходный список: {a}')
first = a[0]
Max = max(a)
Max_index = a.index(Max)
a[0] = Max
a[Max_index] = first

print(f'Отсортированный список: {a}')



    
