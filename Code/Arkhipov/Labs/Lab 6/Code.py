print(
    """
Вычислите значения z, соответствующие каждому значению х
хn <= x <= xk, шаг изменения равен dx
        | (x**3 + ax)**(1/4)
    z = | ------------------
        | ln( ( a**7 + x**(1/2) )**(1/2)  )
Задача: Определить среднее арифметическое значений z
Контрольные значения:
    a = 5.27
    xn = 1, xk = 10, dx = 1
    *Все константы могут принимать дробное значение
        """
)

import math as m
import numpy as np
import pandas as pd
import random as r

Accuracy = None
while Accuracy == None:
    try:
        Accuracy = int(input("Введите точность вычислений:"))
    except ValueError:
        Accuracy = None
        print(f"Ошибка ввода: {Accuracy} не является числом")
def ControlValuesCheck() -> bool: 
    Check = input('Проверить контрольные значения? [Y/N]')
    if Check == 'Y':
        return True
    elif Check = 'N':
        return False
    else: exit('Ошибочное значение. Запустите программу ещё раз.')
if ControlValuesCheck():
    a, Xn, Xk, dx = 5.27, 1, 10, 1
else: 
    a = r.uniform(0.5, 10)
    Xn = r.uniform(0, 10)
    Xk = r.uniform(0, 10)
    if Xn > Xk:
        Xn, Xk = Xk, Xn
    dx = r.uniform(0.5, 3)
N_Values = int((Xk - Xn) / dx) + 1
if N_Values < 1:
    N_Values = 1
X_Values = np.linspace(Xn, Xk, N_Values)


def Z(x):
    num = x**3 + a * x
    den_arg = a**7 + m.sqrt(x)
    if num < 0 or den_arg <= 0:
        return np.nan
    return (num**0.25) / m.log(den_arg**0.5)


z = np.vectorize(Z)
Z_Values = z(X_Values)
if np.all(np.isnan(Z_Values)):
    print("Для выбранных параметров функция не определена ни в одной точке.")
else:
    Z_Mean = np.around(np.nanmean(Z_Values), Accuracy)
RoundedX, RoundedZ = np.around(X_Values, Accuracy), np.around(Z_Values, Accuracy)
Table = pd.DataFrame({"X": RoundedX, "Z": RoundedZ})


print(
    f"""
a = {a}; Xn = {Xn}; Xk = {Xk}, dx = {dx}
Таблица значений: \n{Table}\n
Среднее значение функции z: {Z_Mean}"""
)
