print('''Эта программа находит максимальное значение функции на заданном промежутке [a, b] с шагом h
Функция: y = (cos x)/(sin x)
      ''')
import sys
import os
sys.path.append(os.path.abspath('..'))
from custom_assertions import *
from math import *
a = UserInput('Введите значение a: ', int)
b = UserInput('Введите значение b: ', int)
h = UserInput('Введите значение h: ', int)
output = []

for w in range(a,b+1,h):
    output.append(cos(w)/sin(w))
print(f'Максимальное значение на промежутке: [{a}, {b}] c шагом {h}: {round(max(output), 2)}')