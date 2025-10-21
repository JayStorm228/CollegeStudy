from custom_assertions import *

print('''
Эта программа видоизменяет массив заданного размера по критериям:

Если элемент положительный, он уменьшится в два раза
Если элемент отрицательный, он заменится порядковым номером элемента
''')
Data = CreateList(UserInput('Введите размер массива: ', int), int)


print(f'Исходный список: {Data}')
for i in range(len(Data)):
    if Data[i] > 0:
        Data[i] = Data[i]/2
    if Data[i] < 0:
        Data[i] = i
print(f'Изменённый список: {Data}')
            


    
