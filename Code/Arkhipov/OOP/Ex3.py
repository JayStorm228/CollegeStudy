from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import cos, radians, sin


@dataclass
class Triangle(ABC):
    Side1: float = 0.0
    Side2: float = 0.0
    Angle_12: float = 0.0  # degrees

    def __post_init__(self) -> None:
        self._validate_triangle()

    def _validate_triangle(self) -> None:
        if self.Side1 <= 0 or self.Side2 <= 0:
            raise ValueError(
                f"Стороны должны быть > 0: Side1={self.Side1}, Side2={self.Side2}"
            )

        if not (0 < self.Angle_12 < 180):
            raise ValueError(
                f"Угол Angle_12 должен быть в (0°, 180°): {self.Angle_12}°"
            )

        # Проверка неравенства (Side3 вычисляется)
        side3: float = self.Side3
        if (
            self.Side1 + self.Side2 <= side3
            or self.Side1 + side3 <= self.Side2
            or self.Side2 + side3 <= self.Side1
        ):
            raise ValueError(
                f"Неравенство треугольника: {self.Side1}, {self.Side2}, {side3}"
            )

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    @property
    def Side3(self) -> float:
        angle_rad = radians(self.Angle_12)
        side3_sq = (
            self.Side1**2 + self.Side2**2 - 2 * self.Side1 * self.Side2 * cos(angle_rad)
        )
        if side3_sq < 0:
            raise ValueError("Side3^2 < 0 — невозможно!")
        return round(side3_sq**0.5, 2)

    def __str__(self) -> str:
        return f"""
Triangle ABC: 
    AB = {self.Side1}
    BC = {self.Side2}
    AC = {self.Side3}
    ∠ABC = {self.Angle_12}°
    ---
    Area = {self.area}
    Perimeter = {self.perimeter}
""".strip()


class RightTriangle(Triangle):  # Прямоугольный

    def __init__(self, Side1, Side2) -> None:
        super().__init__(Side1=Side1, Side2=Side2, Angle_12=90.0)

    @property
    def area(self) -> float:
        return 0.5 * self.Side1 * self.Side2

    @property
    def perimeter(self) -> float:
        return self.Side1 + self.Side2 + self.Side3

    def __str__(self) -> str:
        return super().__str__() + "\nType: Right"


@dataclass
class IsoscelesTriangle(Triangle):  # Равнобедренный
    def __init__(self, base, leg, Angle_12):
        super().__init__(Side1=base, Side2=leg, Angle_12=Angle_12)

    @property
    def area(self) -> float:
        return self.Side1 * self.Side2 * sin(radians(self.Angle_12)) / 2

    @property
    def perimeter(self) -> float:
        return self.Side1 + self.Side2 + self.Side3

    def __str__(self) -> str:
        return super().__str__() + "\nType: Isosceles"


@dataclass
class EquilateralTriangle(Triangle):
    def __init__(self, Side) -> None:
        super().__init__(Side1=Side, Side2=Side, Angle_12=60.0)

    @property
    def area(self) -> float:
        return self.Side1**2 * 3**0.5 / 4

    @property
    def perimeter(self) -> float:
        return 3 * self.Side1

    def __str__(self) -> str:
        return super().__str__() + "\nType: Equilateral"
