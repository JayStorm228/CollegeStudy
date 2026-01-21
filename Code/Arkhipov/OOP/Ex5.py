import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

Date_Pattern: re.Pattern[str] = re.compile(
    r"^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$"
)


def validate_date(date_str: str) -> bool:
    if not Date_Pattern.match(date_str):
        return False
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def validate_positive(Number) -> bool:
    try:
        if Number < 0:
            return False
        else:
            return True
    except ValueError:
        return False


@dataclass
class Item(ABC):
    name: str
    price: float

    def __post_init__(self) -> None:
        if not validate_positive(self.price):
            raise ValueError(
                f"{self.price} указано неверно: должно быть положительным числом "
            )

    @abstractmethod
    def can_buy(self, money: float) -> bool:
        return True if (money - self.price) >= 0 else False


@dataclass
class Product(Item):
    Create_date: str
    Expire_date: str

    def __post_init__(self) -> None:
        super().__post_init__()
        if not validate_date(self.Create_date):
            raise ValueError(
                f'{self.Create_date} не соответствует формату: "дд.мм.гггг" или дата введена неверно'
            )
        if not validate_date(self.Expire_date):
            raise ValueError(
                f'{self.Create_date} не соответствует формату: "дд.мм.гггг" или дата введена неверно'
            )

    def can_buy(self, money: float) -> bool:
        return super().can_buy(money)


@dataclass
class Supply(Item):
    Create_date: str
    Expire_date: str
    amount: int

    @property
    def cost(self) -> float:
        return self.price * self.amount

    def __post_init__(self) -> None:
        super().__post_init__()
        if not validate_positive(self.amount):
            raise ValueError(
                f'Количество "{self.amount}" указано неверно - должно быть положительное число'
            )
        if not validate_date(self.Create_date):
            raise ValueError(
                f'{self.Create_date} не соответствует формату: "дд.мм.гггг" или дата введена неверно'
            )
        if not validate_date(self.Expire_date):
            raise ValueError(
                f'{self.Create_date} не соответствует формату: "дд.мм.гггг" или дата введена неверно'
            )

    def can_buy(self, money: float) -> bool:
        return True if (money - self.cost) >= 0 else False


@dataclass
class Phone(Item):

    def can_buy(self, money) -> bool:
        return super().can_buy(money)


def search_available(
    ProductList: list[Product | Supply | Phone], money: float
) -> list[Product | Supply | Phone]:
    return [item for item in ProductList if item.can_buy(money)]
