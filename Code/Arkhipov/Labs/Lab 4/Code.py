import math as m

print(
    """"Эта программа считает табулирование функции:
    F = Sin^2(x) + Ctg(x)
    При параметрах:
    Начальное значение: 1
    Конечное значения: 5
    Шаг: 0.5
"""
)
Accuracy = None
while Accuracy == None:
    Accuracy = input("Введите значение точности: ")
    if "." in Accuracy:
        Accuracy = None
        print(
            "Возможно вы вводите дробное число. Эта величина принимает только целые значения"
        )
    else:
        try:
            Accuracy = int(Accuracy)
        except ValueError:
            Accuracy = None
            print(f"{Accuracy} - Не число")
for w in range(1, 5 * 2 + 1):
    x = m.radians(w)
    F = m.sin(x) ** 2 + m.cos(x) / m.sin(x)
    print(f"Функция #{w}: {round(F, Accuracy)}; Значение аргумента: {w}")

input("\nНажмите ENTER, чтобы выйти.")
