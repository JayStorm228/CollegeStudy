import math as m
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Figure(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass


@dataclass
class Rect(Figure):
    _length: float = 0.0
    _width: float = 0.0

    def __post_init__(self) -> None:
        self.length = self._length
        self.width = self._width

    @property
    def length(self) -> float:
        return self._length

    @property
    def width(self) -> float:
        return self._width

    @length.setter
    def length(self, value) -> None:
        if value <= 0:
            raise ValueError("Length cannot be negative!")
        self._length = value

    @width.setter
    def width(self, value) -> None:
        if value <= 0:
            raise ValueError("Width cannot be negative!")
        self._width = value

    @property
    def area(self) -> float:
        return self.length * self.width

    @property
    def perimeter(self) -> float:
        return (self.length + self.width) * 2

    def __str__(self) -> str:
        return f"""
Rectangle
Length: {self.length}
Width: {self.width}
Area: {self.area}
Perimeter: {self.perimeter}
        """.strip()


@dataclass
class Circle(Figure):
    _radius: float = 0.0

    def __post_init__(self) -> None:
        self.radius = self._radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value) -> None:
        if value <= 0:
            raise ValueError("Radius cannot be negative!")

    @property
    def area(self) -> float:
        return m.pi**2 * self.radius

    @property
    def perimeter(self) -> float:
        return 2 * m.pi * self.radius

    def __str__(self) -> str:
        return f"""
Circle
Radius: {self._radius}
Area: {self.area}
Perimeter: {self.perimeter}
        """.strip()


@dataclass
class Triangle(Figure):
    _sides: tuple[float, float, float] = (0.0, 0.0, 0.0)

    def __post_init__(self) -> None:
        self.sides = self._sides

    @property
    def sides(self) -> tuple[float, float, float]:
        return self._sides

    @sides.setter
    def sides(self, value: tuple[float, float, float]):
        if len(value) != 3 or any(s <= 0 for s in value):
            raise ValueError(
                f"Ошибка: {value} - должно быть три стороны, каждая из них больше нуля"
            )
        a, b, c = sorted(value)
        if a + b <= c:
            raise ValueError(
                f"Ошибка: {value} — не существует треугольник " f"(a+b={a+b} ≤ c={c})"
            )
        self._sides = value

    @property
    def area(self) -> float:
        a, b, c = self._sides
        s: float = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    @property
    def perimeter(self) -> float:
        return sum(self._sides)

    def __str__(self) -> str:
        return f"""
Triangle
Sides(a, b, c): {self._sides[0]}, {self._sides[1]}, {self._sides[2]}
Area: {self.area}
Perimeter: {self.perimeter}
        """.strip()


triangle = Triangle((1, 2, 3))
rectangle = Rect(10, 5)
circle = Circle(5)
Figures = [triangle, rectangle, circle]

for w in Figures:
    print(str(w))
