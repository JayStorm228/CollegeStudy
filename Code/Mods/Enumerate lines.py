Code = '''print("""Эта программа находит значение кусочно-заданной функции:
    y = pi * (x**2) - (7 / (x**2)) # x < 1,3
    y = a * (x**3) + 7 * (x ** (1 / 2)) # x = 1,3
    y = ln(x + 7 * (x ** (1 / 2))) # x > 1,3""")
import math as m
from custom_assertions import UserInput

constant = UserInput("Введите значение а: ", float)
x = UserInput("Введите значение х: ", float)
if x < 1.3:
    Fx = m.pi * (x**2) - (7 / (x**2))
    print(f"f(x) = {Fx}")
elif x == 1.3:
    Fx = constant * (x**3) + 7 * (x ** (1 / 2))
    print(f"f(x) = {Fx}")
elif x > 1.3:
    Fx = m.log(x + 7 * (x ** (1 / 2)))
    print(f"f(x) = {Fx}")'''
lines = Code.strip("\n").split("\n")
for i, line in enumerate(lines, start=1):
    print(f"{i:>3}: {line}")
