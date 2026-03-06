import time
from typing import Callable, Tuple
from enum import Enum


class Algorithm(Enum):
    """Перечисление для выбора варианта работы алгоритма"""
    ITERATIVE = 1   # Итеративный алгоритм
    RECURSIVE = 2   # Рекурсивный алгоритм
    

def fib_iterative(index: int):
    """Последовательность Фибоначчи вида { 0, 1, 1, 2, 3, 5, 8, 13, ... }, рассчитанная с помощью цикла
    :param index: Индекс члена последовательности
    :returns: Значение члена последовательности для выбранного номера
    """
    if index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(3, index + 1):
            a, b = b, a + b
        return b


def fib_recursive(index: int):
    """Последовательность Фибоначчи вида { 0, 1, 1, 2, 3, 5, 8, 13, ... }, рассчитанная с помощью рекурсии
    :param index: Индекс члена последовательности
    :returns: Значение члена последовательности для выбранного номера
    """
    if index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return fib_recursive(index - 2) + fib_recursive(index - 1)


def fibonacci(index: int, algorithm: Algorithm) -> int:
    """Последовательность Фибоначчи вида { 0, 1, 1, 2, 3, 5, 8, 13, ... }
    :param index: Индекс члена последовательности
    :param algorithm: Алгоритм для определения значения члена последовательности
    :returns: Значение члена последовательности для выбранного номера или -1 для обработки ошибок
    """
    if index < 1:
        print(f"Ошибка: номер члена последовательности должен быть больше 0")
        return -1
    elif algorithm == Algorithm.ITERATIVE:
        return fib_iterative(index)
    elif algorithm == Algorithm.RECURSIVE:
        return fib_recursive(index)
    else:
        print(f"Ошибка: выбран нереализованный алгоритм")
        return -1


def fact_iterative(number: int) -> int:
    if number == 0:
        return 1
    else:
        output = 1
        for i in range(1, number + 1):
            output *= i
        return output


def fact_recursive(number: int) -> int:
    if number == 0:
        return 1
    else:
        return fact_recursive(number=number - 1) * number


def factorial(number: int, algorithm: Algorithm) -> int:
    """Расчёт факториала
    :param number: число, для которого считается факториал
    :param algorithm: Алгоритм для расчёта факториала
    :returns: Значение факториала числа или -1 для обработки ошибок
    """
    if number < 0:
        print(f"Ошибка: число должно быть больше или ровняться 0")
        return -1
    elif algorithm == Algorithm.ITERATIVE:
        return fact_iterative(number)
    elif algorithm == Algorithm.RECURSIVE:
        return fact_recursive(number)
    else:
        print(f"Ошибка: выбран нереализованный алгоритм")
        return -1


def calculate_time(func: Callable[[int, Algorithm], int], number:int, algo_type: Algorithm) -> Tuple[int, float]:
    """Расчёт времени работы функции для указанного целочисленного аргумента и типа алгоритма
    :param func: Функция, время работы которой необходимо рассчитать
    :param number: Аргумент функции
    :param algo_type: Тип алгоритма
    :returns: Результат работы функции и значение времени выполнения
    """
    start_time = time.time()
    result = func(number, algo_type)
    end_time = time.time()
    return result, end_time - start_time


def run():
    number = int(input("Введите число для расчёта факториала: "))
    result_iterative, el_time_iterative = calculate_time(func=factorial, number=number, algo_type=Algorithm.ITERATIVE)
    result_recursive, el_time_recursive = calculate_time(func=factorial, number=number, algo_type=Algorithm.RECURSIVE)
    print(f"Результаты для разных типов алгоритмов\n— итеративный: {result_iterative} ({el_time_iterative} с),\n— рекурсивный: {result_recursive} ({el_time_recursive} с).\n")
    index = int(input("Введите номер члена последовательности Фибоначчи: "))
    result_iterative, el_time_iterative = calculate_time(func=fibonacci, number=index, algo_type=Algorithm.ITERATIVE)
    result_recursive, el_time_recursive = calculate_time(func=fibonacci, number=index, algo_type=Algorithm.RECURSIVE)
    print(f"Результаты для разных типов алгоритмов\n— итеративный: {result_iterative} ({el_time_iterative} с),\n— рекурсивный: {result_recursive} ({el_time_recursive} с).\n")


if __name__ == '__main__':
    run()
