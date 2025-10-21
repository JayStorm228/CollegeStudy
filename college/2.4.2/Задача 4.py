from custom_assertions import UserInput
print('''
Этп программа вычисляет максимальное и минимальное значение массива из 10 элементов
''')

Tuple = []
output = []
while True:
    if len(Tuple) == 10:
        break

    Tuple.append(UserInput('Введите число: ', int))
Tuple = tuple(Tuple)

for w in Tuple:
    if w > 0 and w%2 == 1:
        output.append(w)
print(f'''
Удовлетворительные значения: {', '.join(map(str, output))}
Максимальное: {max(output)}
Минимальное: {min(output)}
''')

    
