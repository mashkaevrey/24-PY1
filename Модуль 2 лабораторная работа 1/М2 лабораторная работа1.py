import doctest
from typing import Union
class Santas:
    def __init__(self, num_gifts: int, sack_weight: Union[int, float]):
        """
                Создание и подготовка к работе объекта "Санта"

                :param num_gifts: Количество подарков
                :param sack_weight: Вес мешка

                Примеры:
                >>> santa = Santas(1000, 5000)  # инициализация экземпляра класса
                """
        if not isinstance(num_gifts, int):
            raise TypeError("Количество подарков должно быть типа int")
        if num_gifts < 0:
            raise ValueError("Количество подарков должно быть не отрицательным числом")
        self.num_gifts = num_gifts

        if not isinstance(sack_weight, (int, float)):
            raise TypeError("Вес мешка с подарками должен быть типа int")
        if sack_weight < 0:
            raise ValueError("Вес мешка с подарками должен быть не отрицательным числом")
        self.sack_weight = sack_weight
    def increase_gifts(self, new_gifts: int) -> int:
        """
        Увеличение количества подарков.

        :param new_gifts: Количество новых подарков.
        :raise ValueError: Если количество подарков является отрицательным числом.

        :return: Новое количество подарков

        Примеры:
        >>> santa = Santas(1000, 5000)
        >>> santa.increase_gifts(178)
        """
        if not isinstance(new_gifts, int):
            raise TypeError("Количество новых подарков должно быть типа int")
        if new_gifts < 0:
            raise ValueError("Количество новых подарков должно быть неотрицательным числом")
        ...
    def increase_weight(self, weight_gifts: int) -> int:
        """
        Увеличение веса мешка с подарками.

        :param weight_gifts: Новый вес мешка с подарками.
        :raise ValueError: Если вес подарков является отрицательным числом.

        :return: Новый вес мешка с подарками.

        Примеры:
        >>> santa = Santas(1000, 5000)
        >>> santa.increase_weight(2500)
        """
        if not isinstance(weight_gifts, int):
            raise TypeError("Новый вес подарков должно быть типа int")
        if weight_gifts < 0:
            raise ValueError("Новый вес подарков должно быть неотрицательным числом")
        ...


class Tree:
    def __init__(self, nests: int, birds: int, worm: Union[int, float]):
        """
                 Создание и подготовка к работе объекта "Дерево"

                 :param nests: Количество гнезд
                 :param birds: Количесвто птиц
                 :param worm: Количество червей

                 Примеры:
                 >>> tree = Tree(12, 15, 32)  # инициализация экземпляра класса
                 """
        if not isinstance(nests, int):
            raise TypeError("Количество гнезд должно быть типа int")
        if nests < 0:
            raise ValueError("Количество гнезд не должно быть отрицательным числом")
        self.nests = nests

        if not isinstance(birds, int):
            raise TypeError("Количество птиц должно быть типа int")
        if birds < 0:
            raise ValueError("Количество птиц не должно быть отрицательным числом")
        self.birds = birds

        if not isinstance(worm, (int, float)):
            raise TypeError("Количество червей должно быть типа int или float")
        if worm < 0:
            raise ValueError("Количество червей не должно быть отрицательным числом")
        self.worm = worm


    def increase_nests(self, new_nests: int) -> int:
        """
        Увеличение количества гнезд.

        :param new_nests: Новый вес мешка с подарками.
        :raise ValueError: Если количество гнезд является отрицательным числом.

        :return: Новое количество гнезд.

        Примеры:
        >>> tree = Tree(12, 15, 32)
        >>> tree.increase_nests(7)
        """
        if not isinstance(new_nests, int):
            raise TypeError("Количество новых гнезд должно быть типа int")
        if new_nests < 0:
            raise ValueError("Количество новых гнезд не должно быть отрицательным числом")
        ...
    def lessen_worms(self, eaten_worms: int) -> int:
        """
        Уменьшение количества червей.

        :param eaten_worms: Количество съеденых червей.
        :raise ValueError: Если количество съеденых червей с дерева больше существующих червей на нем.

        :return: Новое количество червей.

        Примеры:
        >>> tree = Tree(12, 15, 32)
        >>> tree.lessen_worms(17)
        """
        if not isinstance(eaten_worms, int):
            raise TypeError("Количество съеденых червей должно быть типа int")
        if eaten_worms < 0:
            raise ValueError("Количество съеденых червей не должно быть отрицательным числом")
        ...

class Telegram:
    def __init__(self, num_chats: int, blocked_users: int):
        """
                 Создание и подготовка к работе объекта "Телеграм"

                 :param num_chats: Количество чатов
                 :param blocked_users: Количесвто заблокированных пользователей

                 Примеры:
                 >>> telegram = Telegram(500, 0)  # инициализация экземпляра класса
                 """
        if not isinstance(num_chats, int):
            raise TypeError("Количество чатов должно быть типа int")
        if num_chats < 0:
            raise ValueError("Количество чатов должно быть не отрицательным числом")
        self.num_chats = num_chats

        if not isinstance(blocked_users, int):
            raise TypeError("Количество заблокированных пользователей должно быть типа int")
        if blocked_users < 0:
            raise ValueError("Количество заблокированных пользователей должно быть не отрицательн")
        self.blocked_users = blocked_users

    def is_empty_blocked_users(self) -> bool:
        """
        Функция которая проверяет является ли черный список пустым

        :return: Является ли черный список пустым

        Примеры:
        >>> telegram = Telegram(500, 1)
        >>> telegram.is_empty_blocked_users()
        """
        ...
    def new_blocked_users(self, new_busers: int) -> int:
        """
        Функция которая добавляет новое количество пользователей в черный список

        :param new_busers: Количество пользователей для черного списка.
        :raise ValueError: Если количество пользоватлей является отрицательным числом.

        :return: Новое количество пользователей в черном спике.

        Примеры:
        >>> telegram = Telegram(500, 1)
        >>> telegram.new_blocked_users(12)
        """
        if isinstance(new_busers, int):
            raise TypeError("Количество новых заблокированных пользователей должно быть типа int")
        if new_busers < 0:
            raise ValueError("Количество новых заблокированных пользователей должно быть не отрицательн")
        ...

# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    doctest.testmod()
    pass
