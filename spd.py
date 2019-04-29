from typing import NamedTuple
from collections import namedtuple


class Salary(NamedTuple):
    developer = 2.5
    architect = 3.3
    manager = 1.7
    tester = 2.2


# часы работы в каждой итерации
BaseCalculation = namedtuple('Calculation', [
    'developer',
    'architect',
    'manager',
    'tester',
])


class Calculation(BaseCalculation):
    def __str__(self):
        return '\t'.join(f'{i}' for i in self)

    def hours(self):
        return sum(self)

    def calc(self):
        return (self.developer * Salary.developer
                + self.architect * Salary.architect
                + self.manager * Salary.manager
                + self.tester * Salary.tester)


def main():
    calculations = [
        # начальная фаза
        Calculation(0, 0, 40, 0),
        Calculation(0, 0, 40, 0),
        Calculation(0, 0, 40, 0),
        # фаза конструирования
        Calculation(25, 25, 25, 0),
        Calculation(25, 25, 25, 0),
        Calculation(0, 0, 10, 25),
        # фаза разработки
        Calculation(0, 20, 20, 0),
        Calculation(20, 20, 10, 0),
        Calculation(40, 40, 20, 0),
        Calculation(0, 0, 10, 20),
        Calculation(20, 20, 10, 0),
        Calculation(0, 0, 10, 0),
        # завершающая фаза
        Calculation(30, 30, 30, 0),
        Calculation(30, 30, 20, 0),
    ]
    for c in calculations:
        print(f'{c} {c.hours()} {c.calc()}')

    print(f'Всего часов:', sum(c.hours() for c in calculations))
    print(f'Всего денег:', sum(c.calc() for c in calculations))

    # lines = [
    #     '\t'.join(
    #         [
    #             'Название задачи',
    #             'Трудозатраты Разработчика',
    #             'Архитектор',
    #             'Менеджер проекта',
    #             'Тестировщик',
    #             'Общие трудозатраты',
    #             'Стоимость реализации',
    #         ]),
    #     'Начальная фаза',
    #     'Определить требования к продукту\t' + '\t'.join()
    # ]


if __name__ == '__main__':
    main()
