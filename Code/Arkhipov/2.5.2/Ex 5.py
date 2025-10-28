print('''Эта программа проверяет, является ли строка палиндромом
''')

InputStr = input('Введите строку: ')

ReversedStr = ''
string_list = []
symbols = ' ,.:(){}[];"\''

for w in InputStr:
    if w not in symbols:
        string_list.append(w)
        
string = ''.join(map(str, string_list))
                 
for w in range(-1, 0-len(string)-1, -1):
    ReversedStr+=string[w]

string = string.lower()
ReversedStr = ReversedStr.lower()
if string == ReversedStr:
    print(f'{InputStr} - Палиндром')
else:
    print(f'{InputStr} - Не палиндром')
input('\nНажмите ENTER, чтобы выйти.')
