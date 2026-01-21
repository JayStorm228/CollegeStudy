from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Edition(ABC):
    Title: str = ""
    AuthorSurname: str = ""

    @abstractmethod
    def __str__(self) -> str:
        pass


@dataclass
class Book(Edition):
    ReleaseYear: str = ""
    Publisher: str = ""

    def __str__(self) -> str:
        return f"Книга: '{self.Title}' ({self.AuthorSurname}, {self.ReleaseYear}, {self.Publisher})"


@dataclass
class Article(Edition):
    Magazine: str = ""
    MagazineID: str = ""
    ReleaseYear: str = ""

    def __str__(self) -> str:
        return f"Статья: '{self.Title}' ({self.AuthorSurname}, Журнал: {self.Magazine}(№{self.MagazineID}, год издания: {self.ReleaseYear})"


@dataclass
class Website(Edition):
    URL: str = ""
    Annotation: str = ""

    def __str__(self) -> str:
        return f"Электронный ресурс: '{self.Title}'(Автор: {self.AuthorSurname}). \n {self.Annotation} "


def search(editions: List[Edition], surname: str) -> List[Edition]:
    output = []
    for obj in editions:
        if obj.AuthorSurname == surname:
            output.append(obj)
    for w in output:
        print(w)
    return output
