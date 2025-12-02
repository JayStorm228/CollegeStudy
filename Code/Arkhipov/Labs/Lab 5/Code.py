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
import pandas as pd

Accuracy = None
while Accuracy == None:
    try:
        Accuracy = int(input("Введите точность вычислений:"))
    except ValueError:
        Accuracy = None
        print(f"Ошибка ввода: {Accuracy} не является числом")

X_Values = np.linspace(-m.pi, m.pi, int((m.pi - (-m.pi)) / (m.pi / 8)) + 1)


def Y(x):
    return 3 * m.cos(2 * x + 1) ** 2


Vector = np.vectorize(Y)
Y_Values = Vector(X_Values)
max_index = np.argmax(Y_Values)
max_x, max_y = X_Values[max_index], Y_Values[max_index]
RoundX, RoundY = np.around(X_Values, Accuracy), np.around(Y_Values, Accuracy)
max_x_rounded, max_y_rounded = np.round(max_x, Accuracy), np.round(max_y, Accuracy)
Table = pd.DataFrame({"x": RoundX, "y": RoundY})

print(
    f"""Таблица всех значений: \n{Table}\n
Максимальное значение У: {max_y_rounded} при х = {max_x_rounded}"""
)
