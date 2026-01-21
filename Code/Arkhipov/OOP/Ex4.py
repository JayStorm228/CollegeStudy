from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Vehicle(ABC):
    mark: str
    ID: str
    speed: float
    carrying_capacity: float

    @property
    @abstractmethod
    def carrying(self) -> float:
        pass

    def __str__(self) -> str:
        return f"""
Vehicle:
    mark: {self.mark}, ID: {self.ID}
    max speed: {self.speed}
    max carrying: {self.carrying_capacity}
""".strip()


class Auto(Vehicle):

    @property
    def carrying(self) -> float:
        return self.carrying_capacity

    def __str__(self) -> str:
        return super().__str__().replace("Vehicle", "Auto")


@dataclass
class Motorcycle(Vehicle):
    has_sidecar: bool = False

    @property
    def carrying(self) -> float:
        return self.carrying_capacity if self.has_sidecar else 0.0

    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace("Vehicle", "Motorcycle")
            .replace(f"{self.carrying_capacity}", f"{self.carrying}")
        )


@dataclass
class Truck(Vehicle):
    has_cargo: bool = False

    @property
    def carrying(self) -> float:
        return (
            (self.carrying_capacity * 2) if self.has_cargo else self.carrying_capacity
        )

    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace("Vehicle", "Truck")
            .replace(f"{self.carrying_capacity}", f"{self.carrying}")
        )
