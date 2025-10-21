from custom_assertions import *
print('''Эта программа создаёт случайный список заданного размера и затем сортирует его.
      ''')
a = CreateRandomList(UserInput('Введите размер списка: ', int), [1, 50], int)

print(f'''\nИсходный список: {', '.join(map(str, a))}
Отсортированный список: {', '.join(map(str, sorted(a)))}
''')


    
