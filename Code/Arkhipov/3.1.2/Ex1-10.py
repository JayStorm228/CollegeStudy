from math import prod
import numpy as np


def filter_not_equal(List: list[int | float], znach: int | float) -> list[int | float]:
    """Переписывает в новый список элементы, не равные заданному значению.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : int | float
        Значение, элементы, равные которому, нужно исключить.

    Возврат
    -------
    list[int | float]
        Новый список, содержащий только элементы, не равные ``znach``.
    """
    return [w for w in List if w != znach]


def fill_list_with_value(znach: float | int) -> list[int | float]:
    """Создаёт список заданной длины, заполненный указанным значением.

    Длина списка вводится пользователем c клавиатуры.

    Параметры
    ----------
    znach : float | int
        Значение, которым заполняется список.

    Возврат
    -------
    list[int | float]
        Список длины, заданной пользователем, заполненный значением ``znach``.
    """
    Len = int(input("Введите количество значений: "))
    return [znach for _ in range(Len)]


def f3(List: list[int | float], znach: float | int) -> int:
    """Подсчитывает количество элементов списка, превышающих заданное значение.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : float | int
        Пороговое значение для сравнения элементов.

    Возврат
    -------
    int
        Количество элементов списка, строго больших ``znach``.
    """
    return len([w for w in List if w > znach])


def f4(List: list[int | float], znach: int | float) -> float:
    """Вычисляет сумму элементов списка, меньших заданного значения.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : int | float
        Пороговое значение для сравнения элементов.

    Возврат
    -------
    float
        Сумма всех элементов списка, строго меньших ``znach``.
    """
    return sum(w for w in List if w < znach)


def f5(List: list[int | float]) -> float | int:
    """Вычисляет произведение всех элементов списка.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.

    Возврат
    -------
    float | int
        Произведение всех элементов списка ``List``.
    """
    return prod(List)


def count_greater_elements(Matrix: np.ndarray, znach: int | float) -> int:  # Ex 6
    """Подсчитывает количество элементов массива, превышающих заданное значение.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив произвольной размерности.
    znach : int | float
        Пороговое значение для сравнения элементов.

    Возврат
    -------
    int
        Количество элементов массива, строго больших ``znach``.
    """
    return len(Matrix[Matrix > znach])


def f7(List: list[int | float], index: int) -> list[int | float]:
    """Удаляет элемент списка по его номеру (нумерация с 1).

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел, который будет изменён.
    index : int
        Порядковый номер удаляемого элемента (начиная с 1).

    Возврат
    -------
    list[int | float]
        Изменённый список после удаления элемента.

    Исключения
    ----------
    IndexError
        Выбрасывается, если элемента с указанным номером не существует.
    """
    if index > len(List) or index < 1:
        raise IndexError("Указанного номера нет в списке!")
    List.pop(index - 1)
    return List


def f8(Matrix: np.ndarray, chislo: int | float) -> np.ndarray:
    """Умножает все элементы массива на заданное число.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив.
    chislo : int | float
        Число, на которое умножаются все элементы массива.

    Возврат
    -------
    numpy.ndarray
        Новый массив, полученный поэлементным умножением на ``chislo``.
    """
    return Matrix * chislo


def f9(Matrix: np.ndarray, znach1: int | float, znach2: int | float) -> np.ndarray:
    """Заменяет все элементы массива, не равные заданному значению, другим значением.

    Параметры
    ----------
    Matrix : numpy.ndarray
        Исходный числовой массив, который будет изменён на месте.
    znach1 : int | float
        Значение, которое требуется сохранить.
    znach2 : int | float
        Значение, которым заменяются все элементы, отличные от ``znach1``.

    Возврат
    -------
    numpy.ndarray
        Тот же массив, в котором все элементы, не равные ``znach1``,
        заменены на ``znach2``.
    """
    Matrix[Matrix != znach1] = znach2
    return Matrix


def f10(List: list[int | float], znach: int | float) -> list[int | float]:
    """Добавляет элемент в список и возвращает отсортированную версию списка.

    Параметры
    ----------
    List : list[int | float]
        Исходный список чисел.
    znach : int | float
        Значение, которое нужно добавить в список.

    Возврат
    -------
    list[int | float]
        Новый отсортированный список, содержащий все элементы ``List`` и ``znach``.
    """
    List.append(znach)
    return sorted(List)


if __name__ == "__main__":
    pass
