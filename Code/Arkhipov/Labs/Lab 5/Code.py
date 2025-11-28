print(
    """
Постройте таблицу значений и найдите наибольшее значение функции y=f(x)
При изменении х на отрезке [a, b] с шагом h

Y = 3*cos(2x +1 )**2
Отрезок: [-pi, pi] шаг pi/8
"""
)

import math as m
import numpy as np

Accuracy = None
while Accuracy == None:
    try:
        Accuracy = int(input("Введите точность вычислений:"))
    except ValueError:
        Accuracy = None
        print(f"Ошибка ввода: {Accuracy} не является числом")

Matrix = np.linspace(-m.pi, m.pi, int((m.pi - (-m.pi)) / (m.pi / 8)) + 1)


def Y(x):
    return 3 * m.cos(2 * x + 1) ** 2


Vector = np.vectorize(Y)
Result = np.round(Vector(Matrix), Accuracy)
table = np.column_stack((Matrix, Result))
print("\tx  y")
print(table)
