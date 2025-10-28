print('''Эта программа подсчитывает среднюю длинну слов во введённой строке
''')

string = input('Введите строку: ')
StrList = string.split(' ')
StrList2 = []
Symbols = ['-', '--']
Len = []
for i in range(len(StrList)):
    StrList[i] = StrList[i].strip(',')
    StrList[i] = StrList[i].strip('/')
    StrList[i] = StrList[i].strip('.')
    StrList[i] = StrList[i].strip(':')
    StrList[i] = StrList[i].strip(';')
    StrList[i] = StrList[i].strip('"')
    StrList[i] = StrList[i].strip("'")
    StrList[i] = StrList[i].strip(")")
    StrList[i] = StrList[i].strip("(")
    StrList[i] = StrList[i].strip("]")
    StrList[i] = StrList[i].strip("[")



for w in StrList:
    if w not in Symbols:
        StrList2.append(w)
for w in StrList2:
    Len.append(len(w))
Avg = sum(Len)/len(Len)
print(f'''Введённая строка: {string}
Слова в ней: {', '.join(map(str, StrList2))}
Их средняя длинна: {Avg}
''')
input('\nНажмите ENTER, чтобы выйти.')
