class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def author(self):
        return self._author  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        self.pages = pages

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages < 0:
            raise ValueError("Количество страниц должно быть не отрицательным числом")
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self._name = name
        self._author = author
        self.duration = duration
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, new_duration: int):
        if not isinstance(new_duration, int):
            raise TypeError("Количество часов должно быть типа int")
        if new_duration < 0:
            raise ValueError("Количество часов должно быть не отрицательным числом")
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
