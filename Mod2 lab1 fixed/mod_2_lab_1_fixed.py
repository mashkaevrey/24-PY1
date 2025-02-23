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


class Car:
    def __init__(self, consumption: Union[int, float], tank_volume: int, mileage: int = 0):
        """
                Создание и подготовка к работе объекта "Машина"

                :param consumption: Потребление топлива на 10 км
                :param tank_volume: Вместительность топливного бака
                :param mileage: Пробег

                Примеры:
                >>> car_1 = Car(10.5, 570)  # инициализация экземпляра класса
                """
        if not isinstance(tank_volume, int):
            raise TypeError("Вместительность топливного бака должна быть типа int")
        if tank_volume < 0:
            raise ValueError("Вместительность топливного бака должна быть не отрицательным числом")
        self.tank_volume = tank_volume

        if not isinstance(consumption, (int, float)):
            raise TypeError("Потребление топлива должно быть типа int")
        if consumption < 0:
            raise ValueError("Потребление топлива должно быть не отрицательным числом")
        self.consumption = consumption
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self) -> str:
        """
        Запуск механизма.
        Примеры:
        >>> car_1 = Car(10.5, 570)
        >>> car_1.start_engine()
        """
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self) -> str:
        """
        Остановка механизма.
        Примеры:
        >>> car_1 = Car(10.5, 570)
        >>> car_1.stop_engine()
        """
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance: int) -> str:
        """
        Функция которая обозначает поездку.
        :param distance: Дистанция, которую проехал автомобиль.
        :raise ValueError: Если дистанция является отрицательным числом.

        :return: Дистанцию, которую проехал автомобиль и остаток топлива.
        Примеры:
        >>> car_1 = Car(10.5, 570)
        >>> car_1.drive(5000)
        """
        if not isinstance(distance, int):
            raise TypeError("Дистанция должна быть типа int")
        if distance < 0:
            raise ValueError("Дистанция должна быть не отрицательным числом")
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
