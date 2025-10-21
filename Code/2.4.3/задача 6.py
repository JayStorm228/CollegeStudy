from custom_assertions import *
print('''Эта программа находит процент нечётных чисел в случайном списке заданного размера.
      ''')
a = CreateRandomList(UserInput('Введите размер списка: ', int), [1, 40], int)

Even = []
Uneven = []

for w in a:
    if w%2 ==1:
        Uneven.append(w)
    else:   Even.append(w)

Uneven_percent = round(len(Uneven)/len(a), 2)

print(f'''Исходный список: {a}
Процент нечётных = {Uneven_percent}''')