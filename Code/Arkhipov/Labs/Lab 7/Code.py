print(
    """
Вычислите и выведите члены последовательности, значение которых больше порогового
x, x^2/2!, x^3/3!, x^n/n!
Пороговое значение: 0.001
Значение х: 0.2
    """
)
import math as m
import pandas as pd

N_Value = 1
X_Value = 0.2


def Function(X, N):
    global N_Value
    return X**N / m.factorial(N)


Critical = 0.001
Func_Value = []
N_Values = []

while Function(X_Value, N_Value) > Critical:
    Func_Value.append(Function(X_Value, N_Value))
    N_Values.append(N_Value)
    N_Value += 1

Table = pd.DataFrame({"N": N_Values, "Значение последовательности": Func_Value})
print(Table)
