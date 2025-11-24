Code = '''
import random as r
import math as m
print(""""Эта программа вычисляет кусочно заданную функцию
      z = 1 - e^(xy + ab) # xy > 0
      z = b - min{ax, y} # xy = 0
      z = max{x^3, e^y, ( |ln y^2| )^( 1/2 )} # xy <0""")
x, a = r.randint(-10, 10), r.randint(-10, 10)
b, y = r.randint(-10, 10), r.randint(-10, 10)
Accuracy = UserInput("Введите количество знаков после запятой: ", int)
if x * y > 0:
    Fx = 1 - m.e ** (x * y + a * b)
    StrFx = "1 - e ^ (xy + ab)  # xy > 0"
elif x * y == 0:
    Fx = b - min(a * x, y)
    StrFx = "z = b - min{ax, y} # xy = 0"
elif x * y < 0:
    Fx = max(x**3, m.e**y, abs(m.log(y**2)) ** (1 / 2))
    StrFx = "max{x^3, e^y, ( |ln y^2| )^( 1/2 )} # xy <0"
print(f"""Исходные значения:
    x = {x} \\ny = {y} \\na = {a} \\nb = {b}
Значение функции z при текущих значениях: {round(Fx, Accuracy)}
Подходящий отрезок кусочно заданной функции: {StrFx}
Точность вычисления: до {Accuracy} знака""")
input("\nНажмите ENTER, чтобы выйти.")
'''
lines = Code.strip("\n").split("\n")
for i, line in enumerate(lines, start=1):
    print(f"{i:>3}: {line}")
